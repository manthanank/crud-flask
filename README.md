
# CRUD Flask Application

A simple CRUD (Create, Read, Update, Delete) application built with Flask.

## Setup Instructions

1. **Clone the repository:**

    ```sh
    git clone https://github.com/manthanank/crud-flask-sqlalchemy.git
    cd crud-flask
    ```

2. **Create a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the database:**

    ```sh
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

    On Windows, use the following command before running the above commands:

    ```sh
    set FLASK_APP=run.py
    ```

    Save the dependencies to `requirements.txt`:

    ```sh
    pip freeze > requirements.txt
    ```

5. **Run the application:**

    ```sh
    flask run
    ```

## Usage

- Open your web browser and go to `http://127.0.0.1:5000/`.
- Use the interface to create, read, update, and delete records.

## Project Structure

- `app/` - Application code.
- `migrations/` - Database migration files.
- `venv/` - Virtual environment directory.
- `requirements.txt` - List of dependencies.
- `run.py` - Entry point to run the application.

## License

This project is licensed under the MIT License.
