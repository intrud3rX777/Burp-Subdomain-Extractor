# Burp Subdomain Extractor

A simple Burp Suite extension to extract subdomains from selected HTTP requests.

## 🔍 Overview

This Burp extension allows you to extract subdomains related to a target domain from HTTP requests selected in Burp's History or Search tab.

- 📥 Select one or more requests from Burp History or Search.
- ✏️ Input the domain you want to extract subdomains for (e.g., `example.com`).
- 📋 The extension extracts all matching subdomains:
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
4. Enter the target domain (e.g., example.com)
5. The extension will:
   - Extract subdomains like api.example.com, dev.example.com, etc.
   - Print them in the extension output.
   - Copy them to your clipboard automatically.
