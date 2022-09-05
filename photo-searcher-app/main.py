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
        (                           # to avoid \ for newline
            self                    # FirstSceen instance, root on .kv file
            .manager                # RootWidget
            .current_screen         # FirstScreen, i think
            .ids                    # list of ids
            .img                    # see frontend.kv
            .source                 # see frontend.kv
        ) = 'files/sunny.jpg'       # set image file for img


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
