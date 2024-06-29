import os
import streamlit as st 
from zutils import levenshtein_distance, load_vocab

if 'userinput' not in st.session_state:
    st.session_state.userinput = ''

def main () :
    st . title (" Word Correction using Levenshtein Distance ")
    word = st . text_input ('Word :', key="userinput")
    vocabs = load_vocab('F:/AIO/AIO2024/M01/Exercise04/data/vocab.txt')
    sorted_distences = dict()
    
    if st . button (" Compute ") :
        # compute levenshtein distance
        leven_distances = dict ()
        for vocab in vocabs :
            leven_distances [ vocab ] = levenshtein_distance ( word , vocab )

        # sorted by distance
        sorted_distences = dict ( sorted ( leven_distances . items () , key = lambda item :item [1]) )
        correct_word = list ( sorted_distences . keys () ) [0]
        st . write ('Correct word : ', correct_word )

    if st.button("Clear"):
        st.session_state.userinput=""
    st.divider()

    col1 , col2 = st . columns (2)
    col1 . write ('Vocabulary :')
    col1 . write ( vocabs )
    col2 . write ('Distances :')
    col2 . write ( sorted_distences )


if __name__ == "__main__":
    main()