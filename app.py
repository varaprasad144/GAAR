#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
from streamlit_option_menu import option_menu

# Page Configuration
st.set_page_config(
    page_title="Premium Felgen & Reifen",
    page_icon="🚗",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .hero {
        background-color: #111;
        padding: 60px;
        border-radius: 15px;
        text-align: center;
        color: white;
    }
    .product-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Navigation Menu
selected = option_menu(
    menu_title=None,
    options=["Startseite", "Felgen", "Reifen", "Über uns", "Kontakt"],
    icons=["house", "circle", "disc", "info-circle", "envelope"],
    orientation="horizontal"
)

# ---------------- STARTSEITE ----------------
if selected == "Startseite":
    st.markdown("""
        <div class="hero">
            <h1>Premium Felgen & Reifen</h1>
            <p>Qualität, Performance & Stil für Ihr Fahrzeug</p>
        </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.subheader("Warum wir?")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.success("✔ Hochwertige Marken")
    with col2:
        st.success("✔ Schnelle Montage")
    with col3:
        st.success("✔ Faire Preise")

# ---------------- FELGEN ----------------
elif selected == "Felgen":
    st.title("Unsere Felgen")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1619767886558-efdc259cde1a", use_column_width=True)
        st.subheader("Sport Felge 19 Zoll")
        st.write("Preis: 299€")
        st.button("Anfragen", key="f1")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1583267746897-2cf415887172", use_column_width=True)
        st.subheader("Alu Felge 18 Zoll")
        st.write("Preis: 249€")
        st.button("Anfragen", key="f2")
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1605559424843-9e4c228f0f2f", use_column_width=True)
        st.subheader("Premium Black Edition")
        st.write("Preis: 349€")
        st.button("Anfragen", key="f3")
        st.markdown('</div>', unsafe_allow_html=True)

# ---------------- REIFEN ----------------
elif selected == "Reifen":
    st.title("Unsere Reifen")

    st.write("Sommerreifen, Winterreifen & Ganzjahresreifen verfügbar.")

    st.table({
        "Modell": ["Sommer Pro X", "Winter Grip 5", "AllSeason Max"],
        "Größe": ["225/40 R18", "205/55 R16", "235/45 R17"],
        "Preis": ["120€", "110€", "130€"]
    })

# ---------------- ÜBER UNS ----------------
elif selected == "Über uns":
    st.title("Über unsere Garage")

    st.write("""
    Wir sind ein deutsches Unternehmen mit Leidenschaft für Fahrzeuge.
    Seit über 10 Jahren bieten wir hochwertige Felgen und Reifen für
    alle Fahrzeugtypen an.
    
    Unser Ziel: Qualität und Kundenzufriedenheit.
    """)

# ---------------- KONTAKT ----------------
elif selected == "Kontakt":
    st.title("Kontaktieren Sie uns")

    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("E-Mail")
        message = st.text_area("Nachricht")
        submitted = st.form_submit_button("Senden")

        if submitted:
            st.success("Vielen Dank! Wir melden uns schnellstmöglich.")

