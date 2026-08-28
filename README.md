# 📶 WiFi QR Code Generator

A simple Python project that generates a QR code for your WiFi network.

Users can scan the generated QR code with their phone to connect to the WiFi network without manually entering the password.

## 🚀 Features

* 📶 Generate WiFi QR codes
* 📱 Easily connect to WiFi by scanning the QR code
* 🔐 Supports password-protected WiFi networks
* 🖼️ Automatically saves the QR code as an image
* 🐍 Simple Python implementation

## 🛠️ Technologies Used

* Python
* wifi-qrcode-generator
* Pillow

## 📦 Installation

Download this repository from GitHub and extract the ZIP file.

Open **Command Prompt (CMD)** and go to your Downloads folder:

```cmd
cd %USERPROFILE%\Downloads
```

Go to the project folder:

```cmd
cd wifi-qr-generator
```

Install the required packages:

```cmd
py -m pip install -r requirements.txt
```

## ▶️ How to Run

Run the Python file:

```cmd
py wifi_qrcode_generator.py
```

If `py` does not work, try:

```cmd
python wifi_qrcode_generator.py
```

## ⚙️ Configuration

Open `wifi_qrcode_generator.py` and change these values:

```python
ssid = "YOUR_WIFI_NAME"
password = "YOUR_WIFI_PASSWORD"
security = "WPA"
```

## 📁 Project Structure

```text
wifi-qr-generator/
│
├── wifi_qrcode_generator.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## 📸 Output

The program automatically generates a WiFi QR code image.

Scan the generated QR code using your phone's camera to connect to the configured WiFi network.

## 🔮 Future Improvements

* Add a graphical user interface
* Allow users to enter WiFi details interactively
* Add custom QR code colors
* Add logo support
* Create a web version
* Add support for different security types

## 👨‍💻 Author

**Vrushabh Kamdi**

⭐ If you like this project, consider giving it a star!
