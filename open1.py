import subprocess

def open_port(port_number):
    try:
        subprocess.run(["sudo", "iptables", "-D", "INPUT", "-p", "tcp", "--dport", str(port_number), "-j", "DROP"])
        print(f"Port {port_number} has been opened.")
    except Exception as e:
        print(f"An error occurred: {e}")

port_to_open = 8080  
open_port(port_to_open)