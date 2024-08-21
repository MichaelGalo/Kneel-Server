import json
import sqlite3


def update_size(id, new_data):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        UPDATE Sizes
        SET carets = ?, price = ?
        WHERE id = ?
        """,
            (new_data["carets"], new_data["price"], id),
        )

        number_of_rows_affected = db_cursor.rowcount

    return True if number_of_rows_affected > 0 else False
