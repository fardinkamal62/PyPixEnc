from PIL import Image
import datetime
from tqdm import tqdm
import logging
import random

logging_format = "%(message)s"
logging.basicConfig(format=logging_format, level=logging.INFO, datefmt="%H:%M:%S")
NAME = "PixEnc"
VERSION = "1.0.0"


def encrypt(image, password):
    """
    Encrypt an image using a password
    :param image: PIL Image object
    :param password: Password to encrypt the image with
    :return: None
    """
    width, height = image.size
    pixels = height * width
    random.seed(password)
    random_numbers = [random.randint(0, 100) for _ in range(pixels)]

    logging.info("Encrypting image...")
    start_time = datetime.datetime.now()
    for i in tqdm(range(pixels)):
        x = i % width
        y = i // width
        pixel_value = image.getpixel((x, y))
        red, green, blue, alpha = pixel_value
        if i < len(random_numbers) - 4:
            red = (red ^ random_numbers[i] * 2)
            green = (green ^ random_numbers[i + 1] * 2)
            blue = (blue ^ random_numbers[i + 2] * 2)
            alpha = (alpha ^ random_numbers[i + 3] * 2)
            write_pixel(image, x, y, red, green, blue, alpha, True)

    end_time = datetime.datetime.now()
    logging.info(f"Encryption took {end_time - start_time} seconds")


def decrypt(image, password):
    """
    Encrypt an image using a password
    :param image: PIL Image object
    :param password: Password to encrypt the image with
    :return: None
    """
    width, height = image.size
    pixels = height * width
    random.seed(password)
    random_numbers = [random.randint(0, 100) for _ in range(pixels)]

    logging.info("Decrypting image...")
    start_time = datetime.datetime.now()
    for i in tqdm(range(pixels)):
        x = i % width
        y = i // width
        pixel_value = image.getpixel((x, y))
        red, green, blue, alpha = pixel_value
        if i < len(random_numbers) - 4:
            red = (red ^ random_numbers[i] * 2)
            green = (green ^ random_numbers[i + 1] * 2)
            blue = (blue ^ random_numbers[i + 2] * 2)
            alpha = (alpha ^ random_numbers[i + 3] * 2)
            write_pixel(image, x, y, red, green, blue, alpha, False)

    end_time = datetime.datetime.now()
    logging.info(f"Decryption took {end_time - start_time} seconds")


def write_pixel(image, x, y, red, green, blue, alpha, do_encrypt=True):
    """
    Write a pixel to an image
    :param do_encrypt:
    :param image: PIL Image object
    :param x: x-coordinate of the pixel
    :param y: y-coordinate of the pixel
    :param red: Red value of the pixel
    :param green: Green value of the pixel
    :param blue: Blue value of the pixel
    :param alpha: Alpha value of the pixel
    :return: None
    """
    new_pixels = (red, green, blue, alpha)
    image.putpixel((x, y), new_pixels)
    image.save(f"{'encrypt' if do_encrypt else 'decrypt'}.png")


def main():
    user_input = input("Encrypt or decrypt? (e/d): ")
    password = input("Password: ")
    if len(password) < 1:
        logging.error("Password cannot be empty")
        return
    if user_input == "e":
        image = Image.open("image.png")
        encrypt(image, password)
        Image.open("encrypt.png").show()
    elif user_input == "d":
        logging.info("On wrong password, the image will not be corrupted but image will not be correct")
        image = Image.open("encrypt.png")
        decrypt(image, password)
        Image.open("decrypt.png").show()
    else:
        logging.error("Invalid input")


if __name__ == "__main__":
    main()
