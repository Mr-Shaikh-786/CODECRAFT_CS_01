# Caesar Cipher Tool

A simple Python command-line tool that encrypts and decrypts text using the Caesar Cipher algorithm.

## Features
- Encrypts text with a custom shift value.
- Decrypts text with the same shift value.
- Preserves spaces, numbers, and symbols.
- Supports both interactive mode and command-line arguments.
- Easy to upload to GitHub.

## Project Structure
```bash
CODECRAFT_CS_01/
├── caesar_cipher.py
└── README.md
```

## Requirements
- Python 3.8 or newer

## Run the Tool
### 1) Interactive mode
```bash
python3 caesar_cipher.py
```

Example:
```text
Mode (encrypt/decrypt/exit): encrypt
Message: Hello World
Shift value: 3
Result: Khoor Zruog
```

### 2) Command-line mode
Encrypt:
```bash
python3 caesar_cipher.py --mode encrypt --text "Hello World" --shift 3
```

Decrypt:
```bash
python3 caesar_cipher.py --mode decrypt --text "Khoor Zruog" --shift 3
```

## How It Works
The Caesar Cipher shifts each alphabetic letter by a fixed number of positions in the alphabet. For example, with a shift of 3:
- A becomes D
- B becomes E
- X becomes A
- Y becomes B
- Z becomes C

Uppercase and lowercase letters are handled separately. Non-alphabetic characters stay unchanged.

---
