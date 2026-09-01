````markdown
# Findings

## Overview

This document summarizes the key findings from the Splunk Security Monitoring Lab.

The lab covered security log generation, Splunk ingestion, field extraction, security searches, detection rules, dashboards, alerting, and incident investigation.

## Key Findings

### 1. Authentication Activity

Failed authentication events were identified in `auth.log`.

```spl
index=security source="*auth.log" "Failed password"
````

These events can be used to identify repeated login failures and potential brute-force activity.

### 2. Firewall Activity

Blocked and suspicious firewall events were identified.

```spl
index=security source="*firewall.log" "blocked"
```

Firewall logs provided useful information such as source IP addresses, ports, and connection actions.

### 3. Web Activity

Apache access logs were analyzed to identify:

* HTTP methods
* Requested URLs
* HTTP status codes
* Request volume
* Client IP addresses

### 4. Suspicious Activity

Suspicious firewall events were investigated using source IP information and event details.

These indicators should be correlated with additional events before confirming malicious activity.

## Dashboard Findings

The Security Operations Dashboard provides visibility into:

* Overall security event volume
* Authentication activity
* Firewall activity
* Blocked events
* Web traffic
* HTTP response codes
* Suspicious firewall activity
* Security activity over time

## Alerting Findings

Three alert scenarios were implemented:

* Failed Login Alert
* Brute-Force Alert
* Suspicious IP Alert

The alerts demonstrate how Splunk searches can be converted into scheduled security monitoring.

## Investigation Findings

The investigation phase demonstrated a basic SOC workflow:

```text
Detection
   ↓
Indicator Identification
   ↓
Event Analysis
   ↓
Investigation
   ↓
Conclusion
   ↓
Recommended Action
```

## Limitations

This project uses generated/sample security logs rather than production data.

Therefore, thresholds and detection logic are intended for **lab and learning purposes**. Production environments would require tuning based on baseline activity, environment-specific behavior, and false-positive analysis.

## Conclusion

The lab demonstrates an end-to-end Splunk security monitoring workflow:

**Log Generation → Ingestion → Field Extraction → Searching → Detection → Dashboard → Alerting → Investigation**

The project provides a foundation for extending the lab with more advanced detection rules, correlation searches, real-world datasets, and automated response.

```
```
