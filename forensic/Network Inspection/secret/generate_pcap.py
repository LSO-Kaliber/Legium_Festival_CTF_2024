from scapy.all import *
from faker import Faker
import random
import string

def generate_ftp(source, host, content):
    pcap_packets = []
    # FTP packet - Request
    ftp_request_packet = IP(src=source, dst=host)/TCP(sport=random.randint(1024, 65535), dport=21, seq=random.randint(1000, 5000))/Raw(load="USER kaliber\r\n")
    pcap_packets.append(ftp_request_packet)
    # FTP packet - Response
    ftp_response_packet = IP(src=host, dst=source)/TCP(sport=21, dport=ftp_request_packet[IP].sport, seq=ftp_request_packet[TCP].ack, ack=ftp_request_packet[TCP].seq + len(ftp_request_packet[Raw]))/Raw(load="331 Please specify the password.\r\n")
    pcap_packets.append(ftp_response_packet)
    # FTP packet - Request (Password)
    ftp_password_request_packet = IP(src=source, dst=host)/TCP(sport=ftp_request_packet[IP].sport+1, dport=21, seq=ftp_response_packet[TCP].ack, ack=ftp_response_packet[TCP].seq + len(ftp_response_packet[Raw]))/Raw(load="PASS qkXBmCv2Y/aU8s+Zgp@\r\n")
    pcap_packets.append(ftp_password_request_packet)
    # FTP packet - Response (Login Successful)
    ftp_login_successful_response_packet = IP(src=host, dst=source)/TCP(sport=21, dport=ftp_password_request_packet[IP].sport, seq=ftp_password_request_packet[TCP].ack, ack=ftp_password_request_packet[TCP].seq + len(ftp_password_request_packet[Raw]))/Raw(load="230 Login successful.\r\n")
    pcap_packets.append(ftp_login_successful_response_packet)
    # FTP packet - Request (PASV - Passive Mode)
    ftp_pasv_request_packet = IP(src=source, dst=host)/TCP(sport=ftp_password_request_packet[IP].sport+1, dport=21, seq=ftp_login_successful_response_packet[TCP].ack, ack=ftp_login_successful_response_packet[TCP].seq + len(ftp_login_successful_response_packet[Raw]))/Raw(load="PASV\r\n")
    pcap_packets.append(ftp_pasv_request_packet)
    # FTP packet - Response (Passive Mode)
    ftp_pasv_response_packet = IP(src=host, dst=source)/TCP(sport=21, dport=ftp_pasv_request_packet[IP].sport, seq=ftp_pasv_request_packet[TCP].ack, ack=ftp_pasv_request_packet[TCP].seq + len(ftp_pasv_request_packet[Raw]))/Raw(load="227 Entering Passive Mode (45,221,208,15,205,0).\r\n")
    pcap_packets.append(ftp_pasv_response_packet)
    # FTP packet - Request (STOR - Store File)
    file_content = content
    ftp_stor_request_packet = IP(src=source, dst=host)/TCP(sport=ftp_pasv_request_packet[IP].sport, dport=205, seq=ftp_pasv_response_packet[TCP].ack, ack=ftp_pasv_response_packet[TCP].seq + len(ftp_pasv_response_packet[Raw]))/Raw(load=f"STOR secret.txt\r\n{file_content}\r\n")
    pcap_packets.append(ftp_stor_request_packet)
    # FTP packet - Response (Transfer Complete)
    ftp_transfer_complete_response_packet = IP(src=host, dst=source)/TCP(sport=205, dport=ftp_stor_request_packet[IP].sport, seq=ftp_stor_request_packet[TCP].ack, ack=ftp_stor_request_packet[TCP].seq + len(ftp_stor_request_packet[Raw]))/Raw(load="226 Transfer complete.\r\n")
    pcap_packets.append(ftp_transfer_complete_response_packet)
    
    return pcap_packets  # Return the generated FTP packets

def read_file_content(file_path):
    with open(file_path, 'rb') as file:
        content = file.read()
    return content

def generate_custom_pcap():

    file_paths = [f'./file/hasil-{i}.txt' for i in range(1, 37)]
    http_response_body_array = [read_file_content(file_path) for file_path in file_paths]

    ip_layer_req = IP(dst="kaliber.or.id")

    pcap_packets = []

    for asd in range(1801):
        random_proto = random.choice(["ICMP", "UDP", "TCP", "DNS", "HTTP", "FTP"])  # Add more protocols as needed
        if random_proto == "ICMP":
            random_packet = IP(src="45.221.208.15", dst="kaliber.or.id") / ICMP()
        elif random_proto == "UDP":
            random_packet = IP(src="45.221.208.15", dst="kaliber.or.id") / UDP(sport=random.randint(1, 65535), dport=random.randint(1, 65535))
        elif random_proto == "TCP":
            random_length = random.randint(1000, 18000)
            random_packet = (IP(src="45.221.208.15", dst="kaliber.or.id") / TCP(sport=random.randint(1, 65535), dport=random.randint(1, 65535)) / Raw(RandString(size=random_length)))
        elif random_proto == "DNS":
            random_packet = IP(src="45.221.208.15", dst="kaliber.or.id") / UDP(dport=53) / DNS(qd=DNSQR(qname="kaliber.or.id"))
        elif random_proto == "HTTP":
            randomnumber = random.randint(1, 8)
            for i in range(randomnumber):
                fake = Faker()
                random_content_length = random.randint(1000, 18000)
                random_content = fake.texts(nb_texts=1, max_nb_chars=random_content_length)[0]
                print(f"get http on 1's debug: {i}/{randomnumber}")
                random_string_k = random.randint(18, 38)
                random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
                random_string2 = ''.join(random.choices(string.ascii_letters + string.digits, k=random_string_k))
                
                url = f"http://kaliber.or.id/{random_string}.php&page={random_string2}"
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                    "Accept-Language": "en-US,en;q=0.5",
                    "Accept-Encoding": "gzip, deflate",
                    "Connection": "keep-alive",
                    "Content-Type": "text/plain",
                    "Content-Length": f"{len(random_content)}"
                }
                http_request = (f"GET {url} HTTP/1.1\r\n"
                                f"Host: kaliber.or.id\r\n"
                                + "\r\n".join([f"{header}: {value}" for header, value in headers.items()]) +
                                f"\r\n\r\n{random_content}")
                random_packet = (IP(src="45.221.208.15", dst="kaliber.or.id") /
                                TCP(sport=random.randint(1, 65535), dport=80) /
                                Raw(load=http_request.encode()))
                pcap_packets.append(random_packet)
        elif random_proto == "FTP":
            random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=38))
            ftpprotocol = generate_ftp("45.221.208.15", "kaliber.or.id", random_string + "==")
            pcap_packets.append(ftpprotocol)
        pcap_packets.append(random_packet)
        print(f"debug 1's: {asd}/1801 - {random_proto}")

    ftpprotocol = generate_ftp("6.71.58.55", "45.221.208.15", "aF93MXIzc2g0a190b19uNHJyb3dfY2E2NzEzNWVkfQ==") # second flag
    pcap_packets.append(ftpprotocol)

    for asd in range(18):
        random_proto = random.choice(["ICMP", "UDP", "TCP", "DNS", "HTTP", "FTP"])  # Add more protocols as needed
        if random_proto == "ICMP":
            random_packet = IP(src="45.221.208.15", dst="kaliber.or.id") / ICMP()
        elif random_proto == "UDP":
            random_packet = IP(src="45.221.208.15", dst="kaliber.or.id") / UDP(sport=random.randint(1, 65535), dport=random.randint(1, 65535))
        elif random_proto == "TCP":
            random_length = random.randint(1000, 18000)
            random_packet = (IP(src="45.221.208.15", dst="kaliber.or.id") / TCP(sport=random.randint(1, 65535), dport=random.randint(1, 65535)) / Raw(RandString(size=random_length)))
        elif random_proto == "DNS":
            random_packet = IP(src="45.221.208.15", dst="kaliber.or.id") / UDP(dport=53) / DNS(qd=DNSQR(qname="kaliber.or.id"))
        elif random_proto == "HTTP":
            randomnumber = random.randint(1, 8)
            for i in range(randomnumber):
                fake = Faker()
                random_content_length = random.randint(1000, 18000)
                random_content = fake.texts(nb_texts=1, max_nb_chars=random_content_length)[0]
                print(f"get http on 2's debug: {i}/{randomnumber}")
                random_string_k = random.randint(18, 38)
                random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
                random_string2 = ''.join(random.choices(string.ascii_letters + string.digits, k=random_string_k))
                
                url = f"http://kaliber.or.id/{random_string}.php&page={random_string2}"
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                    "Accept-Language": "en-US,en;q=0.5",
                    "Accept-Encoding": "gzip, deflate",
                    "Connection": "keep-alive",
                    "Content-Type": "text/plain",
                    "Content-Length": f"{len(random_content)}"
                }
                http_request = (f"GET {url} HTTP/1.1\r\n"
                                f"Host: kaliber.or.id\r\n"
                                + "\r\n".join([f"{header}: {value}" for header, value in headers.items()]) +
                                f"\r\n\r\n{random_content}")
                random_packet = (IP(src="45.221.208.15", dst="kaliber.or.id") /
                                TCP(sport=random.randint(1, 65535), dport=80) /
                                Raw(load=http_request.encode()))
                pcap_packets.append(random_packet)
        elif random_proto == "FTP":
            random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=42))
            ftpprotocol = generate_ftp("45.221.208.15", "kaliber.or.id", random_string + "==")
            pcap_packets.append(ftpprotocol)
        pcap_packets.append(random_packet)
        print(f"debug 2's: {asd}/1801 - {random_proto}")

    for i, response_body in enumerate(http_response_body_array, start=1):
        # Sumber port diacak antara 80 dan 65535
        src_port = random.randint(80, 65535)

        # Buat string acak sepanjang 18 karakter
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=58))

        # Buat paket TCP untuk request POST dengan beberapa header fields dan data dalam body
        tcp_layer_req = IP(src="45.221.208.15", dst="kaliber.or.id")/TCP(sport=src_port, dport=80)
        http_request = (
            f"POST /point{i}.php&file={random_string} HTTP/1.1\r\n"
            f"Host: kaliber.or.id\r\n"
            f"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36\r\n"
            f"Accept-Language: en-US,en;q=0.5\r\n"
            f"Accept-Encoding: gzip, deflate\r\n"
            f"Connection: keep-alive\r\n"
            f"Content-Type: text/plain\r\n"  # Sesuaikan dengan tipe data yang diirimkan
            f"Content-Length: {len(response_body)}\r\n\r\n"
            f"{http_response_body_array[i-1].decode()}\r\n"
        )
        request_packet = ip_layer_req / tcp_layer_req / Raw(load=http_request.encode())

        # Buat paket TCP untuk response
        ip_layer_resp = IP(src="kaliber.or.id", dst="45.221.208.15")  # Ganti "45.221.208.15" dengan alamat IP Anda
        tcp_layer_resp = TCP(sport=80, dport=src_port)

        # Header HTTP Response
        filename = f"loveyou{1}.txt"
        responselove = b"DID YOU LOVE ME PUTT? I LOVE YOU SO MUCH"
        hostname = "kaliber.or.id"
        http_response_headers = (
            f"HTTP/1.1 200 OK\r\n"
            f"Host: {hostname}\r\n"
            f"Content-Type: text/plain\r\n"
            f"Content-Length: {len(responselove)}\r\n"
            f"Content-Disposition: attachment; filename={filename}\r\n\r\n"
        )

        response_packet = ip_layer_resp / tcp_layer_resp / Raw(load=http_response_headers.encode() + responselove)

        pcap_packets.extend([request_packet, response_packet])

    # Tambahkan paket RST setelah deteksi [TCP Retransmission]
    ip_layer_rst = IP(src="kaliber.or.id", dst="45.221.208.15")
    tcp_layer_rst = TCP(sport=80, dport=src_port, flags="R", seq=0)
    rst_packet = ip_layer_rst / tcp_layer_rst

    pcap_packets.append(rst_packet)

    for asd in range(1801):
        random_proto = random.choice(["ICMP", "UDP", "TCP", "DNS", "HTTP", "FTP"])  # Add more protocols as needed
        if random_proto == "ICMP":
            random_packet = IP(src="45.221.208.15", dst="kaliber.or.id") / ICMP()
        elif random_proto == "UDP":
            random_packet = IP(src="45.221.208.15", dst="kaliber.or.id") / UDP(sport=random.randint(1, 65535), dport=random.randint(1, 65535))
        elif random_proto == "TCP":
            random_length = random.randint(1000, 18000)
            random_packet = (IP(src="45.221.208.15", dst="kaliber.or.id") / TCP(sport=random.randint(1, 65535), dport=random.randint(1, 65535)) / Raw(RandString(size=random_length)))
        elif random_proto == "DNS":
            random_packet = IP(src="45.221.208.15", dst="kaliber.or.id") / UDP(dport=53) / DNS(qd=DNSQR(qname="kaliber.or.id"))
        elif random_proto == "HTTP":
            randomnumber = random.randint(1, 8)
            for i in range(randomnumber):
                fake = Faker()
                random_content_length = random.randint(1000, 18000)
                random_content = fake.texts(nb_texts=1, max_nb_chars=random_content_length)[0]
                print(f"get http on 3's debug: {i}/{randomnumber}")
                random_string_k = random.randint(18, 38)
                random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
                random_string2 = ''.join(random.choices(string.ascii_letters + string.digits, k=random_string_k))
                
                url = f"http://kaliber.or.id/{random_string}.php&page={random_string2}"
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                    "Accept-Language": "en-US,en;q=0.5",
                    "Accept-Encoding": "gzip, deflate",
                    "Connection": "keep-alive",
                    "Content-Type": "text/plain",
                    "Content-Length": f"{len(random_content)}"
                }
                http_request = (f"GET {url} HTTP/1.1\r\n"
                                f"Host: kaliber.or.id\r\n"
                                + "\r\n".join([f"{header}: {value}" for header, value in headers.items()]) +
                                f"\r\n\r\n{random_content}")
                random_packet = (IP(src="45.221.208.15", dst="kaliber.or.id") /
                                TCP(sport=random.randint(1, 65535), dport=80) /
                                Raw(load=http_request.encode()))
                pcap_packets.append(random_packet)
        elif random_proto == "FTP":
            random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=38))
            ftpprotocol = generate_ftp("45.221.208.15", "kaliber.or.id", random_string + "==")
            pcap_packets.append(ftpprotocol)
        pcap_packets.append(random_packet)
        print(f"debug 3's: {asd}/1801 - {random_proto}")

    # Simpan paket-paket ke dalam file pcap
    pcap_filename = "network inspection.pcap"
    wrpcap(pcap_filename, pcap_packets)

    print(f"Custom pcap file {pcap_filename} berhasil dibuat.")

if __name__ == "__main__":
    generate_custom_pcap()
