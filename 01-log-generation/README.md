# Phase 1 — Security Log Generation

## Overview

This phase establishes the data-generation component of the Splunk Security Monitoring Lab.

A Security Information and Event Management (SIEM) platform such as Splunk requires log data to analyze system, application, authentication, and network activity. Since this project uses a controlled lab environment rather than a production infrastructure, Python is used to generate synthetic security logs.

The generated logs simulate activity from three common security data sources:

* Apache web server
* Authentication system
* Network firewall

These logs will be ingested into Splunk in Phase 2 and used for field extraction, security searches, detection rules, dashboards, alerting, and incident investigation.

---

## Objectives

The objectives of this phase are:

1. Create a controlled security-log dataset.
2. Generate multiple types of security events using Python.
3. Understand the structure of common security logs.
4. Store the generated logs in a predictable project directory.
5. Validate the generated event counts.
6. Prepare the dataset for ingestion into Splunk.

---

## Project Structure

```text
01-log-generation/
│
├── README.md
├── generate_security_logs.py
│
└── sample_logs/
    ├── apache_access.log
    ├── auth.log
    └── firewall.log
```

### File Description

| File                        | Description                                                            |
| --------------------------- | ---------------------------------------------------------------------- |
| `generate_security_logs.py` | Python script responsible for generating all synthetic security events |
| `apache_access.log`         | Simulated Apache web-server access logs                                |
| `auth.log`                  | Simulated authentication success and failure events                    |
| `firewall.log`              | Simulated firewall network traffic events                              |
| `README.md`                 | Documentation for the log-generation phase                             |

---

## Log Sources

### 1. Apache Access Logs

The Apache log simulates requests received by a web server.

Example:

```text
203.0.113.45 - - [27/Aug/2026:14:20:10] "GET /login HTTP/1.1" 200 1842
```

Important fields represented by this format include:

* Source IP address
* HTTP method
* Requested path
* HTTP protocol
* HTTP status code
* Response size
* Timestamp

These events can later be used to investigate web-server activity, suspicious requests, HTTP errors, and potential web attacks.

Total generated events:

```text
100
```

---

### 2. Authentication Logs

The authentication log simulates user login activity.

Example:

```text
2026-08-27 14:20:10 FAILED_LOGIN user=admin src_ip=185.220.101.45
```

Important fields include:

* Timestamp
* Authentication event type
* Username
* Source IP address

The log contains both successful and failed login attempts.

These events will later be used to demonstrate security detections such as repeated failed authentication and possible brute-force activity.

Total generated events:

```text
30
```

---

### 3. Firewall Logs

The firewall log simulates network traffic passing through a firewall.

Example:

```text
2026-08-27 14:20:10 FIREWALL action=DENY src_ip=185.220.101.45 dst_ip=192.168.1.20 src_port=54321 dst_port=22 protocol=TCP
```

Important fields include:

* Timestamp
* Firewall action
* Source IP
* Destination IP
* Source port
* Destination port
* Network protocol

The generated events include both allowed and denied traffic.

These events will later be used to investigate blocked connections, suspicious network activity, and potentially targeted services.

Total generated events:

```text
40
```

---

## Dataset Summary

| Source              |  Events |
| ------------------- | ------: |
| Apache access logs  |     100 |
| Authentication logs |      30 |
| Firewall logs       |      40 |
| **Total**           | **170** |

The dataset is intentionally synthetic and is designed for security-analysis practice.

---

## Directory Location

The generated logs are stored inside the project directory:

```text
C:\splunk_security_lab\01-log-generation\sample_logs
```

This keeps the generated dataset separate from the Python source code and makes it easy to provide the directory as a Splunk data input in the next phase.

---

## Requirements

The following software is required:

* Windows
* Python 3.x

Python can be verified from Command Prompt using:

```cmd
python --version
```

---

## Running the Log Generator

Open Command Prompt and navigate to the Phase 1 directory:

```cmd
cd C:\splunk_security_lab\01-log-generation
```

Run the Python script:

```cmd
python generate_security_logs.py
```

The script creates the `sample_logs` directory if it does not already exist and generates the three log files.

Expected output includes:

```text
Generated 100 Apache access log entries
Generated 30 auth log entries
Generated 40 firewall log entries
All logs generated successfully
```

---

## Validation

After running the generator, verify that the following files exist:

```text
sample_logs/
├── apache_access.log
├── auth.log
└── firewall.log
```

The number of events can be validated using Windows Command Prompt.

### Apache

```cmd
find /c /v "" sample_logs\apache_access.log
```

Expected count:

```text
100
```

### Authentication

```cmd
find /c /v "" sample_logs\auth.log
```

Expected count:

```text
30
```

### Firewall

```cmd
find /c /v "" sample_logs\firewall.log
```

Expected count:

```text
40
```

The expected total is:

```text
100 + 30 + 40 = 170 events
```

---

## Data Flow

The data flow established during this phase is:

```text
Python Log Generator
        |
        +--------------------+
        |                    |
        v                    v
Apache Logs           Authentication Logs
        |                    |
        +----------+---------+
                   |
                   v
             Firewall Logs
                   |
                   v
          Synthetic Dataset
                   |
                   v
             Splunk (Phase 2)
```

The next phase will connect these generated log files to Splunk.

---

## Security Relevance

Although the dataset is synthetic, the structure represents common categories of security telemetry found in real environments.

The logs provide data that can be used to practice:

* Authentication monitoring
* Failed-login analysis
* Source IP investigation
* Web-server monitoring
* HTTP status analysis
* Firewall event analysis
* Network connection investigation
* Security event correlation
* Detection engineering
* Incident investigation

The generated data is not intended to represent actual production traffic.
