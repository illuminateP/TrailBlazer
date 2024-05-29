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
4. 위젯에 한국어 등록할 때는 전부 font_name='youth' 있어야 함\
5. 이거 모듈화 해야 함

# !note #
1. kivy는 한글 지원 안 해서 폰트로 받아와야 하는데 , 그게 안 되는 Ending_Messages 부분에는 custom title 바 추가하거나 (llama3) , 
    그냥 타이틀에 한글 쳐박으면 된다고 우기거나(gpt4o) 하는데 에러 메시지에 정답이 써 있었음
    결론 : AI는 생각보다 멍청하니까 너무 의존하지 말고 공식 문서를 먼저 보자
    Popup(title = '잘 가요! 이거 만드느라 얼마나 고생했는지 당신은 모를 거에요', title_font='youth' , content=Toast_Layout, auto_dismiss=False, size_hint=(0.8, None))
    -> 이거 title_font 추가해야 한다는 거 프로퍼티 에러 메시지
  TypeError: Properties ['font_name'] passed to __init__ may not be existing property names. Valid properties are 
  ['_anim_alpha', '_anim_duration', '_container', '_is_open', '_window', 'anchor_x', 'anchor_y', 'attach_to', 'auto_dismiss', 'background', 'background_color', 'border', 'center', 'center_x', 'center_y', 'children', 'cls', 'content', 'disabled', 'height', 'ids', 'motion_filter', 'opacity', 'overlay_color', 'padding', 'parent', 'pos', 'pos_hint', 'right', 'separator_color', 'separator_height', 
  'size', 'size_hint', 'size_hint_max', 'size_hint_max_x', 'size_hint_max_y', 'size_hint_min', 'size_hint_min_x', 'size_hint_min_y', 'size_hint_x', 'size_hint_y', 'title', 'title_align', 'title_color', 'title_font', 'title_size', 'top', 'width', 'x', 'y']
  여기서 찾음

  2. 한글 지원 안 되는 라이브러리 쓰니까 진짜 ㅆ
  아니 힘들었다

  3.내가 프론트를 더럽게 못 하는데 AI가 대신 해 줘서 편했다

  4.자료가 정말 없고 그나마 있는 것도 영어 자료니까 한국어로 물어볼 때 AI도 이상한 소리를 많이 한다

"""
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.text import LabelBase
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.core.window import Window

import fonts
import utils

# MyApp 외부 메서드 , 선언 규칙 : Pascal
class MainScreen(Screen):
    def __init__(self, app, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.app = app
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        
        # init 시 폰트 등록
        fonts.register_fonts()

        start_button = Button(text='시작', size_hint=(1, 0.5), font_name='youth')
        start_button.bind(on_press=self.start_button_clicked)
        self.layout.add_widget(start_button)

        first_button = Button(text='1번째 기능', size_hint=(1, 0.5), font_name='youth')
        first_button.bind(on_press=self.first_button_clicked)
        self.layout.add_widget(first_button)

        second_button = Button(text='2번째 기능', size_hint=(1, 0.5), font_name='youth')
        second_button.bind(on_press=self.second_button_clicked)
        self.layout.add_widget(second_button)

        third_button = Button(text='3번째 기능', size_hint=(1, 0.5), font_name='youth')
        third_button.bind(on_press=self.third_button_clicked)
        self.layout.add_widget(third_button)

        exit_button = Button(text='종료', size_hint=(1, 0.5), font_name='youth')
        exit_button.bind(on_press=self.exit_button_clicked)
        self.layout.add_widget(exit_button)
        
        self.add_widget(self.layout)
        
    def start_button_clicked(self, instance):
        print("시작 버튼이 클릭되었습니다.")

    def first_button_clicked(self, instance):
        print("기능 1번 버튼 클릭")
        self.app.switch_to('first_screen') 

    def second_button_clicked(self, instance):
        print("기능 2번 버튼 클릭")

    def third_button_clicked(self, instance):
        print("기능 3번 버튼 클릭")
        
    def exit_button_clicked(self, instance):
        utils.Ending_Messages(self.app)
    
        
        


class First_Screen(Screen):
    def __init__(self, app, **kwargs):
        super(First_Screen, self).__init__(**kwargs)
        self.app = app
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        print("FS!")
        
        exit_button = Button(text='종료', size_hint=(1, 0.5), font_name='youth')
        # 닫기 버튼을 눌렀을 때 종료창 호출
        exit_button.bind(on_press=self.exit_button_clicked)
        
        self.layout.add_widget(exit_button)
        self.add_widget(self.layout)

    def back_to_main(self, instance):
        self.app.switch_to(MainScreen(self.app))
        
    def exit_button_clicked(self, instance):
        utils.Ending_Messages(self.app)
    
        
class MyScreenManager(ScreenManager):  # ScreenManager 추가
    def __init__(self, app, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)
        self.app = app       

class MyApp(App):
    def build(self):
        self.app = App
        self.screen_manager = MyScreenManager(self)
        self.main_screen = MainScreen(self, name='main_screen')  # 수정: name 추가
        self.first_screen = First_Screen(self, name='first_screen')  # 수정: name 추가
        
        self.screen_manager.add_widget(self.main_screen)
        self.screen_manager.add_widget(self.first_screen)
        
        Window.bind(on_request_close=self.on_request_close)
        return self.screen_manager

    def switch_to(self, screen_name):
        self.screen_manager.current = screen_name

    def toast_messages(self, title, message):
        toast_label = Label(text=message, font_name='youth')
        toast_popup = Popup(title=title, content=toast_label, auto_dismiss=False, size_hint=(None, None), size=(200, 100))
        toast_popup.open()
    
    def exit_button_clicked(self, instance):
        utils.Ending_Messages(self.app)
    
    def on_request_close(self, *args):
        utils.Ending_Messages(self.app)
        return True
    