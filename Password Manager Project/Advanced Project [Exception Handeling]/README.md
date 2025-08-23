## Password Manager (with JSON Storage)

A simple but powerful **Password Manager** built using **Python** and **Tkinter**.  
This app allows you to generate strong passwords, copy them directly to your clipboard, and save login credentials securely in a **JSON file** for future retrieval.  
You can also **search for saved credentials** by website name.

---

## Features
- **Generate Secure Passwords**
  - Randomly creates a mix of letters, numbers, and symbols.
  - Automatically copies the password to the clipboard.

- **Save Credentials**
  - Stores website, email/username, and password into `data.json`.
  - If the JSON file is missing or empty, it is created automatically.
  - New entries update existing data without overwriting.

- **Search Functionality**
  - Instantly look up a website to retrieve stored email and password.
  - Provides error messages if the site does not exist in the database.

- **User-Friendly GUI**
  - Built with **Tkinter** for a clean and responsive interface.
  - Includes input fields, buttons, and a lock logo.

---

## File Structure
    ┣ main.py          # Main application
    ┣ data.json        # Stores saved credentials (auto-created)
    ┣ logo.png         # Application logo
    ┗ README.md        # Project documentation