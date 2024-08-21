import json
import sqlite3


def list_all_orders():
    # Open a connection to the database
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute(
            """
        SELECT
            o.id,
            o.jewelryId,
            o.metalId,
            o.sizeId,
            o.styleId
        FROM Orders o
        """
        )
        query_results = db_cursor.fetchall()

        # Initialize an empty list and then add each dictionary to it
        orders = []
        for row in query_results:
            orders.append(dict(row))

        # Serialize Python list to JSON encoded string
        serialized_orders = json.dumps(orders)

    return serialized_orders


def get_order(order_id):
    # Open a connection to the database
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute(
            """
        SELECT
            o.id,
            o.jewelryId,
            o.metalId,
            o.sizeId,
            o.styleId
        FROM Orders o
        WHERE o.id = ?
        """,
            (order_id,),
        )
        row = db_cursor.fetchone()

        # Check if the row is not None
        if row:
            order = dict(row)
            # Serialize Python dictionary to JSON encoded string
            serialized_order = json.dumps(order)
        else:
            serialized_order = json.dumps({"error": "Order not found"})

    return serialized_order
