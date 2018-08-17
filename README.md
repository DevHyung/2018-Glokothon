# 2018-Glokothon
======================
# 1. Project Name 'Baby Bot'
## 1.1. Baby bot?
출산전 산모가 봇에 등록을 하여 실제 아이가 크는 것처럼 진화해가는 채팅봇입니다.
It is a chat bot that evolves as a real child grows up by registering with the mother before the birth.

## 1.2. File Description
```
1. chatbot_server.py : 카카오톡 챗봇 서버 파일입니다. 실행시키고 포워딩된 URL을 
                        입력하면 바로 실행가능합니다.
                        KakaoTalk ChatBot server file. You can run it and run 
                        it by typing in the forwarded URL.
                        
2. requirement.txt : db 스키마와 권한 설정 그리고 스케쥴링 등을 create하는데 
                      기술된 파일입니다.
                    It is a file described for creating db schema, 
                    permission setting and scheduling.
```
## 1.3. Process Description
flask를 이용하여 카카오톡 pipe 서버를 엽니다. 그다음 사용자의 message 에 대한 keyboard 타입과, 메세지에 대한 처리 분기구문을 추가하여서 각기에 맞게끔 처리를 하는 Util.py 를 추가하여서 제작합니다.
Use the flask to open the KakaoTalk pipe server. We then create a keyboard type for the user's message, a processing branch for the message, and add Util.py, which is tailored for each.

# 2. Development environment
## 2.1. Testing
Tested on windows and Mac with Python 3.6 
## 2.2. Development Spec
```
RAM : 8G
OS  : windows 10 pro (Ok), Mac OS X (Ok)
GPU : not neccessary
Env : non Framework, using native Env 
        ㄴ Back-End: Flask, MariaDB, PHP
        ㄴ Front-End: HTML, CSS, JS, JQuery, Python3.6.x
```
# 3. How To Use
## 3.1. Command
```python
# after required package install
# Create DB , kakaoTalk Admin setting 
py -3 chatbot_server.py
```