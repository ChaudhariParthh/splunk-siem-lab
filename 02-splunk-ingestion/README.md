# Phase 2 — Splunk Data Ingestion

## Overview

This phase connects the security logs generated in Phase 1 to Splunk Enterprise.

The log files are stored on the local Windows system. Splunk is configured to monitor the directory containing these files and send the incoming events to a custom index named `security`.

The purpose of this phase is to make the generated security data searchable inside Splunk.

---

## Objectives

The objectives of this phase are:

1. Create a custom Splunk index named `security`.
2. Configure Splunk to monitor the generated log directory.
3. Send the collected events to the `security` index.
4. Search the indexed data using SPL.
5. Verify that all 170 events were successfully ingested.
6. Verify that all three log sources are available in Splunk.

---

## Project Structure

```text
02-splunk-ingestion/
│
├── README.md
│
├── configuration/
│
└── screenshots/
    ├── phase-02-01-security-index.png
    ├── phase-02-02-data-input.png
    ├── phase-02-03-events-ingested.png
    ├── phase-02-04-event-count.png
    └── phase-02-05-source-breakdown.png
```

The `configuration` directory can be used later for Splunk configuration examples such as `inputs.conf`.

---

## Environment

Operating System:

```text
Windows
```

Splunk:

```text
Splunk Enterprise
```

The generated logs are stored at:

```text
D:\Parth\CyberParth\GITHUB\splunk-siem-lab\01-log-generation\sample-logs
```

---

## Step 1 — Create the Security Index

A Splunk index is a location where indexed events are stored.

A custom index named `security` was created for this project.

Configuration:

```text
Index name: security
Index data type: Events
App: Search & Reporting
```

The remaining storage and advanced options were kept at their default settings where appropriate.

Using a separate index makes it easier to search only the security-lab data.

Example:

```spl
index=security
```

---

## Step 2 — Configure the Data Input

Splunk was configured to monitor the directory containing the generated log files.

The monitored directory is:

```text
D:\Parth\CyberParth\GITHUB\splunk-siem-lab\01-log-generation\sample-logs
```

The directory contains:

```text
sample-logs/
├── apache_access.log
├── auth.log
└── firewall.log
```

The input was configured to send the collected data to:

```text
security
```

This creates the following data flow:

```text
Log Files
    |
    v
Splunk Data Input
    |
    v
security Index
    |
    v
Search & Reporting
```

---

## Step 3 — Search the Security Index

After configuring the data input, the data was searched using the Splunk Search & Reporting application.

The basic SPL search used was:

```spl
index=security
```

This searches for events stored in the `security` index.

The time range was set to `All time` during validation to make sure events were not excluded by the time picker.

Event sampling was disabled during the final validation.

---

## Step 4 — Verify the Total Number of Events

The following SPL query was used:

```spl
index=security | stats count
```

The result was:

```text
170
```

This matches the number of events generated during Phase 1.

The original dataset contains:

```text
Apache access logs       100
Authentication logs      30
Firewall logs             40
--------------------------------
Total                    170
```

Therefore, the total number of events successfully indexed by Splunk is:

```text
170
```

---

## Step 5 — Verify the Log Sources

The following SPL query was used:

```spl
index=security | stats count by source
```

The result confirmed that all three log files were successfully ingested.

Expected result:

```text
apache_access.log    100
auth.log              30
firewall.log          40
```

Total:

```text
170
```

This verification is important because checking only the total event count would not prove that every log source was ingested correctly.

---

## Splunk Data Concepts

Several important Splunk concepts were introduced in this phase.

### Index

An index is where Splunk stores indexed data.

Project index:

```text
security
```

---

### Source

The source identifies where the event came from.

In this project, the sources are:

```text
apache_access.log
auth.log
firewall.log
```

---

### Sourcetype

A sourcetype describes the type or format of data being indexed.

Splunk automatically assigned sourcetypes during the initial ingestion.

Sourcetype configuration and normalization will be addressed in a later phase.

---

### Host

The host identifies the system from which the data originated.

In this project, the events were generated and ingested from the local Windows computer.

---

### Event

An event represents an individual log record indexed by Splunk.

For example:

```text
2026-08-27 14:20:10 FAILED_LOGIN user=admin src_ip=185.220.101.45
```

---

## SPL Queries Used

### Search all security events

```spl
index=security
```

### Count all events

```spl
index=security | stats count
```

### Count events by source

```spl
index=security | stats count by source
```

These searches were used to validate the ingestion process.

---

## Validation Results

| Validation            |  Expected |    Actual | Status |
| --------------------- | --------: | --------: | ------ |
| Apache events         |       100 |       100 | Passed |
| Authentication events |        30 |        30 | Passed |
| Firewall events       |        40 |        40 | Passed |
| Total events          |       170 |       170 | Passed |
| Security index        | Available | Available | Passed |
| All three sources     |         3 |         3 | Passed |

---

## Evidence

The following screenshots were captured during this phase:

### Security Index

```text
phase-02-01-security-index.png
```

Shows that the custom `security` index was created successfully.

### Data Input

```text
phase-02-02-data-input.png
```

Shows the configured log directory and the `security` index.

### Events Ingested

```text
phase-02-03-events-ingested.png
```

Shows the security events inside Splunk.

### Event Count

```text
phase-02-04-event-count.png
```

Shows that the `security` index contains 170 events.

### Source Breakdown

```text
phase-02-05-source-breakdown.png
```

Shows the event count for each individual log source.

---

## Phase 2 Result

The Splunk ingestion pipeline was successfully configured.

The final data flow is:

```text
Python Log Generator
        |
        v
Apache / Auth / Firewall Logs
        |
        v
Windows Log Directory
        |
        v
Splunk Data Input
        |
        v
security Index
        |
        v
Search & Reporting
        |
        v
170 Security Events
```

The three log sources were successfully indexed and verified.

---

## Skills Practiced

This phase provided practical experience with:

* Splunk Enterprise
* Splunk Web
* Splunk indexes
* Data inputs
* File and directory monitoring
* Source identification
* Sourcetypes
* Hosts
* Events
* Search & Reporting
* Basic SPL
* Event counting
* Data validation

