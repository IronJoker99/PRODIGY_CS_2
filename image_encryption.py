from PIL import Image
import numpy as np
import sys

def decrypt_image(encrypted_img_path, decryption_key):
    """
    Decrypts the input encrypted image using pixel manipulation techniques based on the decryption key.
    
    Parameters:
        encrypted_img_path (str): Path to the encrypted image file.
        decryption_key (int): Decryption key specifying the manipulation to reverse the encryption process.
    
    Returns:
        Image: The decrypted image.
    """
    # Open the encrypted image
    encrypted_img = Image.open(encrypted_img_path)
    encrypted_img = encrypted_img.convert('RGB')
    
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
        print("Usage: python image_decrypt.py <encrypted_image_path> <decryption_key>")
        sys.exit(1)
    
    # Get encrypted image path and decryption key from command line arguments
    encrypted_image_path = sys.argv[1]
    decryption_key = int(sys.argv[2])
    
    # Decrypt the encrypted image
    decrypted_img = decrypt_image(encrypted_image_path, decryption_key)
    decrypted_img.show()

if __name__ == "__main__":
    main()
