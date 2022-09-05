import os

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.logger import Logger
import time

from filesharer import FileSharer

Builder.load_file('frontend.kv')


class CameraScreen(Screen):
    def start(self):
        self.ids.camera.play = True
        self.ids.camera_button.text = 'Stop Camera'
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        self.ids.camera.play = False
        self.ids.camera_button.text = 'Start Camera'
        self.ids.camera.texture = None

    def capture(self):
        try:
            Logger.info("cwd: %s", os.getcwd())
            os.makedirs('files', exist_ok=True)  # create files/ folder
        except OSError as ose:
            Logger.error(ose)
        else:
            Logger.info("mkdirs: ok")

        current_time = time.strftime('%Y%m%d-%H%M%S')
        filepath = f'files/{current_time}.png'
        self.ids.camera.export_to_png(filepath)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = filepath


class ImageScreen(Screen):
    pass


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
