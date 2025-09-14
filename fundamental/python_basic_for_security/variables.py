#string (IP & Domain)
ip = "8.8.8.8" #you can change for your target
domain = "example.com" #change for your domain

#integer (port)
port = 22 #port

#float (response time)
ping_time = 0.135

#Boolean (status host)
is_alive = True

#List (Ports to Scan"
common_ports = [21, 22, 80, 443]

# dictionary (host info)
host_info = {
  "ip" : "192.168.1.10"
  "os" : "Linux"
  "open_ports" : [22, 80, 443]
}

print(ip, domain)
print("Ports:", common_ports)
print("Info host:", host_info)
