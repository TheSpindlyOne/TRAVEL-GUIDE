#!/usr/bin/env python3
"""Simple CLI travel assistant.

Features:
- Fetches basic location info from Wikipedia.
- Lets users add itinerary items and view them.

Requires internet access to fetch location data from Wikipedia API.
"""

import json
import os
import sys
from urllib import request, parse

ITINERARY_FILE = "itinerary.json"


def load_itinerary():
    if os.path.exists(ITINERARY_FILE):
        with open(ITINERARY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_itinerary(items):
    with open(ITINERARY_FILE, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2)


def get_location_info(location):
    """Return summary info for a location from Wikipedia."""
    title = parse.quote(location)
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"
    try:
        with request.urlopen(url) as resp:
            data = json.load(resp)
        if 'extract' in data:
            return data['extract'] + "\n(Source: Wikipedia)"
        else:
            return "No information found."
    except Exception as exc:
        return f"Error fetching data: {exc}"


def add_itinerary_item(items, item):
    items.append(item)
    save_itinerary(items)


def main():
    items = load_itinerary()
    while True:
        print("\nTravel Assistant")
        print("1. Get location info")
        print("2. Add itinerary item")
        print("3. View itinerary")
        print("4. Exit")
        choice = input("Select an option: ").strip()
        if choice == "1":
            location = input("Enter a location: ").strip()
            info = get_location_info(location)
            print(info)
        elif choice == "2":
            item = input("Enter itinerary item: ").strip()
            if item:
                add_itinerary_item(items, item)
                print("Item added.")
        elif choice == "3":
            if not items:
                print("Itinerary is empty.")
            else:
                for idx, it in enumerate(items, 1):
                    print(f"{idx}. {it}")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting.")
