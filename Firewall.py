import psutil
import logging

def block_unauthorized_access(allowed_ips):
    """Block unauthorized network connections."""
    connections = psutil.net_connections(kind='inet')
    for conn in connections:
        if conn.raddr and conn.raddr.ip not in allowed_ips:
            logging.warning(f"Unauthorized access attempt from {conn.raddr.ip}")
            # Implement blocking mechanism (platform-specific)
            # On Linux, you could use iptables; on Windows, use netsh
            # Example:
            # os.system(f"iptables -A INPUT -s {conn.raddr.ip} -j DROP")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    allowed_ips = ["127.0.0.1", "192.168.1.1"]  # Example allowed IPs
    block_unauthorized_access(allowed_ips)
