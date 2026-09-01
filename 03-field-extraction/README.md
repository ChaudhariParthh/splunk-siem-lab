# Phase 3 — Field Extraction and SPL Fundamentals

## Overview

Phase 3 focuses on understanding raw security logs and extracting useful fields in Splunk.

The goal is to move from simply viewing logs to being able to **search, extract, filter, and analyze security data using SPL (Search Processing Language).**

---

## Objectives

* Understand different security log sources.
* Inspect raw log events.
* Extract useful fields using `rex`.
* Analyze Apache web traffic.
* Analyze authentication activity.
* Filter security events.
* Use `stats` for basic analysis.
* Understand basic SPL building blocks.

---

## GitHub Structure

```text
03-field-extraction/
│
├── README.md
│
├── queries/
│   └── phase3_queries.txt
│
└── screenshots/
    ├── apache/
    ├── authentication/
    └── analysis/
```

---

## Environment

| Component        | Details                          |
| ---------------- | -------------------------------- |
| Operating System | Windows                          |
| SIEM             | Splunk Enterprise                |
| Index            | `security`                       |
| Log Sources      | Apache, Authentication, Firewall |

---

# 1. Log Source Searches

### Apache Logs

```spl
index=security source="*apache_access.log"
```

Used to search Apache web server logs.

### Authentication Logs

```spl
index=security source="*auth.log"
```

Used to search authentication and privileged activity.

### Firewall Logs

```spl
index=security source="*firewall.log"
```

Used to search firewall events.

### Show First Event

```spl
| head 1
```

`|` passes results from the previous command to the next command.

`head 1` displays the first result.

---

# 2. Apache Field Extraction

The Apache logs contain several useful values:

```text
Client IP
HTTP Method
URL
HTTP Status
Response Size
```

### Extract Client IP

```spl
index=security source="*apache_access.log"
| rex "^(?<clientip>[^ ]+)"
```

Creates the `clientip` field.

### Count Requests by Client IP

```spl
index=security source="*apache_access.log"
| rex "^(?<clientip>[^ ]+)"
| stats count by clientip
```

Useful for identifying IP addresses generating large amounts of traffic.

### Extract HTTP Method

```spl
index=security source="*apache_access.log"
| rex "\"(?<http_method>[A-Z]+)"
| stats count by http_method
```

Extracts methods such as:

```text
GET
POST
PUT
DELETE
```

### Extract URL

```spl
index=security source="*apache_access.log"
| rex "\"[A-Z]+ (?<url>[^ ]+)"
| stats count by url
```

Extracts the requested path or URL.

### Extract HTTP Status

```spl
index=security source="*apache_access.log"
| rex "\"[A-Z]+ [^ ]+ HTTP/[0-9.]+\" (?<status>\d+)"
| stats count by status
```

Extracts HTTP response codes such as `200`, `403`, and `404`.

### Extract Response Size

```spl
index=security source="*apache_access.log"
| rex "\"[A-Z]+ [^ ]+ HTTP/[0-9.]+\" \d+ (?<bytes>\d+)"
| stats count avg(bytes) max(bytes) min(bytes)
```

Extracts the response size and calculates basic statistics.

---

# 3. Authentication Field Extraction

Authentication logs contain information about users and privileged commands.

### Extract User

```spl
index=security source="*auth.log"
| rex "sudo: (?<user>\w+)"
| stats count by user
```

Extracts the user executing the `sudo` command.

### Extract Target User

```spl
index=security source="*auth.log"
| rex "USER=(?<target_user>\w+)"
| stats count by target_user
```

Extracts the account that the user attempted to operate as.

For example:

```text
USER=root
```

creates:

```text
target_user=root
```

---

# 4. Basic Security Filtering

### Find HTTP Errors

```spl
index=security source="*apache_access.log" status>=400
```

Searches for HTTP error responses.

Examples include:

```text
403 — Forbidden
404 — Not Found
500 — Server Error
```

### Count HTTP Methods

```spl
index=security source="*apache_access.log"
| stats count by method
```

Groups events according to HTTP method.

### Queries Generated Using Splunk UI

Some searches were also created directly through Splunk's **Add to Search** functionality.

This demonstrates that SPL queries can be constructed manually or through Splunk's interface.

---

# 5. Important SPL Concepts

The main concepts learned in this phase are:

| SPL       | Purpose                                  |                                 |
| --------- | ---------------------------------------- | ------------------------------- |
| `index=`  | Select the Splunk index                  |                                 |
| `source=` | Select a log source                      |                                 |
| `         | `                                        | Pass results to another command |
| `rex`     | Extract fields using regular expressions |                                 |
| `stats`   | Calculate statistics                     |                                 |
| `count`   | Count events                             |                                 |
| `by`      | Group results by a field                 |                                 |
| `head`    | Limit results                            |                                 |
| `>=`      | Compare numeric values                   |                                 |

---

# 6. SPL Learning Approach

The objective is **not to memorize complete queries**.

Instead, SPL queries can be understood as building blocks:

```text
Search
   ↓
index + source
   ↓
Filter / Extract
   ↓
rex or conditions
   ↓
Analyze
   ↓
stats / count / sort
```

For example:

```spl
index=security source="*apache_access.log"
| stats count by clientip
```

can be understood as:

```text
Search security index
        ↓
Select Apache logs
        ↓
Count events
        ↓
Group them by client IP
```

This approach makes it easier to construct new queries during an investigation.

---

# 7. Security Investigation Relevance

The fields extracted during this phase can support investigations such as:

* Identifying high-volume source IPs
* Investigating HTTP errors
* Reviewing unusual HTTP methods
* Finding suspicious URLs
* Reviewing privileged user activity
* Investigating commands executed with `sudo`
* Identifying unusual activity patterns

A field extraction by itself does **not** prove that an event is malicious. It provides structured information that can be investigated further.

---

# 8. Evidence

Screenshots captured during this phase should demonstrate:

* Raw Apache log event
* Client IP extraction
* HTTP method extraction
* URL extraction
* HTTP status extraction
* Response-size analysis
* Authentication user extraction
* Target-user extraction
* Security filtering/analysis

The screen recording should demonstrate the overall workflow rather than every individual query attempt.

---

# 9. Phase 3 Outcome

By completing this phase, the raw security logs can now be searched and analyzed using structured fields such as:

```text
clientip
http_method
url
status
bytes
user
target_user
```

