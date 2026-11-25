import random
import streamlit as st

words = [
    "python",
    "javascript",
    "csharp",
    "cplusplus",
    "assembly",
    "blocks"
]
#Page settings
st.set_page_config(page_title="Hangman",page_icon="🕺")

#Man draws
man_draws = [
    """
       +---+
       |
       |
       |
      ===
    """,
    """
       +---+
       |   O
       |
       |
      ===
    """,
    """
       +---+
       |   O
       |   |
       |
      ===
    """,
    """
       +---+
       |   O
       |  /|
       |
      ===
    """,
    """
       +---+
       |   O
       |  /|\\
       |
      ===
    """,
    """
       +---+
       |   O
       |  /|\\
       |  /
      ===
    """,
    """
       +---+
       |   O
       |  /|\\
       |  / \\
      ===
    """
]

#Start of the game

def new_game():
    st.session_state.word = random.choice(words)
    st.session_state.predictions = []
    st.session_state.due = 6

#Create a game in webside

if "word" not in st.session_state:
    new_game()

st.title("HANGAME")
st.write("Please find the secret word and save me!")
#How will the player see the man?
st.code(man_draws[6-st.session_state.due])

#How will the player see the unkown word?
sword = " ".join(
    letter if letter in st.session_state.predictions else "_"
    for letter in st.session_state.word
)
st.subheader(sword)
#Homework is here, you need to be do ad chance messages for like in 1 write under text
if st.session_state.due == 5:
    st.write("Oh oh ohh, we are in the start, i wanna say BE ATTENTION!!5️⃣")
elif st.session_state.due == 4:
    st.write("Fuuu, i'm relax but so tiny a nervous, anyway do it, keep goin WITH rights okey?4️⃣")
elif st.session_state.due == 3:
    st.write("What i say it ha? Be attention, but i look you didn't listened me YOU PIEC-(Silenced by the police)3️⃣")
elif st.session_state.due == 2:
    st.write("For God's sake, let someone else come!!2️⃣")
elif st.session_state.due == 1:
    st.write("My life is in your hands, AND YOU HAVE ONLY ONE CHANCE. If I die, I won’t let you get away with it!1️⃣")
elif st.session_state.due == 0:
    st.write("0️⃣ Your chances are overed")
#Game mention(Win,lose anywy)
win = all(
    letter in st.session_state.predictions
    for letter in st.session_state.word
)

lose = st.session_state.due == 0

#Letter buttons
letters = "abcdefghijklmonpqrstuvwxyz"
for i in range(0,len(letters),8):
    colons = st.columns(8)
    for j, letter in enumerate(letters[i:i + 8]):
        with colons[j]:
            if st.button(
                    letter.lower(),
                    key=letter,
                    disabled=(
                            letter in st.session_state.predictions
                            or win
                            or lose)):
                st.session_state.predictions.append(letter)
                if letter not in st.session_state.word:
                    st.session_state.due -= 1
                st.rerun()

#Control of the win or lose
if win:
    st.write("(This is a message from your saved person.)")
    st.success("Ohh,God!😵 Thank you so much, you saved my life düd!")
elif lose:
    st.write("(This is a message from your didN'T saved person!)")
    st.error("Wait? YOU LOSED IT THIS GAME?!?!? THIS IS yOUr fAuL-")

if win or lose:
    st.write(f"The true word is {st.session_state.word}.")
    if st.button("Do you want to play again?"):
        new_game()
        st.rerun()
