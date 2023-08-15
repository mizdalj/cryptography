from Crypto.Cipher import AES
import base64

def pad(data):
    """
    Pad the input data to be a multiple of 16 bytes.
    """
    return data + (16 - len(data) % 16) * chr(16 - len(data) % 16)

def unpad(data):
    """
    Unpad the input data.
    """
    return data[:-data[-1]]

def encrypt(plain_text, key):
    """
    Encrypt the plaintext using AES encryption.
    """
    # Ensure the data and key are of correct lengths
    padded_data = pad(plain_text)
    if len(key) not in [16, 24, 32]: # AES supports 128, 192, and 256 bit keys.
        raise ValueError("Key must be 16, 24, or 32 bytes long")

    cipher = AES.new(key.encode(), AES.MODE_ECB)
    encrypted = cipher.encrypt(padded_data.encode())

    # Return as base64 encoded string for better readability
    return base64.b64encode(encrypted).decode('utf-8')

def decrypt(cipher_text, key):
    """
    Decrypt the ciphertext using AES decryption.
    """
    encrypted_data = base64.b64decode(cipher_text)
    if len(key) not in [16, 24, 32]:
        raise ValueError("Key must be 16, 24, or 32 bytes long")

    cipher = AES.new(key.encode(), AES.MODE_ECB)
    decrypted = cipher.decrypt(encrypted_data)
    return unpad(decrypted).decode('utf-8')
