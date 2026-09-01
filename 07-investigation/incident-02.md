````markdown
# Incident 02 — Suspicious Firewall Activity Investigation

## Overview

Investigation of suspicious network activity identified in the Splunk `security` index.

## Detection Query

```spl
index=security source="*firewall.log" "suspicious"
````

## Investigation Steps

1. Search for suspicious firewall events.
2. Identify the source IP address.
3. Identify the destination port or service.
4. Determine whether the connection was blocked.
5. Review related firewall activity from the same source.
6. Assess the activity and document the findings.

## Observed Indicators

| Indicator        | Value                        |
| ---------------- | ---------------------------- |
| Event Type       | Suspicious Firewall Activity |
| Source IP        | `<source_ip>`                |
| Destination Port | `<port>`                     |
| Action           | `<blocked/allowed>`          |
| Timestamp        | `<timestamp>`                |

## Analysis

Suspicious firewall activity involving an unexpected or commonly targeted service may require investigation.

A firewall event alone does not confirm a successful attack. The analyst should verify the source, destination, action taken by the firewall, and any related events.

## Conclusion

**Status:** `<Benign / Suspicious / Requires Further Investigation>`

**Reason:** `<Brief explanation based on observed firewall events>`

## Recommended Actions

* Review additional activity from the source IP.
* Check whether similar connection attempts occurred.
* Verify the destination service and port.
* Confirm whether the firewall blocked the connection.
* If malicious activity is confirmed, consider blocking or monitoring the source IP.
* Continue monitoring for related network activity.

## Evidence

Screenshots related to this investigation should be stored in:

```text
08-investigation/screenshots/
```

```
```
