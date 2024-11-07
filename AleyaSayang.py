import streamlit as st
import time

# Function to add balloon and hearts animation
def add_balloon_hearts():
    st.balloons()  # adds balloon animation
    st.markdown(
        """
        <style>
        @keyframes heart {
            0% { transform: scale(1); }
            25% { transform: scale(1.2); }
            50% { transform: scale(1); }
            75% { transform: scale(1.2); }
            100% { transform: scale(1); }
        }
        .heart {
            color: red;
            font-size: 40px;
            animation: heart 1s infinite;
        }
        </style>
        """, unsafe_allow_html=True
    )
    st.markdown("<div class='heart'>❤️ ❤️ ❤️</div>", unsafe_allow_html=True)

# Title of the page
st.title("💌 Surprise for My Sayang 💌")

# Create a button with a mail icon
if st.button("📧 Press me to reveal your surprise!"):
    # Wait a bit for suspense
    with st.spinner("Preparing your surprise..."):
        time.sleep(2)  # Pause for effect
    
    # Display message and image
    st.subheader("To the Most Beautiful Person in My Life 💖")
    st.write("""
        My dearest Aleya Nadhirah,

I know you are going through a really tough time right now. Awak kena hadap jadual yang packed, kene prepare for seminar and kena study at the same time. I know you will feel overwhelming and its okay to feel stressed and anxious baby. In fact menda tu completely normal for us manusia biasa sayang. You push yourself to achieve something incredible.

You already achieve so much and you will achieve more sayang im sure. I know i cant take your pressure away. But i want you to know that i am here for you. I can be your ear, your shoulder to cry on, someone to end your day with. Im here sayang and i will always support your journey.
Im very proud of all that youre accomplishing.

So take a deep breath sayang and remember why you choose this path. You got this sayang and i cant wait to be successful with you my dear love.


I love you more than words can say.

Forever yours,

Shahrul Hafiz 💘
    """)

    
    # Add animations
    add_balloon_hearts()
else:
    st.write("KLIK BUTANG ATAS  NI SAYANGGG! 💌")
