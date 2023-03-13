from flask import Flask, request, abort
import requests
import json
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

# 設定 LINE 聊天機器人的基本資訊
line_channel_secret = "YOUR_LINE_CHANNEL_SECRET"
line_channel_access_token = "YOUR_LINE_CHANNEL_ACCESS_TOKEN"

# 建立 LineBotApi 和 WebhookHandler 實例
line_bot_api = LineBotApi(line_channel_access_token)
handler = WebhookHandler(line_channel_secret)

# 設定 ChatGPT 的 API 資訊
chatgpt_endpoint = "YOUR_CHATGPT_API_ENDPOINT"
chatgpt_api_key = "YOUR_CHATGPT_API_KEY"

# 設定 LINE 聊天機器人的 Webhook URL
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers.get('X-Line-Signature')
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理 LINE 聊天機器人的回應
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text
    user_id = event.source.user_id

    # 使用 ChatGPT API 進行對話生成
    headers = {"Authorization": "Bearer " + chatgpt_api_key}
    data = {"prompt": text, "length": 50}
    response = requests.post(chatgpt_endpoint, headers=headers, data=json.dumps(data))
    result = response.json()["replies"][0]

    # 透過 LINE 聊天機器人發送對話生成的回應
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=result)
    )
