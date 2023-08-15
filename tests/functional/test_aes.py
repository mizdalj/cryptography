import pytest

from src.algorithms.symmetric.aes import encrypt, decrypt
from src.benchmark.symmetric import aes_benchmark
from src.algorithms.symmetric import aes as custom_aes


def test_aes_encryption_decryption_benchmark():
    # Plain text for testing
    plain_text = "This is a test message!"

    # Key for encryption. AES supports key sizes of 128, 192, or 256 bits.
    # For simplicity, let's use 128 bits (16 bytes) key for this test.
    key = "Sixteen byte key"

    # Encrypt
    encrypted_text = aes_benchmark.encrypt(plain_text, key)
    print(f"""Benchmark AES encrypted value:{encrypted_text}""")

    # Ensure the encrypted text is not same as plain text
    assert encrypted_text != plain_text

    # Decrypt
    decrypted_text = aes_benchmark.decrypt(encrypted_text, key)
    print(f"""Benchmark AES decrypted value:{decrypted_text}""")

    # Ensure the decrypted text is same as original plain text
    assert decrypted_text == plain_text


import base64

def test_custom_aes_encryption_decryption():
    test_cases = [
        ("This is a test!!", "Sixteen byte key"),
    ]

    for plain_text, key in test_cases:
        print(f"Length of plain_text: {len(plain_text)}")
        print(f"Length of key: {len(key)}")

        # Ensure valid lengths
        if len(plain_text) != 16 or len(key) != 16:
            raise ValueError("Plaintext or key is of invalid length")

        # Encrypt
        encrypted_text = encrypt(plain_text, key)
        encrypted_base64 = base64.b64encode(encrypted_text.encode()).decode()
        print(f"Custom AES encrypted value (Base64): {encrypted_base64}")

        # Ensure the encrypted text is not the same as the plain text
        assert encrypted_text != plain_text

        # Decrypt
        decrypted_text = decrypt(encrypted_text, key)
        print(f"Custom AES decrypted value: {decrypted_text}")

        # Ensure the decrypted text is the same as the original plain text
        assert decrypted_text == plain_text
