"""
##################################################################################
# !rule #
1. TrailBlazer.py -> 구동부
2. screens.py -> 화면 내 로직과 위젯 관리 , 위젯부와 로직부 분리할 지 생각 중이다. 현재는 스크린 내 로직도 작성되어 있다.
screen 명 작성 규칙 : snake
3. utils.py -> 종료와 farewell 기능 불러오는 위젯이고 화면 구성 시 종료 , 취소 버튼과 screen 내에서 binding한다.
4. fonts.py -> 폰트 불러오는 모듈 , first_screen __init__가 아니라 myAPP build 시로 가야 한다.
5. strings.py -> 사용할 스트링 불러오는 모델 , fonts.py랑 묶어서 처리하도록 바꿔야 한다
6. map.py -> 지도 기능에 사용할 모듈이고 기능별로 모듈 분리할거면 first_screen 여기다 붙혀야 한다.


7. 위젯에 한국어 등록할 때는 전부 font_name='youth' 있어야한다. 이는 비 라틴언어 모두에 해당하며 , 영어 제외하면 폰트 전부 적어줘야 한다.
8. 기능별로 모듈 분리할지 , 화면별로 분류해서 Screen.py에 배치할 지 생각 , 내부 로직부분과 분리하는 게 좋을 것 같은데


##################################################################################


"""

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.popup import Popup
import os


def Show_Image(app):
    
    # 현재 파일이 있는 디렉토리 경로 가져오기
    current_dir = os.path.dirname(__file__)

    # 이미지 파일 경로 설정 (상대 경로)
    image_path = os.path.join(current_dir, "assets", "blueprintmap.png")


    # 이미지 뷰 생성
    image_widget = Image(source=image_path)

    # 종료 버튼 생성
    exit_button = Button(text='종료', size_hint=(1, 0.5), font_name='youth')
    exit_button.bind(on_press=lambda instance: app.root_window.close())  # MyApp의 root_window 닫기

    # 레이아웃 생성
    layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
    layout.add_widget(image_widget)
    layout.add_widget(exit_button)

    # 팝업 생성
    popup = Popup(title="Image", content=layout, size_hint=(0.5, 0.5))
    popup.open()