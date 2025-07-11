import http.server
import socketserver
import socket
import os
import pyqrcode
import webbrowser

PORT = 8010
desktop = os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop")

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
server_url = f"http://{local_ip}:{PORT}"

qr = pyqrcode.create(server_url)
qr_file = "myqr.svg"
qr.svg(qr_file, scale=8)

webbrowser.open(f"file://{os.path.abspath(qr_file)}")

print(f"\n✅ Server Ready!")
print(f"📁 Serving files from: {desktop}")
print(f"🌐 Access it at: {server_url}")
print(f"📱 Or scan the QR code (myqr.svg)")

os.chdir(desktop)

handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"\n🚀 Server running on port {PORT}... Press Ctrl+C to stop.")
    httpd.serve_forever()
