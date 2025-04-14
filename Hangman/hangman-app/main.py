import streamlit as st
import random

# --- Word List ---
words = ['python', 'streamlit', 'hangman', 'code', 'developer', 'game']

# --- Initialize Session State ---
if 'word' not in st.session_state:
    st.session_state.word = random.choice(words)
    st.session_state.guessed = ['_' for _ in st.session_state.word]
    st.session_state.attempts = 6
    st.session_state.wrong_guesses = []

# --- Title ---
st.markdown("<h1 style='color:#FF4B4B;'>🎯 Hangman Game</h1>", unsafe_allow_html=True)
st.write("Guess the letters of the secret word!")

# --- Display Word ---
display_word = ' '.join(st.session_state.guessed)
st.subheader(f"Word: {display_word}")

# --- Input ---
guess = st.text_input("Enter a letter:", max_chars=1)

# --- Game Logic ---
if guess:
    guess = guess.lower()
    if guess in st.session_state.word:
        for idx, letter in enumerate(st.session_state.word):
            if letter == guess:
                st.session_state.guessed[idx] = guess
    else:
        if guess not in st.session_state.wrong_guesses:
            st.session_state.attempts -= 1
            st.session_state.wrong_guesses.append(guess)

# --- Display Attempts ---
st.write(f"Remaining attempts: {st.session_state.attempts}")
st.write(f"Wrong guesses: {', '.join(st.session_state.wrong_guesses)}")

# --- Check for Win/Lose ---
if '_' not in st.session_state.guessed:
    st.success("🎉 Congratulations! You guessed the word!")
    if st.button("Play Again"):
        st.session_state.clear()
        st.rerun()

elif st.session_state.attempts == 0:
    st.error(f"💀 You lost! The word was '{st.session_state.word}'.")
    if st.button("Try Again"):
        st.session_state.clear()
        st.rerun()
