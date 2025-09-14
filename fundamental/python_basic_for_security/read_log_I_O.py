with open("access.log", "r") as f:
    for line in f:
        if "404" in line:
            print("Error ditemukan:", line.strip())
