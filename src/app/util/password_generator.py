from sqlalchemy import select, func, Integer


def generate_custom_id(connection, model, prefix: str, id_column):
    numeric_part = func.substring(id_column, len(prefix) + 1)

    result = connection.execute(
        select(func.max(func.cast(numeric_part, Integer)))
    ).scalar()

    next_number = (result or 0) + 1
    return f"{prefix}{next_number:03d}"