import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs('/home/ubuntu/cloud-honeypot-analysis/results', exist_ok=True)

df_attempts = pd.read_csv('login_attempts.csv')
df_success = pd.read_csv('successful_logins.csv')
df_commands = pd.read_csv('commands.csv')

sns.set(style="darkgrid")

# 5.1 Top usernames
plt.figure(figsize=(8, 5))
sns.barplot(x=df_attempts['username'].value_counts().index,
            y=df_attempts['username'].value_counts().values, palette='Blues_d')
plt.title('Top Usernames Attempted')
plt.xlabel('Username')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('/home/ubuntu/cloud-honeypot-analysis/results/top_usernames.png')
plt.close()
print("Saved top_usernames.png")

# 5.1 Top passwords
plt.figure(figsize=(10, 5))
sns.barplot(x=df_attempts['password'].value_counts().index,
            y=df_attempts['password'].value_counts().values, palette='Reds_d')
plt.title('Top Passwords Attempted')
plt.xlabel('Password')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('/home/ubuntu/cloud-honeypot-analysis/results/top_passwords.png')
plt.close()
print("Saved top_passwords.png")

# 5.2 Most active source IPs
plt.figure(figsize=(8, 5))
sns.barplot(x=df_attempts['src_ip'].value_counts().index,
            y=df_attempts['src_ip'].value_counts().values, palette='Greens_d')
plt.title('Most Active Attacker IPs')
plt.xlabel('Source IP')
plt.ylabel('Login Attempts')
plt.tight_layout()
plt.savefig('/home/ubuntu/cloud-honeypot-analysis/results/top_ips.png')
plt.close()
print("Saved top_ips.png")

# 5.3 Most executed commands
plt.figure(figsize=(12, 5))
cmd_counts = df_commands['input'].value_counts().head(15)
sns.barplot(x=cmd_counts.index, y=cmd_counts.values, palette='Purples_d')
plt.title('Most Frequently Executed Commands')
plt.xlabel('Command')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('/home/ubuntu/cloud-honeypot-analysis/results/top_commands.png')
plt.close()
print("Saved top_commands.png")

# 5.4 Attacks over time
plt.figure(figsize=(10, 5))
df_attempts['timestamp'] = pd.to_datetime(df_attempts['timestamp'])
df_attempts.set_index('timestamp', inplace=True)
df_attempts.resample('1min').size().plot(kind='line', color='red')
plt.title('Attack Attempts Over Time')
plt.xlabel('Time')
plt.ylabel('Number of Attempts')
plt.tight_layout()
plt.savefig('/home/ubuntu/cloud-honeypot-analysis/results/attacks_over_time.png')
plt.close()
print("Saved attacks_over_time.png")

print("\nAll visualisations saved to /results folder.")
