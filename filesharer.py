# import os
# import webbrowser
#
from filestack import Client


class FileSharer:
    """
    represents a filestack api instance
    """
    from secret.filestack_apikey import API_KEY         # import secret api key

    def __init__(self, file_path, api_key=API_KEY):
        self.file_path = file_path
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)                   # instantiate filestack client
        new_filelink = client.upload(                   # upload file and get link
            filepath=self.file_path
        )
        return new_filelink.url                         # return link
