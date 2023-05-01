import streamlit as st
from st_annotated_text import annotated_text

# Define some example text
text = "This is some annotated text that we will display in our Streamlit app."

# Define the annotations
annotations = [
    (15, 25, {"color": "red", "tooltip": "This is a tooltip"}),
    (34, 41, {"color": "green", "tooltip": "Another tooltip"}),
]

# Display the annotated text
st.write("Here is some annotated text:")
annotated_text(text, annotations)
