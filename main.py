from PIL import Image
from file_selector import FileSelector
from operation import Operation
import datetime
import logging


logging_format = "%(message)s"
logging.basicConfig(format=logging_format, level=logging.INFO)
NAME = "PixEnc"
VERSION = "3.1.1"


def main():
    print(f"{NAME} v{VERSION}\n")
    user_input = input("Encrypt or decrypt? (e/d): ")
    file_selector = FileSelector()
    if user_input == "e":
        logging.info("Chose image file:\n")
        file_path = file_selector.select_file()
        # All errors are handled inside the select_file method
        image = Image.open(file_path).convert("RGBA")

        password = input("Password: ")
        if len(password) < 1:
            logging.error("Password cannot be empty")
            return

        logging.info("Encrypting image...")
        start_time = datetime.datetime.now()
        Operation(image, password, True)
        end_time = datetime.datetime.now()
        logging.info(f"Encryption took {end_time - start_time} seconds")

    elif user_input == "d":
        logging.info("On wrong password, the image will not be corrupted but image will not be correct")
        logging.info("Chose image file:\n")
        file_path = file_selector.select_file()
        image = Image.open(file_path).convert("RGBA")

        password = input("Password: ")
        if len(password) < 1:
            logging.error("Password cannot be empty")
            return

        logging.info("Decrypting image...")
        start_time = datetime.datetime.now()
        Operation(image, password, False)
        end_time = datetime.datetime.now()
        logging.info(f"Decryption took {end_time - start_time} seconds")
    else:
        logging.error("Invalid input")


if __name__ == "__main__":
    main()
