import streamlit as st
import nltk
import re
# import  streamlit_toggle as tog


try:
    nltk.data.find("corpora/words")
except LookupError:
    nltk.download('words')

st.write('# Number Plate Game!')
st.write('thanks ronan 🥰')

np = st.text_input("What's the number plate?")
letters = re.sub(r'[0-9]',r'', np)

with st.sidebar:
    hardmode = st.checkbox('activate HARDMODE 💀 (not ronan-approved)')
    dev_mode = st.checkbox('dev mode')
# with st.sidebar:
#     tog.st_toggle_switch(label="Activate Hardmode", 
#                         default_value=False, 
#                         label_after = True, 
#                         inactive_color = '#D3D3D3', 
#                         active_color="#11567f", 
#                         track_color="#29B5E8"
#                         )


pattern = "^"
if hardmode:
    for i, c in enumerate(letters):
        if i == len(letters)-1:
            pattern += c
            break
        pattern += c + '[^' + letters[(i+1):] + ']*'
else:
    pattern += '.*'.join(letters)
pattern += '$'

pattern = pattern.lower()

if dev_mode:
    st.text(pattern)


if np:
    words = nltk.corpus.words.words()

    answers = list(filter(lambda word: re.match(pattern, word), nltk.corpus.words.words()))

    if answers:
        st.success('Answers found!')
        go = st.button('Show')
        if go:
            st.write(list(filter(lambda word: re.match(pattern, word), nltk.corpus.words.words())))
    else:
        st.error('No answers found :(')