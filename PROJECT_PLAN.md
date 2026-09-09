# 妖契者 — VTuber 團隊官網 企劃書

## 1. 專案簡介

妖契者是由幾位朋友共同發起的計畫。目前成員都還是個人 YouTuber（訂閱數皆在 200 以內），正朝著成為 VTuber 團隊的方向前進。本專案目標是建立一個團隊官方網站，作為觀眾認識成員、觀看影片與直播回放，以及了解團隊與合作洽詢的入口。

- **前台網站**：純靜態頁面（HTML / CSS / JavaScript），由 GitHub Pages 直接託管
- **內容資料**：`content.json`、`channels.json`、`videos.json` 三份 JSON，前台頁面用 `fetch()` 讀取後動態渲染，不需要重新編輯 HTML 原始碼
- **後台編輯**：`admin.html` 提供密碼登入的編輯介面，透過外部 Cloudflare Worker（`WORKER_URL`，不在此 repo 內）呼叫 GitHub API 讀寫上述 JSON 檔案
- **影片自動抓取**：`.github/workflows/fetch-videos.yml` 每 6 小時自動執行 `scripts/fetch_videos.py`，抓取 `channels.json` 中各頻道最新影片並覆寫 `videos.json`
- **託管方式**：GitHub Pages（免費、無用量額度限制，適合純靜態站台）
- **目標受眾**：頻道觀眾、潛在合作方、新粉絲

## 2. 資訊架構（網站頁面）

| 頁面 | 檔案 | 內容狀態 |
|---|---|---|
| 首頁 | `index.html` | ✅ 完整內容（導覽列、橫幅、成員預覽、影片精選、團隊簡介、頁尾）|
| 成員介紹 | `members.html` | ✅ 完整內容，六位成員卡片（名稱、代表動物、簡介、頻道連結） |
| 影片精選 | `videos.html` | ✅ 框架與資料串接完成，分為「影片」／「直播」兩個分頁；實際影片列表待 `channels.json` 填入正確頻道 ID 後由自動化流程抓取 |
| 關於我們／聯絡我們 | `about.html` | ✅ 完整內容（團隊故事 + 合作洽詢），聯絡表單／信箱待後台填入 Formspree ID 或聯絡信箱後啟用 |
| 後台編輯 | `admin.html` | ✅ 完整內容，可編輯上述四頁的文字與成員名單，並管理 YouTube 頻道清單 |

導覽選單：
`首頁 / 成員介紹 / 影片精選 / 關於我們·聯絡我們`

（原本規劃的「直播行程」獨立頁面已移除，直播回放內容併入「影片精選」頁的「直播」分頁；後台入口為隱藏功能，於首頁頁尾 Logo 連續點擊 5 下進入，不出現在導覽選單中）

## 3. 視覺設計規範

**色彩系統**
| 用途 | 色碼 |
|---|---|
| 主背景 | `#0b0f16` |
| 卡片/區塊背景 | `#121821` |
| 分隔線 | `#212b38` |
| 主要文字 | `#eef3f7` |
| 次要文字 | `#a7b3c0` |
| 強調色（電光青，所有青色文字統一使用此亮度） | `#7bf0f7` |
| 強調色背景／邊框用 | `#35d6e0` |

**字體**
- 標題／Logo：Space Grotesk（Google Fonts）
- 內文：Inter（Google Fonts）

**版面原則**
- 深色背景 + 淡格線紋理，營造科技/星空氛圍
- 卡片以細邊框與左側強調線區分層次，避免統一圓角陰影的樣板感
- 導覽列 Logo 靠左側邊緣，減少留白
- Hero 橫幅圖片可自由更換，疊加漸層與標語文字
- 手機版採漢堡選單，RWD 全面適配

## 4. 技術架構

- 純 HTML5 + CSS3 + Vanilla JavaScript，無框架、無建置流程
- 共用樣式集中於 `style.css`，各頁面共用同一套設計系統
- `videos.html` 內建分頁切換邏輯（影片／直播），純前端 JS 控制顯示/隱藏
- 所有前台動態文字、成員名單、影片資料皆由 JSON 檔案提供，前端一律先跳脫（escape）再輸出，並限制連結只接受 `http`/`https` 協定，避免後台內容被誤植惡意內容時影響訪客
- 圖片（Logo、橫幅、成員照）已换成實際檔案；`team-photo.jpg` 尚待上傳，未上傳前首頁會顯示文字佔位區塊而非破圖

## 5. 檔案結構

```
vtuber-site/
├── index.html                       首頁
├── members.html                     成員介紹
├── videos.html                      影片精選（影片／直播分頁）
├── about.html                       關於我們／聯絡我們
├── admin.html                       後台編輯（隱藏入口，見上表說明）
├── style.css                        共用樣式（含後台編輯介面樣式）
├── content.json                     全站文字與成員名單資料
├── channels.json                    YouTube 頻道清單（供自動抓取使用）
├── videos.json                      自動抓取結果（由 GitHub Actions 產生，不需手動編輯）
├── requirements.txt                 抓取腳本的 Python 相依套件
├── scripts/fetch_videos.py          YouTube 影片自動抓取腳本
├── .github/workflows/fetch-videos.yml  排程每 6 小時執行一次抓取腳本
├── logo.png / banner.jpg / member-0X.jpg  網站圖片
├── PROJECT_PLAN.md                  本企劃書
└── README.md                        部署操作說明
```

## 6. GitHub Pages 部署與更新

- 使用 GitHub 網頁版的 **Upload files** 功能上傳／更新檔案（不需要在本機安裝 Git）
- 上傳同名檔案會自動覆蓋舊版本，commit 後 GitHub Pages 約 1～2 分鐘會自動重新部署
- 詳細步驟見 `README.md`

## 7. 後續擴充建議（待討論）

- **聯絡表單**：`about.html` 的合作洽詢表單已支援串接 [Formspree](https://formspree.io) 免費方案，只需到後台「關於我們頁」分頁填入 Formspree 表單 ID 即可啟用；未填時會顯示聯絡信箱或社群連結作為備援
- **影片自動抓取**：需在 GitHub repository 的 **Settings → Secrets and variables → Actions** 設定 `YOUTUBE_API_KEY`（YouTube Data API v3 金鑰），並在後台「YouTube 頻道清單」分頁填入各成員正確的頻道 ID，工作流程才會實際抓到資料
- **自訂網域**：如需綁定自訂網域，於 GitHub Pages 設定中新增 CNAME 即可

## 8. 待辦清單

- [ ] 上傳 `team-photo.jpg`（團隊合照，首頁「我們是誰」區塊使用；未上傳前會顯示文字佔位區塊）
- [ ] 在後台「YouTube 頻道清單」分頁填入六位成員正確的頻道 ID
- [ ] 在 GitHub repository 設定 `YOUTUBE_API_KEY` 這組 Secret，讓自動抓取影片的排程真正生效
- [ ] （選用）在後台「關於我們頁」分頁填入 Formspree 表單 ID 或聯絡信箱，啟用合作洽詢表單
- [ ] （選用）綁定自訂網域
