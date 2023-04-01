# ChatGPT Discord Bot
このREADMEでは、Discordで動作するChatGPTボットのセットアップと使用方法について説明します。

## 前提条件
Python 3.10がインストールされていること
Discordアカウントが作成されていること
OpenAI APIキーが取得されていること
依存関係のインストール
このプロジェクトでは、以下のPythonライブラリが必要です。

discord.py
openai
python-dotenv
以下のコマンドで、これらのライブラリをインストールできます。

```
pip install discord.py openai python-dotenv
```

##設定ファイルの作成
プロジェクトディレクトリに.envファイルを作成します。
次の環境変数をファイルに追加します。

```
OPENAI_API_KEY=<your_openai_api_key>
BOT_NAME=<your_bot_name>
DISCORD_TOKEN=<your_discord_bot_token>
```
各環境変数を実際の値に置き換えてください。

## ボットの実行
プロジェクトディレクトリで、次のコマンドを実行してボットを起動します。

```
python main.py
```
##使用方法
ボットをDiscordサーバーに招待します。
メッセージチャンネルで、ボット名に続けて質問を入力します。
ボットがOpenAI GPT-3.5-turboモデルを使用して回答を生成し、メッセージチャンネルに送信します。
例:

```
<your_bot_name> こんにちは！
```
ボットは、「こんにちは！」と回答します。

## クラスと関数の説明
ChatGPT クラス: ユーザーからの入力を受け取り、OpenAI APIを使用して回答を生成します。
on_ready 関数: ボットが起動したときに呼び出されます。
on_message 関数: メッセージが送信されたときに呼び出されます。ユーザーからの質問を受け取り、ChatGPTクラスを使用して回答を生成し、メッセージチャンネルに送信します。
## 注意事項
このボットはデモンストレーション目的で作成されており、実際のアプリケーションでの使用には適切なエラーハンドリングやセキュリティ対策が必要です。