import streamlit as st
import nltk
import re

nltk.download('words')

st.write('# Number Plate Game!')
st.write('thanks ronan 🥰')

np = st.text_input("What's the number plate?")
letters = re.sub(r'[0-9]',r'', np)

pattern = "^"
for i, c in enumerate(letters):
    if i == len(letters)-1:
        pattern += c
        break
    pattern += c + '[^' + letters[(i+1):] + ']*'
    
pattern += '$'

pattern = pattern.lower()

st.text(pattern)

words = nltk.corpus.words.words()

answers = list(filter(lambda word: re.match(pattern, word), nltk.corpus.words.words()))

if answers:
    st.success('Answers found!')
    go = st.button('Show')
    if go:
        st.write(list(filter(lambda word: re.match(pattern, word), nltk.corpus.words.words())))
else:
    st.error('No answers found :(')