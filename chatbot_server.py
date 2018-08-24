from flask import Flask
from flask import request
from flask import jsonify
from flask import json
from googletrans import Translator
translator = Translator()
app = Flask(__name__)


@app.route("/keyboard")
def keyboard():
    return jsonify(type="text")


@app.route("/message", methods=["POST"])
def message():

    print(request.data)
    data = json.loads(request.data)
    print(request.headers)
    # request.headers['X-Forwarded-For'] = '110.76.143.234'
    print(request.data)
    content = data["content"]
    ###

    translated = translator.translate(content, dest="en", src="ko")
    result = translated.text
    ###
    text = result
    response = {
        "message": {
            "text": text
        }
    }

    response = json.dumps(response, ensure_ascii=False)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
    #./ngrok http 8888 --region ap