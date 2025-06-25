import streamlit as st
from shared.header import show_header  # Gemeinsamer Header

st.set_page_config(
    page_title="Aicura – Paradigmenanalyse",
    layout="wide",
    initial_sidebar_state="collapsed"
)

show_header()

# --- Hero-Bild: https://www.immo-invest.ch/paradigmenwechsel-in-der-proptech-welt/---
st.markdown("""
<style>
.hero-about {
    position: relative;
    width: 100%;
    height: 700px;
    background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)),
    url('https://raw.githubusercontent.com/Reik98/Landingpage/main/Paradigmawechsel.jpg');
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: white;
    text-align: center;
    text-shadow: 0 0 10px rgba(0,0,0,0.6);
}
.hero-about h1 {
    font-size: 3rem;
    margin-bottom: 0.5rem;
}
.hero-about p {
    font-size: 1.3rem;
    margin-top: 5.5rem;
}
</style>
<div class="hero-about">
    <h1> </h1>
    <p>Bewertung klassischer OE-Modelle wie Luhmann, Kotter oder Senge in Bezug auf KI-Fähigkeit.</p>
</div>
""", unsafe_allow_html=True)

# --- Catchfrase / Vorstellung ---
st.markdown("""
<div class="catchfrase">
    <h3>Seite im Aufbau</h3>
    <p>Weitere Inhalte folgen.</p>
</div>
""", unsafe_allow_html=True)


st.markdown("""
### Analyse Ihrer besteheneden Veränderungslogik

- Passt sich Ihr Unternehmen kontinuierlich an interne und externe Veränderungen / Herausforderungen an?
- Ist Ihre Organisation ein lebendiges / dynamisches System - Nachhaltige Verbesserung des Verhaltens von Mitarbeitenden, Strukturen und Prozesse
- Wie sieht der geplante langfristige Veränderungsprozess Ihrer Organisation aus?

""")

# Bewertung aktueller Modelle auf Zukunftstauglichkeit
st.markdown("""
### Bewertung aktueller Modelle auf Zukunftstauglichkeit

Unsere Organisationsentwickler:innen haben in einer groß angelegten Studie Modelle zur Organisationsentwicklung bezüglich Ihrer Tauglichkeit einer KI-Integration untersucht.

Wir helfen Ihnen dabei, das richtige Modell zu finden und Ihre Organisation auf ein neues Level zu heben!
""")

# --- Teamvorstellung ---
st.markdown("""
### Drittens

...
""")

# --- Footer ---
st.markdown('<footer style="margin-top: 5rem; text-align: center; font-size: 0.9rem; color: #888;">&copy; 2025 Aicura Consulting – DSGVO-konform · Impressum · Datenschutz</footer>', unsafe_allow_html=True)
