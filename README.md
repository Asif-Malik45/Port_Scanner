# 🔎 Python Port Scanner

A beginner-friendly **Port Scanner** written in Python. This tool scans a target IP address for open TCP ports in a user-defined range using basic socket programming.

---

## 🚀 Features

- Scans a range of ports on any given IP address
- Uses Python’s built-in `socket` and `datetime` modules
- Reports which ports are open
- Gives the output ports with name and it service
- Measures total scan time
- Includes basic error handling (host resolution, connection issues, Ctrl+C)

---

## 🛠️ Technologies Used

- Python 3
- `socket` module — for network communication
- `datetime` module — for tracking scan duration

---

## 📷 Screenshot

```bash
Enter the IP address to scan: 192.168.1.1
Enter start port: 20 
Enter end port: 100 

Scanning target 192.168.1.1 from port 20 to 100
Port 22 is OPEN --> FTP (DATA)
Port 80 is OPEN --> Unknown

Scan completed in: 0:00:10.532000
