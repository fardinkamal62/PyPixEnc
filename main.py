from PIL import Image
import datetime
from tqdm import tqdm
import logging
import random
import threading
import os

logging_format = "%(message)s"
logging.basicConfig(format=logging_format, level=logging.INFO, datefmt="%H:%M:%S")
NAME = "PixEnc"
VERSION = "Beta 2.3.0"


pixel_values = {}


def encrypt(image, random_numbers, pixel_start, pixel_end):
    """
    Encrypt an image using a password
    :param image: PIL Image object
    :param random_numbers: Random numbers to encrypt the image with
    :param pixel_start: Pixel to start at
    :param pixel_end: Pixel to end at
    :return: None
    """
    width, height = image.size
    with file_lock:
        pixels = image.load()

    logging.info("Encrypting image for pixels {pixel_start} to {pixel_end}...")
    start_time = datetime.datetime.now()
    j = 0
    for i in tqdm(range(pixel_start, pixel_end)):
        j += 1
        x = i % width
        y = i // width
        pixel_value = pixels[x, y]
        red, green, blue, alpha = pixel_value
        if j < len(random_numbers) - 4:
            red = (red ^ random_numbers[j] * 2)
            green = (green ^ random_numbers[j + 1] * 2)
            blue = (blue ^ random_numbers[j + 2] * 2)
            alpha = (alpha ^ random_numbers[j + 3] * 2)
            pixel_values[i] = (red, green, blue, alpha)

    end_time = datetime.datetime.now()
    logging.info(f"Encryption took {end_time - start_time} seconds for pixels {pixel_start} to {pixel_end}")


def decrypt(image, random_numbers, pixel_start, pixel_end):
    """
    Encrypt an image using a password
    :param pixel_start: Pixel to start at
    :param pixel_end: Pixel to end at
    :param random_numbers:
    :param image: PIL Image object
    :return: None
    """
    width, height = image.size
    with file_lock:
        pixels = image.load()

    logging.info("Decrypting image for pixels {pixel_start} to {pixel_end}...")
    start_time = datetime.datetime.now()
    j = 0
    for i in tqdm(range(pixel_start, pixel_end)):
        j += 1
        x = i % width
        y = i // width
        pixel_value = pixels[x, y]
        red, green, blue, alpha = pixel_value
        if j < len(random_numbers) - 4:
            red = (red ^ random_numbers[j] * 2)
            green = (green ^ random_numbers[j + 1] * 2)
            blue = (blue ^ random_numbers[j + 2] * 2)
            alpha = (alpha ^ random_numbers[j + 3] * 2)
            pixel_values[i] = (red, green, blue, alpha)

    end_time = datetime.datetime.now()
    logging.info(f"Decryption took {end_time - start_time} seconds for pixels {pixel_start} to {pixel_end}")


file_lock = threading.Lock()


def write_pixels(image, pixels_chunk, do_encrypt=True):
    """
    Write a chunk of pixels to an image
    :param image: PIL Image object
    :param pixels_chunk: A chunk of pixels
    :param do_encrypt: Flag to identify if the image is to be encrypted or decrypted
    :return: None
    """
    width, height = image.size
    for pixel in tqdm(pixels_chunk):
        x = pixel % width
        y = pixel // width
        red, green, blue, alpha = pixels_chunk[pixel]
        new_pixels = (red, green, blue, alpha)
        image.putpixel((x, y), new_pixels)
    image.save(f"{'encrypt' if do_encrypt else 'decrypt'}.png")


def write_image(image, pixels, do_encrypt=True):
    """
    Write an image to a file
    :param image: PIL Image object
    :param pixels: Pixels to write to the image
    :param do_encrypt: Flag to identify if the image is to be encrypted or decrypted
    :return: None
    """
    # Divide the pixels into chunks
    thread_count = os.cpu_count() // 2
    pixels_list = list(pixels.items())
    chunks = [pixels_list[i::thread_count] for i in range(thread_count)]

    threads = []
    for chunk in chunks:
        thread = threading.Thread(target=write_pixels, args=(image, dict(chunk), do_encrypt))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()


def multi_threading(image, password, do_encrypt=True):
    """
    Run multiple threads to encrypt the image
    :param do_encrypt: Flag to identify if the image is to be encrypted or decrypted
    :param image: PIL Image object
    :param password: Password to encrypt the image with
    :return: None
    """
    width, height = image.size
    pixels = height * width
    random.seed(password)
    random_numbers = [random.randint(0, 100) for _ in range(pixels)]

    thread_count = os.cpu_count() // 2
    op_per_thread = pixels // thread_count
    logging.info(f"Starting {thread_count} threads")
    threads = []
    for _ in range(thread_count):
        pixel_start = _ * op_per_thread
        pixel_end = ((_ + 1) * op_per_thread - 1)
        arr = random_numbers[pixel_start:pixel_end]

        if do_encrypt:
            thread = threading.Thread(target=encrypt, args=(image, arr, pixel_start, pixel_end))
        else:
            thread = threading.Thread(target=decrypt, args=(image, arr, pixel_start, pixel_end))
        threads.append(thread)
        logging.info(f"Thread {_} started for pixels {pixel_start} to {pixel_end}")
        thread.start()
    for thread in threads:
        thread.join()


def main():
    user_input = input("Encrypt or decrypt? (e/d): ")
    password = input("Password: ")
    if len(password) < 1:
        logging.error("Password cannot be empty")
        return
    if user_input == "e":
        image = Image.open("diu_logo.png")
        multi_threading(image, password)
        logging.info("Writing image...")
        write_image(image, pixel_values, True)
    elif user_input == "d":
        logging.info("On wrong password, the image will not be corrupted but image will not be correct")
        image = Image.open("encrypt.png")
        multi_threading(image, password, False)
        logging.info("Writing image...")
        write_image(image, pixel_values, False)
    else:
        logging.error("Invalid input")


if __name__ == "__main__":
    main()
