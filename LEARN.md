<div align="center"><h1>PixEnc</h1></div>

<div align="center">Encrypt image by manipulating pixels</div>

# Procedure
## Encryption
1. Read the image with Python Pillow Library. It will return a list of pixels.
2. From the list of pixels we can

    - Get the RGB value of each pixel.
    - Generate random numbers for each pixel from 0 to 100.
3. Do XOR operation between the RGB value and 2 times the random number and assign the result to the RGB value.
4. Save the image.

### Example

I have a 32x32 image. It has 1024 pixels. First generate 1024 random numbers with password as seed, so everytime with the correct password, we will get the same 1024 random values.

Let’s say we’ll change the 10-th pixel. Our 10-th random number is 3 and the 10-th pixel value is R: 81 G: 123 B:21 A:100. 

Let’s do XOR of 10-th random value, 3, with R/G/B/A value. The new pixel value will be R: 82 G:120 B: 129 A: 210.

As you've noticed we're doing 2 times the random number because when we do XOR, the result is close to the original value. So, when we do 2 times the random number, the result will be far from the original value.

## Decryption
Decryption is the reverse process of encryption. We’ll do XOR operation between the RGB value and 2 times the random number and assign the result to the RGB value.

As we're doing XOR operation, we'll get the original RGB value back if we do XOR operation again with the same random number.
Let's say 81 XOR 3 = 82, so 82 XOR 3 or 3 XOR 82 will be 81 again. 
