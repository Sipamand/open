import subprocess

def close_port(port_number):
    try:
        subprocess.run(["sudo", "iptables", "-A", "INPUT", "-p", "tcp", "--dport", str(port_number), "-j", "DROP"])
        print(f"Port {port_number} has been closed.")
    except Exception as e:
        print(f"An error occurred: {e}")

port_to_close = 8080  

close_port(port_to_close)
