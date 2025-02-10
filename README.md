
# CRUD Flask Application

This is a simple CRUD (Create, Read, Update, Delete) application built with Flask.

## Setup Instructions

1. Clone the repository:

    ```sh
    git clone https://github.com/manthanank/crud-flask.git
    cd crud-flask
    ```

2. Create a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Set up the database:

    ```sh
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

5. Run the application:

    ```sh
    flask run
    ```

## Usage

- Open your web browser and go to `http://127.0.0.1:5000/`.
- Use the interface to create, read, update, and delete records.

## Project Structure

- `app/` - Contains the application code.
- `migrations/` - Contains database migration files.
- `venv/` - Virtual environment directory.
- `requirements.txt` - List of dependencies.
- `run.py` - Entry point to run the application.

## License

This project is licensed under the MIT License.
