import socket
import termcolor


def scan(target, ports):
    print("\n" + "Starting Scan for " + str(target) + " :")
    for port in range(1, ports):
        scan_port(target, port)


def scan_port(ip_address, port):
    try:
        sock = socket.socket()
        sock.connect((ip_address, port))
        print(
            f"[+]{termcolor.colored(f'Port {port} is open on {ip_address}', 'green')}"
        )
        sock.close()
    except:
        pass


targets = input("[*] Enter the targets to scan(split them by ,): ")
ports = int(input("[*] Enter the target port(s): "))
if "," in targets:
    print("[*] Scanning multiple targets...")
    for ip_addr in targets.split(","):
        scan(ip_addr.strip(" "), ports)
else:
    scan(targets, ports)
