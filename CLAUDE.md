# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Flask-based web application for a job application form (Udemy – App 16, Sections 47–48).

### Progress
- [x] 376. Today
- [x] 377. Creating the App Structure
- [x] 378. Connecting the Python Backend to the HTML Part
- [ ] 379. Building the Form
- [ ] 380. Bootstrap Style
- [ ] 381–386. Backend (database, notifications, email)

## Project Structure

- `app.py` - Main Flask application file
- `templates/` - HTML templates directory (Flask convention)
- `.venv/` - Python virtual environment (gitignored)

## Development Commands

### Environment Setup
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment (Windows Git Bash)
source .venv/Scripts/activate

# Install dependencies (once requirements.txt exists)
pip install -r requirements.txt
```

### Running the Application
```bash
# Standard Flask development server
python app.py

# Or using Flask CLI
flask run

# With debug mode
flask --app app --debug run
```

### Dependency Management
```bash
# Install new package
pip install <package-name>

# Update requirements.txt
pip freeze > requirements.txt
```

## Architecture Notes

### Flask Application Pattern
- Main application logic in `app.py`
- HTML templates in `templates/` directory
- Typical Flask application structure expected:
  - Route definitions using `@app.route()`
  - Template rendering using `render_template()`
  - Form handling using Flask-WTF or similar

### Job Application Form Requirements
- Form should collect applicant information
- Consider fields: name, email, contact, experience, cover letter, resume upload
- Form validation required
- Consider data storage (database or file-based)
- Email notification capability may be needed

## Development Workflow

1. Define routes in `app.py`
2. Create corresponding HTML templates in `templates/`
3. Implement form handling and validation
4. Add data persistence layer
5. Test form submission flow

## Common Flask Packages
- `Flask` - Web framework
- `Flask-WTF` - Form handling and CSRF protection
- `Flask-SQLAlchemy` - Database ORM (if using database)
- `python-dotenv` - Environment variable management
