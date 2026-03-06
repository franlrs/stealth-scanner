#!/usr/bin/env python3
import os
import random
import concurrent.futures
from scapy.all import IP, TCP, sr1, send

def scanner(target, port):
    # Generate a random source port to evade basic filtering
    src_port = random.randint(1024, 65535)
    
    # 1. Build and send the SYN packet
    packet = IP(dst=target)/TCP(sport=src_port, dport=port, flags="S")
    response = sr1(packet, timeout=1, verbose=0)
    
    if response is None:
        return None # Port filtered or host down
        
    elif response.haslayer(TCP):
        # 0x12 means SYN-ACK (Port is OPEN)
        if response.getlayer(TCP).flags == 0x12: 
            # 2. Send RST packet to close connection stealthily without logging
            rst_packet = IP(dst=target)/TCP(sport=src_port, dport=port, flags="R")
            send(rst_packet, verbose=0)
            return "Open"
            
        # 0x14 means RST-ACK (Port is CLOSED)
        elif response.getlayer(TCP).flags == 0x14: 
            return None 
            
    return None

if __name__ == "__main__":
    # Fetch target IP from Docker environment variables
    target_ip = os.getenv("TARGET_IP", "127.0.0.1") # 127.0.0.1 default value (localhost)
    ports = range(1, 1000) 
    
    print(f"[-] Starting Stealth Scan on {target_ip} ...")
    print(f"[-] Scanning {len(ports)} ports. Please wait...\n")
    
    # Use ThreadPoolExecutor for fast concurrent scanning (parallelization)
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        responses = executor.map(lambda p: (p, scanner(target_ip, p)), ports)
        
        for port, status in responses:
            if status: 
                print(f"[+] Port {port: <5} - {status}")
                
    print("\n[*] Scan finished.")