<div align="center"><h1>PyPixEnc</h1></div>
<div align="center"><a href="https://github.com/fardinkamal62/PixEnc">PixEnc</a> in Python</div>
<div align="center">Encrypt image by manipulating pixels</div>
<div align="center" style="color: grey"><sub>Version: 3.1.1</sub></div>
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

# Installation
1. Clone the repository
2. Install Python 3.8 or above
3. Install required packages from `requirements.txt`
4. Run `main.py`

# Usage
### Encrypting Image
1. Keep the image you want to encrypt in the same directory as `main.py`
2. Run main.py
3. Select the image you want to encrypt
4. Enter the password you want to use to encrypt the image
5. It will generate a file named `encrypt.png`

### Decrypting Image
1. To decrypt the image, run `main.py` again
2. Enter the password you used to encrypt the image
3. Select the image you want to decrypt
4. It will generate a file named `decrypt.png`


# Release Note
### 3.1.1 (Current)
- Renamed FileSelector.py to file_selector.py
- Changed user flow from selection -> password -> file selection to selection -> file selection -> password
- Made file explorer case-insensitive

### 3.1.0
- Added file explorer to select image

### 3.0.1
- Converted codebase to OOP, separating encryption-decryption logic, image generation logic & entry point
- Fixed issue with Palette mode PNG & Grayscale mode PNG

### 2.4.0
- Added support for JPG image

#### Known Issue
- White pixels are not encrypted properly

### Beta 2.3.1
- Changes in logging

#### Known Issue
- Only PNG image support

### Beta 2.3.0
- Added multithreading support for decryption

#### Known Issue
- Only PNG image support

### Beta 2.2.0
- Added multithreading support for image generation resulting in faster encryption & image generation

#### Known Issue
- Decryption is not operational
- Only PNG image support

### Beta 2.1.0
- Added multithreading support for encryption

#### Known Issue
- Pixel encryption is working fine but problem is in creating image from encrypted pixels. It is the bottleneck.
- Only PNG image support

### Beta 2.0.0
- Added multithreading; but image generation is not proper

#### Known Issue
- Threads creation & sharing workload is working fine but image generation & encryption is not proper. It's giving partial output. And giving error on pixel read-write on big image.
- Only PNG image support

### Stable 1.0.0
- Can encrypt & decrypt PNG image

#### Known Issue
- Single threaded
- Only PNG image support
