import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from ttkthemes import ThemedTk

from config import ALGORITHMS, CMD
from ciphers import caesar, vigenere, substitution
from ciphers import transposition


class Encryptor:
    def __init__(self) -> None:
        self.root = ThemedTk(theme="arc")
        self.root.title("Encryptor APP")
        self.root.resizable(False, False)

        self.current_algorithm = tk.StringVar()
        self.current_key = tk.StringVar()
        self.build()

    def build_input_frame(self):
        msg_frame = ttk.Frame(self.content_frame)
        msg_frame.grid(row=0, column=0, padx=20, pady=20)

        msg_label = ttk.Label(msg_frame, text="Input text")
        msg_label.grid(row=0, column=0, sticky=tk.N)
        self.input_msg = ScrolledText(msg_frame, wrap=tk.WORD, width=40, height=6)
        self.input_msg.grid(row=1, column=0, padx=10, pady=10)
        self.input_msg.focus()

    def build_configuration(self):
        config_frame = ttk.Frame(self.content_frame)
        config_frame.grid(row=0, column=1, sticky=tk.NSEW, padx=20, pady=20)

        algorithms_label = ttk.Label(config_frame, text="Choose algorithm:")
        algorithms_label.grid(row=0, column=1, sticky=tk.W)

        algorithms = ttk.Combobox(
            config_frame,
            textvariable=self.current_algorithm,
            width=30,
            state="readonly",
        )
        algorithms["value"] = (
            ALGORITHMS.CAESAR.value,
            ALGORITHMS.VIGENERE.value,
            ALGORITHMS.SUBSTITUTION.value,
            ALGORITHMS.TRANSPOSITION.value,
        )
        algorithms.current(0)
        algorithms.grid(row=1, column=1, sticky=tk.W)

        # Encryption/Decryption Key
        key_label = ttk.Label(config_frame, text="Choose key:")
        key_label.grid(row=2, column=1, sticky=tk.SW)

        key_entry = ttk.Entry(config_frame, textvariable=self.current_key, width=30)
        key_entry.grid(row=3, column=1, sticky=tk.SW)

    def build_output_frame(self):
        msg_frame = ttk.Frame(self.content_frame)
        msg_frame.grid(row=0, column=2, padx=20, pady=20)

        msg_label = ttk.Label(msg_frame, text="Output text")
        msg_label.grid(row=0, column=2, sticky=tk.N)

        self.output_msg = ScrolledText(msg_frame, wrap=tk.WORD, width=40, height=6)
        self.output_msg.grid(row=1, column=2, padx=10, pady=10)

    def build_controller(self):
        control_frame = ttk.Frame(self.content_frame)
        control_frame.grid(row=2, column=0, sticky="ew", padx=20, pady=20)

        encrypt_button = ttk.Button(
            control_frame,
            text="Encrypt message",
            command=lambda: self.apply_cipher(CMD.ENCRYPT),
        )
        encrypt_button.grid(row=2, column=0, padx=10, pady=10)

        decrypt_button = ttk.Button(
            control_frame,
            text="Decrypt message",
            command=lambda: self.apply_cipher(CMD.DECRYPT),
        )
        decrypt_button.grid(row=2, column=1, padx=10, pady=10)

    def build(self):
        self.content_frame = ttk.Frame(self.root)
        self.content_frame.grid(row=0, column=0)

        self.build_input_frame()
        self.build_configuration()
        self.build_output_frame()
        self.build_controller()

    def apply_cipher(self, cmd: CMD):
        match self.current_algorithm.get():
            case ALGORITHMS.CAESAR.value:
                self.run(caesar.cipher, int(self.current_key.get()), cmd)

            case ALGORITHMS.VIGENERE.value:
                self.run(vigenere.cipher, self.current_key.get(), cmd)

            case ALGORITHMS.SUBSTITUTION.value:
                self.run(substitution.cipher, self.current_key.get(), cmd)

            case ALGORITHMS.TRANSPOSITION.value:
                self.run(transposition.cipher, int(self.current_key.get()), cmd)

    def run(self, fun, key, cmd):
        input_msg = self.input_msg.get("1.0", "end-1c")

        self.output_msg.delete("1.0", "end")
        output_msg = fun(text=input_msg, key=key, cmd=cmd)
        self.output_msg.insert("1.0", output_msg)


if __name__ == "__main__":
    app = Encryptor()
    app.root.mainloop()
