"""
QR 출석체크 메시지 띄워주는 프로그램
---------------------------------
resource_path() : 상대경로를 절대경로를 바꿔주는 코드.
                  이미지파일을 실행파일에 넣고자 할 경우 입력해야 파일을 찾을 수 있음.
               
프로세스 :   1. Tkinter로 윈도우 인스턴스 생성
            2. QR 코드 이미지를 레이블로 불러옴
            3. 레이블을 윈도우에 붙이고 화면에 출력.

* 추가작업 : 윈도우 작업스케쥴러에서 am.9시, pm.6시에 이 프로그램을 실행하도록 설정.
"""




import os
from tkinter import *


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


window = Tk()
window.title("QR출석체크")

# 현재 작업파일이 있는 상위 디렉토리를 제외하고 상대경로를 입력하면 된다. 
qr_image = PhotoImage(file=resource_path("qr.gif"))
label1 = Label(window, image=qr_image)
#for리눅스용(한줄추가)
label1.image = qr_image

label1.pack()

window.mainloop()


# 상대경로 바꿔주는 코드 입력 안해서 개고생함
# 아래 코드를 터미널창에 입력하면 실행파일 생성됨.
# pyinstaller -w --add-data='*.gif;./' -F -i='qr_icon.ico' .\vs_code\QR_message.py
