# Burp Subdomain Extractor

A simple Burp Suite extension to extract subdomains from selected HTTP responses.

## 🔍 Overview

This Burp extension allows you to extract subdomains based on a root domain (e.g., example) from HTTP responses selected in Burp's History or Search tab.

- 📥 Select one or more requests from Burp History or Search.
- ✏️ Input only the root domain (e.g., example).
- 📋 The extension extracts all matching subdomains regardless of TLD:
  - ✅ Prints them to the extension output panel.
  - ✅ Copies them to your clipboard for easy access.

## 🛠 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/intrud3rX777/Burp-Subdomain-Extractor.git
2. Load the py file in extensions.

## 🚀 Usage
1. Navigate to the Proxy → HTTP History or Search tab in Burp Suite.
2. Select one or more HTTP requests.
3. Right-click and choose the extension option (e.g., "Extract Subdomains").
4. Enter the root domain name (e.g., example)
5. The extension will:
   - Extract subdomains like api.example.com, dev.example.org, cdn.example.in, etc.
   - Print them in the extension output.
   - Copy them to your clipboard automatically.

<img width="958" alt="image" src="https://github.com/user-attachments/assets/81b8fae0-2b7d-410c-83d9-bae545433a3e" />

