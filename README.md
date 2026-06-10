# Armchair Adventurer

A short interactive quiz built in Python that recommends a travel book 
based on your hobbies and dream destination. Answer two quick questions 
and get a personalized reading suggestion before you book that flight!

---

## How to Run

Make sure Python is installed on your machine, then run:

```python armchair_adventurer.py```

No additional libraries or installations required.

---

## How to Play

1. Run the program in your terminal
2. Answer Question 1 — choose your hobby:
   - Hiking
   - Sightseeing
   - Historical Tours
3. Answer Question 2 — choose your dream destination:
   - Spain
   - Scotland
   - Italy
4. Receive your personalized book recommendation!

---

## Project Structure

armchair_adventurer.py    ← main game file
README.md                 ← you are here

---

## Functions

| Function | What it does |
|---|---|
| `armchair_adventurer_game()` | Prints the welcome message |
| `hobby()` | Asks and validates Question 1 |
| `country()` | Asks and validates Question 2 |
| `get_book()` | Looks up and prints the book recommendation |
| `main()` | Ties all functions together and runs the game |

---

## Book Recommendations

| Hobby | Country | Book |
|---|---|---|
| Hiking | Spain | The Long Road Home by Alesa Teague |
| Hiking | Scotland | Scotland by Rick Steves |
| Hiking | Italy | The Best Day Hikes Italy by Lonely Planet |
| Sightseeing | Spain | The Ornament of the World by María Rosa Menocal |
| Sightseeing | Scotland | Scotland the Best by Peter Irvine |
| Sightseeing | Italy | Experience Italy by Lonely Planet |
| Historical Tours | Spain | Shadow of the Wind by Carlos Ruiz Zafón |
| Historical Tours | Scotland | Historic Weekends Scotland Guidebook by Bradt Guides |
| Historical Tours | Italy | Best of Italy by Rick Steves |

---

## Future Iterations

This was a class project with limited scope. However, I became intrigued by this project and would 
love to develop it with more ideas in the future to include: 

| More destinations around the world beyond Spain, Scotland, and Italy |
| More diverse hobbies and interests to capture real tourism interests |
| Add web interface to build this into an app that captures live results through web searches |
| Would include links to Goodreads, Amazon, and Barnes and Noble, etc. |


## Author

Created by Alesa Wittlief
Python 3.14
