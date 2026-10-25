import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_Path = BASE_DIR / "data" / "processed" / "food_nutrition.db" 

def get_food_nutrition(dish_name):
    conn = sqlite3.connect(DB_Path)
    conn.row_factory = sqlite3.Row

    try:
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT*
            FROM food_nutrition
            WHERE "Dish Name" = ?
            """,
            (dish_name,)
        )
        result = cursor.fetchone()
        if result is None:
            return None
        return dict(result)
    finally:
        conn.close()

        