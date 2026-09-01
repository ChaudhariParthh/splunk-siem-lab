````markdown
# Incident 01 — Failed Login Investigation

## Overview

Investigation of failed authentication activity identified in the Splunk `security` index.

## Detection Query

```spl
index=security source="*auth.log" "Failed password"
````

## Investigation Steps

1. Search for failed authentication events.
2. Identify the source IP address.
3. Identify the targeted username.
4. Review the event timestamp and related activity.
5. Determine whether the activity appears suspicious.
6. Document the findings and recommended action.

## Observed Indicators

| Indicator   | Value                  |
| ----------- | ---------------------- |
| Event Type  | Failed Authentication  |
| Source IP   | `<source_ip>`          |
| Target User | `<username>`           |
| Timestamp   | `<timestamp>`          |
| Attempts    | `<number_of_attempts>` |

## Analysis

Repeated failed authentication attempts from the same source IP may indicate password guessing or brute-force activity.

A single failed login is not sufficient to confirm an attack. The source IP, frequency of attempts, targeted accounts, and surrounding events should be considered.

## Conclusion

**Status:** `<Benign / Suspicious / Requires Further Investigation>`

**Reason:** `<Brief explanation based on observed Splunk events>`

## Recommended Actions

* Review additional authentication activity from the source IP.
* Check whether successful login activity followed the failures.
* Investigate the targeted account.
* If confirmed malicious, consider blocking or monitoring the source IP.
* Continue monitoring for repeated authentication attempts.

## Evidence

Screenshots related to this investigation should be stored in:

```text
08-investigation/screenshots/
```

```
```
