
# Cryptify

## Introduction

Cryptify is a simple GUI-based application built with Python that allows users to encrypt and decrypt text using a basic Base64 encoding and decoding method. The application uses `customtkinter` for the GUI and provides a straightforward interface for text encryption and decryption with a secret key.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)
- [License](#license)

## Installation

To run Cryptify, ensure you have Python installed. You'll also need to install the `customtkinter` package.

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/cryptify.git

2.Install the required dependencies:
   ```bash
   pip install customtkinter
   ```


 ## Usage
To start the application, run the script main.py:
   ```bash
   python main.py
   ```
Once the application is running:

1. Enter the text you want to encrypt or decrypt in the text box provided.
2. Input the secret key (password) 1234.
3. Click on the "ENCRYPT" button to encrypt the text or the "DECRYPT" button to decrypt it.
4. The output will be displayed in a new window.
## Features
- Text Encryption: Encrypts the input text using Base64 encoding.
- Text Decryption: Decrypts the Base64 encoded text back to its original form.
- Simple GUI: User-friendly interface with buttons for encryption, decryption, and resetting the input.
## Dependencies
- Python 3.x
- customtkinter package
- tkinter (usually comes pre-installed with Python)

## Configuration
No special configuration is needed. However, you can modify the encryption key or change the appearance and theme settings by editing the script.

## Examples
- Encrypting Text:
Enter your text in the provided input field, input the password 1234, and press the "ENCRYPT" button.

- Decrypting Text:
To decrypt an encrypted message, paste the encoded text, input the password 1234, and press the "DECRYPT" button.

## Troubleshooting
- Invalid Password: If an incorrect password is entered, an error message will be displayed. Ensure that the password is set to 1234.
- Empty Input Fields: The application will warn you if you try to encrypt or decrypt without entering text or a password.
## Contributors
- Sai Krishna - Initial work
## License
This project is licensed under the MIT License. See the LICENSE file for details.
