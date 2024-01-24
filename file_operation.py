import threading
from tqdm import tqdm
import os


class FileOperation:
    def __init__(self, image, pixels, do_encrypt=True):
        self.image = image
        self.pixels = pixels
        self.do_encrypt = do_encrypt
        self.__multi_threading(image, pixels, do_encrypt)

    def __multi_threading(self, image, pixels, do_encrypt=True):
        """
        Write an image to a file
        :param image: PIL Image object
        :type image: Pil.Image.Image
        :param pixels: Pixels to write to the image
        :type pixels: dict
        :param do_encrypt: Flag to identify if the image is to be encrypted or decrypted
        :type do_encrypt: bool
        :return: None
        """
        thread_count = os.cpu_count() // 2
        pixels_list = list(pixels.items())
        chunks = [pixels_list[i::thread_count] for i in range(thread_count)]

        threads = []
        for chunk in chunks:
            thread = threading.Thread(target=self.__write_pixels, args=(image, dict(chunk), do_encrypt))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    def __write_pixels(self, image, pixels_chunk, do_encrypt=True):
        """
        Write a chunk of pixels to an image
        :param image: PIL Image object
        :type image: Pil.Image.Image
        :param pixels_chunk: A chunk of pixels
        :type pixels_chunk: dict
        :param do_encrypt: A flag to identify if the image is to be encrypted or decrypted
        :type do_encrypt: bool
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
