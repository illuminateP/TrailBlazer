from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.text import LabelBase
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.core.window import Window

import os
import random

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

# 현재 파일의 디렉토리 경로
current_dir = os.path.dirname(os.path.abspath(__file__))

# 폰트 파일의 상대 경로를 생성합니다.
font_path_y = os.path.join(current_dir, 'fonts', 'Youth.ttf')
font_path_c = os.path.join(current_dir, 'fonts', 'Chosun.ttf')

# 청소년체 'youth'라는 이름으로 사용
LabelBase.register(name='youth', fn_regular=font_path_y)
# 궁서체 'chosun'이라는 이름으로 사용
LabelBase.register(name='chosun', fn_regular=font_path_c)

# MyApp 외부 메서드 , 선언 규칙 : snake ,
# !farewell #
# 프로그램 종료 시 메시지를 출력하는 메서드#
def farewell():
    li = ['안녕' , '잘가' , '이건 테스트 메시지야','이렇게 대충 좋은 말 하면서','작별 인사를 하면','좀','있어 보이겠지?']
    random_num = random.randint(0,len(li)-1)
    return li[random_num]

# !MyApp #
class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        # 시작 버튼
        start_button = Button(text='시작', size_hint=(1, 0.5), font_name='youth')
        start_button.bind(on_press=self.Start_Button_Clicked)
        layout.add_widget(start_button)

        # 1번째 기능 버튼
        first_button = Button(text='1번째 기능', size_hint=(1, 0.5), font_name='youth')
        first_button.bind(on_press=self.First_Button_Clicked)   
        layout.add_widget(first_button)

        # 2번째 기능 버튼
        second_button = Button(text='2번째 기능', size_hint=(1, 0.5), font_name='youth')
        second_button.bind(on_press=self.Second_Button_Clicked)
        layout.add_widget(second_button)   

        # 3번째 기능 버튼
        third_button = Button(text='3번째 기능', size_hint=(1, 0.5), font_name='youth')
        third_button.bind(on_press=self.Third_Button_Clicked)
        layout.add_widget(third_button)  

        # 종료 버튼
        exit_button = Button(text='종료', size_hint=(1, 0.5), font_name='youth')
        exit_button.bind(on_press=self.Exit_Button_Clicked)
        layout.add_widget(exit_button) 

        # x 버튼으로 창을 닫는 경우 구현  
        Window.bind(on_request_close=self.on_request_close)
        return layout
    
    # 내부 메서드 정의 , 선언 규칙 : Pascal , 메서드 내 property : snake

    # !Toast_Messages #
    # 토스트 메시지 출력하는 메서드 , parameter : 제목 , 내용 , default : auto_dismiss = false #
    def Toast_Messages(self, Title , Message):
        toast_label = Label(text=Message, font_name='youth')
        toast_popup = Popup(title=Title, content=toast_label, auto_dismiss=False, size_hint=(None, None), size=(200, 100))
        toast_popup.open()

    def Start_Button_Clicked(self, instance):
        print("시작 버튼이 클릭되었습니다.")
    
    def First_Button_Clicked(self,instance):
        print("기능 1번 버튼 클릭")

    def Second_Button_Clicked(self,instance):
        print("기능 2번 버튼 클릭")

    def Third_Button_Clicked(self,instance):
        print("기능 3번 버튼 클릭")

    
    def Ending_Messages(self):
        Message = farewell()
        print(Message)

        toast_label = Label(text=Message, font_name='chosun', size_hint_y=None, height=120)  # Label 높이 설정

        def cancel_toast(instance):
            toast_popup.dismiss()
            
        def close_toast(instance):
            toast_popup.dismiss()
            App.get_running_app().stop()

        cancel_button = Button(text='닫기', font_name='youth')  # 버튼 높이 설정
        cancel_button.bind(on_press=close_toast)

        close_button = Button(text='취소', font_name='youth')  # 버튼 높이 설정
        close_button.bind(on_press=cancel_toast)

        Toast_Layout = BoxLayout(orientation='vertical', padding=[20, 20, 20, 20], spacing=20)
        Toast_Layout.add_widget(toast_label)

        Button_Layout = BoxLayout(orientation='horizontal', padding=[10, 10, 10, 10], spacing=20, size_hint=(1, None), height=60)
        Button_Layout.add_widget(cancel_button) 
        Button_Layout.add_widget(close_button)

        Toast_Layout.add_widget(Button_Layout)


        toast_popup = Popup(title = '잘 가요! 이거 만드느라 얼마나 고생했는지 당신은 모를 거에요', title_font='youth' , content=Toast_Layout, auto_dismiss=False, size_hint=(0.8, None),height=300)
        toast_popup.open()  


        
    # x 표시 눌렀을 때 랜덤 메시지와 함께 창 닫히는 기능 구현    
    def on_request_close(self, *args):
        self.Ending_Messages()
        return True
    
    # 닫기 버튼 눌렀을 때 랜덤 메시지와 함께 창 닫히는 기능 구현 
    def Exit_Button_Clicked(self, instance):
        self.Ending_Messages()
    
if __name__ == '__main__':
    MyApp().run()
