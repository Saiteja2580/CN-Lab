# ARP/RARP Table (IP to MAC mapping)
arp_table = {
    "192.168.1.1": "00:0a:95:9d:68:16",
    "192.168.1.2": "00:0a:95:9d:68:17",
    "192.168.1.3": "00:0a:95:9d:68:18",
}

# Reverse ARP table (MAC to IP)
rarp_table = {mac: ip for ip, mac in arp_table.items()}

def arp(ip_address):
    print("\n[ARP] Resolving MAC for IP:", ip_address)
    mac = arp_table.get(ip_address)
    if mac:
        print(f"Found MAC address: {mac}")
    else:
        print("MAC address not found for given IP.")

def rarp(mac_address):
    print("\n[RARP] Resolving IP for MAC:", mac_address)
    ip = rarp_table.get(mac_address)
    if ip:
        print(f"Found IP address: {ip}")
    else:
        print("IP address not found for given MAC.")

def main():
    while True:
        print("\n===== ARP / RARP Simulation =====")
        print("1. ARP (Get MAC from IP)")
        print("2. RARP (Get IP from MAC)")
        print("3. Show ARP Table")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            ip = input("Enter IP address: ")
            arp(ip)
        elif choice == "2":
            mac = input("Enter MAC address: ")
            rarp(mac)
        elif choice == "3":
            print("\nCurrent ARP Table:")
            for ip, mac in arp_table.items():
                print(f"{ip} -> {mac}")
        elif choice == "4":
            print("Exiting simulation.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
