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

        # Label for instructions
        self.add_widget(Label(text='Paste the link you want to\n convert in the box below.'))

        # Add TextInput for pasting the link
        self.textinput = TextInput(multiline=False, size_hint=(1,0.2))
        self.add_widget(self.textinput)

        

        # Convert Button
        self.button = Button(text='Convert')
        self.button.bind(on_press=self.generate_qr_code)
        self.add_widget(self.button)
        
    # What happens when I press convert
    def generate_qr_code(self, instance):
        link = self.textinput.text
        img = qrcode.make(link)
        img.save('qrcode.png')




        
