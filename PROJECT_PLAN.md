# 星軌計畫 STARPATH — VTuber 團隊官網 企劃書

## 1. 專案簡介

星軌計畫（STARPATH）是由幾位朋友共同發起的獨立 VTuber 團隊。本專案目標是建立一個團隊官方網站，作為觀眾認識成員、掌握直播行程、回顧精選影片，以及了解團隊與合作洽詢的入口。

- **網站性質**：純靜態網站（HTML / CSS / JavaScript），無需後端伺服器
- **託管方式**：GitHub Pages（免費、無用量額度限制，適合純靜態站台）
- **目標受眾**：團隊觀眾、潛在合作方、新粉絲

## 2. 資訊架構（網站頁面）

| 頁面 | 檔案 | 內容狀態 |
|---|---|---|
| 首頁 | `index.html` | ✅ 完整內容（導覽列、橫幅、成員預覽、影片精選、團隊簡介、頁尾）|
| 成員介紹 | `members.html` | 🔲 框架完成，待補完整成員資料 |
| 直播行程 | `schedule.html` | 🔲 框架完成，待補排程格式與時間表 |
| 影片精選 | `videos.html` | 🔲 框架完成，待補影片分類與連結 |
| 關於我們／聯絡我們 | `about.html` | 🔲 框架完成，待補團隊故事與聯絡方式 |

導覽選單（不含首頁，點擊 Logo 可回首頁）：
`成員介紹 / 直播行程 / 影片精選 / 關於我們·聯絡我們`

## 3. 視覺設計規範

**色彩系統**
| 用途 | 色碼 |
|---|---|
| 主背景 | `#0b0f16` |
| 卡片/區塊背景 | `#121821` |
| 分隔線 | `#212b38` |
| 主要文字 | `#eef3f7` |
| 次要文字 | `#a7b3c0` |
| 強調色（電光青） | `#35d6e0` |
| 強調色亮版 | `#7bf0f7` |

**字體**
- 標題／Logo：Space Grotesk（Google Fonts）
- 內文：Inter（Google Fonts）

**版面原則**
- 深色背景 + 淡格線紋理，營造科技/星空氛圍
- 卡片以細邊框與左側強調線區分層次，避免統一圓角陰影的樣板感
- Hero 橫幅圖片可自由更換，疊加漸層與標語文字
- 手機版採漢堡選單，RWD 全面適配

## 4. 技術架構

- 純 HTML5 + CSS3 + Vanilla JavaScript，無框架、無建置流程
- 共用樣式集中於 `assets/style.css`，各頁面共用同一套設計系統
- 圖片目前使用 `placehold.co` 佔位圖，標記 `<!-- TODO -->` 處待換上實際圖片連結（Logo、橫幅、成員照、影片縮圖）

## 5. 檔案結構（扁平化，方便手機上傳無需建資料夾）

```
vtuber-site/
├── index.html          首頁
├── members.html        成員介紹（框架）
├── schedule.html        直播行程（框架）
├── videos.html          影片精選（框架）
├── about.html            關於我們／聯絡我們（框架）
├── style.css              共用樣式
├── PROJECT_PLAN.md       本企劃書
└── README.md             部署操作說明
```

## 6. GitHub Pages 部署步驟（手機版，網頁操作不需打指令）

1. 到 [github.com](https://github.com) 登入帳號，建立一個新的 **Public repository**（例如命名 `starpath-site`），不勾選「Add a README file」
2. 進入空的 repository，點藍字 **uploading an existing file**（或 **Add file → Upload files**）
3. 點 **choose your files**，把解壓縮後的所有檔案一次選取上傳（不用建資料夾，全部放在根目錄）
4. 下方填寫 commit 訊息，點 **Commit changes**
5. 進入 **Settings → Pages**，Source 選擇 `Deploy from a branch`，Branch 選擇 `main` / `/(root)`，儲存
6. 等待 1–2 分鐘，網站會發布在：
   `https://你的帳號.github.io/starpath-site/`
7. 之後要更新內容，直接在 GitHub 網頁上點檔案 → 右上角鉛筆圖示編輯 → Commit changes，會自動重新部署。完全免費、沒有額度限制。

> 如果之後改用電腦操作，也可以改用傳統 Git 指令流程：`git init` → `git add .` → `git commit` → `git remote add origin ...` → `git push`，效果相同。

## 7. 自訂網域（選用）

若之後想綁定自己的網域（例如 `starpath.tw`）：
1. 向網域註冊商購買網域
2. 在 repository 的 `Settings → Pages → Custom domain` 填入網域
3. 到網域註冊商的 DNS 設定中，新增一筆 CNAME 記錄指向 `你的帳號.github.io`
4. GitHub 會自動簽發 HTTPS 憑證

## 8. 後續擴充建議（待討論）

- **聯絡表單**：`about.html` 的合作洽詢表單可串接 [Formspree](https://formspree.io) 免費方案，讓表單直接寄信到指定信箱，不需要自己架後端
- **成員介紹內容**：待提供每位成員的立繪連結、人設文案、社群連結
- **直播行程**：待決定呈現方式（週曆式或列表式）與各成員固定時段
- **影片精選**：待提供 YouTube 影片連結與分類方式（歌回／雜談／遊戲實況）

## 9. 待辦清單

- [ ] 替換 Logo 與橫幅圖片連結
- [ ] 補齊成員介紹頁內容
- [ ] 補齊直播行程頁內容
- [ ] 補齊影片精選頁內容
- [ ] 補齊關於我們／聯絡我們頁內容
- [ ] （選用）串接 Formspree 聯絡表單
- [ ] （選用）綁定自訂網域
