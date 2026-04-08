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

## Upload to GitHub
### Option 1: Using Git from terminal
```bash
git init
git add .
git commit -m "Initial commit - Caesar Cipher tool"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/caesar-cipher-tool.git
git push -u origin main
```

### Option 2: Upload from GitHub website
1. Create a new repository on GitHub named `caesar-cipher-tool`.
2. Click **Add file** > **Upload files**.
3. Upload `caesar_cipher.py` and `README.md`.
4. Commit the files.

## GitHub Hosting Guide
This Python script itself cannot run on GitHub Pages because GitHub Pages hosts static files such as HTML, CSS, and JavaScript, not Python backend code.

You have three practical options:

### A. Host the code repository only
Best if you want to showcase the tool and let users download or clone it.

### B. Host documentation on GitHub Pages
Create a static project page with usage instructions, screenshots, and code snippets.

Basic steps:
1. Create `index.html` in the repository.
2. Go to GitHub repository **Settings** > **Pages**.
3. Under **Build and deployment**, choose **Deploy from a branch**.
4. Select branch `main` and folder `/ (root)`.
5. Save and wait for the site URL.

### C. Make a web version
Convert the cipher logic to JavaScript and host that HTML/JS app on GitHub Pages.

## Suggested Next Upgrade
- Add brute-force mode for trying all 26 shifts.
- Add file input/output support.
- Add a simple HTML + JavaScript web interface for GitHub Pages.
- Add unit tests with `pytest`.

## License
You can use this project for learning, practice, and portfolio purposes.
