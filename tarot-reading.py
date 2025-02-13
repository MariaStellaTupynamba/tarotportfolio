import random

# Simple Tarot Deck with Upright Meanings
tarot_deck = {
    "The Fool": "New beginnings, spontaneity, free spirit.",
    "The Magician": "Manifestation, resourcefulness, power.",
    "The High Priestess": "Intuition, wisdom, mystery.",
    "The Empress": "Abundance, nurturing, fertility.",
    "The Emperor": "Authority, structure, stability.",
    "The Hierophant": "Tradition, spiritual wisdom, guidance.",
    "The Lovers": "Love, harmony, relationships.",
    "The Chariot": "Control, willpower, determination.",
    "Strength": "Courage, inner strength, compassion.",
    "The Hermit": "Soul-searching, introspection, solitude.",
    "Wheel of Fortune": "Change, cycles, fate.",
    "Justice": "Fairness, truth, law.",
    "The Hanged Man": "Letting go, new perspective, surrender.",
    "Death": "Transformation, endings, new beginnings.",
    "Temperance": "Balance, moderation, patience.",
    "The Devil": "Materialism, addiction, attachment.",
    "The Tower": "Sudden change, upheaval, revelation.",
    "The Star": "Hope, inspiration, spirituality.",
    "The Moon": "Illusions, intuition, subconscious.",
    "The Sun": "Success, vitality, joy.",
    "Judgment": "Reflection, reckoning, awakening.",
    "The World": "Completion, accomplishment, travel."
}

def draw_card():
    card = random.choice(list(tarot_deck.keys()))
    meaning = tarot_deck[card]
    return card, meaning

def tarot_reading():
    print("Welcome to the Tarot Reading Program!")
    choice = input("Would you like a one-card or three-card reading? (1/3): ")
    
    if choice == "1":
        card, meaning = draw_card()
        print(f"\nYour card: {card}\nMeaning: {meaning}")
    elif choice == "3":
        print("\nYour three-card reading:")
        for i in range(3):
            card, meaning = draw_card()
            print(f"Card {i+1}: {card} - {meaning}")
    else:
        print("Invalid choice. Please restart and select either 1 or 3.")

if __name__ == "__main__":
    tarot_reading()
