import socket

def skeniraj_metu(ip):
    # Lista uobicajnih portova za proveru
    portovi = {21: "FTP", 22: "SSH", 23: "Telnet", 80: "HTTP",443: "HTTPS", 3306: "MySQLR"}

    print(f"\n🔍 Provera IP adrese: {ip}")

    for port, servis in portovi.items():
        try:
            # Kreiramo socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.3) # Brzo skeniranje

            # Pokusaj povezivanja
            rezultat = s.connect_ex((ip,port))

            if rezultat == 0:
                print(f" ✅ Port {port} ({servis}) je OTVOREN!")

                # Pokusaj da "uhvatis" banner (identifikacija servisa)
                try:
                    s.send(b'Hello\r\n')
                    banner = s.recv(1024).decode().strip()
                    if banner:
                        print(f"    [INFO] Banner: {banner}")
                except:
                    pass
            s.close()
        except Exception:
            pass

def pokreni_lab_skener():
    mreza = "10.0.2." # Promeni ovo u skladu sa tvojom mrezom u VirtualBox-u
    print(f"🚀 Pokrecem skeniranje mreze {mreza}0/24...")

    for i in range(1, 15): # Skenira adrese od .1 do .14
        skeniraj_metu(f"{mreza}{i}")

if __name__ == "__main__":
    pokreni_lab_skener()