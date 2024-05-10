import os
import random
import requests
import json
from termcolor import colored
from tarot_cards_ascii import ascii_art
from branding_tarot import boxes, title, subtitle
from tarot_card_list import cards

OLLAMA_API_URL = "http://localhost:11434"
OLLAMA_MODEL_NAME = "llama3:8b"

def print_title():
    os.system("clear")
    print(colored(boxes, "blue"))
    print(colored(title, "cyan"))
    print(colored(subtitle, "yellow"))

def generate(prompt):
    headers = {"Content-Type": "application/json"}
    data = {
        'model': OLLAMA_MODEL_NAME,
        'prompt': prompt,
        'stream': True
    }
    response = requests.post(f"{OLLAMA_API_URL}/api/generate", headers=headers, json=data, stream=True)
    response.raise_for_status()
    response_parts = []
    for line in response.iter_lines():
        if line:
            body = json.loads(line)
            response_parts.append(body.get('response', ''))
            if 'error' in body:
                raise Exception(body['error'])
            if body.get('done', False):
                break
    return ''.join(response_parts)

print_title()
cards = cards  # List of all tarot cards

topic = input('What current situation or question would you like to ask about in your tarot reading? ')
tarot_spreads = ['One-Card', 'Three-Card Spread', 'Past, Present, Future', 'Celtic Cross', 'Linear']
print("Choose a tarot spread:")
for i, spread in enumerate(tarot_spreads, start=1):
    print(f"{i}. {spread}")

selected_spread_index = int(input('Enter the number corresponding to your chosen tarot spread: '))
selected_spread = tarot_spreads[selected_spread_index - 1]

# Define number of cards for each spread
spread_card_count = {
    'One-Card': 1,
    'Three-Card Spread': 3,
    'Past, Present, Future': 4,
    'Celtic Cross': 10,
    'Linear': 0  # Prompt for number of cards if Linear is chosen
}

# Determine the number of cards to draw
if selected_spread.lower() == 'linear':
    num_cards = int(input('How many cards would you like in your tarot reading? '))
else:
    num_cards = spread_card_count[selected_spread]

# Randomly draw the cards
selected_cards = random.sample(cards, num_cards)
prompt = f'You are an amazingly accurate tarot reader who is highly intuitive and in touch with the divine energies of creation. Take a moment to center yourself, and then interpret the following cards {", ".join(selected_cards)} for a question about {topic}. Please provide detailed insights for the user based on your intuitive prowess. SPREAD RULES: If 3 cards then do Situation - Obstacle - Advice. If 4 cards then do Past - Present - Future - Outcome. If 1 card then do open-ended and deep dive into archtypes. If 10 cards, interpret as the Celtic Cross spread and read the cards in order for spread placement. If any other number do a path oriented spread.'

response_text = generate(prompt)
print(colored(response_text, "cyan"))

# Optionally, display ASCII art for each drawn card
for card in selected_cards:
    if card in ascii_art:
        print(f"\n{card}:\n{ascii_art[card]}\n")
