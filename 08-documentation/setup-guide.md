# Splunk Security Monitoring Lab — Setup Guide

## Prerequisites

* Splunk Enterprise
* Python 3
* Basic SPL knowledge
* Windows/Linux system capable of running Splunk

## 1. Generate Security Logs

Navigate to:

```text
01-log-generation/
```

Run:

```bash
python generate_security_logs.py
```

This generates sample:

* Apache access logs
* Authentication logs
* Firewall logs

The generated logs are stored in:

```text
01-log-generation/sample_logs/
```

## 2. Create Splunk Index

Create an index named:

```text
security
```

This index stores all logs used in the project.

## 3. Ingest the Logs

Configure Splunk to monitor:

```text
01-log-generation/sample_logs/
```

The project contains an example configuration in:

```text
02-splunk-ingestion/configuration/inputs.conf.example
```

Verify ingestion with:

```spl
index=security
```

## 4. Extract Security Fields

Review the field extraction configuration in:

```text
03-field-extraction/
```

The project demonstrates extraction of fields such as:

* Source IP
* HTTP method
* URL
* HTTP status
* Bytes
* Username

SPL `rex` was used for several field extractions.

## 5. Perform Security Searches

Security searches are organized in:

```text
04-security-searches/
```

Example:

```spl
index=security source="*auth.log" "Failed password"
```

These searches cover authentication, firewall, and web activity.

## 6. Configure Detection Rules

Detection examples are available in:

```text
05-detection-rules/
```

These demonstrate identifying potentially suspicious activity from the collected logs.

## 7. Create the Dashboard

The Security Operations Dashboard is documented in:

```text
06-dashboard/
```

Dashboard source:

```text
06-dashboard/dashboard.xml
```

Dashboard screenshot:

```text
06-dashboard/screenshots/security-dashboard.png
```

The dashboard provides visibility into authentication, firewall, web, blocked, and suspicious activity.

## 8. Configure Alerts

Alert configurations are documented in:

```text
07-alerting/
```

The project includes:

* Failed Login Alert
* Brute-Force Alert
* Suspicious IP Alert

## 9. Perform Investigations

Investigation examples are available in:

```text
08-investigation/
```

The incidents demonstrate a basic SOC workflow from detection through analysis and recommended action.

## 10. Review Documentation

Additional project documentation is available in:

```text
09-documentation/
```

including:

* Architecture
* Setup guide
* Findings

## Project Workflow

```text
Generate Logs
      ↓
Splunk Ingestion
      ↓
Field Extraction
      ↓
Security Searches
      ↓
Detection Rules
      ↓
Dashboard
      ↓
Alerting
      ↓
Investigation
      ↓
Findings & Documentation
```

## Verification

After completing the setup, verify that Splunk returns events with:

```spl
index=security
```

Then test individual sources:

```spl
index=security source="*auth.log"
```

```spl
index=security source="*firewall.log"
```

```spl
index=security source="*apache_access.log"
```

If all three return events, the core lab environment is functioning correctly.
