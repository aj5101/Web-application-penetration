# 🔓 Python Brute Forcer Tools

This project contains two Python scripts designed for **educational purposes** in ethical hacking and penetration testing:

1. **Login Brute Forcer** – Attempts to crack a web login by trying multiple passwords.
2. **Directory Brute Forcer** – Scans for hidden or unlisted directories in a target web application.

> ⚠️ **Disclaimer**: These tools are strictly for educational use or testing on authorized targets only. Unauthorized usage is illegal and unethical.

---

## 📁 Project Files

- `bruteforcer.py` – Performs login brute force attacks using a list of passwords.
- `directories.py` – Performs directory brute forcing to discover hidden paths.
- `passwords.txt` – A list of potential passwords used for login attacks.
- `common.txt` – A list of common directory names used for directory scanning.

---

## ⚙️ Requirements

- Python 3.x
- [`requests`](https://pypi.org/project/requests/) library

Install dependencies using pip:

```bash
pip install requests
```
# 🔐 Login Brute Forcer


## 🎯 Purpose:
- Attempts to crack a known username's password by iterating through a list of potential passwords.

## ⚙️ How It Works:
- Sends POST requests to the login form.
- Reads passwords from passwords.txt.
- Uses the requests library to automate the process.


## 🧪 Usage Example:
- python login_bruteforcer.py
- Make sure to update the target URL and form field names in the script.
- The data payload should look like:
data = {
    'username': 'admin',
    'password': 'password123'
}
# 📂 Directory Brute Forcer

## 🎯 Purpose:
- Scans for hidden or common directories on a web server, such as on DVWA, Metasploitable, or other test platforms.

## ⚙️ How It Works:
- Sends GET requests to each path listed in wordlist.txt.
- If the server responds with a 200 OK, the directory likely exists.

## 🧪 Usage Example:
- python directories.py
- Be sure to set the base URL correctly at the top of the script.

## 📝 Notes

- Always test in legal and authorized environments like:
- DVWA (Damn Vulnerable Web App)
- Metasploitable 2
- Your own web application

## ⚠️ Legal Disclaimer

- This software is intended for legal security research and educational purposes only.

- ❗ Unauthorized use of brute force or scanning tools on systems you do not own or have explicit permission to test is a criminal offense.
- Always think before you scan.

