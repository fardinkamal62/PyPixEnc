<div align="center"><h1>PixEnc</h1></div>
<div align="center">Encrypt image by manipulating pixels</div>
<div align="center">
  <strong>
    <a href="https://fardinkamal62.vercel.app/projects/pixenc">Website</a>
    •
    <a href="https://docs.google.com/document/d/173xWvlrEQd1esI3rtD1SmtqtZ1rmFFwKzwRIdWKSTQw/edit?usp=sharing">Docs</a>
    </strong>
</div>

# Technologies
- Python
- Python Pillow Library

# Example
## Original Image
**Original Image**

![Original Image](https://i.ibb.co/717YFZ3/image.png)
![Original Image](https://i.ibb.co/GPrdJjp/image.png)

**Encrypted Image**

![Encrypted Image](https://i.ibb.co/5LmfRkH/encrypt.png)
![Encrypted Image](https://i.ibb.co/smCG4fY/encrypt.png)

**Decrypted Image**

![Decrypted Image](https://i.ibb.co/9rhKkgr/decrypt.png)
![Decrypted Image](https://i.ibb.co/HgSTFV5/decrypt.png)


### Note
In the example above, I used a small image of 32x32 pixels. As it is single threaded(as of now), it takes some time to encrypt & decrypt large images. I am working on it.

# Installation
1. Clone the repository
2. Install Python 3.8 or above
3. Install required packages from requirements.txt
4. Run main.py

# Usage
## Encrypting Image
1. Keep the image you want to encrypt in the same directory as main.py
2. Change the name of the image to `image.png`
3. Run main.py
4. Enter the password you want to use to encrypt the image
5. It will generate a file named `encrypt.png`

## Decrypting Image
1. To decrypt the image, run main.py again
2. Enter the password you used to encrypt the image
3. It will generate a file named `decrypt.png`
