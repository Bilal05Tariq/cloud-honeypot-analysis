import pandas as pd

df_attempts = pd.read_csv('login_attempts.csv')
df_success = pd.read_csv('successful_logins.csv')
df_commands = pd.read_csv('commands.csv')

# 4.1 Attacker behaviour analysis
print("=== ATTACKER BEHAVIOUR ===")
print(f"Total login attempts: {len(df_attempts)}")
print(f"Total successful logins: {len(df_success)}")
print(f"Success vs Failure ratio: {len(df_success)} successes / {len(df_attempts)} failures")
print("\nLogin attempts per IP:")
print(df_attempts['src_ip'].value_counts())

# 4.2 Credential analysis
print("\n=== CREDENTIAL ANALYSIS ===")
print("\nTop usernames attempted:")
print(df_attempts['username'].value_counts().head(10))
print("\nTop passwords attempted:")
print(df_attempts['password'].value_counts().head(10))

# 4.3 Command analysis
print("\n=== COMMAND ANALYSIS ===")
print("\nMost frequently executed commands:")
print(df_commands['input'].value_counts().head(10))
print("\nCommands grouped by session:")
for session, group in df_commands.groupby('session'):
    print(f"\nSession {session}:")
    print(group['input'].tolist())

# 4.4 Temporal analysis
print("\n=== TEMPORAL ANALYSIS ===")
df_attempts['timestamp'] = pd.to_datetime(df_attempts['timestamp'])
df_attempts['hour'] = df_attempts['timestamp'].dt.hour
print("\nAttacks per hour:")
print(df_attempts.groupby('hour').size())
