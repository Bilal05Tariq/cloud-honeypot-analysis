import pandas as pd
import os

os.makedirs('/home/ubuntu/cloud-honeypot-analysis/results', exist_ok=True)

df_attempts = pd.read_csv('login_attempts.csv')
df_success = pd.read_csv('successful_logins.csv')
df_commands = pd.read_csv('commands.csv')

# 6.1 Session reconstruction
print("=== SESSION RECONSTRUCTION ===")
all_events = pd.concat([
    df_attempts[['timestamp', 'session', 'src_ip', 'username', 'password']].assign(event='login_failed'),
    df_success[['timestamp', 'session', 'src_ip', 'username', 'password']].assign(event='login_success'),
    df_commands[['timestamp', 'session', 'src_ip', 'input']].assign(event='command')
], ignore_index=True)

all_events['timestamp'] = pd.to_datetime(all_events['timestamp'])
all_events.sort_values('timestamp', inplace=True)

print("\nFull attacker session timeline (first 20 events):")
print(all_events[['timestamp', 'session', 'src_ip', 'event', 'input']].head(20).to_string())

# 6.2 Brute force detection
print("\n=== BRUTE FORCE DETECTION ===")
THRESHOLD = 3
attempts_per_ip = df_attempts.groupby('src_ip').size().reset_index(name='attempt_count')
attempts_per_ip['classification'] = attempts_per_ip['attempt_count'].apply(
    lambda x: 'Brute Force' if x >= THRESHOLD else 'Targeted'
)
print("\nIP Classification:")
print(attempts_per_ip.to_string())

# 6.3 Export final clean dataset
all_events.to_csv('/home/ubuntu/cloud-honeypot-analysis/results/full_session_timeline.csv', index=False)
attempts_per_ip.to_csv('/home/ubuntu/cloud-honeypot-analysis/results/ip_classification.csv', index=False)
df_attempts.to_csv('/home/ubuntu/cloud-honeypot-analysis/results/login_attempts.csv', index=False)
df_success.to_csv('/home/ubuntu/cloud-honeypot-analysis/results/successful_logins.csv', index=False)
df_commands.to_csv('/home/ubuntu/cloud-honeypot-analysis/results/commands.csv', index=False)

print("\n=== EXPORT COMPLETE ===")
print("All files saved to /results folder:")
print("- full_session_timeline.csv")
print("- ip_classification.csv")
print("- login_attempts.csv")
print("- successful_logins.csv")
print("- commands.csv")
