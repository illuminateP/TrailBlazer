from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
import difflib
import map

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
import difflib
import map

class InputForm(BoxLayout):
    text_input = ObjectProperty(None)
    hint_label = ObjectProperty(None)

    def __init__(self, layout, on_search_callback, **kwargs):
        super(InputForm, self).__init__(**kwargs)

        self.text_input = TextInput(size_hint=(1, None), height=30, font_name='youth', multiline=False)
        self.text_input.bind(on_text_validate=on_search_callback)  # Enter 키가 눌렸을 때 on_search_callback 호출
        self.text_input.bind(text=self.update_hint)
        layout.add_widget(self.text_input)

        self.hint_label = TextInput(size_hint=(1, None), height=30, readonly=True, font_name='youth', opacity=0)
        layout.add_widget(self.hint_label)
        self.hints = self.load_hints()

    def load_hints(self):
        graph_manager = map.create_graph()
        labels = [data['name'] for node, data in graph_manager.get_graph().nodes(data=True)]
        return labels

    def update_hint(self, instance, value):
        print("!")
        if value:
            hint = difflib.get_close_matches(value, self.hints, n=1)
            self.hint_label.text = hint[0] if hint else ''
            self.hint_label.opacity = 1 if hint else 0
        else:
            self.hint_label.text = ''
            self.hint_label.opacity = 0
    