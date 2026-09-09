# 妖契者 VTuber Team Site

妖契者 VTuber 團隊官方網站。純靜態網站，使用 GitHub Pages 免費託管。

## 手機版部署步驟（不用打指令）

1. **解壓縮** `vtuber-site.zip`（手機內建的「檔案」App 或任何解壓縮 App 都可以，例如 iOS「檔案」App 長按選「解壓縮」，Android 用「Files by Google」或 ZArchiver）
2. 用手機瀏覽器開 [github.com](https://github.com)，登入帳號（沒有的話先免費註冊）
3. 點右上角 **＋** → **New repository**
   - Repository name 填 `starpath-site`
   - 選 **Public**
   - 不用勾選「Add a README file」
   - 點 **Create repository**
4. 進入剛建立的空 repository，點 **uploading an existing file** 這行藍字（或 **Add file → Upload files**）
5. 點 **choose your files**，把解壓縮出來、位於最上層的檔案「全部選取」一次上傳：
   `index.html、members.html、videos.html、about.html、admin.html、style.css、content.json、channels.json、videos.json、requirements.txt、README.md、PROJECT_PLAN.md、logo.png、banner.jpg、member-01.jpg ~ member-06.jpg`
   （這些檔案都放在同一層，不用建資料夾，手機上傳不會出錯）
6. 下方 Commit 訊息隨意打（例如「上傳網站」），點綠色 **Commit changes**
7. **`scripts/fetch_videos.py` 與 `.github/workflows/fetch-videos.yml` 這兩個檔案在子資料夾裡，手機的「Upload files」選檔案時通常無法保留資料夾結構，改用下面方式個別建立：**
   - 回到 repository 首頁，點 **Add file → Create new file**
   - 檔名欄位直接輸入完整路徑 `scripts/fetch_videos.py`（輸入斜線 `/` 會自動建立 `scripts` 資料夾），把檔案內容貼到下方文字框，點 **Commit changes**
   - 重複一次，檔名輸入 `.github/workflows/fetch-videos.yml`，貼上內容後 **Commit changes**
8. 上傳完成後，點上方 **Settings** → 左側選單 **Pages**
9. **Build and deployment** → Source 選 `Deploy from a branch`，Branch 選 `main` / `/(root)`，點 **Save**
10. 等 1–2 分鐘，網站會發布在：
    `https://你的帳號.github.io/starpath-site/`
11. 若要讓「影片精選」頁自動抓取 YouTube 影片，還需要到 **Settings → Secrets and variables → Actions → New repository secret**，
    Name 填 `YOUTUBE_API_KEY`，Value 填你申請到的 YouTube Data API v3 金鑰

## 之後想更新文字內容（成員介紹、關於我們文案、社群連結等）

**優先用後台編輯，不需要動到程式碼**：到首頁最下方，快速連點頁尾的 Logo 5 下（3 秒內），會跳轉到隱藏的後台編輯頁 `admin.html`，登入後即可修改上表列出的所有頁面文字與成員名單，儲存後 GitHub Pages 約 1 分鐘會自動更新。

如果是要換 Logo／橫幅／成員照片等圖片檔案，或修改程式碼本身：

1. 到 repository 裡點要改的檔案（例如 `logo.png`）
2. 點右上角鉛筆圖示（Edit this file，圖片檔案則是重新上傳同檔名覆蓋）
3. 直接在網頁上修改內容，改完點 **Commit changes**
4. GitHub Pages 會自動重新部署，等 1 分鐘左右刷新網站即可看到更新

## 待辦事項

詳見 `PROJECT_PLAN.md` 的「後續擴充建議」與「待辦清單」章節，包括：
- 上傳 `team-photo.jpg`（團隊合照）
- 在後台填入正確的 YouTube 頻道 ID，並設定 `YOUTUBE_API_KEY` 這組 GitHub Secret
- （選用）在後台填入 Formspree 表單 ID 或聯絡信箱，啟用合作洽詢表單
- （選用）綁定自訂網域

## 檔案結構

```
vtuber-site/
├── index.html                          首頁
├── members.html                        成員介紹
├── videos.html                         影片精選
├── about.html                          關於我們／聯絡我們
├── admin.html                          後台編輯（隱藏入口）
├── style.css                           共用樣式
├── content.json / channels.json / videos.json   網站文字與影片資料
├── requirements.txt
├── scripts/fetch_videos.py             影片自動抓取腳本
├── .github/workflows/fetch-videos.yml  自動抓取排程
├── logo.png / banner.jpg / member-0X.jpg
├── PROJECT_PLAN.md
└── README.md
```
