# Job Application Form

> 🇬🇧 English version below / 🇨🇿 Česká verze níže

---

## 🇬🇧 English

### Description

A Flask web application that collects job applications via an HTML form.
Submitted data is stored in a SQLite database and the applicant receives
a confirmation email automatically.

### Features

- Responsive Bootstrap 5 form (name, email, start date, occupation)
- Data persistence via SQLite + Flask-SQLAlchemy ORM
- Confirmation email sent via Gmail SMTP (Flask-Mail)
- Flash notification displayed after successful submission
- Secure password handling via environment variables

### How to Run

```bash
pip install -r requirements.txt
export PASSWORD="your_gmail_app_password"   # Linux/Mac
# $env:PASSWORD="your_gmail_app_password"  # PowerShell (Windows)
python app.py
```

### Project Structure

```
JOB_APPLICATION_FORM/
├── app.py
├── templates/
│   └── index.html
├── requirements.txt
└── data.db  (auto-generated on first run)
```

### Key Concepts Practiced

- Flask routing with GET/POST methods
- ORM with Flask-SQLAlchemy (model definition, session, commit)
- Jinja2 templating (flash messages, control flow)
- Email sending via SMTP (Flask-Mail)
- Environment variables for secret management

---

## 🇨🇿 Česky

### Popis

Flask webová aplikace pro sběr žádostí o zaměstnání přes HTML formulář.
Odeslaná data se ukládají do SQLite databáze a uchazeči je automaticky
odeslán potvrzovací email.

### Funkce

- Responzivní Bootstrap 5 formulář (jméno, email, datum nástupu, zaměstnání)
- Ukládání dat do SQLite přes Flask-SQLAlchemy ORM
- Potvrzovací email přes Gmail SMTP (Flask-Mail)
- Flash notifikace po úspěšném odeslání
- Bezpečné uchovávání hesla přes proměnné prostředí

### Jak spustit

```bash
pip install -r requirements.txt
$env:PASSWORD="tvoje_gmail_app_heslo"   # PowerShell (Windows)
python app.py
```

### Klíčové koncepty

- Flask routing, GET/POST požadavky
- ORM přes Flask-SQLAlchemy (model, session, commit)
- Jinja2 šablony (flash zprávy, podmínky, smyčky)
- Odesílání emailů přes SMTP (Flask-Mail)
- Proměnné prostředí pro správu přihlašovacích údajů
