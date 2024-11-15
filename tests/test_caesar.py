from cipher.ciphers import caesar
from cipher.config.common import CMD
import pytest


def test_simple_shift():
    # Basic test with a positive shift
    assert caesar.cipher("ABC", 3, CMD.ENCRYPT) == "DEF"
    assert caesar.cipher("xyz", 2, CMD.ENCRYPT) == "zab"

    assert caesar.cipher("DEF", 3, CMD.DECRYPT) == "ABC"
    assert caesar.cipher("zab", 2, CMD.DECRYPT) == "xyz"


def test_shift_wraparound():
    # Test wraparound at the end of the alphabet
    assert caesar.cipher("XYZ", 3, CMD.ENCRYPT) == "ABC"
    assert caesar.cipher("xyz", 4, CMD.ENCRYPT) == "bcd"

    assert caesar.cipher("ABC", 3, CMD.DECRYPT) == "XYZ"
    assert caesar.cipher("bcd", 4, CMD.DECRYPT) == "xyz"


def test_negative_shift():
    # Test negative shifts (shifts left instead of right)
    assert caesar.cipher("ABC", -3, CMD.ENCRYPT) == "XYZ"
    assert caesar.cipher("xyz", -2, CMD.ENCRYPT) == "vwx"

    assert caesar.cipher("XYZ", -3, CMD.DECRYPT) == "ABC"
    assert caesar.cipher("vwx", -2, CMD.DECRYPT) == "xyz"


def test_large_shift():
    # Test large shifts (should behave the same as shift % 26)
    assert caesar.cipher("ABC", 29, CMD.ENCRYPT) == "DEF"  # 29 % 26 ==
    assert caesar.cipher("xyz", 52, CMD.ENCRYPT) == "xyz"  # 52 % 26 ==

    assert caesar.cipher("DEF", 29, CMD.DECRYPT) == "ABC"
    assert caesar.cipher("xyz", 52, CMD.DECRYPT) == "xyz"


def test_non_alpha_characters():
    # Test that non-alphabet characters remain the same
    assert caesar.cipher("Hello, World!", 5, CMD.ENCRYPT) == "Mjqqt, Btwqi!"
    assert caesar.cipher("12345 !@#$%", 10, CMD.ENCRYPT) == "12345 !@#$%"

    assert caesar.cipher("Mjqqt, Btwqi!", 5, CMD.DECRYPT) == "Hello, World!"
    assert caesar.cipher("12345 !@#$%", 10, CMD.DECRYPT) == "12345 !@#$%"


def test_no_shift():
    # Test shift of zero (should return the original string)
    assert caesar.cipher("Hello, World!", 0, CMD.ENCRYPT) == "Hello, World!"


def test_full_alphabet_shift():
    # Test shifting by 26 (full rotation) should return the same string
    assert (
        caesar.cipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 26, CMD.ENCRYPT)
        == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    )
    assert (
        caesar.cipher("abcdefghijklmnopqrstuvwxyz", 26, CMD.ENCRYPT)
        == "abcdefghijklmnopqrstuvwxyz"
    )


def test_case_sensitivity():
    # Ensure the case is preserved in the shifted result
    assert caesar.cipher("AbC", 1, CMD.ENCRYPT) == "BcD"
    assert caesar.cipher("aBc", -1, CMD.ENCRYPT) == "zAb"

    assert caesar.cipher("BcD", 1, CMD.DECRYPT) == "AbC"
    assert caesar.cipher("zAb", -1, CMD.DECRYPT) == "aBc"


def test_invalid_shift_type():
    # Test for non-integer shift (should raise an error)
    with pytest.raises(TypeError):
        caesar.cipher("Hello", "a", CMD.ENCRYPT)


def test_boundary_shift_values():
    # Test edge case shifts at boundaries like 1 and -1
    assert caesar.cipher("A", 1, CMD.ENCRYPT) == "B"
    assert caesar.cipher("A", -1, CMD.ENCRYPT) == "Z"

    assert caesar.cipher("B", 1, CMD.DECRYPT) == "A"
    assert caesar.cipher("Z", -1, CMD.DECRYPT) == "A"
