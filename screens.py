"""
# !rule #
1 . TrailBlazer.py -> 구동부
2. screens.py -> 화면 내 로직과 위젯 관리 , 위젯부와 로직부 분리할 지 생각 중이다. 현재는 스크린 내 로직도 작성되어 있다.
screen 명 작성 규칙 : snake 
★ screen 추가 시 1) 이름이 소문자인지 , snake 규칙을 따르는지 확인하고
2)
class first_screen(Screen):
    def __init__(self, app, **kwargs):
        super(first_screen, self).__init__(**kwargs)
        self.app = app
    으로 init시 app parameter passing 확인하며
3)
class MyApp(App):
    def build(self):
        self.screen_manager.add_widget(self.main_screen)
        self.screen_manager.add_widget(self.first_screen)
    로 screen_mananger에 스크린 등록하고 있는지 확인!  
    
3. utils.py -> 종료와 farewell 기능 불러오는 위젯이고 화면 구성 시 종료 , 취소 버튼과 screen 내에서 binding한다.
4. fonts.py -> 폰트 불러오는 모듈 , first_screen __init__가 아니라 myAPP build 시로 가야 한다.
5. strings.py -> 사용할 스트링 불러오는 모델 , fonts.py랑 묶어서 처리하도록 바꿔야 한다
6. map.py -> 지도 기능에 사용할 모듈이고 기능별로 모듈 분리할거면 first_screen 여기다 붙혀야 한다.


7. 위젯에 한국어 등록할 때는 전부 font_name='youth' 있어야한다. 이는 비 라틴언어 모두에 해당하며 , 영어 제외하면 폰트 전부 적어줘야 한다.
8. 기능별로 모듈 분리할지 , 화면별로 분류해서 Screen.py에 배치할 지 생각 , 내부 로직부분과 분리하는 게 좋을 것 같은데

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
from kivy.garden.mapview import MapView

import fonts
import utils

import os

# MyApp 외부 메서드 , 선언 규칙 : 스크린 = snake , 위젯 , 위젯 바인딩 메서드 = _pascal
class main_screen(Screen):
    def __init__(self, app, **kwargs):
        super(main_screen, self).__init__(**kwargs)
        self.app = app
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        
        # init 시 폰트 등록
        fonts.register_fonts()

        First_Button = Button(text='길찾기 기능!', size_hint=(1, 0.5), font_name='youth')
        First_Button.bind(on_press=self.First_Button_Clicked)
        self.layout.add_widget(First_Button)

        Second_Button = Button(text='2번째 기능', size_hint=(1, 0.5), font_name='youth')
        Second_Button.bind(on_press=self.Second_Button_Clicked)
        self.layout.add_widget(Second_Button)

        Third_Button = Button(text='3번째 기능', size_hint=(1, 0.5), font_name='youth')
        Third_Button.bind(on_press=self.Third_Button_Clicked)
        self.layout.add_widget(Third_Button)

        Exit_Button = Button(text='종료', size_hint=(1, 0.5), font_name='youth')
        Exit_Button.bind(on_press=self.Exit_Button_Clicked)
        self.layout.add_widget(Exit_Button)
        
        self.add_widget(self.layout)

    def First_Button_Clicked(self, instance):
        print("first button pressed")
        self.app.Switch_To('first_screen') 

    def Second_Button_Clicked(self, instance):
        print("second button pressed")

    def Third_Button_Clicked(self, instance):
        print("third button pressed")
        
    def Exit_Button_Clicked(self, instance):
        utils.Ending_Messages(self.app)
    
        
        

# 길찾기 제공하는 화면 
class first_screen(Screen):
    def __init__(self, app, **kwargs):
        super(first_screen, self).__init__(**kwargs)
        self.app = app
        self.layout = BoxLayout(orientation='horizontal', spacing=10, padding=20)
        self.toolbar = BoxLayout(orientation='vertical', spacing=10, padding=20)
        
        # main_screen으로 돌아가는 버튼
        Back_Button = Button(text='뒤로 가기', size_hint=(1, 0.5), font_name='youth')
        Back_Button.bind(on_press=self.Back_To_Main)
        self.toolbar.add_widget(Back_Button)
        
        First_Functional_Button = Button(text='첫 번째 기능', size_hint=(1, 0.5), font_name='youth')
        First_Functional_Button.bind(on_press=self.First_Functional_Button_Clicked)
        self.toolbar.add_widget(First_Functional_Button)
        
        Second_Functional_Button = Button(text='두 번째 기능', size_hint=(1, 0.5), font_name='youth')
        Second_Functional_Button.bind(on_press=self.Second_Functional_Button_Clicked)
        self.toolbar.add_widget(Second_Functional_Button)
        
        
        Third_Functional_Button = Button(text='세 번째 기능', size_hint=(1, 0.5), font_name='youth')
        Third_Functional_Button.bind(on_press=self.Third_Functional_Button_Clicked)
        self.toolbar.add_widget(Third_Functional_Button)

        Fourth_Functional_Button = Button(text='네 번째 기능', size_hint=(1, 0.5), font_name='youth')
        Fourth_Functional_Button.bind(on_press=self.Fourth_Functional_Button_Clicked)
        self.toolbar.add_widget(Fourth_Functional_Button)

        Fifth_Functional_Button = Button(text='다섯 번째 기능', size_hint=(1, 0.5), font_name='youth')
        Fifth_Functional_Button.bind(on_press=self.Fifth_Functional_Button_Clicked)
        self.toolbar.add_widget(Fifth_Functional_Button)
        
        # 닫기 버튼을 눌렀을 때 종료창 호출
        Exit_Button = Button(text='종료', size_hint=(1, 0.5), font_name='youth')
        Exit_Button.bind(on_press=self.Exit_Button_Clicked)
        self.toolbar.add_widget(Exit_Button)
        
        self.layout.add_widget(self.toolbar)
        
        # 맵뷰와 이미지 겹쳐 표시할 위젯
        self.map_layout = BoxLayout(orientation='horizontal', spacing=10, padding=20)
        self.map_view = MapView(zoom=11, lat=37.7749, lon=-122.4194, size_hint=(1, 0.7))  # Example coordinates for San Francisco
        
        current_dir = os.path.dirname(__file__)
        image_path = os.path.join(current_dir, "assets", "blueprintmap.png")
        Image_Blueprint = Image(source=image_path)
        self.map_layout.add_widget(self.map_view)
        self.map_layout.add_widget(Image_Blueprint)

        self.layout.add_widget(self.map_layout)
        self.add_widget(self.layout)
    

    
    def Back_To_Main(self, instance):
        self.app.Switch_To('main_screen') 

        
    def Exit_Button_Clicked(self, instance):
        utils.Ending_Messages(self.app)
    
    def First_Functional_Button_Clicked(self,instance):
        print("First Functinal Button clicked!")
        
    def Second_Functional_Button_Clicked(self,instance):
        print("Second Functional Button clicked!")
    
    def Third_Functional_Button_Clicked(self,instance):
        print("Third Functional Button clicked!")
        
    def Fourth_Functional_Button_Clicked(self,instance):
        print("Fourth Functional Button clicked!")
          
    def Fifth_Functional_Button_Clicked(self,instance):
        print("Fifth Functional Button clicked!")
    
    

""" 
# map.py 내용 보여줄 스크린
class map_screen(Screen):
    def __init__(self, app, **kwargs):
        super(map_screen, self).__init__(**kwargs)
        self.app = app
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        
        # 지도 이미지 설정
        self.image = Image(source="assets/blueprintmap.png")
        self.layout.add_widget(self.image) 

        # 뒤로 가기 버튼
        Back_Button = Button(text='뒤로 가기', size_hint=(1, 0.5), font_name='youth')
        Back_Button.bind(on_press=self.Back_To_First)
        self.layout.add_widget(Back_Button)

        # 종료 버튼
        Exit_Button = Button(text='종료', size_hint=(1, 0.5), font_name='youth')
        Exit_Button.bind(on_press=self.Exit_Button_Clicked)
        self.layout.add_widget(Exit_Button)

        self.add_widget(self.layout)

    def Back_To_First(self, instance):
        self.app.Switch_To('first_screen')

    def Exit_Button_Clicked(self, instance):
        utils.Ending_Messages(self.app)        
    
"""       
class MyScreenManager(ScreenManager):  # ScreenManager 추가
    def __init__(self, app, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)
        self.app = app       

class MyApp(App):
    def build(self):
        self.app = App
        self.screen_manager = MyScreenManager(self)
        fonts.register_fonts()
        
        self.main_screen = main_screen(self, name='main_screen')  
        self.first_screen = first_screen(self, name='first_screen')  
        
        
        self.screen_manager.add_widget(self.main_screen)
        self.screen_manager.add_widget(self.first_screen)
        
        # 창에 상관없이 전역적으로 처리 
        Window.bind(on_request_close=self.on_request_close)
        return self.screen_manager

    def Switch_To(self, screen_name):
        self.screen_manager.current = screen_name

    def Toast_Messages(self, title, message):
        toast_label = Label(text=message, font_name='youth')
        toast_popup = Popup(title=title, content=toast_label, auto_dismiss=False, size_hint=(None, None), size=(200, 100))
        toast_popup.open()
    
    def Exit_Button_Clicked(self, instance):
        utils.Ending_Messages(self.app)
    
    def on_request_close(self, *args):
        utils.Ending_Messages(self.app)
        return True
    