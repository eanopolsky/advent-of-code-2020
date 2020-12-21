#!/usr/bin/python3

import loader

inp = loader.string_list("input_day21")

foods = []
for raw_food_data in inp:
    ingredients = raw_food_data.split(" (contains ")[0].split(" ")
    allergens = raw_food_data.split(" (contains ")[1].rstrip(")").split(", ")
    food = {"i": ingredients,
            "a": allergens}
    foods.append(food)

all_ingredients = list()
all_allergens = list()
for food in foods:
    all_ingredients += food["i"]
    all_allergens += food["a"]

all_ingredients = set(all_ingredients)
all_allergens = set(all_allergens)

ingredients_x_allergens = set() # represents possible food-allergen pairings
for i in all_ingredients:
    for a in all_allergens:
        ingredients_x_allergens.add((i,a))

for food in foods:
    for food_allergen in food["a"]:
        impossible_ingredients = all_ingredients - set(food["i"])
        for impossible_ingredient in impossible_ingredients:
            try:
                ingredients_x_allergens.remove((impossible_ingredient,food_allergen))
            except KeyError:
                pass

while True:
    allergen_ingredients_count = {}
    for allergen in all_allergens:
        allergen_ingredients_count[allergen] = len([element for element in ingredients_x_allergens if element[1] == allergen])
    if max(allergen_ingredients_count.values()) == 1:
        break
    identified_allergens = [allergen for allergen in allergen_ingredients_count if allergen_ingredients_count[allergen] == 1]
    for identified_allergen in identified_allergens:
        corresponding_ingredient = [element[0] for element in ingredients_x_allergens if element[1] == identified_allergen][0]
        for allergen in all_allergens:
            if allergen == identified_allergen:
                continue
            try:
                ingredients_x_allergens.remove((corresponding_ingredient,allergen))
            except KeyError:
                pass

ingredients_x_allergens = list(ingredients_x_allergens)
ingredients_x_allergens.sort(key=lambda x: x[1])
canonical_list = ','.join([element[0] for element in ingredients_x_allergens])
print(canonical_list)

