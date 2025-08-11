## Caesar Cipher Encoder/Decoder

## 📜 Overview

This Python program implements a **Caesar Cipher**, a classic encryption technique used to encode and decode messages by shifting letters of the alphabet by a fixed number of positions.

## The program supports:

* **Encoding** messages (encryption)
* **Decoding** messages (decryption)
* Handling **non-alphabet characters** (numbers, symbols, spaces) without altering them
* Continuous use until the user decides to exit

## 🛠 Features

* **Simple Encryption & Decryption** using a shift number.
* **Preserves Non-Alphabet Characters** (spaces, punctuation, numbers).
* **Loop Functionality** to run multiple operations without restarting the program.
* **Interactive User Interface** via terminal input/output.

## ⚙️ How It Works

* **Alphabet List**: Stores letters `a` to `z`.
* **Shift Logic**: Shifts characters forward (encode) or backward (decode) using modular arithmetic.
* **Non-Alphabet Handling**: Characters not in the alphabet remain unchanged.
* **Restart Mechanism**: A `while` loop lets users run multiple operations in one session.


## 📌 Notes

* Shift numbers larger than 26 are handled using the modulus operator `%`.
* The program works only with lowercase letters (input is automatically converted).
* Ensure that `art.py` exists in the same folder for the ASCII art logo to display.