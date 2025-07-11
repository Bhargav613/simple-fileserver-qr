# simple-fileserver-qr
FileShare-HTTP-QR
A lightweight Python-based file sharing tool that lets you serve your Desktop folder over HTTP and generate a QR code for quick access across devices on the same local network.

Features
HTTP Server: Serves files from your Desktop folder using Python’s built-in http.server.

Auto IP Detection: Detects your local IP and binds the server to it.

QR Code Generation: Generates a QR code pointing to the local server’s URL.

Cross-Device Access: Share files with smartphones, tablets, or other systems on the same Wi-Fi network.

Zero Configuration: No database or complex setup required.

Technologies Used

Python 3.x

Modules: http.server, socket, pyqrcode, pypng, os, webbrowser

🛠️ How to Run
Clone this repository or download the script:
git clone https://github.com/your-username/fileshare-http-qr
Install required packages:
pip install pyqrcode pypng
Run the script:
python fileshare.py
Scan the myqr.png QR code with any device or open the printed link in a browser.

Use Cases
Share files quickly in a lab or classroom

Transfer files to mobile without a USB cable

Present files from your Desktop during team meetings

Note
Works best when all devices are on the same local network (e.g., same Wi-Fi).

Make sure port 8010 is not blocked by firewall or already in use.
