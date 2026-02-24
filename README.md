# SIMPLE FORM - Flask
A lightweight web application built with **Flask** and **SQLite** that captures user data through a semantic HTML5 form and persists it in a relational database. This repo focuses on **server-side form processing**, **relational data storage** in a single-table schema, and **dynamic UI rendering** (bootstrap 🔛🔝). 

![Flask App Demo](./demo/form-demo.gif)

## Tech Stack
- Python, Flask
- SQLite, Flask-SQLAlchemy
- HTML, Jinja, Bootstrap

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rachelannec/simple-form.git
   cd form-db
   ```
2. **Set up a virtual environment**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```
3. Install dependencies:
   ```Bash
    pip install -r requirements.txt
    ```
4. Run the app:
   ```Bash
    python app.py
    ````
    > Tho, I myself, use `flask run` 🙈.

***The app will be available at http://127.0.0.1:5000.***

## Database Location

By default, the SQLite database is handled as follows:

* **File Name:** `form_data.db`
* **Location:** The file is automatically created in the `/instance` folder (or the root directory) upon the first successful run of the application.
* **Persistence:** Because SQLite is file-based, your data stays saved even if you restart the Flask server.

> The `.db` file is excluded from version control via `.gitignore` to ensure that local development data is not accidentally pushed to GitHub. 🙉

## SAMPLE METADATA/SCHEMA
The database consists of a single table `FormData` with the following structure. You may put the following command on the terminal youself. 
```bash
sqlite3 instance/form_data.db
sqlite> .header on  
sqlite> .mode box
sqlite> PRAGMA table_info(form_data);
┌─────┬──────────┬──────────────┬─────────┬────────────┬────┐
│ cid │   name   │     type     │ notnull │ dflt_value │ pk │
├─────┼──────────┼──────────────┼─────────┼────────────┼────┤
│ 0   │ id       │ INTEGER      │ 1       │            │ 1  │
│ 1   │ username │ VARCHAR(80)  │ 1       │            │ 0  │
│ 2   │ email    │ VARCHAR(120) │ 0       │            │ 0  │
└─────┴──────────┴──────────────┴─────────┴────────────┴────┘
```

- `cid` means column id
- `notnull`: `1` means field is required, `0` means it can be empty
- `pk`: `1` means its a primary key
