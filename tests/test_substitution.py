from cipher.ciphers import substitution
from cipher.config.common import CMD
import pytest


class TestCipher:
    @pytest.fixture
    def simple_key(self) -> str:
        return "qwertyuiopasdfghjklzxcvbnm"

    @pytest.fixture
    def partial_key(self) -> str:
        return "qwerty"  # Should be automatically completed with remaining letters

    def test_encrypt_basic(self, simple_key):
        text = "HELLO"
        expected = "itssg"
        assert substitution.cipher(text, simple_key, CMD.ENCRYPT) == expected

    def test_decrypt_basic(self, simple_key):
        text = "itssg"
        expected = "hello"
        assert substitution.cipher(text, simple_key, CMD.DECRYPT) == expected

    def test_encrypt_with_spaces(self, simple_key):
        text = "hello world"
        expected = "itssg vgksr"
        assert substitution.cipher(text, simple_key, CMD.ENCRYPT) == expected

    def test_decrypt_with_spaces(self, simple_key):
        text = "itssg vgksr"
        expected = "hello world"
        assert substitution.cipher(text, simple_key, CMD.DECRYPT) == expected

    def test_encrypt_with_punctuation(self, simple_key):
        text = "hello, world!"
        expected = "itssg, vgksr!"
        assert substitution.cipher(text, simple_key, CMD.ENCRYPT) == expected

    def test_partial_key_encryption(self, partial_key):
        text = "hello"
        expected = "btggj"
        assert substitution.cipher(text, partial_key, CMD.ENCRYPT) == expected

    def test_partial_key_decryption(self, partial_key):
        text = "btggj"
        expected = "hello"
        assert substitution.cipher(text, partial_key, CMD.DECRYPT) == expected

    def test_empty_string(self, simple_key):
        assert substitution.cipher("", simple_key, CMD.ENCRYPT) == ""
        assert substitution.cipher("", simple_key, CMD.DECRYPT) == ""

    def test_special_characters_only(self, simple_key):
        text = "123!@#"
        assert substitution.cipher(text, simple_key, CMD.ENCRYPT) == text
        assert substitution.cipher(text, simple_key, CMD.DECRYPT) == text

    def test_roundtrip(self, simple_key):
        original = "hello world"
        encrypted = substitution.cipher(original, simple_key, CMD.ENCRYPT)
        decrypted = substitution.cipher(encrypted, simple_key, CMD.DECRYPT)
        assert decrypted == original

    def test_key_completion(self):
        # Test that a partial key is correctly completed with remaining letters
        partial_key = "abc"
        text = "xyz"
        # The key should be completed as "abcdefghijklmnopqrstuvwxyz"
        result = substitution.cipher(text, partial_key, CMD.ENCRYPT)
        expected = "xyz"  # Since the completed portion will map x->x, y->y, z->z
        assert result == expected
