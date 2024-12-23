# P2HACKS2024 アピールシート 

プロダクト名  
**FLUSH**

コンセプト  
Flush には、「照れる」という意味がある  
そこから連想される「ツンデレ」がコンセプトの作品  
ツンデレの「ツンツンしている部分」と「デレデレしている部分」の二面性を併せ持つ性質を生かしたチャットアプリ  

対象ユーザ  
 * やる気が維持できない人々  
 * メンタルがきつい人


利用の流れ  
 * サイト、またはスマホアプリ（Android、iPhoneどちらでも可能）で、ツンデレキャラと会話ができる  
 * 自分の友達や好きな人を使用して、ツンデレにして会話ができる  
 * ツンデレキャラは、ユーザの入力からツンデレなテキスト、音声、動画を再生してインタラクションする  

推しポイント  
 * 友達や好きな人をツンデレにすることで、さびしくない！面白い！  
 * ログインして利用すると、ツンデレキャラは、ユーザとの会話を記憶することができる。  
 * ツンデレを統計的に分析した結果を反映した本物のツンデレリアクションを推論している。  
 * ユーザが落ち込んでたり、やる気がないときに、自動的にパラメータが更新されて、出力が変わる。  

  
スクリーンショット(任意)  

## 開発体制  

役割分担  
|担当|担当者|
|----|----|
|マネジメント|鈴木|
|iOS|山本|
|Android|山本、鈴木|
|フロントエンド|山本、島田|
|バックエンド|山本|
|AI|鈴木、山本|
|デザイン|島田|
|文献調査|鈴木|
|発表|山本|
|プレゼン資料|鈴木、島田|  

詳しい分担、タスク表は以下のNotionで管理  
(https://fifth-principle-306.notion.site/1566f83e80b080578dfac0dc9f41d8c2)
  
開発における工夫した点  
 * GPUを積んだサーバで、動画生成・音声合成を行うことでできる限り高速化を図った。  
 * リアルな表情を生成するためにAIのテキスト出力から母音を予測して動画を生成した。
 * シンプルなUIで、簡単に扱えるようにした
 * ユーザの感情に合わせて会話内容が変わることが効果的であることを論理的に示した。
   * 内容は発表資料参照（https://www.canva.com/design/DAGY9qhdg_c/fpFqjE9nkFjHBMuXQgzM2w/edit?utm_content=DAGY9qhdg_c&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton )
 * 沢山のタスクをNotionで役割ごとに管理し、タスクの可視化を行うことで、できる限りタスク漏れのないようにした。


## 開発技術 

利用したプログラミング言語  
 * Typescript
 * Kotlin
 * Swift
 * JavaScript
 * Python

利用したフレームワーク・ライブラリ  
 * Next.js
 * React
 * JetpackCompose
 * SwiftUI

その他開発に使用したツール・サービス  
 * VSCode
 * AndroidStudio
 * Xcode
 * CloudFlare D1
 * CloudFlared
 * CloudFlare R2
 * CloudFlare Workers
 * CloudFlare Tunnel
