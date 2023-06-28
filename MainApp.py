import kivy
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label

class Main_App(App):
    def build(self):
        return Label(text='Under Construction')

if __name__ == "__main__":
    Main_App().run()
