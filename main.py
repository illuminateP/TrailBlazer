from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        start_button = Button(text='시작', size_hint=(1, 0.5))
        start_button.bind(on_press=self.start_button_clicked)
        layout.add_widget(start_button)

        exit_button = Button(text='종료', size_hint=(1, 0.5))
        exit_button.bind(on_press=self.exit_button_clicked)
        layout.add_widget(exit_button)

        return layout

    def start_button_clicked(self, instance):
        print("시작 버튼이 클릭되었습니다.")

    def exit_button_clicked(self, instance):
        App.get_running_app().stop()

if __name__ == '__main__':
    MyApp().run()