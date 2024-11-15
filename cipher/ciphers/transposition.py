from encryptor.config.common import CMD


def cipher(text: str, key: int, cmd: CMD) -> str:
    result = [""] * len(text)
    letter_idx = 0

    for col in range(key):
        pointer = col

        while pointer < len(text):
            match cmd:
                case CMD.ENCRYPT:
                    result[col] += text[pointer]
                case CMD.DECRYPT:
                    result[pointer] = text[letter_idx]
                    letter_idx += 1

            pointer += key

    return "".join(result)
