from encryptor.config.common import CMD, NUM_LETTERS


def create_keyword(text: str, key: str) -> str:
    repeat = len(text) // len(key) + 1
    return (key * repeat)[: len(text)]


def cipher(text: str, key: str, cmd: CMD) -> str:
    if not text or not key or str(key).isdigit():
        raise TypeError

    keyword = create_keyword(text, key)

    result = ""
    step = 0

    for index, char in enumerate(text):
        if not char.isalpha():
            result += char
            step += 1
            continue

        shift_base = ord("A") if char.isupper() else ord("a")
        key_code = ord(keyword[index - step]) - shift_base
        char_code = ord(char) - shift_base

        match cmd:
            case CMD.ENCRYPT:
                char_code = (char_code + key_code) % NUM_LETTERS
            case CMD.DECRYPT:
                char_code = (char_code - key_code) % NUM_LETTERS

        result += chr(char_code + shift_base)

    return result
