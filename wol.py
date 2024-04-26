import socket

def send_magic_packet(mac):
    # Remove any separator in MAC and convert to bytes
    bytes_mac = bytes.fromhex(mac.replace(':', '').replace('-', '').replace('.', ''))
    
    # Create the magic packet from MAC address
    magic_packet = b'\xFF' * 6 + bytes_mac * 16

    # Create socket for broadcasting the packet
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(magic_packet, ('<broadcast>', 9))
    
    print(f"Magic packet sent to {mac}")

# MAC ADDRESS HERE
# EXAMPLE: 00:11:22:AA:BB:CC
mac_address = "" 
send_magic_packet(mac_address)