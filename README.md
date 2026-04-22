# Go to the bottom to view the "How To Run" section. Its a detailed guide on running the project

# Cloud-Based Honeypot System for Attacker Behaviour Analysis

**Author:** Bilal Tariq | Final Year Cybersecurity Project

---

## Overview

This project deploys a Cowrie SSH honeypot on an AWS EC2 instance to capture and analyse attacker behaviour. A custom Python-based brute force attacker script simulates realistic SSH attack traffic against the honeypot, and a Python data pipeline extracts, analyses and visualises the captured logs. The focus of the project is **behavioural analysis** — understanding how attackers interact with exposed SSH services, what credentials they use, and what commands they execute after gaining access.

---

## System Architecture

Attacker Script (EC2) → Cowrie SSH Honeypot (AWS EC2 — Port 2222) → cowrie.json (Structured log file) → extract.py → login_attempts.csv / successful_logins.csv / commands.csv → analyse.py + visualise.py + advanced_analysis.py → Charts, CSVs, Session Timeline, Brute Force Classification

---

## Technologies

| Technology | Purpose |
|---|---|
| AWS EC2 (Ubuntu 22.04) | Cloud hosting for honeypot |
| Cowrie | SSH honeypot capturing attacker interactions |
| Python 3.10 | Attack simulation and data analysis pipeline |
| pandas | Data extraction and analysis |
| matplotlib / seaborn | Data visualisation |
| sshpass | SSH password automation for attacker script |
| Git / GitHub | Version control |
| WSL2 Ubuntu | Local development environment |

---

## Project Structure

cloud-honeypot-analysis/ ├── cowrie/ → Cowrie honeypot source ├── results/ → Generated charts and CSVs ├── attacker.py → Automated brute force attack script ├── extract.py → Log parsing and CSV export ├── analyse.py → Statistical analysis ├── visualise.py → Data visualisation ├── advanced_analysis.py → Session reconstruction and brute force detection ├── cowrie.json → Raw honeypot logs ├── login_attempts.csv → Failed login dataset ├── successful_logins.csv → Successful login dataset └── commands.csv → Command execution dataset

---

## Key Features

- Automated brute force attacker simulating 20 failed attempts before a successful login
- Cowrie configured with userdb.txt to only accept a single whitelisted credential
- Full data extraction pipeline parsing Cowrie JSON logs into structured CSVs
- Statistical analysis of credential patterns, command usage and temporal behaviour
- Session reconstruction showing full attacker timelines
- Brute force IP classification based on attempt thresholds
- Five visualisation charts exported as PNG for reporting

---

## Security Notice

All attack traffic is simulated against the project's own honeypot instance on its own AWS EC2 infrastructure for academic research purposes only.

# HOW TO RUN

### Prerequisites
- Windows machine with WSL2 installed (Ubuntu 22.04)
- AWS account with an EC2 instance running Ubuntu 22.04
- SSH key pair (.pem file) downloaded and stored at ~/.ssh/cowrie-key.pem
- EC2 security group configured with inbound rules for port 22 (SSH) and port 2222 (Cowrie)

### Step 1 — Connect to EC2

From your WSL terminal: ssh -i ~/.ssh/cowrie-key.pem ubuntu@<EC2_PUBLIC_IP>

Note: If you are connecting from a different location, update your EC2 security group inbound rule for port 22 to allow your current public IP.

### Step 2 — Start Cowrie

cd ~/cloud-honeypot-analysis/cowrie
source ../cowrie-env/bin/activate
pip install -e .
PYTHONPATH=src twistd3 -n cowrie

Verify Cowrie is listening on port 2222: ss -tulnp | grep 2222

Expected output: tcp LISTEN 0 50 0.0.0.0:2222 0.0.0.0:* users:(("twistd3",pid=1322,fd=8))

### Step 3 — Run the Attacker Script

Open a second terminal and SSH into EC2 again, then run:

ssh -i ~/.ssh/cowrie-key.pem ubuntu@<EC2_PUBLIC_IP>
cd ~/cloud-honeypot-analysis
source ~/cloud-honeypot-analysis/cowrie-env/bin/activate
python3 attacker.py <EC2_PUBLIC_IP>

Expected output:
[*] Trying ubuntu:letmein
[-] Failed: ubuntu:letmein
[*] Trying ubuntu:qwerty
[-] Failed: ubuntu:qwerty
...
[*] Trying ubuntu:ubuntu
[+] ubuntu:ubuntu | ran: whoami
[+] ubuntu:ubuntu | ran: id
[+] ubuntu:ubuntu | ran: uname -a

Run the script multiple times to generate a larger dataset.

### Step 4 — Monitor Logs (Optional)

Open a third terminal, SSH into EC2 and watch logs in real time: tail -f ~/cloud-honeypot-analysis/cowrie/var/log/cowrie/cowrie.json

### Step 5 — Export Logs

Copy the log file to the project directory: cp ~/cloud-honeypot-analysis/cowrie/var/log/cowrie/cowrie.json ~/cloud-honeypot-analysis/cowrie.json

To download logs to your local machine, run this from your local WSL terminal (not SSH'd into EC2): scp -i ~/.ssh/cowrie-key.pem ubuntu@<EC2_PUBLIC_IP>:~/cloud-honeypot-analysis/cowrie/var/log/cowrie/cowrie.json ~/cloud-honeypot-analysis/

### Step 6 — Run the Data Pipeline

From inside EC2 with the virtual environment active:

Extract data from logs into CSVs: python3 extract.py

Expected output:
Login attempts: 51
Successful logins: 33
Commands executed: 33
CSVs saved successfully.

Run statistical analysis: python3 analyse.py

Generate visualisation charts: python3 visualise.py

Expected output:
Saved top_usernames.png
Saved top_passwords.png
Saved top_ips.png
Saved top_commands.png
Saved attacks_over_time.png
All visualisations saved to /results folder.

Run advanced analysis and session reconstruction: python3 advanced_analysis.py

### Step 7 — View Results

All output files are saved to: ~/cloud-honeypot-analysis/results/

To view charts on your Windows machine, open File Explorer and navigate to: \\wsl$\Ubuntu\home\<your-username>\cloud-honeypot-analysis\results

Download results from EC2 to local machine: scp -i ~/.ssh/cowrie-key.pem -r ubuntu@<EC2_PUBLIC_IP>:~/cloud-honeypot-analysis/results ~/cloud-honeypot-analysis/







