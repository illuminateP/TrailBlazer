from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
import difflib
import map

class InputForm(BoxLayout):
    text_input = ObjectProperty(None)
    hint_label = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(InputForm, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.text_input = TextInput(size_hint=(1, None), height=30)
        self.hint_label = TextInput(size_hint=(1, None), height=30, readonly=True)
        self.text_input.bind(text=self.update_hint)
        self.add_widget(self.text_input)
        self.add_widget(self.hint_label)
        self.hints = self.load_hints()

    def load_hints(self):
        graph_manager = map.create_graph()
        labels = [data['label'] for node, data in graph_manager.get_graph().nodes(data=True)]
        return labels

    def update_hint(self, instance, value):
        if value:
            hint = difflib.get_close_matches(value, self.hints, n=1)
            self.hint_label.text = hint[0] if hint else ''
        else:
            self.hint_label.text = ''
