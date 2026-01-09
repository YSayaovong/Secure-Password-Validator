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

```
secure_password_validator.py   # Core implementation + CLI
test_checker.py                # Isolated unit tests (mocked API)
requirements.txt               # Dependencies
```

---

## ▶️ How to Run

### 1. Set up environment
```bash
python -m venv .venv
```

Activate:

**Windows**
```powershell
.venv\Scripts\Activate.ps1
```

**macOS / Linux**
```bash
source .venv/bin/activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the validator
```bash
python secure_password_validator.py
```

You will be prompted securely:
```
Enter password to check (not stored):
```

---

## 🧪 Tests

Tests are written using **pytest** and mock the HIBP API to ensure:

- No network calls during testing  
- Fast, deterministic results  
- Clear coverage of success and failure cases  

Run tests with:
```bash
pytest -v
```

---

## 📌 Example Output

**Compromised password**
```
This password appeared in breaches 23,456 times. Choose another.
```

**Not found**
```
Password not found in breach database.
```

---

## 🧠 Why This Project

This project focuses on:

- Correct API usage  
- Secure handling of sensitive input  
- Separation of concerns (CLI vs logic)  
- Testability through dependency injection  
- Clean, readable Python  

It demonstrates how small tools can be built **safely and responsibly** when dealing with user security data.

---

## ⚠️ Notes

- A “not found” result does **not** guarantee a password is safe.  
- Always use **unique passwords** and **multi-factor authentication (MFA)**.

---

## 📚 References

- Have I Been Pwned — Pwned Passwords API  
  https://haveibeenpwned.com/API/v3#PwnedPasswords
