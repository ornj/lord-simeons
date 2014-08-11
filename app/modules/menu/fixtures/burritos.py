# -*- coding: utf-8 -*-

from app import db
from ..models.food_item import Types, FoodItem

from pprint import pprint

data = [{
    "name": "The Beefeater",
    "description": "Grilled strip steak, cheese, onions, and green bell peppers.",
    "price": "Your loyalty to the crown.",
    "image_url": ""
}, {
    "name": "The Black Hole",
    "description": "Black Truffle and Quinoa wrap around deep fried bacon, cheetos, pork belly and miracle whip.",
    "price": "1 BTC",
    "image_url": ""
}, {
    "name": "Captain James Cook",
    "description": "Pineapple, pulled bbq pork, onion, and chili. Inspired by the cuisine of the Hawaiians who killed him, enjoy this delight while sitting out back on a raft in our salt water pool.",
    "price": "Scurvy",
    "image_url": ""
}, {
    "name": "The Earl of Sandwich",
    "description": "Blackforest Ham, Sharp Cheddar, Mayo, and a leaf of lettuce. A new take on an old classic; this sandwich is cut into a square shape (contents to match).",
    "price": "$5.00",
    "image_url": ""
}, {
    "name": "The Edinburgh",
    "description": "Eggs, beef, mustard, wrapped in a tight english muffin style tortilla of suppression.",
    "price": "$150.00 mostly tax because you are not free.",
    "image_url": ""
}, {
    "name": "Elizabeth II",
    "description": "Beef, lamb, and duck with carrots, celery and a bed of leaves on a crusty wrap",
    "price": "$42.00",
    "image_url": ""
}, {
    "name": "The Full Monty",
    "description": "Coconuts Avocado ranch, fried Swallows (mix between African and regular), elderberries jam, garnished with a shrubbery.",
    "price": "3, I mean 5. I mean 3.",
    "image_url": ""
}, {
    "name": "The Gattaca",
    "description": u"Genetically modified chicken, blue beans, jalapeño, white rice, pineapple salsa, dunked in salt water. Served on a bed of hair and skin flakes.",
    "price": "30.2 Dollars, read as thirty-point-two.",
    "image_url": ""
}, {
    "name": "The Honduran",
    "description": "Loose tobacco leaves wrapped in a whole wheat tortilla.",
    "price": "Price varies by location due to local taxes.",
    "image_url": ""
}, {
    "name": "Nessie",
    "description": "Seaweed wrapped squid, haggis and potatoes brined in Guiness&trade; and Jameson&trade;, wrapped again in cheezy tortilla.",
    "price": "About tree fiddy",
    "image_url": ""
}, {
    "name": "The Oaktown",
    "description": "Sliced Green apple, siracha aioli, pork sausage, pickled radish, wrapped in chicken skin coated with crushed up honey nut cheerios deep fried and served on dutch crunch.",
    "price": "$14.99",
    "image_url": ""
}, {
    "name": "The Princess Di",
    "description": "Mild salsa, refried beans, gouda style cheese imported from wales. Served cold, smashed against the wall of the restaurant.",
    "price": "Tears of the entire british nation.",
    "image_url": ""
}, {
    "name": "The Sir Issac Newton",
    "description": "Apple Chicken Sausage, Red Onion, Olive Oil. Dropped on your head.",
    "price": "An Alchemist's Stone of Transmutation",
    "image_url": ""
}, {
    "name": "The Troubles",
    "description": "Mashed potatoes. Wash it down with a nice cold black and tan.",
    "price": "&pound;17.99 You will pay with British Pounds.",
    "image_url": ""
}]

burritos = [FoodItem(type=Types.burrito, **item) for item in data]


def install(dry_run=False):
    """
    Jam burritos into the database's stupid mouth.

    @todo Should be made repeatable.

    :param dry_run: <bool> If true, no queries will be executed.
    :return: <list> containing <FoodItem>
    """
    db.session.add_all(burritos)
    if not dry_run:
        db.session.commit()
        return burritos
    else:
        print 'Dry run. Would have created:'
        pprint(burritos)
