from flask import Flask
from flask import request
from flask import jsonify
from flask import json
from googletrans import Translator
import Util
#=== CONFIG
IS_TALK_MODE = False


#====================
translator = Translator()
app = Flask(__name__)


@app.route("/keyboard")
def keyboard():
    return jsonify(type="text")


@app.route("/message", methods=["POST"])
def message():
    global IS_TALK_MODE
    data = json.loads(request.data)
    content = data["content"]
    ###

    translated = translator.translate(content, dest="en", src="ko")
    result = translated.text
    ###
    text = result
    if content == '아기랑 대화하기' and not IS_TALK_MODE:#대화모드를 맨처음 클릭하셨을때
        IS_TALK_MODE = True
        response = Util.return_res_by_code(1)
    elif IS_TALK_MODE:#대화 모드 중일 때
        response = Util.return_res_by_code(2)
    elif content == '대화종료' and IS_TALK_MODE:#대화모드에서 종료
        IS_TALK_MODE = False
        response = Util.return_res_by_code(0)
    else:
        response = Util.return_res_by_code(0)

    response = json.dumps(response, ensure_ascii=False)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
    #./ngrok http 8888 --region ap