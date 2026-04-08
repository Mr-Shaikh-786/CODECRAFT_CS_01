#!/usr/bin/env python3
import argparse
import sys


def shift_char(char: str, shift: int) -> str:
    if char.isalpha():
        base = ord('A') if char.isupper() else ord('a')
        return chr((ord(char) - base + shift) % 26 + base)
    return char


def caesar_cipher(text: str, shift: int, mode: str = "encrypt") -> str:
    normalized_shift = shift % 26
    if mode == "decrypt":
        normalized_shift = -normalized_shift
    return "".join(shift_char(ch, normalized_shift) for ch in text)


def interactive_mode() -> None:
    print("Caesar Cipher Tool")
    print("Type 'encrypt' or 'decrypt' to continue. Type 'exit' to quit.\n")

    while True:
        mode = input("Mode (encrypt/decrypt/exit): ").strip().lower()
        if mode == "exit":
            print("Goodbye!")
            return
        if mode not in {"encrypt", "decrypt"}:
            print("Invalid mode. Please choose 'encrypt' or 'decrypt'.\n")
            continue

        message = input("Message: ")
        try:
            shift = int(input("Shift value: "))
        except ValueError:
            print("Shift value must be an integer.\n")
            continue

        result = caesar_cipher(message, shift, mode)
        print(f"Result: {result}\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Encrypt or decrypt text using the Caesar Cipher algorithm.")
    parser.add_argument("-m", "--mode", choices=["encrypt", "decrypt"], help="Choose whether to encrypt or decrypt.")
    parser.add_argument("-t", "--text", help="Text to process.")
    parser.add_argument("-s", "--shift", type=int, help="Shift value for the cipher.")
    parser.add_argument("-i", "--interactive", action="store_true", help="Run the tool in interactive mode.")
    args = parser.parse_args()

    if args.interactive or not all([args.mode, args.text is not None, args.shift is not None]):
        interactive_mode()
        return

    result = caesar_cipher(args.text, args.shift, args.mode)
    print(result)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("\nInterrupted by user.")
