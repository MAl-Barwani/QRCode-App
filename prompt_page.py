import qrcode 
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class PromptPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Decide the number of columns 
        self.cols = 1

        self.add_widget(Label(text="testing"))

        
