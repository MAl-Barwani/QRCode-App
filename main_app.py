from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from prompt_page import PromptPage
from result_page import ResultPage


class MainApp(App):
    def build(self):
        # Load the prompt page
        self.screen_manager = ScreenManager()
        screen = Screen(name='PromptPage')
        self.prompt_page = PromptPage()
        screen.add_widget(self.prompt_page)
        self.screen_manager.add_widget(screen)

        # Load the result page
        screen = Screen(name='ResultPage')
        self.result_page = ResultPage()
        screen.add_widget(self.result_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


if __name__ == "__main__":
    MainApp().run()
