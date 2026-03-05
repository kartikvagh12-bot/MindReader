import time
import random
import json
import os

MEMORY_FILE = "mind_memory.json"

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {}

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f)

def analyze_color(color):
    color = color.lower()
    if color in ["black"]:
        return "You value control, strength, and privacy. You don’t reveal everything."
    elif color in ["blue"]:
        return "You seek stability. You prefer calm over chaos."
    elif color in ["red"]:
        return "You feel things intensely. Passion drives many of your decisions."
    elif color in ["white"]:
        return "You like clarity and order. You dislike emotional mess."
    else:
        return "You don’t like being boxed into obvious categories."

def analyze_number(number):
    n = int(number)
    if n == 7:
        return "You want to feel different from the average person."
    elif n % 2 == 0:
        return "You prefer balance and structure, even if you don't consciously notice it."
    else:
        return "You like subtle unpredictability."

def analyze_personality_type(p):
    if p.lower() == "introvert":
        return ("You process deeply before you speak. "
                "You observe more than people realize. "
                "You recharge alone, even if others think you're fine.")
    else:
        return ("You gain energy from interaction. "
                "You naturally influence the mood of a room. "
                "But sometimes you avoid sitting alone with your thoughts.")

def combine_analysis(color, number, personality, secret, hesitation):
    insights = []

    insights.append(analyze_color(color))
    insights.append(analyze_number(number))
    insights.append(analyze_personality_type(personality))

    if secret.lower() == "yes":
        insights.append("There is something unresolved in you. It shaped you more than you admit.")
    else:
        insights.append("You try to convince yourself you’ve moved on completely.")

    if hesitation > 3:
        insights.append("You hesitated before answering. That wasn’t random.")
        insights.append("Part of you debated how honest to be.")

    # subtle contradiction detection
    if personality.lower() == "extrovert" and hesitation > 3:
        insights.append("You present confidence outwardly, but internally you measure yourself carefully.")

    if personality.lower() == "introvert" and secret.lower() == "no":
        insights.append("You guard your vulnerabilities well.")

    return insights

def main():
    memory = load_memory()

    slow_print("Take a moment.")
    time.sleep(1)
    slow_print("Answer without overthinking.\n")

    name = input("Your name: ")

    if name in memory:
        slow_print(f"\nWelcome back, {name}.")
        slow_print("Patterns tend to repeat.\n")
        time.sleep(1)

    color = input("Pick a color: ")
    number = input("Pick a number between 1 and 10: ")
    personality = input("Introvert or Extrovert? ")
    month = input("Your birth month: ")

    slow_print("\nThink of something you rarely talk about.")
    start = time.time()
    secret = input("Does it still affect you? (yes/no): ")
    hesitation = time.time() - start

    slow_print("\n...\n")
    time.sleep(2)

    insights = combine_analysis(color, number, personality, secret, hesitation)

    slow_print("Here is what I see:\n")

    for line in insights:
        slow_print(line)
        time.sleep(0.7)

    slow_print("\nOne more thing.")
    time.sleep(2)

    slow_print("You care more about becoming better than staying comfortable.")
    slow_print("That tension drives you.")

    memory[name] = {
        "color": color,
        "number": number,
        "personality": personality
    }

    save_memory(memory)

main()
