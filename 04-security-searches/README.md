# Phase 4 — Security Searches

## Overview

This phase focuses on using Splunk to investigate security-related activity from different log sources.

The searches are divided into three areas:

* **Authentication** — login failures, user activity, and privileged commands
* **Firewall** — blocked traffic, source IPs, destinations, and suspicious connections
* **Web Attacks** — HTTP errors, suspicious URLs, SQL injection indicators, and unusual web requests

## Log Sources

| Log                 | Purpose                             |
| ------------------- | ----------------------------------- |
| `auth.log`          | Authentication and user activity    |
| `firewall.log`      | Network traffic and firewall events |
| `apache_access.log` | Web server requests                 |

## Skills Practiced

During this phase, I practiced:

* Searching specific log sources
* Filtering security events
* Using the `rex` command to extract fields
* Using `stats` to summarize events
* Grouping results with `by`
* Sorting results using `sort`
* Investigating suspicious IP addresses
* Investigating suspicious URLs and ports
* Identifying possible attack indicators

## Folder Structure

```text
04-security-searches/
├── README.md
├── authentication-searches.spl
├── firewall-searches.spl
├── web-attack-searches.spl
└── screenshots/
```

## Key Splunk Commands

```text
rex
stats
sort
search
```

### Important Concept

Splunk searches are built step by step using the pipe `|`.

```text
Search events
    |
Extract information
    |
Summarize results
    |
Sort results
```

For example:

```spl
index=security source="*firewall.log"
| rex "from (?<source_ip>\d+\.\d+\.\d+\.\d+)"
| stats count by source_ip
| sort - count
```

This searches firewall logs, extracts source IP addresses, counts their occurrences, and displays the highest counts first.

## Outcome

By completing Phase 4, I gained practical experience in turning raw security logs into useful investigation results using Splunk SPL.

The focus was not on memorizing every command, but on understanding the investigation workflow:

**Find → Extract → Filter → Aggregate → Investigate**
