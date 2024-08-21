# Kneel Diamonds Server

This project is a server for managing orders for Kneel Diamonds. It uses Python's built-in `http.server` module to handle HTTP requests and SQLite for the database.

## Requirements

- Python 3.x
- SQLite

## Installation

1. Clone the repository:

    ```sh
    git clone SSH key
    cd kneel-server
    ```

2. Ensure you have Python and SQLite installed.

3. Set up the database:

    ```sh
    sqlite3 kneeldiamonds.sqlite3 < schema.sql
    ```

## Running the Server

To run the server, execute the following command:

```sh
python json-server.py