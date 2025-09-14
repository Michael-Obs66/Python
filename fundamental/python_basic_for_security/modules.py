import os, re, socket

#os
print("Current directory:", os.getcwd())

#re (regex)
text = "Ping from 192.168.1.1 successful"
ip = re.findall(r"(?:\d{1,3}\.){3}\d{1,3}", text)
print("IP Found:", ip)
