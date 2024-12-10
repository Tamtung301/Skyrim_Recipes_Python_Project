"""
Hector Mojica Arevalo
08 December 2024
Python Project

This program will be a recipe book for Skyrim.
It will have a list of recipes that the player can make in the game.
"""

# Importing the necessary libraries
import json

def load_potions():
    with open('potions.json', 'r') as file:
        return json.load(file)["potions"]

def load_ingredients():
    with open('ingredients.json', 'r') as file:
        return json.load(file)["ingredients"]

def search_potions(potions, keyword):
    matches = [potion for potion in potions if keyword.lower() in potion["name"].lower()]
    return matches

def find_potion_by_ingredients(potions, ingredients):
    ingredients_set = set(ingredients)

    for potion in potions:
        potion_ingredients_set = set(potion["ingredients"])

        if ingredients_set == potion_ingredients_set:
            return potion

    return None

def main():
    potions = load_potions()
    print("Welcome to Skyrim's Recipe Book!")
    print("By Hector, Dovahkiin\n")

    while True:
        print("What would you like to do?")
        print("1. Search for a potion")
        print("2. Find a potion by ingredients.")
        print("3. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            keyword = input("Enter the keyword to search for potions: ")
            matches = search_potions(potions, keyword)
            if matches:
                for match in matches:
                    i = matches.index(match) + 1
                    print(f"{i} {match['name']} - {match['effect']}")
                try:
                    selection = int(input("\nEnter the number of the potion you want to view: ")) - 1
                    if 0 <= selection < len(matches):
                        selected_potion = matches[selection]
                        print(f"\nPotion: {selected_potion['name']}")
                        print(f"Ingredients: {', '.join(selected_potion['ingredients'])}")
                        print(f"Effects: {selected_potion['effect']}\n")
                    else:
                        print("Invalid selection.")
                except ValueError:
                    print("Please enter a valid number.")
            else: 
                print(f"No potions found containing that keyword: {keyword}")
        elif choice == "2":
            ingredients = input("Enter ingredients (comma-separated): ").title()
            ingredients = ingredients.split(",")
            ingredients = [ing.strip() for ing in ingredients]
            result = find_potion_by_ingredients(potions, ingredients)
            if result:
                print(f"\nPotion: {result['name']}")
                print(f"Ingredients: {', '.join(result['ingredients'])}")
                print(f"Effects: {result['effect']}\n")
            else:
                print("No potion found with those ingredients.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid number.")

if __name__ == "__main__": 
    main()