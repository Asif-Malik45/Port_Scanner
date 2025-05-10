import socket
import threading
from datetime import datetime

#Common Ports & its Services:
common_ports = {
    20: "FTP (DATA)",
    21: "FTP (CONTROL)",
    22: "SSH (OpenSSH)",
    23: "Telnet",
    25: "SMTP (sendmail)",
    53: "DNS",
    80: "HTTP (Apache,nginx)",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP (Remote Desktop)",
    8080: "HTTP Proxy (Apache Tomcat,ngnix)"    
} 

# Get user input to target:
target = input("Enter the target ip: ")
start_port = int(input("Enter starting range of port: "))
end_port = int(input("Enter end of port: "))

#Start time set:
print(f"\nScanning target {target} from {start_port - end_port}.. ")
start_time = datetime.now()


#connecting to ip and port to scan:
try:
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = sock.connect_ex((target, port))
        if result == 0:
            service = common_ports.get(port, "Unknown")
            print(f"\n Port {port} is OPEN --> {service}")
        sock.close()

#excepting errors:
except KeyboardInterrupt:
    print("\nScan interrupted by user.")
except socket.gaierror:
    print("\nHostname could not be resolved.")
except socket.error:
    print("\nCould not connect to server.")



#Set end time:
end_time = datetime.now()
print(f"\nScan Completed in {start_time - end_time}..")

