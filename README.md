# 📶 WiFi QR Code Generator

A simple Python application that generates a QR code for your WiFi network.

Enter your WiFi name, password, and security type in the application, and it will generate a scannable QR code. Guests can scan the QR code with their phone to connect to the WiFi without manually typing the password.

## ✨ Features

* 📶 Enter WiFi network name (SSID)
* 🔒 Enter WiFi password
* 🛡️ Choose security type
* 📱 Generate a scannable WiFi QR code
* 🖼️ Preview the QR code directly in the application
* 💾 Automatically save QR codes as PNG files
* 📁 Automatically creates a `QR_Codes` folder
* 🔄 Create multiple QR codes easily

## 📦 Requirements

Make sure Python is installed on your computer.

Install the required library:

```cmd
C:\Users\Admin\AppData\Local\Programs\Python\Python314\python.exe -m pip install "qrcode[pil]"
```

## 🚀 How to Run

Open Command Prompt and run:

```cmd
cd %USERPROFILE%\Documents
C:\Users\Admin\AppData\Local\Programs\Python\Python314\python.exe wifiqrcodegenerator.py
```

## 🖥️ How It Works

1. Open the application.
2. Enter your WiFi name.
3. Enter your WiFi password.
4. Select the security type.
5. Click **Generate QR Code**.
6. The input screen disappears.
7. Your QR code appears on the screen.
8. The QR code is automatically saved as a PNG inside the `QR_Codes` folder.
9. Scan the QR code with a compatible phone to connect to the WiFi.

## 🔐 Security Types

* `WPA` – Recommended for most modern WiFi networks
* `WEP` – For older WiFi networks
* `nopass` – For open WiFi networks without a password

## 🛠️ Built With

* Python
* Tkinter
* qrcode
* Pillow

## 📄 License

This project is open source and available under the MIT License.

---

Made with ❤️ using Python

Author: Vrushabh Kamdi 

