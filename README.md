# 🔐 Agentic AI–Powered IoT Security System (LangChain Enabled)

## 📌 Overview
This project implements an **Agentic AI–powered home IoT security system** that autonomously discovers, monitors, analyzes, and protects all devices connected to a home network.

Unlike traditional rule-based firewalls, this system uses **LangChain-based AI agents** to:
- Reason about security threats
- Decide actions autonomously
- Call real security tools (firewall, honeypots)
- Explain decisions in human-readable form

The system is designed as a **plug-and-play security gateway** that can run on a Linux machine, VM, or edge device (Raspberry Pi).

---

## 🎯 Key Objectives
- Automatically discover all IoT devices on the network
- Build behavioral baselines for devices
- Detect anomalous or malicious activity
- Autonomously respond to threats
- Use deception (honeypots) to trap attackers
- Provide explainable security decisions to users

---

## 🧠 Why Agentic AI?
Traditional security systems:
- Detect threats
- Alert users
- Wait for manual action ❌

This system:
- Detects threats
- Reasons about context
- Takes autonomous action
- Learns from outcomes ✅

This **sense → think → act → learn** loop is the core of Agentic AI.

---

## 🏗️ High-Level Architecture


---

## 🤖 Agentic AI Design (LangChain)

### Role of LangChain
LangChain is used as the **autonomous reasoning engine**, NOT as a chatbot.

It:
- Receives signals from detection modules
- Chooses which security tools to invoke
- Coordinates actions
- Maintains context and memory
- Produces explainable outputs

---

### Agent Capabilities
| Capability     | Description                                     |
|----------------|-------------------------------------------------|
| Tool Calling   | Invokes firewall, honeypot, and detection tools |
| Reasoning      | Applies security logic and policies             |
| Autonomy       | Acts without human intervention                 |
| Memory         | Maintains context of past actions               |
| Explainability | Outputs human-readable decisions                |

---

### Tools Exposed to the Agent
- **DetectAnomaly** – Detects abnormal network behavior
- **BlockIP** – Blocks malicious IP addresses
- **DeployHoneypot** – Deploys deceptive fake services

The LangChain agent decides *when and how* to use these tools.

---

## 📂 Project Structure

## 🛠️ Tech Stack
- **Language:** Python 3.10+
- **Backend:** FastAPI
- **AI Orchestration:** LangChain
- **Networking:** Nmap, Scapy
- **Security:** Firewall abstraction, Honeypots
- **LLM:** OpenAI (replaceable with local LLMs)

---

## 🚀 Installation & Setup

### 1️⃣ System Requirements
- Linux OS (Ubuntu recommended)
- Python 3.10+
- Nmap installed

```bash
sudo apt install nmap# Agentic-AI-Powered-IoT-Security-System
