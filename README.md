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

## 後台編輯（改文字不用碰程式碼）

網站文字已經抽成 `content.json`（首頁標語、成員預覽卡片、關於我們文案、頁尾社群連結等）與
`channels.json`（YouTube 頻道清單），可以直接從後台網頁編輯、存檔，不用再手動改 HTML。

### 為什麼需要 GitHub Token，不能自己設一組帳密？

這是純靜態網站，沒有伺服器、沒有資料庫，網站上顯示的每個字，實體上就是 GitHub 這個
repository 裡的 `content.json` 檔案。後台按下「儲存」時，一定要有辦法真的去改到 GitHub 上的檔案，
而 GitHub 只認得「有授權的 Token」，不會認得寫死在網頁程式碼裡的密碼（而且寫死的密碼任何人
按右鍵「檢視原始碼」就能看到，形同虛設）。所以 Token 其實同時扮演「密碼」和「真正能存檔的授權」
兩個角色，這是所有靜態網站後台系統（不只這個網站）通用的做法。

為了不用每次都重新貼那一長串 Token，後台加了「解鎖密碼」機制：**Token 只需要貼一次**，
之後會用你自訂的一組解鎖密碼把它**加密**保存在瀏覽器裡（不是明文），下次只要輸入短密碼
就能解鎖繼續編輯。

### 第一步：申請 GitHub Personal Access Token（只需要做一次）

1. 用電腦或手機瀏覽器登入 [github.com](https://github.com)
2. 網址列直接開啟：`https://github.com/settings/personal-access-tokens/new`
   （或手動走：右上角自己的頭像 → **Settings** → 左側選單最下面 **Developer settings** →
   **Personal access tokens** → **Fine-grained tokens** → **Generate new token**）
3. **Token name** 隨意填，例如「網站後台」
4. **Expiration**（有效期限）選一個你覺得合理的天數（例如 90 天或 1 年），之後過期只要
   重新做一次這個步驟、申請一組新的即可，不影響網站本身
5. **Repository access** 選 **Only select repositories**，接著在下拉選單選擇這個網站所在的
   repository（例如 `starpath-site`）
6. 往下捲，找到 **Permissions → Repository permissions**，把 **Contents** 這一項改成
   **Read and write**（其他權限不用動，預設 No access 就好）
7. 捲到最下面按綠色的 **Generate token**
8. 畫面上會出現一長串 `github_pat_...` 開頭的文字，**這是唯一一次會顯示**，請立刻整串複製起來
   （建議先貼到手機備忘錄暫存，關掉這頁之後就再也看不到了，只能重新申請一組新的）

### 第二步：進入後台、貼上 Token、設定解鎖密碼

1. 打開網站首頁，捲到最下面，找到頁尾左下角的團隊 Logo，**連續點擊 5 下**（2 秒內點完），
   會自動跳到隱藏的後台頁面 `admin.html`
2. 第一次使用會看到「初次設定」表單，依序填：
   - **Repository**：填 `你的GitHub帳號/repo名稱`，例如 `abc123/starpath-site`
   - **分支**：不確定就留預設值 `main`
   - **Personal Access Token**：貼上第一步複製的那一長串 `github_pat_...`
   - **設定一組解鎖密碼**：自己想一組好記、但別人猜不到的密碼（建議 6 個字以上）
   - **再輸入一次確認解鎖密碼**：跟上面打一樣的
   - 「在這台裝置加密保存」勾選框：**保持勾選**（除非你是在公用電腦操作，才建議取消勾選）
3. 按 **登入並設定**，系統會先向 GitHub 驗證這組 Token 有沒有效、有沒有寫入權限，成功後
   直接進入編輯畫面

### 之後怎麼登入

- 同一台裝置、同一個瀏覽器：之後打開後台只會看到「輸入解鎖密碼」一個欄位，
  **輸入你剛剛設定的短密碼**就能解鎖進入，不用再貼 Token
- 換了新裝置、或清過瀏覽器資料：會回到「初次設定」畫面，需要重新走一次上面「第一步」
  申請 Token（如果舊的 Token 還沒過期可以直接沿用、不用重新申請，只是要重新貼一次）
- 忘記解鎖密碼：在解鎖畫面點「忘記密碼／要換一組 Token？點這裡重新設定」，
  這只會清除**這台裝置本機保存的加密複本**，不會影響 GitHub 上的 Token，清除後重新走一次
  「初次設定」即可（如果連 Token 是否還有效都不確定，回 GitHub 的 Token 設定頁面重新申請一組新的最保險）

### 開始編輯

登入後可以切換分頁編輯：首頁文字／成員介紹頁／關於我們頁／影片精選頁／社群連結與頁尾／
YouTube 頻道清單，改完按「儲存所有變更」會直接透過 GitHub API 幫你 commit，
GitHub Pages 大約 1 分鐘後就會更新到正式網站，跟自己上 GitHub 網頁編輯的效果一樣。

Token 可以隨時到 `https://github.com/settings/personal-access-tokens` 這個頁面刪除或重新產生，
不會動到你的 GitHub 帳號密碼本身。

## 影片自動抓取（已經做好，只差設定）

`videos.html` 和首頁的「精選影片與直播回顧」已經接好自動抓取機制，不用再手動改程式碼貼影片。
運作方式：

- `.github/workflows/update-videos.yml` 這個 GitHub Actions 排程，每 6 小時會自動執行一次
- `scripts/fetch_videos.py` 會讀取 `channels.json` 裡列出的每個頻道 ID，抓最新影片的
  名稱、簡介、縮圖、來源頻道，並自動判斷是一般影片還是直播回放
- 結果會寫回 `videos.json`，網站前端就會自動顯示最新內容

要讓它真的動起來，只需要做兩件事（都只需要做一次）：

1. **填入每位成員的頻道 ID**：可以直接從剛剛介紹的後台「YouTube 頻道清單」分頁編輯，
   不用手動改 `channels.json`
2. **設定 YouTube API 金鑰**：到 [Google Cloud Console](https://console.cloud.google.com/) 免費申請一組
   YouTube Data API v3 的 API Key，然後到 GitHub repository 的
   **Settings → Secrets and variables → Actions → New repository secret**，
   Name 填 `YOUTUBE_API_KEY`，Value 貼上金鑰。這一步基於安全考量無法從後台網頁完成，
   只需要設定這一次即可

設定完成後，可以到 GitHub 的 **Actions** 分頁手動點一次 `Run workflow` 立即測試，
不用等到下一次排程時間。

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
├── admin.html         隱藏後台編輯頁（首頁 Logo 連點 5 下進入）
├── content.json       網站文字內容（後台編輯的就是這份檔案）
├── channels.json      YouTube 頻道清單（後台也可以編輯）
├── videos.json        自動抓取影片結果（GitHub Actions 自動產生，不用手動改）
├── style.css
├── scripts/fetch_videos.py           影片自動抓取腳本
├── .github/workflows/update-videos.yml   排程設定
├── PROJECT_PLAN.md
└── README.md
```
