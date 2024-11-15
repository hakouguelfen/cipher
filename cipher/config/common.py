from enum import Enum

MIN_ASCII = 97
MAX_ASCII = 122
NUM_LETTERS = 26


class CMD(Enum):
    ENCRYPT = "encrypt"
    DECRYPT = "decrypt"


class ALGORITHMS(Enum):
    CAESAR = "Caesar"
    VIGENERE = "Vigenere"
    SUBSTITUTION = "Substitution"
    TRANSPOSITION = "Uransposition"
