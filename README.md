# MedSecure-Pipeline (UK GDPR Compliant)

## 🎯 Project Motivation
In the 2026 UK healthcare landscape, the integration of clinical data is governed by strict **NHS Digital** security standards and **UK GDPR**. This project was developed to demonstrate a production-grade, secure ETL (Extract, Transform, Load) pipeline designed for clinical research environments. 

The goal is to solve the "Privacy-Utility Paradox": enabling high-quality data analysis for life-saving clinical trials while ensuring that **Personally Identifiable Information (PII)** is never exposed or stored in an unencrypted state. This project aligns with the **NHS Data Security and Protection Toolkit (DSPT)** and focuses on a **Zero-Trust architecture**.

## 🛠️ Key Technical Features
* **Automated PII Scrubbing:** Utilizes Microsoft Presidio to identify and mask sensitive entities (Names, NHS Numbers, Locations) with high precision.
* **Zero-Trust Security Model:** Implements "Shift-Left" security by validating data integrity and encryption before it reaches the storage layer.
* **Advanced Cryptography:** AES-256 encryption at-rest and TLS 1.3 in-transit simulation.
* **Audit Logging:** Immutable logging of all data transformations to meet ISO 27001 compliance standards.

## 🚀 Tech Stack
* **Language:** Python 3.10+ (Pandas, Presidio, Cryptography)
* **Cloud Architecture:** Azure-ready (Key Vault for secret management)
* **DevOps:** GitHub Actions for automated unit testing (Pytest)
* **Compliance Framework:** UK GDPR & NHS DSPT
