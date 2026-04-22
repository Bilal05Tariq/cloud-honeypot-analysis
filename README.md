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
