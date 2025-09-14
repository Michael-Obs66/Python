import re

log = "User login from admin@example.com, IP 10.0.0.5"
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", log)
ips = re.findall(r"(?:\d{1,3}\.){3}\d{1,3}", log)

print("Emails:", emails)
print("IPs:", ips)
