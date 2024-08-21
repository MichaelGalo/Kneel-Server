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
            o.styleId,
            s.id AS size_id,
            s.carets,
            s.price AS size_price,
            st.id AS style_id,
            st.style,
            st.price AS style_price,
            m.id AS metal_id,
            m.metal,
            m.price AS metal_price,
            j.id AS jewelry_id,
            j.type,
            j.price AS jewelry_price
        FROM Orders o
        JOIN Sizes s ON s.id = o.sizeId
        JOIN Style st ON st.id = o.styleId
        JOIN Metals m ON m.id = o.metalId
        JOIN Jewelry j ON j.id = o.jewelryId
        """
        )
        query_results = db_cursor.fetchall()

        # Initialize an empty list and then add each dictionary to it
        orders = []
        for row in query_results:

            order = {
                "id": row["id"],
                "jewelry_id": row["jewelryId"],
                "metal_id": row["metalId"],
                "size_id": row["sizeId"],
                "style_id": row["styleId"],
                "size": {
                    "id": row["size_id"],
                    "carets": row["carets"],
                    "price": row["size_price"],
                },
                "style": {
                    "id": row["style_id"],
                    "style": row["style"],
                    "price": row["style_price"],
                },
                "metal": {
                    "id": row["metal_id"],
                    "metal": row["metal"],
                    "price": row["metal_price"],
                },
                "jewelry": {
                    "id": row["jewelry_id"],
                    "type": row["type"],
                    "price": row["jewelry_price"],
                },
            }

            orders.append(order)

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


def create_order(new_order):
    # Open a connection to the database
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        # Write the SQL query to insert a new order
        db_cursor.execute(
            """
        INSERT INTO Orders
            (jewelryId, metalId, sizeId, styleId)
        VALUES
            (?, ?, ?, ?)
        """,
            (
                new_order["jewelryId"],
                new_order["metalId"],
                new_order["sizeId"],
                new_order["styleId"],
            ),
        )

        # Get the primary key of the newly created order
        new_order_id = db_cursor.lastrowid

    return new_order_id


def delete_order(id):
    # Open a connection to the database
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to delete the order
        db_cursor.execute(
            """
        DELETE FROM Orders
        WHERE id = ?
        """,
            (id,),
        )
        number_of_rows_affected = db_cursor.rowcount

    return True if number_of_rows_affected > 0 else False
