# 🔐 Secure Password Validator  
**Have I Been Pwned (HIBP) Password Breach Checker — Python**

This project implements a secure, testable password validation tool using the **Have I Been Pwned (HIBP) Pwned Passwords API**.  
It allows users to check whether a password has appeared in known data breaches **without ever sending the password itself over the network**.

The implementation follows HIBP’s **k-anonymity model**, ensuring privacy while delivering reliable breach detection.

---

## ⚙️ What This Tool Does

- Accepts a password securely via terminal input
- Hashes the password locally using **SHA-1**
- Sends **only the first 5 characters** of the hash to the HIBP API
- Compares returned hash suffixes locally
- Reports how many times the password has appeared in known breaches
- Never logs, prints, or transmits the plaintext password

---

## 🔒 Security & Privacy Design

This tool follows best practices recommended by HIBP:

- **K-anonymity**: only partial hashes are transmitted
- **No plaintext passwords** are ever exposed
- Uses `getpass` to prevent terminal echo
- Adds API padding headers to reduce metadata leakage
- Does not store passwords or hashes

---

## 🧱 Project Structure

