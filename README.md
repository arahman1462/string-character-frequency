# String Character Frequency Counter

This project counts character occurrences in a string while preserving the order of first appearance.

Example:

Input
hello world

Output
h:1, e:1, l:3, o:2, w:1, r:1, d:1

---

## Assumptions

• Case sensitive  
• Whitespace ignored  
• Special characters counted  
• Works with UTF-8 strings  

---

## Setup

Clone repository

git clone https://github.com/YOURNAME/string-character-frequency.git

Install dependencies

pip install -r requirements.txt

---

## Run Program

python run.py

---

## Run Tests

pytest

---

## Architecture Decisions

Dictionary used to maintain insertion order and provide O(1) lookup.

Program structured into:

src folder for application logic  
tests folder for automated tests  
run.py as CLI entry point  

---

## Edge Cases Handled

• Empty string  
• Strings with only spaces  
• Mixed case characters  
• Special characters  

---

## Extending the Project

Possible improvements

• CLI flags for case sensitivity  
• Optional whitespace counting  
• JSON output format  
• Support for file input
