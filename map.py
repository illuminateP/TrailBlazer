"""
# !todo #
farewell에 메시지 추가 - AI generate
버튼이랑 레이아웃 싹 다듬고 절대위치가 아니라 relativelayout으로 해야 크로스 플랫폼 동작이 되겠죠?
설치 파일로 압축하는 모듈이 있을거고
테스트도 해야 하고  

# !rule #
1. myAPp 안에서는 Pascal , 밖에서는 snake로 선언
2. 되도록 위젯만 MyApp 안에 추가
3. 기능 관련 기능은 다 밖으로 빼서 선언
4. 위젯에 한국어 등록할 때는 전부 font_name='youth' 있어야 함
5. 메인에서 kivy 받아 와서 사용

"""

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.popup import Popup
import os

# 현재 파일이 있는 디렉토리 경로 가져오기
current_dir = os.path.dirname(__file__)

# 이미지 파일 경로 설정 (상대 경로)
image_path = os.path.join(current_dir, "images", "map.png")

def show_image(app):
    # 이미지 경로 설정
    image_path = "path/to/your/image.jpg"  

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