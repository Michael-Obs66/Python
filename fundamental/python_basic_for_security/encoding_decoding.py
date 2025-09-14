import base64
import urllib.parse

msg = "admin:password123"

# Base64
encoded = base64.b64encode(msg.encode()).decode()
decoded = base64.b64decode(encoded).decode()
print("Base64 Encoded:", encoded)
print("Base64 Decoded:", decoded)

# URL encoding
url = "https://example.com/login?user=admin password"
encoded_url = urllib.parse.quote(url)
decoded_url = urllib.parse.unquote(encoded_url)
print("URL Encoded:", encoded_url)
print("URL Decoded:", decoded_url)
