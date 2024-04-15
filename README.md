# PRODIGY_CS_2
# Image Encryption Tool Using Pixel Manipulation

## Description
This tool allows you to encrypt and decrypt images using pixel manipulation techniques. It uses basic mathematical operations to alter the pixel values of the image, making it unreadable without the decryption key.

### image_encrypt.py
This script encrypts an input image using a specified encryption key. It applies pixel manipulation techniques to alter the image data and saves the encrypted image as 'encrypted_image.jpg'.

#### Description
This script takes an input image and encrypts it using pixel manipulation techniques. It applies the specified encryption key to alter the pixel values, making the image unreadable without the corresponding decryption key.

#### Usage
```py
python image_encrypt.py <input_image_path> <encryption_key>
```

### image_decrypt.py
This script decrypts an encrypted image using the decryption key. It reverses the pixel manipulation performed during encryption and displays the decrypted image.

#### Description
This script takes an encrypted image and the decryption key as input and decrypts the image using pixel manipulation techniques. It reverses the encryption process to reveal the original image.

#### Usage
```py
python image_decrypt.py <encrypted_image_path> <decryption_key>
```

## Requirements
- Python 3.x
- Pillow library (install using `pip install Pillow`)

## Example
python image_encrypt.py input_image.jpg 50
python image_decrypt.py encrypted_image.jpg 50


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
