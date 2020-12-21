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

ingredients_possibly_with_allergens = set([element[0] for element in ingredients_x_allergens])
ingredients_definitely_without_allergens = all_ingredients - ingredients_possibly_with_allergens

safe_ingredients_appearance_count = 0
for safe_ingredient in ingredients_definitely_without_allergens:
    for food in foods:
        if safe_ingredient in food["i"]:
            safe_ingredients_appearance_count += 1

print(safe_ingredients_appearance_count)
