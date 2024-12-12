import streamlit as st
import pandas as pd
import random

# I want to create an Interactive Story Generator that allows users to input 
# their name, a place, their favorite animal, an adjective, and a hobby 
# to generate a random story.

st.markdown(
    """
    <style>
    .main {
        background-color: #ADD8E6;  
    }
    h1 {
        color: #000080;  
    }
    p {
        color: #000080; 
    }
    .stTextInput, .stSelectbox, .stButton {
        color: black;  
    }
    </style>
    """,
    unsafe_allow_html=True,
)


st.title('Interactive Story Generator')

st.write('This app generates a personalized story based on your inputs!')

user_name = st.text_input('Enter your name:')
user_place = st.text_input('Enter a place:')
user_animal = st.text_input('Enter your favorite animal:').strip().lower()
user_adjective = st.text_input('Enter an adjective:').strip().lower()
user_hobby = st.text_input('Enter a hobby:').strip().lower()

story_type_selector = st.selectbox('Select the type of story:', ['Funny', 'Sad', 'Happy'])


if st.button('Generate My Story!'):
    if user_name and user_place and user_animal and user_adjective and user_hobby:

        if story_type_selector == 'Funny': 
            story_options = (
                f"One day, {user_name} went to {user_place} and found a {user_adjective} {user_animal}. They tried {user_hobby} together, but as you can imagine, {user_animal}'s aren't very good at that!",
                f"In {user_place}, {user_name} noticed a {user_adjective} {user_animal} attempting to {user_hobby}. It turned out the {user_animal} was better at {user_hobby} than {user_name} is!"
            )
        elif story_type_selector == 'Sad':
            story_options = (
                f"While exploring {user_place}, {user_name} discovered a {user_adjective} {user_animal}. {user_name} tried to teach {user_animal} how to {user_hobby}, so that they could go on tour and become rich, but the {user_animal} couldn't do it. It looks like {user_name} won't be rich after all.",
                f"As you know, {user_adjective} {user_animal}'s used to be common in {user_place}. They have recently begun disappearing as a result of too much {user_hobby}! {user_name} has made it their mission to stop this extinction, but they have been unsuccessful so far."
            )
        elif story_type_selector == 'Happy':
            story_options = (
                f"One bright day in {user_place}, {user_name} met a {user_adjective} {user_animal}. They took the {user_animal} home with them and even taught them how to {user_hobby}!",
                f"{user_name} has always loved to {user_hobby}, but they never had anyone to do it with. One day, they met a {user_animal} that could {user_hobby}, and they became best friends!"
            )
        story = random.choice(story_options)

        st.subheader('Your Story:')
        st.write(story)
    else:
        st.warning('Please fill out all the fields to generate your story')

#python3 -m streamlit run Final_Project_Streamlit.py



