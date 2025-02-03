import random

def generate_random_ip():
    # Menghasilkan IP dalam format 192.168.x.x
    return f"192.168.{random.randint(0, 255)}.{random.randint(1, 254)}"

def check_firewall_rules(ip, rules):
    # Memeriksa apakah IP ada dalam rules
    if ip in rules:
        return rules[ip]  # action (block/allow)
    return "allow"  # IP tidak ditemukan, kembalikan "allow"

def main():
    # rules firewall
    firewall_rules = {
        "192.168.45.123": "block",
        "192.168.201.78": "block",
        "192.168.12.234": "block",
        "192.168.167.56": "block",
        "192.168.89.12": "block",
        "192.168.34.189": "block",
    }
    
    # Loop untuk menghasilkan 12 IP randp, dan memeriksa rules firewall
    for _ in range(12):
        ip_address = generate_random_ip()  # Generate IP
        action = check_firewall_rules(ip_address, firewall_rules)  # Cek the rules
        random_number = random.randint(0, 9999)  # Generate angka acak
        print(f"IP {ip_address}, Action: {action}, Random: {random_number}")

if __name__ == "__main__":
    main()