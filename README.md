## EnigmaForge

- EnigmaForge is a simple Cybersecurity project. It is a very effective tool for encrypting and decrypting messages, providing users with a secure way to protect their sensitive communications. Using Python's Tkinter library for the graphical interface and Base64 encoding for message transformation, EnigmaForge ensures that only intended recipients can access the message content.

Author & Licence copyright (c) 2024 Najma W Thande


## Table of Contents

Features
Project Setup
Usage
Requirements
Project Structure

## Features

- User-Friendly GUI: Simple and intuitive interface for easy message encryption and decryption.
- Password-Based Access: Only users with the correct password can decrypt messages.
- Base64 Encoding: Provides fundamental security for communication.
- Accessible for Non-Technical Users: No advanced technical knowledge is needed.

## Project Setup

To set up EnigmaForge locally, follow these steps:

- Clone the repository:

git clone https://github.com/........
cd EnigmaForge
Install required dependencies: Make sure you have Python installed. Tkinter is part of the standard Python library, but if not included, install it:

# For Debian/Ubuntu
sudo apt-get install python3-tk

# For macOS
brew install python-tk

# For Windows, Tkinter comes with Python installation by default

- Run the application:

python enigmaforge.py


Author & Licence copyright (c) 2024 Najma W Thande


## Usage

- Open EnigmaForge: Run the enigmaforge.py script to launch the GUI.

- Encrypt a Message:
Type your message in the provided input field.

- Set a password.
Click the Encrypt button to see the encoded message.

- Decrypt a Message:
Enter the encrypted message and password.

- Click Decrypt to view the original message.


## Requirements 

Python 3.x
Tkinter (for the GUI)
Base64 (part of Python's standard library)

## Project Structure

EnigmaForge/
│
├── enigmaforge.py      # Main application file
├── README.md           # Project documentation
├── requirements.txt    # Dependencies (if any additional packages are used)
└── assets/             # Optional: place for icons or other assets

Author & Licence copyright (c) 2024 Najma W Thande
