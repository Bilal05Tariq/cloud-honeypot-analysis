# Cloud-Based Honeypot with Automated Attack Log Analysis

## Project Overview

This project implements a **cloud-based honeypot environment** designed to capture, collect, and analyse malicious activity targeting exposed network services. The system deploys a **Cowrie SSH/Telnet honeypot** on an AWS EC2 instance and integrates it with a log processing pipeline using the **Elastic Stack (ELK)**.

The primary objective is to simulate vulnerable services in a controlled environment to observe attacker behaviour, capture attack data, and process the collected logs for analysis.

The system demonstrates how cloud infrastructure can be used to deploy honeypots and build an automated pipeline for security monitoring and threat analysis.

---

# Project Motivation

Cyber attacks targeting exposed services such as SSH are extremely common on the public internet. Attackers frequently attempt:

* Brute force login attempts
* Automated credential attacks
* Malware deployment
* Command execution

Traditional defensive systems often block attacks but provide limited insight into attacker behaviour.

A **honeypot** allows researchers to safely observe malicious activity by simulating vulnerable systems. By capturing attacker interactions, security analysts can gain insight into:

* Attack methods
* Credential dictionaries
* Automated attack tools
* Common command sequences

This project aims to build a **controlled environment for capturing and analysing these interactions**.

---

# Project Objectives

The key objectives of the project are:

1. Deploy a **cloud-hosted honeypot** capable of simulating vulnerable services.
2. Capture attacker login attempts and command activity.
3. Automatically collect honeypot logs.
4. Process and normalise captured log data.
5. Store structured attack data for analysis.
6. Provide a platform for further visualisation and threat analysis.

---

# System Architecture

Attacker
↓
Cowrie Honeypot (AWS EC2)
↓
Filebeat (Log Collection)
↓
Logstash (Log Processing)
↓
Elasticsearch (Log Storage)
↓
Kibana (Visualisation)

---

# Technologies Used

| Technology             | Purpose                                                  |
| ---------------------- | -------------------------------------------------------- |
| AWS EC2 (Ubuntu 22.04) | Cloud environment hosting the honeypot                   |
| Cowrie Honeypot        | Simulated SSH/Telnet service capturing attacker activity |
| Python 3.10            | Runtime environment for Cowrie                           |
| Filebeat               | Log shipping tool                                        |
| Logstash               | Log processing and parsing                               |
| Elasticsearch          | Storage and indexing of log data                         |
| Git / GitHub           | Version control and backup                               |
| WSL2 Ubuntu            | Local development environment                            |

---

# Project Structure

cloud-honeypot-analysis/

cowrie/                 → Cowrie honeypot source code
etc/                    → Configuration files
docs/                   → Project documentation
analysis/               → Log analysis scripts (future work)
README.md
.gitignore

---

# Development Progress

## Task 1 — Local Environment Setup

### Completed

* Installed **WSL2**
* Installed **Ubuntu Linux**
* Installed required tools:

  * Git
  * Python
  * OpenSSH
  * Nmap
  * Bash utilities
* Created project directories

### Lessons Learned

* Importance of using a consistent Linux environment
* Managing dependencies using Python virtual environments

---

# Task 2 — AWS Cloud Infrastructure

### Completed

* Created AWS account
* Launched **Ubuntu EC2 instance**
* Generated SSH key pair
* Configured **security groups**
* Connected to EC2 from WSL using SSH

Example connection command:

ssh -i ~/.ssh/cowrie-key.pem ubuntu@<EC2-IP>

### Challenges

* Correctly configuring AWS security groups
* Managing SSH keys and access permissions

### Lessons Learned

* Cloud instances require strict firewall configuration
* Proper SSH key management is essential for secure access

---

# Task 3 — Deploy Cowrie Honeypot

### Completed

* Installed required dependencies
* Created Python virtual environment
* Cloned Cowrie repository
* Configured honeypot settings
* Enabled SSH and Telnet honeypot services
* Verified attacker connections
* Confirmed logs were generated

Example Cowrie startup command:

PYTHONPATH=src twistd -n cowrie

### Challenges

During deployment several issues were encountered:

* Python version compatibility
* Missing honeypot filesystem files
* Configuration errors
* Runtime dependency issues

### Solutions

These issues were resolved by:

* Downgrading Python version to **3.10**
* Correcting configuration paths
* Ensuring required directories existed
* Verifying Cowrie dependencies

### Lessons Learned

* Honeypot software is sensitive to environment configuration
* Debugging logs is essential for diagnosing deployment issues

---

# Task 4 — Log Collection Pipeline

## Task 4.1 — Filebeat

### Completed

* Installed Filebeat on EC2
* Configured Filebeat to monitor Cowrie logs
* Verified log collection

### Lessons Learned

* Filebeat acts as a lightweight log shipper
* Proper file path configuration is required

---

## Task 4.2 — Logstash

### Completed

* Installed Logstash
* Created Logstash pipeline
* Configured input from Filebeat
* Parsed incoming Cowrie JSON logs

Pipeline structure:

Filebeat → Logstash → Elasticsearch

### Challenges

* Performance issues on small EC2 instances
* Resource limitations on free-tier hardware

### Solution

The EC2 instance type was upgraded to improve performance.

---

# Task 4.3 — Elasticsearch (Current Stage)

The next stage of the project is the deployment of **Elasticsearch** to store and index captured honeypot logs.

This will allow:

* Structured storage of attack data
* Fast searching of attacker activity
* Integration with Kibana dashboards

---

# Example Honeypot Log Entry

Example Cowrie JSON log:

{
"eventid": "cowrie.session.connect",
"src_ip": "161.74.224.2",
"protocol": "ssh",
"message": "New connection"
}

These logs will be indexed in Elasticsearch for further analysis.

---

# Backup Strategy

To prevent data loss, multiple backup methods were implemented:

1. EC2 EBS Snapshot
2. Local compressed backup archive
3. GitHub repository backup
4. Cloud instance backup

This ensures the project can be restored if the instance fails.

---

# Security Considerations

The honeypot operates in a **controlled cloud environment**. Security measures include:

* Restricted inbound ports
* Isolated instance configuration
* No exposure of sensitive infrastructure
* Controlled log storage

The system captures simulated attack activity for research purposes.

---

# Future Work

The remaining development stages include:

* Completing Elasticsearch deployment
* Installing Kibana for data visualisation
* Building attack dashboards
* Analysing attacker behaviour patterns
* Generating statistics from captured logs

---

# Educational Context

This project is developed as part of a **Final Year Cybersecurity Project** focusing on:

* Honeypot deployment
* Cloud security
* Attack monitoring
* Automated log analysis

---

# Author

Bilal Tariq
Final Year Cybersecurity Project
