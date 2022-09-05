import os

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.logger import Logger
from kivy.core.clipboard import Clipboard
import webbrowser
import time

from filesharer import FileSharer

Builder.load_file('frontend.kv')


class CameraScreen(Screen):
    def start(self):
        """
        Starts camera and changes button text
        """
        self.ids.camera.opacity = 1
        self.ids.camera.play = True
        self.ids.camera_button.text = 'Stop Camera'
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        """
        Stops camera and changes button text
        :return:
        """
        self.ids.camera.opacity = 0
        self.ids.camera.play = False
        self.ids.camera_button.text = 'Start Camera'
        self.ids.camera.texture = None

    def capture(self):
        """
        Creates a filename with the current time and captures
        and saves a photo image under that filename
        :return:
        """
        try:
            Logger.info("cwd: %s", os.getcwd())
            os.makedirs('files', exist_ok=True)  # create files/ folder
        except OSError as ose:
            Logger.error(ose)
        else:
            Logger.info("mkdirs: ok")

        current_time = time.strftime('%Y%m%d-%H%M%S')
        self.filepath = f'files/{current_time}.png'
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = self.filepath
        Logger.info('self.manager.current_screen.ids.img.source: %s', self.manager.current_screen.ids.img.source)


class ImageScreen(Screen):
    link_message = 'Create a link first!'

    def create_link(self):
        """
        Accesses the photo file path, uploads it to the web
        and inserts the link in the Label widget
        :return:
        """
        filepath = App.get_running_app().root.ids.camera_screen.filepath
        fileshare = FileSharer(filepath)
        self.url = fileshare.share()
        self.ids.link.text = self.url
        Logger.info('url: %s', self.url)

    def copy_link(self):
        try:
            Clipboard.copy(self.url)
        except:
            self.ids.link.text = self.link_message

    def open_link(self):
        try:
            webbrowser.open(self.url)
        except:
            self.ids.link.text = self.link_message


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
