# The four main objects of Kivy
#
#                     +------------------+
#                     |       App        |
#                     +------------------+
#
#                     +------------------+
#                     |   ScreenManager  |
#                     +------------------+
#
#                     +------------------+
#                     |      Screen      |
#                     +------------------+
#
#                     +------------------+
#                     |      Widget      |
#                     +------------------+
#
################################################################################
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file('frontend.kv')


class FirstScreen(Screen):          # one for every screen
    def search_image(self):         # logic of screen
        pass


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
