from encryptor.config.common import CMD
import math


def cipher(text: str, key: int, cmd: CMD) -> str:
    result = ""

    rows = math.ceil(len(text) / key)
    letters = [""] * len(text)
    letter_idx = 0

    for k in range(key):
        for r in range(rows):
            index = k + (r * key)

            match cmd:
                case CMD.ENCRYPT:
                    if index < len(text):
                        result += text[index]

                case CMD.DECRYPT:
                    if index < len(text):
                        letters[index] = text[letter_idx]
                        letter_idx += 1

    match cmd:
        case CMD.ENCRYPT:
            return result

        case CMD.DECRYPT:
            return "".join(letters)
