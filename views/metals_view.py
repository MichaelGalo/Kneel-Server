import json
import sqlite3


def update_metal(id, new_data):
    # Open a connection to the database
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to update the metal
        db_cursor.execute(
            """
        UPDATE Metals
        SET metal = ?, price = ?
        WHERE id = ?
        """,
            (new_data["metal"], new_data["price"], id),
        )

        # Check if any rows were affected
        number_of_rows_affected = db_cursor.rowcount

    return True if number_of_rows_affected > 0 else False
