# SIMPLE FORM - Flask

![Flask App Demo](./demo/form-demo.gif)

## Tech Stack
- Python, Flask
- SQLite, Flask-SQLAlchemy
- HTML, Jinja, Bootstrap

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/form-db.git](https://github.com/your-username/form-db.git)
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
    Tho, I myself, use `flask run` 🙈.

***The app will be available at http://127.0.0.1:5000.***

## SAMPLE METADATA/SCHEMA
The database consists of a single table `FormData` with the following structure:
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
