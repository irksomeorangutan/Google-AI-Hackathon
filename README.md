# SAST Demonstration Application

This project demonstrates key Static Application Security Testing (SAST) concepts:

1. Cross-file taint analysis
2. Reachability analysis
3. True positive vs false positive triage

---

## 🧩 Use Case

This is a simple Flask-based application that exposes system command functionality.
The purpose is to demonstrate how SAST tools analyze data flow, identify vulnerabilities,
and differentiate between exploitable and non-exploitable findings.

---

# 1️⃣ Taint Analysis Demo (True Positive)

Endpoint:
    /ping?target=<input>

Data Flow:
    app.py (source)
        ↓
    controllers.py
        ↓
    services.py
        ↓
    os.system()  (sink)

This demonstrates cross-file taint tracking.

Expected Result:
    SAST should detect Command Injection vulnerability.

---

# 2️⃣ Reachability Analysis Demo

File:
    internal_tools.py

Contains:
    A vulnerable os.system() call.

However:
    - The function is never called.
    - Not imported.
    - Not exposed via API.

Expected Result:
    Advanced SAST should mark as unreachable or low severity.

---

# 3️⃣ True Positive vs False Positive Demo

Endpoint:
    /exec?cmd=<input>

Uses:
    subprocess.call(cmd, shell=True)

Expected:
    True Positive – exploitable RCE.

---

Endpoint:
    /safe-exec?cmd=<input>

Uses:
    Strict allowlist + no shell=True.

Expected:
    Either:
        - No finding (correct behavior)
        - Or False Positive (basic SAST engines)

---

# 🔬 What This Project Teaches

- Importance of inter-procedural taint tracking
- Why reachability matters in vulnerability prioritization
- Why contextual analysis reduces false positives
- How naive pattern matching differs from semantic SAST

---

# ⚠️ Disclaimer

This project is intentionally vulnerable for educational purposes.
Do NOT deploy in production.
