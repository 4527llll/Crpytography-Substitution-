# Cryptography Toolkit: From Caesar to Vigenère

## 📖 Project Overview
A Python-based cryptography toolkit implementing classic encryption algorithms. This project demonstrates the conceptual evolution from monoalphabetic substitution (Caesar Cipher) to polyalphabetic substitution (Vigenère Cipher), highlighting the vulnerabilities of frequency analysis and the necessity of dynamic keys in information security.

## ✨ Core Features
* **Vigenère Cipher Implementation:** Encrypts and decrypts text using a keyword loop (`keyIndex % keyLength`). This flattens letter frequencies to defend against statistical attacks.
* **Brute-Force & Frequency Analysis:** Includes tools to exhaust the 25-key space of the Caesar cipher and auto-detect the optimal shift by targeting the high-frequency letter 'e'.
* **File I/O Integration:** Securely reads target text from `content.txt` and outputs to `encryptionResult.txt`, ensuring plaintext and ciphertext are isolated from the core logic.

## 🛡️ Security Concepts Demonstrated
* **Confidentiality (CIA Triad):** Secures plaintext readability through algorithmic substitution.
* **Cryptanalysis Mitigation:** Demonstrates how monoalphabetic ciphers fail against frequency analysis and how Vigenère mitigates this by breaking the 1-to-1 mapping rule (Confusion).
* **Key Desynchronization Awareness:** Handles file I/O meticulously (using exact overwrite modes `w` instead of append `a`) to prevent metadata or headers from corrupting the continuous key stream during decryption.

## 🚀 Quick Start

### Prerequisites
* Python 3.14.2

### Usage
1. Place your target text inside `content.txt`.
2. Run the main interactive script in the terminal:
   ```bash
   python Vigenere-mix.py