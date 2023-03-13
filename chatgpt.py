from flask import Flask, request, jsonify

app = Flask(__name__)

# 設定 API 路由
@app.route('/hello', methods=['GET'])
def hello():
    return "Hello World!"

# 設定 API 路由，使用 POST 請求進行對話生成
@app.route('/chat', methods=['POST'])
def chat():
    # 從請求中獲取使用者的訊息
    data = request.get_json()
    text = data["text"]

    # 使用 ChatGPT 進行對話生成
    result = chatgpt_generate(text)

    # 將生成的回應打包成 JSON 格式返回
    response = {"result": result}
    return jsonify(response)

# 使用 ChatGPT 進行對話生成的函數
def chatgpt_generate(text):
    # TODO: 使用 ChatGPT API 進行對話生成
    return "Hello, I'm ChatGPT!"

# 啟動 Flask 伺服器
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

