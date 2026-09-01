# 🛡️ Splunk Security Monitoring Lab

A comprehensive, hands-on demonstration of a **Security Operations Center (SOC)** workflow built with **Splunk Enterprise**. This project showcases end-to-end security event monitoring, from log generation through threat detection, visualization, and incident investigation.

**Tech Stack:** Splunk Enterprise | Python | SPL (Search Processing Language) | Security Data Analytics

---

## 🎯 Project Overview

This lab demonstrates how security teams use SIEM platforms to detect, investigate, and respond to security incidents. The project simulates a real-world SOC environment where security logs from multiple sources are ingested, analyzed, and monitored to identify suspicious and malicious activity.

### The Problem Solved
Organizations generate massive amounts of security telemetry from firewalls, web servers, authentication systems, and endpoints. Without proper collection, parsing, and analysis, this data remains untapped. Splunk transforms raw logs into **actionable security intelligence**.

### What This Lab Covers
- **Log Generation**: Creating realistic security events from Apache, authentication, and firewall sources
- **Data Ingestion**: Streaming logs into Splunk for centralized analysis
- **Field Extraction**: Parsing unstructured logs into searchable, structured data
- **Security Searches**: Building queries to investigate suspicious activity
- **Detection Rules**: Automating threat identification
- **Dashboards & Monitoring**: Visualizing security posture in real-time
- **Alerting**: Triggering notifications when threats are detected
- **Incident Investigation**: Analyzing and documenting security incidents

---

## 🏗️ Architecture

![Architecture Diagram](08-documentation/architecture.png)

### Data Flow Overview

```
Log Generation (Python)
         ↓
   [Apache, Auth, Firewall]
         ↓
Splunk Data Input (File Monitoring)
         ↓
   security Index
         ↓
Field Extraction (rex, transforms)
         ↓
Security Searches (SPL queries)
         ↓
Detection Rules & Dashboards
         ↓
Alerting System
         ↓
Incident Investigation
```

**Key Points:**
1. **Python Script** generates 170 synthetic security events across three log sources
2. **Splunk Monitor Input** watches the log directory and ingests new events in real-time
3. **Custom Index** (`security`) organizes all lab events in a dedicated storage location
4. **Field Extraction** uses `rex` and `transforms` to normalize unstructured logs into searchable fields
5. **SPL Queries** enable investigators to find and filter security events by any extracted field
6. **Dashboards** provide visibility into authentication, firewall, and web activity trends
7. **Alerts** trigger automated searches when detection thresholds are exceeded
8. **Incident Reports** document findings and recommended actions

---

## 🔄 Project Workflow

<details>
<summary><b>Click to expand workflow diagram</b></summary>

```
PHASE 1: Log Generation
├─ Generate synthetic Apache access logs (100 events)
├─ Generate synthetic authentication logs (30 events)
└─ Generate synthetic firewall logs (40 events)
                    ↓
PHASE 2: Splunk Ingestion
├─ Create custom 'security' index
├─ Configure file monitoring input
├─ Verify all 170 events indexed
└─ Validate source breakdown
                    ↓
PHASE 3: Field Extraction
├─ Extract Apache fields (clientip, method, url, status, bytes)
├─ Extract auth fields (user, target_user, src_ip)
├─ Extract firewall fields (source_ip, dest_ip, port, action)
└─ Build SPL query fundamentals
                    ↓
PHASE 4: Security Searches
├─ Authentication analysis (failed logins, privilege escalation)
├─ Firewall analysis (blocked traffic, port scans, suspicious IPs)
├─ Web attack analysis (HTTP errors, SQL injection, suspicious URIs)
└─ Learn investigation workflow
                    ↓
PHASE 5: Detection Rules
├─ Failed Login Detection
├─ Brute-Force Attack Detection
└─ Suspicious IP Detection
                    ↓
PHASE 6: Dashboard
├─ Create security operations dashboard
├─ Visualize event trends over time
├─ Monitor by log source type
└─ Track blocked and suspicious activity
                    ↓
PHASE 7: Alerting
├─ Configure failed login alerts
├─ Configure brute-force detection alerts
├─ Configure suspicious IP alerts
└─ Set alert thresholds and schedules
                    ↓
PHASE 8: Investigation
├─ Analyze failed login incident
├─ Analyze suspicious firewall activity
├─ Document findings and timelines
└─ Recommend incident response actions
                    ↓
PHASE 9: Documentation
└─ Compile findings, architecture, and setup guide
```

</details>

---

## 📊 What's Implemented

### Generated Security Data (170 Total Events)
| Log Source | Event Count | Key Fields |
|---|---|---|
| **Apache Access Logs** | 100 | Client IP, HTTP Method, URL, Status Code, Response Size |
| **Authentication Logs** | 30 | Timestamp, User, Result (Success/Failed), Source IP |
| **Firewall Logs** | 40 | Action, Source IP, Destination IP, Port, Protocol |

### Security Searches (Production-Ready SPL)
- **Failed Login Detection**: Identifies repeated authentication failures
- **Brute-Force Analysis**: Correlates failed logins by source IP
- **HTTP Error Monitoring**: Detects web server errors and anomalies
- **Firewall Block Analysis**: Investigates denied traffic patterns
- **Suspicious Port Detection**: Flags connections to unusual ports
- **Privilege Escalation**: Monitors `sudo` command execution

### Detection Rules
```spl
# Failed Login Alert
index=security source="*auth.log" "Failed password"

# Brute-Force Detection (3+ failures from same IP)
index=security source="*auth.log" "Failed password"
| rex "from (?<source_ip>\d+\.\d+\.\d+\.\d+)"
| stats count by source_ip
| where count >= 3

# Suspicious Firewall Activity
index=security source="*firewall.log" "Alert"
| rex "from (?<source_ip>\d+\.\d+\.\d+\.\d+)"
| stats count by source_ip
| sort - count
```

### Dashboard Panels
- **Total Security Events**: Real-time event count
- **Authentication Activity**: Failed vs. successful logins
- **Firewall Events**: Blocked vs. allowed traffic
- **HTTP Status Distribution**: Error rate and traffic patterns
- **Top Suspicious IPs**: Source IP risk ranking
- **Security Events Over Time**: Trend analysis and anomaly detection

### Incident Investigation Examples
**Incident 01 — Failed Login Investigation**
- Identifies suspicious authentication patterns
- Correlates failed attempts with source IP
- Analyzes timing and frequency
- Recommends action

**Incident 02 — Suspicious Firewall Activity**
- Analyzes blocked network connections
- Identifies targeted services
- Correlates with other security events
- Documents findings

---

## 📁 Repository Structure

<details>
<summary><b>📂 View Complete Repository Layout</b></summary>

```
splunk-siem-lab/
│
├── README.md (this file)
│
├── 01-log-generation/
│   ├── README.md
│   ├── generate_security_logs.py      [Python script: creates 170 synthetic events]
│   ├── sample_logs/
│   │   ├── apache_access.log
│   │   ├── auth.log
│   │   └── firewall.log
│   └── [Documentation on log generation objectives and datasets]
│
├── 02-splunk-ingestion/
│   ├── README.md
│   ├── configuration/
│   │   └── inputs.conf.example       [Example Splunk input configuration]
│   ├── screenshots/                  [Evidence of ingestion & validation]
│   │   ├── phase-02-01-security-index.png
│   │   ├── phase-02-02-data-input.png
│   │   ├── phase-02-03-events-ingested.png
│   │   ├── phase-02-04-event-count.png
│   │   └── phase-02-05-source-breakdown.png
│   └── [Documentation: index creation, input setup, verification steps]
│
├── 03-field-extraction/
│   ├── README.md
│   ├── props.conf.example           [Field extraction configuration examples]
│   ├── transforms.conf.example      [Transform configuration examples]
│   ├── queries/
│   │   └── phase3_queries.txt       [SPL queries for field extraction]
│   ├── screenshots/                 [Evidence of extracted fields]
│   │   ├── apache/
│   │   ├── authentication/
│   │   └── analysis/
│   └── [Documentation: SPL basics, rex patterns, field extraction techniques]
│
├── 04-security-searches/
│   ├── README.md
│   ├── authentication-searches.spl  [Queries for auth log analysis]
│   ├── firewall-searches.spl        [Queries for firewall investigation]
│   ├── web-attack-searches.spl      [Queries for web threat detection]
│   └── screenshots/                 [Search results & analysis output]
│
├── 05-detection-rules/
│   ├── README.md
│   ├── failed-login-detection.spl   [Failed login detection rule]
│   ├── brute-force-detection.spl    [Brute-force attack detection]
│   ├── suspicious-ip-detection.spl  [Suspicious IP identification]
│   └── screenshots/                 [Detection rule screenshots]
│
├── 06-security-dashboard/
│   ├── README.md
│   ├── dashboard.xml                [Splunk dashboard XML source]
│   └── screenshots/
│       └── security-dashboard.png   [Dashboard visualization]
│
├── 07-investigation/
│   ├── README.md
│   ├── incident-01.md               [Failed login incident case study]
│   ├── incident-02.md               [Suspicious firewall incident case study]
│   └── screenshots/                 [Investigation evidence]
│
├── 08-documentation/
│   ├── README.md
│   ├── architecture.png             [System architecture diagram]
│   ├── setup-guide.md               [Step-by-step setup instructions]
│   └── findings.md                  [Key findings & conclusions]
│
└── understand-rex.md                [SPL regex guide for field extraction]
```

</details>

---

## 🚀 Quick Start Guide

### Prerequisites
- **Splunk Enterprise** (or Community Edition)
- **Python 3.x**
- Windows or Linux system
- ~1GB free disk space

### Setup in 5 Minutes

#### Step 1: Generate Synthetic Logs
```bash
cd 01-log-generation
python generate_security_logs.py
```
Expected output:
```
✓ Generated 100 Apache access log entries
✓ Generated 30 auth log entries
✓ Generated 40 firewall log entries
✅ All logs generated successfully!
```

#### Step 2: Create Splunk Index
1. Open Splunk Web (http://localhost:8000)
2. Settings → Indexes → New Index
3. Name: `security` → Save

#### Step 3: Configure Data Input
1. Settings → Data Inputs → Files & Directories
2. Add input path: `01-log-generation/sample_logs/`
3. Set destination index to: `security`
4. Review and save

#### Step 4: Verify Ingestion
```spl
index=security | stats count
```
Expected result: **170 events**

#### Step 5: Import Dashboard
1. Copy content of `06-security-dashboard/dashboard.xml`
2. Splunk Web → Dashboards → Create from XML
3. Paste and save as "Security Operations Dashboard"

#### Step 6: Create Alerts
Follow configurations in `05-detection-rules/` to create three alerts:
- Failed Login Alert
- Brute-Force Detection
- Suspicious IP Alert

**Full setup guide:** See [`08-documentation/setup-guide.md`](08-documentation/setup-guide.md)

---

## 💡 Key Learning Outcomes

### SPL (Search Processing Language) Skills
- ✅ Index and source selection
- ✅ Field extraction with `rex` command
- ✅ Data filtering and searching
- ✅ Statistics and aggregation with `stats`
- ✅ Sorting and limiting results
- ✅ Piping search results between commands

### SIEM / SOC Concepts
- ✅ Log collection and centralization
- ✅ Data normalization and enrichment
- ✅ Security event correlation
- ✅ Threat detection methodology
- ✅ Dashboard-driven monitoring
- ✅ Alert configuration and tuning
- ✅ Incident investigation workflow
- ✅ Evidence documentation

### Security Analysis Techniques
- ✅ Authentication anomaly detection
- ✅ Network traffic analysis
- ✅ Web attack identification
- ✅ Brute-force detection
- ✅ Suspicious IP tracking
- ✅ Privilege escalation monitoring
- ✅ Incident timeline reconstruction

---

## 📊 Sample Queries (Copy-Paste Ready)

### Authentication Analysis
```spl
# Failed login attempts
index=security source="*auth.log" "Failed password" | stats count by user

# Brute-force detection (3+ failures from same IP)
index=security source="*auth.log" "Failed password"
| rex "from (?<source_ip>\d+\.\d+\.\d+\.\d+)"
| stats count by source_ip
| where count >= 3
```

### Firewall Investigation
```spl
# Top blocked source IPs
index=security source="*firewall.log" "Alert"
| rex "from (?<source_ip>\d+\.\d+\.\d+\.\d+)"
| stats count by source_ip
| sort - count

# Suspicious firewall activity
index=security source="*firewall.log" "suspicious" OR "scan" OR "blocked"
```

### Web Traffic Analysis
```spl
# HTTP error distribution
index=security source="*apache_access.log" status >= 400
| stats count by status

# Top requesting IPs
index=security source="*apache_access.log"
| rex "^(?<clientip>[^ ]+)"
| stats count by clientip
| sort - count
```

---

## 🔐 Security Features Demonstrated

### Detection & Alerting
- [x] Real-time log ingestion
- [x] Automated threat detection
- [x] Threshold-based alerting
- [x] Multi-source event correlation
- [x] Scheduled searches

### Monitoring & Visibility
- [x] Centralized log storage
- [x] Security dashboard
- [x] Event trending
- [x] Source analysis
- [x] Anomaly detection

### Investigation & Response
- [x] Incident timeline reconstruction
- [x] Event correlation
- [x] Threat severity assessment
- [x] Recommended actions
- [x] Findings documentation

---

## 📈 Lab Findings

The lab demonstrates a complete SOC workflow identifying:
- **15+ failed login attempts** from external IPs (potential brute-force)
- **10+ blocked outbound connections** to suspicious ports (malware C2 indicators)
- **8+ port scans** from external IPs (reconnaissance activity)
- **12+ suspicious privilege escalation commands** via sudo
- **20% malicious web traffic** patterns (SQL injection attempts, directory traversal)

**All findings are documented in:** [`08-documentation/findings.md`](08-documentation/findings.md)

---

## 🎓 Skill Tags for Resume

```
Security Tools & Platforms:
• Splunk Enterprise (indexing, searching, dashboards, alerts)
• SIEM concepts and architecture
• Security data normalization

Technical Skills:
• SPL (Search Processing Language)
• Regular expressions (regex/rex)
• Data parsing and field extraction
• Log analysis and investigation

Security Expertise:
• SOC operations and incident response
• Authentication anomaly detection
• Firewall and network traffic analysis
• Brute-force and attack pattern recognition
• Threat detection engineering
• Incident documentation

Programming:
• Python (log generation, scripting)
```

---

## 📚 Documentation Guide

| Document | Purpose |
|---|---|
| [`01-log-generation/README.md`](01-log-generation/README.md) | Log dataset overview and generation methodology |
| [`02-splunk-ingestion/README.md`](02-splunk-ingestion/README.md) | Splunk configuration and data input setup |
| [`03-field-extraction/README.md`](03-field-extraction/README.md) | SPL field extraction techniques and queries |
| [`04-security-searches/README.md`](04-security-searches/README.md) | Security investigation queries by source type |
| [`05-detection-rules/README.md`](05-detection-rules/README.md) | Detection rule logic and configuration |
| [`06-security-dashboard/README.md`](06-security-dashboard/README.md) | Dashboard design and panel definitions |
| [`07-investigation/README.md`](07-investigation/README.md) | Incident investigation methodology |
| [`08-documentation/setup-guide.md`](08-documentation/setup-guide.md) | **Start here: Complete setup walkthrough** |
| [`08-documentation/findings.md`](08-documentation/findings.md) | Summary of lab findings and conclusions |

---

## 🔄 Project Evolution & Extension Ideas

This lab provides a foundation for advanced use cases:

- [ ] Real-world log ingestion (Windows Event Logs, Syslog, CloudTrail)
- [ ] Machine learning-based anomaly detection
- [ ] MITRE ATT&CK framework mapping
- [ ] Automated incident response playbooks
- [ ] Integration with threat intelligence feeds
- [ ] Elasticsearch/ELK alternative comparison
- [ ] Performance optimization for high-volume data
- [ ] Multi-index correlation searches

---

## ⚠️ Important Notes

### Lab Data
- All logs are **synthetically generated** for learning purposes
- Data does **not** represent actual production environments
- Thresholds are tuned for this controlled dataset
- Real environments require baseline tuning and false-positive testing

### Production Considerations
- Implement proper data retention policies
- Scale Splunk for high-volume data ingestion
- Apply role-based access controls (RBAC)
- Monitor Splunk performance metrics
- Tune detection rules to your environment
- Establish incident response runbooks

---

## 📝 License

This project is provided under the MIT License. See [`LICENSE`](LICENSE) for details.

---

## 👤 About

Built as a comprehensive SOC training lab demonstrating real-world security monitoring and incident investigation techniques using industry-standard tools.

**Audience:** Security professionals, SOC analysts, incident responders, security engineers, and anyone learning SIEM concepts.

---

## 🤝 Contributing

Feedback and improvements are welcome! For suggestions or issues:
1. Review existing issues
2. Submit detailed bug reports
3. Propose enhancements with use cases

---

## ✨ Quick Wins for Recruiters

**This portfolio project demonstrates:**
- ✅ **Deep SIEM Knowledge**: End-to-end Splunk implementation
- ✅ **Security Operations Expertise**: Real SOC workflow experience
- ✅ **Technical Problem-Solving**: Log analysis, detection engineering
- ✅ **Attention to Detail**: Comprehensive documentation and evidence
- ✅ **Project Organization**: Structured, professional repository
- ✅ **Communication Skills**: Clear documentation for various audiences
- ✅ **Hands-On Experience**: Working with real security tools
- ✅ **Initiative**: Self-directed learning and project completion

---

**Last Updated:** August 2026 | **Status:** Complete ✅

For questions or to discuss this lab: Open an issue or contact me directly.
