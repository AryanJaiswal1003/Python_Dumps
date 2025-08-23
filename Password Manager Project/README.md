# Password Manager (Tkinter)

A simple **Password Manager** built using **Python** and **Tkinter**.  
It allows users to generate strong passwords, copy them automatically to the clipboard, and save login credentials (website, email, and password) into a local file.

---

## Features
- **Password Generator**  
  - Creates secure passwords with random letters, numbers, and symbols.  
  - Automatically copies the generated password to the clipboard.  

- **Credential Storage**  
  - Saves website, email/username, and password into `data.txt`.  
  - Prevents saving if any field is left empty.  
  - Confirms with the user before saving details.  

- **User-Friendly UI**  
  - Built with **Tkinter** for a simple and responsive interface.  
  - Includes input fields, buttons, and a logo for a better experience.  

---

## 📁 PasswordManager
    ┣ 📜 password_manager.py   # Main application script
    ┣ 📜 data.txt              # Saved credentials (generated after first save)
    ┣ 🖼️ logo.png              # App logo (must be in same folder)
    ┗ 📜 README.md             # Project documentation