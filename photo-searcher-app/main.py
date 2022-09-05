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
from kivy.logger import Logger
import wikipedia
import requests
import os

Builder.load_file('frontend.kv')


class FirstScreen(Screen):                              # one for every screen
    def search_image(self):                             # logic of screen
        query = (                                       # get user query from text input
            self                                        # FirstSceen instance, root on .kv file
            .manager                                    # RootWidget
            .current_screen                             # FirstScreen, i think
            .ids                                        # list of ids
            .user_query                                 # see frontend.kv
            .text                                       # see frontend.kv
        )

        Logger.info("query: %s", query)

        try:
            page = wikipedia.page(                          # get wikipedia page
                query,
                auto_suggest=False                          # solve DisambiguationError
                                                            # ref: https://stackoverflow.com/a/70409134
            )
        except wikipedia.DisambiguationError as de:
            page = wikipedia.page(                          # get wikipedia page
                de.options[0],                              # workaround from source code
                auto_suggest=False
            )
        except wikipedia.PageError as pe:
            Logger.error("wikipedia: %s", pe)
            return

        image_link = page.images[0]                     # get first image link
        Logger.info("image_link: %s", image_link)

        response = requests.get(                        # dowload the image
            image_link,
            headers={                                   # solve error 403: https://stackoverflow.com/a/38489588
                "user-agent":
                    "Mozilla/5.0 (X11; Linux x86_64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/87.0.4280.141 Safari/537.36"
            }
        )

        if response.status_code == 200:
            Logger.info("status code: %s", response.status_code)

            filename = (                                # get wikipedia image name from query
                query.replace(" ", "-")
            )
            extension = image_link.split(".")[-1]
            imagepath = f'files/{filename}.{extension}'.lower()
            Logger.info("filename: %s", filename)
            Logger.info("extension: %s", extension)
            Logger.info("filepath: %s", imagepath)

            try:
                Logger.info("cwd: %s", os.getcwd())
                os.makedirs('files', exist_ok=True)
            except OSError as ose:
                Logger.error(ose)
                # exit(1)
            else:
                Logger.info("mkdirs: ok")

            try:
                with open(imagepath, 'wb') \
                        as file:                            # save the file
                    file.write(response.content)
                    Logger.info("create %s: ok", imagepath)
            except Exception as e:
                Logger.error(e)
                exit(1)

        (                                 # to avoid \ for newline
            self                          # FirstSceen instance, root on .kv file
            .manager                      # RootWidget
            .current_screen               # FirstScreen, i think
            .ids                          # list of ids
            .img                          # see frontend.kv
            .source                       # see frontend.kv
        ) = imagepath                      # set image file for img


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
