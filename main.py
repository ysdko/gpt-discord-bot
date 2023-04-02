import discord
import openai
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()
import os

# OpenAI APIキーを設定
openai.api_key =  os.getenv('OPENAI_API_KEY')

# Discord Bot名を設定
bot_name = os.getenv('BOT_NAME')

# Discord Botトークンを設定
discord_bot_token  = os.getenv('DISCORD_TOKEN')

class ChatGPT:
    def __init__(self, system_setting):
        # システムの設定をセット
        self.system = {"role": "system", "content": system_setting}
        # ユーザーの入力を保持するためのリストを初期化
        self.input_list = [self.system]
        # ログを保持するためのリストを初期化
        self.logs = []

    # ユーザーからの入力を受け取り、OpenAI APIを使って回答を生成
    def input_message(self, input_text):
        # ユーザーの入力をリストに追加
        self.input_list.append({"role": "user", "content": input_text})
        # OpenAI APIを使って回答を生成
        result = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=self.input_list
        )
        # 生成した回答をログに追加
        self.logs.append(result)
        # 生成した回答をリストに追加
        self.input_list.append(
            {"role": "assistant", "content": result.choices[0].message.content}
        )

# Discord Botを作成するための準備
intents = discord.Intents.all()
client = discord.Client(intents=intents)

# Discord Botが起動したときに呼び出される関数
@client.event
async def on_ready():
    print("起動完了")

# Discordでメッセージが送信されたときに呼び出される関数
@client.event
async def on_message(message):
    # Bot自身が送信したメッセージには反応しない
    if message.author == client.user:
        return

    # ユーザーからの質問を受け取る
    if message.clean_content.startswith(bot_name):
        question = message.clean_content.replace(bot_name, '')

        # ChatGPTクラスを使って回答を生成する
        api = ChatGPT(system_setting="あなたは優秀な作家になりきってください。")
        api.input_message(question)

        # 生成した回答を取得する
        answer = api.input_list[-1]["content"]

        # 回答を送信する
        await message.channel.send(answer)

# Discordボットを実行します
client.run(discord_bot_token)
