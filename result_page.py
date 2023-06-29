from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.app import App


class ResultPage(GridLayout):
    image = Image(source='qrcode.png', fit_mode='scale-down')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1

        # Display Image
        self.add_widget(self.image)

        # Label to screenshot

        self.add_widget(
            Label(text='Screenshot this QRCode to\n save it to your device.'))

        # Generate Another Code Button
        self.button = Button(text='Generate Another QRCode')
        self.button.bind(on_press=self.go_back)
        self.add_widget(self.button)

    def go_back(self, instance):
        App.get_running_app().root.current = 'PromptPage'
