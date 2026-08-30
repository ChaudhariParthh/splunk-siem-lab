# Phase 7 — Alerting

## Overview

This phase focuses on converting security searches into **automated Splunk alerts**.

The alerts monitor authentication and firewall activity and trigger when the defined search conditions are met.

## Alerts Created

### 1. Failed Login Alert

Detects failed authentication attempts.

```spl
index=security source="*auth.log" "Failed password"
```

**Purpose:** Identify failed login activity that may require investigation.

**Configuration:**

```text
Alert Type: Scheduled
Schedule: Every 5 minutes
Trigger: Number of results > 0
```

---

### 2. Brute-Force Alert

Detects repeated failed login attempts from the same source IP.

```spl
index=security source="*auth.log" "Failed password"
| rex "from (?<source_ip>\d+\.\d+\.\d+\.\d+)"
| stats count by source_ip
| where count >= 3
```

**Purpose:** Identify source IPs generating multiple failed authentication attempts.

**Detection logic:**

```text
Failed login events
        ↓
Extract source IP
        ↓
Count attempts per IP
        ↓
Check threshold
        ↓
Generate alert
```

The threshold of three attempts is used for this lab. In a production environment, thresholds should be tuned according to normal authentication behavior to reduce false positives.

---

### 3. Suspicious IP Alert

Detects source IPs associated with suspicious firewall activity.

```spl
index=security source="*firewall.log" "suspicious"
| rex "from (?<source_ip>\d+\.\d+\.\d+\.\d+)"
| stats count by source_ip
| sort - count
```

**Purpose:** Identify IP addresses associated with suspicious firewall events for further investigation.

---

## Splunk Alert Workflow

```text
Security Logs
      ↓
SPL Search
      ↓
Detection Condition
      ↓
Scheduled Search
      ↓
Alert Triggered
      ↓
Security Investigation
```

