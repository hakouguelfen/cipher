from encryptor.config.common import CMD, NUM_LETTERS


def create_keyword(msg, key):
    keyword = ""

    msg_len = len(msg.replace(" ", ""))
    key_len = len(key.replace(" ", ""))
    remaining = msg_len % key_len

    if remaining == 0:
        keyword = key * int(msg_len / key_len)
    else:
        repeat = (msg_len - remaining) / key_len
        keyword = key * int(repeat) + key[:remaining]

    return keyword


def cipher(text: str, key: str, cmd: CMD) -> str:
    keyword = create_keyword(text, key)

    result = ""
    step = 0

    for index, char in enumerate(text):
        if char.isspace():
            result += " "
            step += 1
            continue
        if not char.isalpha():
            result += char
            step += 1
            continue

        shift_base = ord("A") if char.isupper() else ord("a")
        key_code = ord(keyword[index - step]) - shift_base
        char_code = ord(char) - shift_base

        # print(f"shift base: {shift_base}")
        # print(f"key: {keyword[index - step]} => {key_code}")
        # print(f"chr: {char} => {char_code} \n")

        if cmd == CMD.ENCRYPT:
            char_code = (char_code + key_code) % NUM_LETTERS
        elif cmd == CMD.DECRYPT:
            char_code = (char_code - key_code) % NUM_LETTERS

        result += chr(shift_base + char_code)

    return result


# msg = cipher("Hello, World!", "KEY", CMD.ENCRYPT)
# print(msg)
