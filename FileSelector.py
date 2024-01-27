from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
import os
import logging


class FileSelector:
    """
    A class for selecting a file from the local file system.

    Attributes:
        pwd (str): The current working directory.
        path (list): A list of files and directories in the current working directory.
        extension (str): The file extension of the selected file.
        extension_list (list): A list of supported image file extensions.
    """

    pwd = os.getcwd()
    path = os.listdir(pwd)
    path = WordCompleter(path)

    def __init__(self):
        self.extension = ""
        self.extension_list = [
            "jpg",
            "jpeg",
            "png",
            "bmp",
            "gif",
            "tiff",
            "tif",
            "webp",
            "heif",
            "hevc",
        ]

    def select_file(self):
        """
        Prompts the user to select a file from the local file system.

        Returns:
            str: The absolute path of the selected file.
        """
        while True:
            last_dir = self.pwd.split("\\")[-1]
            answer = prompt(f"Now at {last_dir}/: ", completer=self.path)

            if answer == ".." or os.path.isdir(answer):
                self.pwd = os.path.abspath(os.path.join(self.pwd, answer))
                os.chdir(self.pwd)
                self.path = WordCompleter(os.listdir(self.pwd))
            elif os.path.isfile(answer):
                break

        self.extension = answer.split(".")[-1]

        if self.extension not in self.extension_list:
            logging.error("Not an image.")
            exit(1)
        else:
            return os.path.abspath(answer)
