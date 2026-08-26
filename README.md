# # 📶 WiFi QR Code Generator

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

Clone this repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Go to the project folder:

```bash
cd wifi-qr-generator
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## ▶️ How to Run

Run the Python file:

```bash
py generate_wifi_qr.py
```

Or:

```bash
python generate_wifi_qr.py
```

## ⚙️ Configuration

Open `generate_wifi_qr.py` and change these values:

```python
ssid = "YOUR_WIFI_NAME"
password = "YOUR_WIFI_PASSWORD"
security = "WPA"
```

## 📁 Project Structure

```text
wifi-qr-generator/
│
├── generate_wifi_qr.py
├── requirements.txt
├── README.md
└── wifi_qr.png
```

## 📸 Output

The program generates a file called:

```text
wifi_qr.png
```

Scan the QR code using your phone's camera to connect to the configured WiFi network.

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
