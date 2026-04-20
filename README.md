# IAEA_Keyword_Search
Simple IAEA document keyword search prototype 
# IAEA Document Keyword Search

A simple Python tool to search through nuclear safeguards documents using basic keyword matching. Built as a prototype for the SGIM internship application.

## What it does

- Reads all `.txt` files from a `documents` folder
- Takes a search query and splits it into keywords
- Counts keyword occurrences in each document
- Ranks results by total matches
- Displays a relevance percentage and a short preview
- Highlights key safeguards terms like countries, facilities, and materials

## How to run

1. Make sure Python 3 is installed
2. Clone or download this repository
3. Open a terminal in the project folder
4. Run:
5. 5. Type a query like `Iran centrifuges` and press Enter

## Sample queries

- `Iran`
- `Brazil nuclear`
- `IAEA safeguards Middle East`

## Files included

- `search_engine.py` – the main script
- `documents/` – three sample text files with safeguards‑related content

## Why this exists

I wanted to show a working search tool that needs no external libraries or internet connection. It's not fancy, but it's clean and gets the job done for small document sets.

For a more advanced version using semantic search and BERT‑based entity extraction, check out my other repository: `IAEA_Semantic_Search`.

---

*Built with Python and late‑night coffee.*
