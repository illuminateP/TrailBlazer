from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.text import LabelBase
from kivy.uix.label import Label
from kivy.uix.popup import Popup
import os
import random

# 현재 파일의 디렉토리 경로
current_dir = os.path.dirname(os.path.abspath(__file__))

# 폰트 파일의 상대 경로를 생성합니다.
font_path = os.path.join(current_dir, 'fonts', 'Youth.ttf')

# 청소년체 'youth'라는 이름으로 사용
LabelBase.register(name='youth', fn_regular=font_path)

# 프로그램 종료 시 메시지를 출력하는 메서드
def farewell():
    li = ['안녕', '잘가', '이건 테스트 메시지야', '이렇게 대충 좋은 말 하면서', '작별 인사를 하면', '좀', '있어 보이겠지?']
    random_num = random.randint(0, len(li) - 1)
    return li[random_num]

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        # 시작 버튼
        start_button = Button(text='시작', size_hint=(1, 0.5), font_name='youth')
        start_button.bind(on_press=self.start_button_clicked)
        layout.add_widget(start_button)

        # 1번째 기능 버튼
        first_button = Button(text='1번째 기능', size_hint=(1, 0.5), font_name='youth')
        first_button.bind(on_press=self.first_button_clicked)
        layout.add_widget(first_button)

        # 2번째 기능 버튼
        second_button = Button(text='2번째 기능', size_hint=(1, 0.5), font_name='youth')
        second_button.bind(on_press=self.second_button