# Security Investigation

## Overview

This phase demonstrates a basic SOC investigation workflow using Splunk alerts and security logs.

The investigation focuses on identifying suspicious authentication and firewall activity, analyzing relevant indicators, and documenting the findings.

## Investigations

### Incident 01 — Failed Login Investigation

Investigates failed authentication activity and examines:

* Source IP
* Target username
* Timestamp
* Number of attempts
* Related authentication activity

See [`incident-01.md`](incident-01.md).

### Incident 02 — Suspicious Firewall Activity

Investigates suspicious network activity and examines:

* Source IP
* Destination port
* Firewall action
* Timestamp
* Related network activity

See [`incident-02.md`](incident-02.md).

## Investigation Workflow

```text
Alert / Suspicious Event
        ↓
Identify Indicators
        ↓
Search Related Events
        ↓
Analyze Activity
        ↓
Determine Severity
        ↓
Document Findings
        ↓
Recommend Action
```

## Skills Demonstrated

* Splunk event investigation
* Authentication analysis
* Firewall investigation
* Source IP analysis
* Event correlation
* Basic incident documentation
* SOC investigation methodology

## Files

```text
08-investigation/
├── README.md
├── incident-01.md
├── incident-02.md
└── screenshots/
```

## Evidence

Investigation screenshots and supporting evidence are stored in the `screenshots/` directory.
