"""
妖契者 網站 — YouTube 影片自動抓取腳本

用途：
  讀取 channels.json 裡列出的每個頻道，抓取最新上傳影片，
  並判斷該影片是否為直播（含直播回放），輸出成 videos.json
  給網站前端 JavaScript 讀取顯示。

需要的環境變數：
  YOUTUBE_API_KEY — 在 Google AI / Cloud Console 申請的免費 YouTube Data API v3 金鑰

用量說明（零成本方案）：
  - 每個頻道用「上傳播放清單」(uploads playlist) 撈最新影片，
    playlistItems.list 每次呼叫成本很低（約 1 unit）
  - 批次用 videos.list 查詢是否為直播，成本同樣很低（約 1 unit / 50 部影片）
  - 完全不使用昂貴的 search.list（100 units/次），一天執行 4 次
    對 4~10 個頻道來說，每日用量遠低於免費額度（10,000 units/天）
"""

import json
import os
import sys
from datetime import datetime, timezone

import requests

API_KEY = os.environ.get("YOUTUBE_API_KEY")
CHANNELS_FILE = "channels.json"
OUTPUT_FILE = "videos.json"
MAX_PER_CHANNEL = 8      # 每個頻道最多抓幾部最新影片
MAX_OUTPUT_PER_TYPE = 12  # 影片/直播各自最多保留幾筆到最終輸出
DESCRIPTION_LIMIT = 120   # 簡介截斷長度

API_BASE = "https://www.googleapis.com/youtube/v3"


def uploads_playlist_id(channel_id: str) -> str:
    """標準頻道的上傳播放清單 ID，是把 UC 開頭換成 UU。"""
    if channel_id.startswith("UC"):
        return "UU" + channel_id[2:]
    return channel_id


def fetch_playlist_items(playlist_id: str, channel_name: str):
    url = f"{API_BASE}/playlistItems"
    params = {
        "key": API_KEY,
        "part": "snippet",
        "playlistId": playlist_id,
        "maxResults": MAX_PER_CHANNEL,
    }
    resp = requests.get(url, params=params, timeout=20)
    if resp.status_code != 200:
        print(f"[警告] 抓取頻道「{channel_name}」失敗：{resp.status_code} {resp.text[:200]}", file=sys.stderr)
        return []
    items = resp.json().get("items", [])
    results = []
    for item in items:
        snippet = item.get("snippet", {})
        video_id = snippet.get("resourceId", {}).get("videoId")
        if not video_id:
            continue
        thumb = (
            snippet.get("thumbnails", {}).get("high")
            or snippet.get("thumbnails", {}).get("medium")
            or snippet.get("thumbnails", {}).get("default")
            or {}
        )
        description = (snippet.get("description") or "").strip().replace("\n", " ")
        if len(description) > DESCRIPTION_LIMIT:
            description = description[:DESCRIPTION_LIMIT].rstrip() + "…"
        results.append({
            "id": video_id,
            "title": snippet.get("title", ""),
            "description": description,
            "thumbnail": thumb.get("url", ""),
            "channel": channel_name,
            "publishedAt": snippet.get("publishedAt", ""),
            "url": f"https://www.youtube.com/watch?v={video_id}",
        })
    return results


def fetch_live_status(video_ids):
    """回傳 { videoId: True/False }，True 代表這部影片是（或曾是）直播。"""
    status = {}
    for i in range(0, len(video_ids), 50):
        batch = video_ids[i:i + 50]
        url = f"{API_BASE}/videos"
        params = {
            "key": API_KEY,
            "part": "liveStreamingDetails",
            "id": ",".join(batch),
        }
        resp = requests.get(url, params=params, timeout=20)
        if resp.status_code != 200:
            print(f"[警告] 查詢直播狀態失敗：{resp.status_code} {resp.text[:200]}", file=sys.stderr)
            continue
        for item in resp.json().get("items", []):
            vid = item.get("id")
            details = item.get("liveStreamingDetails")
            status[vid] = bool(details and details.get("actualStartTime"))
    return status


def main():
    if not API_KEY:
        print("[錯誤] 找不到 YOUTUBE_API_KEY 環境變數，請確認 GitHub Secrets 有設定。", file=sys.stderr)
        sys.exit(1)

    with open(CHANNELS_FILE, encoding="utf-8") as f:
        config = json.load(f)

    all_videos = []
    for ch in config.get("channels", []):
        channel_id = ch.get("channel_id", "")
        name = ch.get("name", "")
        if not channel_id or channel_id.startswith("UC替換"):
            print(f"[略過] 「{name}」尚未填入正確的頻道 ID，先跳過。", file=sys.stderr)
            continue
        playlist_id = uploads_playlist_id(channel_id)
        videos = fetch_playlist_items(playlist_id, name)
        all_videos.extend(videos)

    if not all_videos:
        print("[提醒] 沒有抓到任何影片，videos.json 將維持現狀不覆蓋。", file=sys.stderr)
        sys.exit(0)

    live_status = fetch_live_status([v["id"] for v in all_videos])
    for v in all_videos:
        v["type"] = "stream" if live_status.get(v["id"]) else "video"

    all_videos.sort(key=lambda v: v.get("publishedAt", ""), reverse=True)

    output = {
        "updatedAt": datetime.now(timezone.utc).isoformat(),
        "videos": [v for v in all_videos if v["type"] == "video"][:MAX_OUTPUT_PER_TYPE],
        "streams": [v for v in all_videos if v["type"] == "stream"][:MAX_OUTPUT_PER_TYPE],
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"完成，共 {len(output['videos'])} 部影片、{len(output['streams'])} 部直播回放。")


if __name__ == "__main__":
    main()
