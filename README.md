# Travel Guide AI Assistant

This repository contains a simple command-line travel assistant designed to help organise travel plans and retrieve background information about destinations.

## Features
- **Location Information**: Fetches a short summary for a location using the public Wikipedia REST API. The assistant prints the summary and indicates Wikipedia as the source.
- **Itinerary Management**: Allows adding and viewing itinerary items that are stored locally in `itinerary.json`.

## Requirements
- Python 3.6 or newer.
- Internet access is required when fetching location information from Wikipedia.

## Usage
Run the assistant from the command line:

```bash
python3 travel_assistant.py
```

Follow the on-screen menu to request location info or manage your itinerary.
