import streamlit as st
import requests
from datetime import date

st.set_page_config(page_title="Catholic Daily", page_icon="✝️")

# Sidebar for navigation
st.sidebar.title("Menu")
page = st.sidebar.radio("Go to:", ["Daily Home", "Prayer Library", "Novena Tracker", "My Intentions"])

if page == "Daily Home":
    st.title("🙏 Catholic Daily")
    today = date.today()
    st.write(f"### {today.strftime('%A, %B %d, %Y')}")

    # Get Saint of the Day
    try:
        res = requests.get("http://calapi.inadiutorium.cz/api/v1/calendars/general-en/today").json()
        saint = res['celebrations'][0]['title']
    except: saint = "Ordinary Time"

    # Get Bible Verse
    try:
        res = requests.get("https://bible-api.com/verse_of_the_day?translation=dra").json()
        text, ref = res['verse']['text'], res['verse']['name']
    except: text, ref = "The Lord is my shepherd...", "Psalm 23"

    st.info(f"**Today's Saint/Feast:** {saint}")
    st.divider()
    st.subheader("📖 Daily Scripture")
    st.write(f"*{text}*")
    st.caption(f"— {ref} (Douay-Rheims)")

elif page == "Prayer Library":
    st.title("📿 Prayers")
    prayer = st.selectbox("Select Prayer", ["Anima Christi", "St. Michael Prayer"])
    if prayer == "Anima Christi":
        st.write("Soul of Christ, sanctify me. Body of Christ, save me...")
    else:
        st.write("St. Michael the Archangel, defend us in battle...")

elif page == "Novena Tracker":
    st.title("⏳ Novena")
    n_name = st.text_input("Novena Name", "St. Jude")
    day = st.slider("Day", 1, 9)
    st.write(f"You are on Day {day} of your {n_name} novena.")

elif page == "My Intentions":
    st.title("📝 Prayer Intentions")
    note = st.text_area("What are you praying for today?")
    if st.button("Save Intention"):
        st.success("Intention saved in your heart!")
  
