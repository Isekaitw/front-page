# 妖世 VTuber Team Site

妖世 VTuber 團隊官方網站。純靜態網站，使用 GitHub Pages 免費託管。

## 手機版部署步驟（不用打指令）

1. **解壓縮** `vtuber-site.zip`（手機內建的「檔案」App 或任何解壓縮 App 都可以，例如 iOS「檔案」App 長按選「解壓縮」，Android 用「Files by Google」或 ZArchiver）
2. 用手機瀏覽器開 [github.com](https://github.com)，登入帳號（沒有的話先免費註冊）
3. 點右上角 **＋** → **New repository**
   - Repository name 填 `starpath-site`
   - 選 **Public**
   - 不用勾選「Add a README file」
   - 點 **Create repository**
4. 進入剛建立的空 repository，點 **uploading an existing file** 這行藍字（或 **Add file → Upload files**）
5. 點 **choose your files**，把解壓縮出來的檔案「全部選取」一次上傳：
   `index.html、members.html、videos.html、about.html、style.css、README.md、PROJECT_PLAN.md`
   （這些檔案現在都放在同一層，不用建資料夾，手機上傳不會出錯）
6. 下方 Commit 訊息隨意打（例如「上傳網站」），點綠色 **Commit changes**
7. 上傳完成後，點上方 **Settings** → 左側選單 **Pages**
8. **Build and deployment** → Source 選 `Deploy from a branch`，Branch 選 `main` / `/(root)`，點 **Save**
9. 等 1–2 分鐘，網站會發布在：
   `https://你的帳號.github.io/starpath-site/`

## 之後想更新內容（例如換 Logo 圖片連結）

1. 到 repository 裡點要改的檔案（例如 `index.html`）
2. 點右上角鉛筆圖示（Edit this file）
3. 直接在網頁上修改內容，改完點 **Commit changes**
4. GitHub Pages 會自動重新部署，等 1 分鐘左右刷新網站即可看到更新

## 待辦事項

詳見 `PROJECT_PLAN.md` 的「後續擴充建議」與「待辦清單」章節，包括：
- 替換 Logo／橫幅圖片連結
- 補齊成員介紹、影片精選、關於我們頁內容
- （選用）串接 Formspree 聯絡表單
- （選用）綁定自訂網域

## 檔案結構（扁平化，方便手機上傳）

```
vtuber-site/
├── index.html
├── members.html
├── videos.html
├── about.html
├── style.css
├── PROJECT_PLAN.md
└── README.md
```
