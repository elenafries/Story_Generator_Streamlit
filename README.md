# Story_Generator_Streamlit
For my final project for Survey of Software Engineering with Python, I created an app using Streamlit that generates a random story based on user inputs. The app takes user inputs such as their name, a place, favorite animal, an adjective, and a hobby and generates a random story. Users can also select if they want a funny, sad, or happy story.

Features
- User Inputs: The user provides the requested inputs into a text input. These inputs are used to generate a story.
- Story Type Selection: The user uses a selectbox to choose if the story generated is a funny, sad, or happy story.
- Story Generation: Once the user clicks the "Generate My Story" button, the app randomly selects a predefined story template and adds in the user inputed characteristics to customize the story to that user. Note: I think that this app would benefit from using openAI, but I did not have the funds to do that for this project.
- Defensive Programming: If the user fails to fill in all fields, the app gives them a warning message asking them to complete all inputs. I also programmed it so that no matter what they input, the app will turn the given words to lower case so that there are not upper case words in the stories that do not belong.
- Custom Styling: I used some HTML styling to make the app more colorful and visually appealing.
