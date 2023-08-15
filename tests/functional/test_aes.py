import pytest
from src.benchmark.symmetric import aes_benchmark
def test_aes_encryption_decryption():
    # Plain text for testing
    plain_text = "This is a test message!"

    # Key for encryption. AES supports key sizes of 128, 192, or 256 bits.
    # For simplicity, let's use 128 bits (16 bytes) key for this test.
    key = "Sixteen byte key"

    # Encrypt
    encrypted_text = aes_benchmark.encrypt(plain_text, key)

    # Ensure the encrypted text is not same as plain text
    assert encrypted_text != plain_text

    # Decrypt
    decrypted_text = aes_benchmark.decrypt(encrypted_text, key)

    # Ensure the decrypted text is same as original plain text
    assert decrypted_text == plain_text