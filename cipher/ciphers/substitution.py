from encryptor.config.common import CMD


def cipher(text: str, key: str, cmd: CMD) -> str:
    # TODO: try to handle UpperCase too
    text = text.lower()
    key = key.lower()

    result = ""

    letters = "abcdefghijklmnopqrstuvwxyz"
    key += "".join([letter for letter in letters if letter not in key])

    for char in text:
        if not char.isalpha():
            result += char
            continue

        match cmd:
            case CMD.ENCRYPT:
                result += key[letters.index(char)]
            case CMD.DECRYPT:
                result += letters[key.index(char)]

    return result
