import streamlit as st
import time
import random
import json
import os

MEMORY_FILE = "mind_memory.json"


# ---------------- MEMORY ---------------- #

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {}

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f)


# ---------------- ANALYSIS FUNCTIONS ---------------- #

def analyze_color(color):
    color = color.lower()
    if color == "black":
        return "You value control, strength, and privacy. You don’t reveal everything."
    elif color == "blue":
        return "You seek stability. You prefer calm over chaos."
    elif color == "red":
        return "You feel things intensely. Passion drives many of your decisions."
    elif color == "white":
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

    if personality.lower() == "extrovert" and hesitation > 3:
        insights.append("You present confidence outwardly, but internally you measure yourself carefully.")

    if personality.lower() == "introvert" and secret.lower() == "no":
        insights.append("You guard your vulnerabilities well.")

    return insights


# ---------------- APP UI ---------------- #

st.title("🔮 Psychological Pattern Reader")

st.write("Take a moment. Answer without overthinking.")

memory = load_memory()

name = st.text_input("Your name")

if name and name in memory:
    st.info(f"Welcome back, {name}. Patterns tend to repeat.")

color = st.text_input("Pick a color")
number = st.slider("Pick a number between 1 and 10", 1, 10)

personality = st.selectbox(
    "Introvert or Extrovert?",
    ["Introvert", "Extrovert"]
)

month = st.text_input("Your birth month")

st.write("Think of something you rarely talk about.")

# hesitation timer
if "secret_start_time" not in st.session_state:
    st.session_state.secret_start_time = time.time()

secret = st.selectbox(
    "Does it still affect you?",
    ["yes", "no"]
)

hesitation = time.time() - st.session_state.secret_start_time


if st.button("Analyze"):

    with st.spinner("Analyzing psychological patterns..."):
        time.sleep(2)

    insights = combine_analysis(color, number, personality, secret, hesitation)

    st.subheader("Here is what I see:")

    for line in insights:
        st.write(line)
        time.sleep(0.3)

    st.write("---")
    st.write("One more thing.")
    time.sleep(1)

    st.write("You care more about becoming better than staying comfortable.")
    st.write("That tension drives you.")

    memory[name] = {
        "color": color,
        "number": number,
        "personality": personality
    }

    save_memory(memory)

st.markdown(
    """
    <hr style="margin-top:50px;margin-bottom:10px;">
    <p style="text-align:center; color:gray; font-size:12px;">
    created by Kartik Vagh
    </p>
    """,
    unsafe_allow_html=True
)
