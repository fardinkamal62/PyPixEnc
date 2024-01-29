from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
import os
import logging

# TODO: Start file selector at the directory of the script


class FileSelector:
    """
    A class for selecting a file from the local file system.

    Attributes:
        pwd (str): The current working directory.
        extension (str): The file extension of the selected file.
        extension_list (list): A list of supported image file extensions.
    """

    pwd = os.getcwd()

    def __init__(self):
        """
        Initialize the class attributes.
        """
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

    def filter(self):
        """
        Filter the list of files in the current directory based on the supported image file extensions.

        Returns:
            list: A list of files that match the supported image file extensions.
        """
        directories = list()
        files = list()
        for filename in os.listdir(self.pwd):
            if filename.split(".")[-1] in self.extension_list:
                files.append(filename)
            elif os.path.isdir(filename):
                directories.append(filename)
        image_file_list = directories + files
        image_file_list.insert(0, "..")
        return image_file_list

    def select_file(self):
        """
        Prompts the user to select a file from the local file system.

        Returns:
            str: The absolute path of the selected file.
        """
        paths = WordCompleter(self.filter(), True)
        virgin = True
        while True:
            last_dir = self.pwd.split("\\")[-1]
            try:
                if virgin:
                    virgin = False
                answer = prompt(f"Now at {last_dir}/ (Press Tab): ", completer=paths)
            except KeyboardInterrupt:
                logging.info("Exit")  # Graceful exit
                exit(1)

            if answer == ".." or os.path.isdir(answer):
                self.pwd = os.path.abspath(os.path.join(self.pwd, answer))
                os.chdir(self.pwd)
                paths = WordCompleter(self.filter(), True)
            elif os.path.isfile(answer):
                break

        self.extension = answer.split(".")[-1]

        if self.extension not in self.extension_list:
            logging.error("Not an image.")
            exit(1)
        else:
            logging.info(f"Selected file: {answer}")
            return os.path.abspath(answer)
