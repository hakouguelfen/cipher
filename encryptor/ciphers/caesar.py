from encryptor.config.common import CMD, NUM_LETTERS


def cipher(text: str, key: int, cmd: CMD) -> str:
    result = ""

    for char in text:
        if not char.isalpha():
            result += char
            continue

        shift_base = ord("A") if char.isupper() else ord("a")
        char_code = ord(char) - shift_base

        match cmd:
            case CMD.ENCRYPT:
                char_code = (char_code + key) % NUM_LETTERS
            case CMD.DECRYPT:
                char_code = (char_code - key) % NUM_LETTERS

        result += chr(shift_base + char_code)

    return result


res = cipher("", 5, CMD.ENCRYPT)
print(res)
