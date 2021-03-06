from flask import Flask
from flask import request
from flask import jsonify
from flask import json
import Util
#=== CONFIG VAR
Util.update_db() #init
USER_DICT,BABY_DICT,AGE_DICT = Util.get_all_data()
button_List = ["의료 정보","음식 정보","태교 정보"]
#====================
app = Flask(__name__)
@app.route("/keyboard")
def keyboard():
    return jsonify(type="text")

@app.route("/message", methods=["POST"])
def message():
    global USER_DICT,BABY_DICT,AGE_DICT
    data = json.loads(request.data)
    content = data["content"]
    if data['user_key'] not in USER_DICT.keys():
        USER_DICT[data['user_key']] = {'IS_TALK_MODE':False}
        BABY_DICT[data['user_key']] = ''
        AGE_DICT[data['user_key']] = ''

    ### Code
    if content == '아기랑 대화하기' and not USER_DICT[data['user_key']]['IS_TALK_MODE']:#대화모드를 맨처음 클릭하셨을때
        USER_DICT[data['user_key']]['IS_TALK_MODE'] = True
        response = Util.return_res_by_code(1)
        response['message']['text'] = '{}(이)한테 하고 싶은말 적어주세요 ~'.format(BABY_DICT[data['user_key']])

    elif content == '엄마가' and USER_DICT[data['user_key']]['IS_TALK_MODE']:#대화모드에서 종료
        USER_DICT[data['user_key']]['IS_TALK_MODE'] = False
        response = Util.return_res_by_code(2)

    elif content == '아기 정보입력' or content.replace(' ','') == '아기정보입력':#
        response = Util.return_res_by_code(3)

    elif  USER_DICT[data['user_key']]['IS_TALK_MODE']:#대화 모드 중일 때
        Util.register_talk(data['user_key'],content)
        response = Util.return_res_by_code(-1)
        print(content)
    elif content not in button_List:#아기정보입력되었을때 여기서 나중에 처리해줘야함
        response = Util.return_res_by_code(0)
        babyname, age = content.split(',')
        BABY_DICT[data['user_key']] =babyname
        AGE_DICT[data['user_key']] = age
        Util.register_baby(data['user_key'],babyname.strip(),age.strip())
        response['message']['text'] = '{}(이)의 정보가 입력되었습니다 ~'.format(babyname)
    elif content == '태교 정보':
        response = Util.return_res_by_code(0)
        response['message']['text'] = Util.recommend_tagyo()
    elif content == '의료 정보':
        response = Util.return_res_by_code(0)
        response['message']['text'] = Util.recommend_medi(AGE_DICT[data['user_key']])
    elif content == '음식 정보':
        response = Util.return_res_by_code(0)
        response['message']['text'] = Util.recommend_food()
    else: # 기본 FAQ 모드일때
        response = Util.return_res_by_code(0)
    # return res
    response = json.dumps(response, ensure_ascii=False)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
    #./ngrok http 8888 --region ap