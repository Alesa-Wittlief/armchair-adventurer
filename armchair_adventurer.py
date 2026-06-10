
# Armchair Adventurer
# This quiz includes a simple 2-part quiz that takes the player's hobbies and countries of interest into account and matches them to a book recommendation. Ultimately, the goal
# is to motivate the person to take that dream vacation. 
# A 2-part quiz that recommends a travel book
# based on your hobby and dream destination.
# ─────────────────────────────────────────

def armchair_adventurer_game():
    print("Welcome to Armchair Adventurer!")
    print("Have an insatiable thirst to learn more about your dream")
    print("destination before you book that flight? Take our short")
    print("quiz and we'll suggest the perfect book for your journey!")
    
def hobby():
    print("\nWhich of the following hobbies interests you the most?")
    print("1. Hiking")
    print("2. Sightseeing")
    print("3. Historical Tours")
        
    choice = input("Enter 1, 2, or 3: ")

    if choice == "1": 
        return "hiking"
    elif choice == "2": 
        return "sightseeing"
    elif choice == "3":
        return "historical tours"
    else:
        print("Please enter 1, 2, or 3")
        return hobby()    #asks again if answer is not valid
            
def country():
    print("\nWhich of the following countries are you dreaming about?")
    print("1. Spain")
    print("2. Scotland")
    print("3. Italy")

    choice = input("Enter 1, 2, or 3: ")

    if choice == "1": 
        return "spain"
    elif choice == "2": 
        return "scotland"
    elif choice == "3":
        return "italy"
    else:
        print("Please enter 1, 2, or 3")
        return country() # Asks again if answer is not valid
    
def get_book(hobby, country):
    books = {
        ("hiking", "spain"):              "The Long Road Home by Alesa Teague",
        ("hiking", "scotland"):           "Scotland by Rick Steves",
        ("hiking", "italy"):              "The Best Day Hikes Italy by Lonely Planet",
        ("sightseeing", "spain"):         "The Ornament of the World by María Rosa Menocal",
        ("sightseeing", "scotland"):      "Scotland the Best by Peter Irvine",
        ("sightseeing", "italy"):         "Experience Italy by Lonely Planet",
        ("historical tours", "spain"):    "Shadow of the Wind by Carlos Ruiz Zafón",
        ("historical tours", "scotland"): "Historic Weekends Scotland Guidebook by Bradt Guides",
        ("historical tours", "italy"):    "Best of Italy by Rick Steves",
    }
    recommendation = books[(hobby, country)]
    print(f"\nBased on your love of {hobby} and your dream trip to")
    print(f"{country.title()}, we recommend:")
    print(f"\n  📖  {recommendation}\n")
    print("Happy reading, and happy travels!")

def main():
    armchair_adventurer_game()
    player_hobby   = hobby()
    player_country = country()
    get_book(player_hobby, player_country)

main()




