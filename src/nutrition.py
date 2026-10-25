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

def calculate_nutrition(food, quantity_g):
    if food is None or quantity_g <= 0:
        return None
    
    scaled = {}

    for key, value in food.items():
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            scaled[key] = round(value * quantity_g / 100, 2)
        else:
            scaled[key] = value

    return scaled
