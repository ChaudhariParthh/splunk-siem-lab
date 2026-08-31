# Security Operations Dashboard

A Splunk dashboard for monitoring and analyzing security events collected in the `security` index.

## Dashboard Panels

* **Total Security Events** — Overall event count
* **Blocked Firewall Events** — Number of blocked firewall events
* **Web Events** — Apache web activity
* **Authentication Events** — Authentication activity
* **Firewall Events** — Firewall activity
* **HTTP Status Codes** — Distribution of HTTP response codes
* **Top Blocked Source IPs** — Top source IPs associated with blocked traffic
* **Security Events Over Time** — Event activity trend
* **Suspicious Firewall Events** — Suspicious firewall activity

## Features

* Time-range filtering
* SPL-based security analysis
* Firewall and authentication monitoring
* Web traffic analysis
* Source IP investigation
* Visual security event trends

## Files

```text
06-dashboard/
├── README.md
├── dashboard.xml
└── screenshots/
    └── security-dashboard.png
```

## Screenshot

![Security Operations Dashboard](screenshots/security-dashboard.png)

## Skills Demonstrated

* Splunk SPL
* Dashboard creation
* Data visualization
* Security event monitoring
* Firewall analysis
* Authentication analysis
* Basic SOC investigation
