import qrcode 
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.app import App
from result_page import ResultPage
from kivy.uix.image import Image

class PromptPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Decide the number of columns 
        self.cols = 1

        # Label for instructions
        self.add_widget(Label(text='Paste the link you want to\n convert in the box below.', font_size=20))

        # Add TextInput for pasting the link
        self.textinput = TextInput(multiline=False, size_hint=(1,0.2))
        self.add_widget(self.textinput)

 

        # Convert Button
        self.button = Button(text='Convert to QRCode', font_size=20)
        self.button.bind(on_press=self.generate_qr_code)
        self.add_widget(self.button)
        
    # What happens when I press convert
    def generate_qr_code(self, instance):
        # Generate the QR Code
        link = self.textinput.text
        img = qrcode.make(link)
        img.save('qrcode.png')
        #Reload next scene's QRCode
        ResultPage.image.reload()
        # Move to the results page
        App.get_running_app().root.current = 'ResultPage'




        
