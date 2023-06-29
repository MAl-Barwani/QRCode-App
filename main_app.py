from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from prompt_page import PromptPage

class MainApp(App):
    def build(self):
        # Load the prompt page
        self.screen_manager = ScreenManager()
        screen = Screen(name='PromptPage')
        self.prompt_page = PromptPage()
        screen.add_widget(self.prompt_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager
    
    
if __name__ == "__main__":
    MainApp().run()
