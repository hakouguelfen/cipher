from cipher.ciphers import transposition
from cipher.config.common import CMD
import pytest

# Test data
messages = [
    ("", 1),  # Edge case: empty message
    ("A", 1),  # Single character
    ("AB", 1),  # Single key
    ("AB", 2),  # Key equal to message length
    ("This is a test message!", 4),  # Common case
    ("Short", 10),  # Key greater than message length
    ("EdgeCase", 3),  # Odd message length
    ("AnotherTest", 5),  # Key not dividing message length evenly
]


@pytest.mark.parametrize("message, key", messages)
def test_encrypt_decrypt(message, key):
    """Test encryption followed by decryption returns the original message."""
    encrypted = transposition.cipher(message, key, CMD.ENCRYPT)
    decrypted = transposition.cipher(encrypted, key, CMD.DECRYPT)
    assert decrypted == message


def test_encrypt_empty_message():
    """Encrypting an empty message should return an empty string."""
    assert transposition.cipher("", 4, CMD.ENCRYPT) == ""


def test_decrypt_empty_message():
    """Decrypting an empty message should return an empty string."""
    assert transposition.cipher("", 4, CMD.DECRYPT) == ""


def test_key_one():
    """Encrypting with key=1 should return the original message."""
    message = "This is a test"
    encrypted = transposition.cipher(message, 1, CMD.ENCRYPT)
    assert encrypted == message


def test_large_key():
    """Key greater than message length should not alter the message."""
    message = "Test"
    encrypted = transposition.cipher(message, 10, CMD.ENCRYPT)
    assert encrypted == message


def test_non_divisible_key():
    """Test with key not evenly dividing the message length."""
    message = "Hello World!"
    key = 5
    encrypted = transposition.cipher(message, key, CMD.ENCRYPT)
    decrypted = transposition.cipher(encrypted, key, CMD.DECRYPT)
    assert decrypted == message


def test_long_message():
    """Test with a long message."""
    message = "A" * 1000  # 1000 'A's
    key = 7
    encrypted = transposition.cipher(message, key, CMD.ENCRYPT)
    decrypted = transposition.cipher(encrypted, key, CMD.DECRYPT)
    assert decrypted == message
