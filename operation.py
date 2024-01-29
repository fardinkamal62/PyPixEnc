import os
import random
import threading
import logging
from tqdm import tqdm

from file_operation import FileOperation


class Operation:
    def __init__(self, image, password, do_encrypt=True):
        """
        Perform encryption or decryption on an image.

        Args:
            image (PIL.Image.Image): The PIL Image object to be processed.
            password (str): Password used for encryption or decryption.
            do_encrypt (bool, optional): Flag to identify if the image should be encrypted (default is True).

        Attributes:
            image (PIL.Image.Image): The PIL Image object associated with the operation.
            password (str): The password used for encryption or decryption.
            do_encrypt (bool): Flag to identify if the image should be encrypted.

        Note:
            The actual encryption or decryption is performed in a separate method called '__multi_threading',
            followed by file operations using 'FileOperation' class.
        """
        self.image = image
        self.password = password
        self.file_lock = threading.Lock()
        self.pixel_values = {}

        self.__multi_threading(image, password)
        FileOperation(image, self.pixel_values, do_encrypt)

    def __multi_threading(self, image, password):
        """
        Run multiple threads to encrypt & decrypt the image
        :param image: PIL Image object
        :type image: Pil.Image.Image
        :param password: Password to encrypt the image with
        :type password: str
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

            thread = threading.Thread(target=self.__encrypt_decrypt, args=(image, arr, pixel_start, pixel_end))
            threads.append(thread)
            logging.info(f"Thread {_+1} started for pixels {pixel_start} to {pixel_end}")
            thread.start()
        for thread in threads:
            thread.join()

    def __encrypt_decrypt(self, image, random_numbers, pixel_start, pixel_end):
        """
        Encrypt/decrypt an image using a password
        :param image: PIL Image object
        :type image: Pil.Image.Image
        :param random_numbers: Random numbers to encrypt the image with
        :type random_numbers: list
        :param pixel_start: Pixel to start at
        :type pixel_start: int
        :param pixel_end: Pixel to end at
        :type pixel_end: int
        :return: None
        """
        width, height = image.size
        with self.file_lock:
            pixels = image.load()

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
                self.pixel_values[i] = (red, green, blue, alpha)
