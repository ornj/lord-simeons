from .food_item import Types, FoodItem


def find_all(limit=0, offset=0):
    query = FoodItem.query
    if limit:
        query = query.limit(limit)
    if offset:
        query = query.offset(offset)
    return query.all()
