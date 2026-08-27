splunk-security-monitoring-lab/
│
├── README.md
│
├── 01-log-generation/
│   ├── generate_security_logs.py
│   ├── sample_logs/
│   │   ├── apache_access.log
│   │   ├── auth.log
│   │   └── firewall.log
│   └── README.md
│
├── 02-splunk-ingestion/
│   ├── README.md
│   ├── screenshots/
│   │   ├── 01-create-index.png
│   │   ├── 02-data-input.png
│   │   └── 03-events-ingested.png
│   └── configuration/
│       └── inputs.conf.example
│
├── 03-field-extraction/
│   ├── README.md
│   ├── props.conf.example
│   ├── transforms.conf.example
│   └── screenshots/
│
├── 04-security-searches/
│   ├── README.md
│   ├── authentication-searches.spl
│   ├── firewall-searches.spl
│   ├── web-attack-searches.spl
│   └── screenshots/
│
├── 05-detection-rules/
│   ├── README.md
│   ├── brute-force-detection.spl
│   ├── suspicious-ip-detection.spl
│   ├── failed-login-detection.spl
│   └── screenshots/
│
├── 06-dashboard/
│   ├── README.md
│   ├── dashboard.xml
│   └── screenshots/
│       └── security-dashboard.png
│
├── 07-alerting/
│   ├── README.md
│   └── screenshots/
│
├── 08-investigation/
│   ├── README.md
│   ├── incident-01.md
│   ├── incident-02.md
│   └── screenshots/
│
├── 09-documentation/
│   ├── architecture.png
│   ├── setup-guide.md
│   └── findings.md
│
└── LICENSE