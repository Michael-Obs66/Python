def check_port(ip, port):
  # (dummy check, without socket for learn)
  if port in [22, 80, 443]
      return True
  return False

print(check_port("192.168.1.100", 22)) # True
print(check_port("192.168.1.100", 21)) # False
