from PIL import Image
import numpy as np
import sys

def encrypt_image(image_path, encryption_key):
    """
    Encrypts the input image using pixel manipulation techniques based on the encryption key.
    
    Parameters:
        image_path (str): Path to the input image file.
        encryption_key (int): Encryption key specifying the manipulation to be applied to each pixel.
    
    Returns:
        Image: The encrypted image.
    """
    # Open the input image
    img = Image.open(image_path)
    img = img.convert('RGB')
    
    # Convert image to numpy array for faster processing
    img_array = np.array(img)
    
    # Apply pixel manipulation based on encryption key
    encrypted_array = img_array + encryption_key
    
    # Clip pixel values to ensure they remain within 0-255 range
    encrypted_array = np.clip(encrypted_array, 0, 255)
    
    # Convert back to image
    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'), 'RGB')
    
    return encrypted_img

def decrypt_image(encrypted_img, decryption_key):
    """
    Decrypts the input encrypted image using pixel manipulation techniques based on the decryption key.
    
    Parameters:
        encrypted_img (Image): The encrypted image.
        decryption_key (int): Decryption key specifying the manipulation to reverse the encryption process.
    
    Returns:
        Image: The decrypted image.
    """
    # Convert image to numpy array for faster processing
    encrypted_array = np.array(encrypted_img)
    
    # Reverse the encryption process
    decrypted_array = encrypted_array - decryption_key
    
    # Clip pixel values to ensure they remain within 0-255 range
    decrypted_array = np.clip(decrypted_array, 0, 255)
    
    # Convert back to image
    decrypted_img = Image.fromarray(decrypted_array.astype('uint8'), 'RGB')
    
    return decrypted_img

def main():
    # Check if correct number of arguments provided
    if len(sys.argv) != 3:
        print("Usage: python image_encrypt.py <input_image_path> <encryption_key>")
        sys.exit(1)
    
    # Get input image path and encryption key from command line arguments
    input_image_path = sys.argv[1]
    encryption_key = int(sys.argv[2])
    
    # Encrypt the input image
    encrypted_img = encrypt_image(input_image_path, encryption_key)
    encrypted_img.save("encrypted_image.jpg")
    print("Image encrypted successfully. Saved as 'encrypted_image.jpg'")
    
    # Decrypt the encrypted image (just for demonstration purposes)
    decrypted_img = decrypt_image(encrypted_img, encryption_key)
    decrypted_img.show()

if __name__ == "__main__":
    main()
