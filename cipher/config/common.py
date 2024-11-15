from enum import Enum

NUM_LETTERS = 26


class CMD(Enum):
    ENCRYPT = "encrypt"
    DECRYPT = "decrypt"


class ALGORITHMS(Enum):
    CAESAR = "Caesar"
    VIGENERE = "Vigenere"
    SUBSTITUTION = "Substitution"
    TRANSPOSITION = "Transposition"
