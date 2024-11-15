from cipher.ciphers import vigenere
from cipher.config.common import CMD
import pytest


def test_simple_encryption():
    # Basic encryption with a simple key
    assert vigenere.cipher("HELLO", "KEY", CMD.ENCRYPT) == "RIJVS"
    assert vigenere.cipher("hello", "key", CMD.ENCRYPT) == "rijvs"


def test_simple_decryption():
    # Basic decryption with a simple key
    assert vigenere.cipher("RIJVS", "KEY", CMD.DECRYPT) == "HELLO"
    assert vigenere.cipher("rijvs", "key", CMD.DECRYPT) == "hello"


def test_key_longer_than_text():
    # Test when key is longer than the text
    assert vigenere.cipher("ABC", "LONGKEY", CMD.ENCRYPT) == "LPP"
    assert vigenere.cipher("LPP", "LONGKEY", CMD.DECRYPT) == "ABC"


def test_key_shorter_than_text():
    # Test when key is shorter than the text (key should repeat)
    assert vigenere.cipher("HELLOWORLD", "KEY", CMD.ENCRYPT) == "RIJVSUYVJN"
    assert vigenere.cipher("RIJVSUYVJN", "KEY", CMD.DECRYPT) == "HELLOWORLD"


def test_non_alpha_characters():
    # Test that non-alphabet characters are not shifted
    assert vigenere.cipher("Hello, World!", "KEY", CMD.ENCRYPT) == "Rijvs, Uyvjn!"
    assert vigenere.cipher("Rijvs, Uyvjn!", "KEY", CMD.DECRYPT) == "Hello, World!"


def test_mixed_case_text_and_key():
    # Test encryption with mixed case in both text and key
    assert vigenere.cipher("HelloWorld", "KeY", CMD.ENCRYPT) == "RijvsUyvjn"
    assert vigenere.cipher("RijvsUyvjn", "KeY", CMD.DECRYPT) == "HelloWorld"


def test_full_alphabet_encryption_and_decryption():
    # Test encryption and decryption across the full alphabet
    text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = "KEY"
    encrypted_text = vigenere.cipher(text, key, CMD.ENCRYPT)
    decrypted_text = vigenere.cipher(encrypted_text, key, CMD.DECRYPT)
    assert decrypted_text, text


def test_key_with_spaces():
    # Test behavior with a key that includes spaces (spaces in the key should be ignored)
    assert vigenere.cipher("HELLO", "K E Y", CMD.ENCRYPT) == "RIJVS"
    assert vigenere.cipher("RIJVS", "K E Y", CMD.DECRYPT) == "HELLO"


def test_single_character_key():
    # Test encryption and decryption with a single-character key (behaves like Caesar cipher)
    assert vigenere.cipher("HELLO", "A", CMD.ENCRYPT) == "HELLO"  # Shift by 0
    assert vigenere.cipher("HELLO", "B", CMD.ENCRYPT) == "IFMMP"  # Shift by 1


def test_invalid_key_type():
    # Test error handling for invalid key type
    with pytest.raises(TypeError):
        vigenere.cipher("HELLO", 123, CMD.ENCRYPT)  # Non-string key

    with pytest.raises(TypeError):
        vigenere.cipher("HELLO", None, CMD.DECRYPT)
