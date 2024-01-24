from PIL import Image
import datetime
import logging
import os

from operation import Operation

logging_format = "%(message)s"
logging.basicConfig(format=logging_format, level=logging.INFO)
NAME = "PixEnc"
VERSION = "3.0.1"


def main():
    user_input = input("Encrypt or decrypt? (e/d): ")
    password = input("Password: ")
    if len(password) < 1:
        logging.error("Password cannot be empty")
        return
    if user_input == "e":
        if os.path.isfile("image.jpg"):
            image = Image.open("image.jpg").convert("RGBA")
        elif os.path.isfile("image.png"):
            image = Image.open("image.png").convert("RGBA")
        else:
            logging.error("No image found")
            return

        logging.info("Encrypting image...")
        start_time = datetime.datetime.now()
        Operation(image, password, True)
        end_time = datetime.datetime.now()
        logging.info(f"Encryption took {end_time - start_time} seconds")

    elif user_input == "d":
        logging.info("On wrong password, the image will not be corrupted but image will not be correct")
        image = Image.open("encrypt.png")

        logging.info("Decrypting image...")
        start_time = datetime.datetime.now()
        Operation(image, password, False)
        end_time = datetime.datetime.now()
        logging.info(f"Decryption took {end_time - start_time} seconds")
    else:
        logging.error("Invalid input")


if __name__ == "__main__":
    main()
