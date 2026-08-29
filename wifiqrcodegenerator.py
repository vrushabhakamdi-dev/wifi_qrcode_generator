import tkinter as tk
from tkinter import ttk, messagebox
import qrcode
from PIL import ImageTk
import os
from datetime import datetime


def generate_qr():
    wifi_name = wifi_name_entry.get().strip()
    wifi_password = wifi_password_entry.get()
    security_type = security_var.get()

    # Validation
    if not wifi_name:
        messagebox.showerror("Error", "Please enter your WiFi name.")
        return

    if security_type != "nopass" and not wifi_password:
        messagebox.showerror("Error", "Please enter your WiFi password.")
        return

    # Create WiFi QR data
    wifi_data = (
        f"WIFI:T:{security_type};"
        f"S:{wifi_name};"
        f"P:{wifi_password};;"
    )

    # Generate QR code
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4
    )

    qr.add_data(wifi_data)
    qr.make(fit=True)

    img = qr.make_image(
        fill_color="black",
        back_color="white"
    )

    # Get the folder where this Python script is located
    script_folder = os.path.dirname(os.path.abspath(__file__))

    # Create QR_Codes folder automatically
    save_folder = os.path.join(script_folder, "QR_Codes")
    os.makedirs(save_folder, exist_ok=True)

    # Create unique filename using date and time
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"wifi_qr_{timestamp}.png"

    # Full save path
    file_path = os.path.join(save_folder, filename)

    # Save QR code
    try:
        img.save(file_path)
    except Exception as e:
        messagebox.showerror(
            "Save Error",
            f"Could not save QR code:\n{e}"
        )
        return

    # Resize QR code for display
    display_img = img.resize((350, 350))

    # Convert image for Tkinter
    qr_image = ImageTk.PhotoImage(display_img)

    # Hide input screen
    input_frame.pack_forget()

    # Display QR code
    qr_label.config(image=qr_image)
    qr_label.image = qr_image

    # Update saved file message
    saved_label.config(
        text=f"Saved in QR_Codes folder\n{filename}"
    )

    # Show QR screen
    qr_frame.pack(expand=True, fill="both")


def go_back():
    # Hide QR screen
    qr_frame.pack_forget()

    # Clear previous inputs
    wifi_name_entry.delete(0, tk.END)
    wifi_password_entry.delete(0, tk.END)
    security_var.set("WPA")

    # Show input screen
    input_frame.pack(expand=True, fill="both")


# ==========================================
# MAIN WINDOW
# ==========================================

root = tk.Tk()
root.title("WiFi QR Code Generator")
root.geometry("500x600")
root.resizable(False, False)


# ==========================================
# INPUT SCREEN
# ==========================================

input_frame = tk.Frame(root)
input_frame.pack(expand=True, fill="both")


title = tk.Label(
    input_frame,
    text="WiFi QR Code Generator",
    font=("Arial", 20, "bold")
)

title.pack(pady=30)


# WiFi Name
tk.Label(
    input_frame,
    text="WiFi Name (SSID)",
    font=("Arial", 12)
).pack()

wifi_name_entry = tk.Entry(
    input_frame,
    width=35,
    font=("Arial", 13)
)

wifi_name_entry.pack(pady=8)


# WiFi Password
tk.Label(
    input_frame,
    text="WiFi Password",
    font=("Arial", 12)
).pack()

wifi_password_entry = tk.Entry(
    input_frame,
    width=35,
    font=("Arial", 13),
    show="*"
)

wifi_password_entry.pack(pady=8)


# Security Type
tk.Label(
    input_frame,
    text="Security Type",
    font=("Arial", 12)
).pack()

security_var = tk.StringVar(value="WPA")

security_menu = ttk.Combobox(
    input_frame,
    textvariable=security_var,
    values=["WPA", "WEP", "nopass"],
    state="readonly",
    width=32,
    font=("Arial", 12)
)

security_menu.pack(pady=8)


# Generate Button
generate_button = tk.Button(
    input_frame,
    text="Generate QR Code",
    font=("Arial", 13, "bold"),
    command=generate_qr,
    width=22
)

generate_button.pack(pady=30)


# ==========================================
# QR CODE SCREEN
# ==========================================

qr_frame = tk.Frame(root)


qr_title = tk.Label(
    qr_frame,
    text="Your WiFi QR Code",
    font=("Arial", 22, "bold")
)

qr_title.pack(pady=20)


qr_label = tk.Label(qr_frame)
qr_label.pack(pady=10)


info_label = tk.Label(
    qr_frame,
    text="Scan this QR code to connect to the WiFi",
    font=("Arial", 12)
)

info_label.pack(pady=8)


saved_label = tk.Label(
    qr_frame,
    text="",
    font=("Arial", 10)
)

saved_label.pack(pady=5)


back_button = tk.Button(
    qr_frame,
    text="Create Another QR Code",
    font=("Arial", 11),
    command=go_back
)

back_button.pack(pady=20)


# Start application
root.mainloop()
