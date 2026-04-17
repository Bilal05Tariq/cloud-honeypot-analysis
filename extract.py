import json
import pandas as pd

LOG_FILE = "/home/ubuntu/cloud-honeypot-analysis/cowrie.json"

login_attempts = []
successful_logins = []
commands = []

with open(LOG_FILE, 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue

        eventid = entry.get('eventid', '')

        if eventid == 'cowrie.login.failed':
            login_attempts.append({
                'timestamp': entry.get('timestamp'),
                'src_ip': entry.get('src_ip'),
                'username': entry.get('username'),
                'password': entry.get('password'),
                'session': entry.get('session'),
                'eventid': eventid
            })

        elif eventid == 'cowrie.login.success':
            successful_logins.append({
                'timestamp': entry.get('timestamp'),
                'src_ip': entry.get('src_ip'),
                'username': entry.get('username'),
                'password': entry.get('password'),
                'session': entry.get('session'),
                'eventid': eventid
            })

        elif eventid == 'cowrie.command.input':
            commands.append({
                'timestamp': entry.get('timestamp'),
                'src_ip': entry.get('src_ip'),
                'session': entry.get('session'),
                'input': entry.get('input'),
                'eventid': eventid
            })

df_attempts = pd.DataFrame(login_attempts)
df_success = pd.DataFrame(successful_logins)
df_commands = pd.DataFrame(commands)

df_attempts.to_csv('/home/ubuntu/cloud-honeypot-analysis/login_attempts.csv', index=False)
df_success.to_csv('/home/ubuntu/cloud-honeypot-analysis/successful_logins.csv', index=False)
df_commands.to_csv('/home/ubuntu/cloud-honeypot-analysis/commands.csv', index=False)

print(f"Login attempts: {len(df_attempts)}")
print(f"Successful logins: {len(df_success)}")
print(f"Commands executed: {len(df_commands)}")
print("CSVs saved successfully.")
