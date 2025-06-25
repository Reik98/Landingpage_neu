

import streamlit as st
from shared.header import show_header  # Gemeinsamer Header

st.set_page_config(
    page_title="Aicura – KI_Framing_Workshops",
    layout="wide",
    initial_sidebar_state="collapsed"
)

show_header()

# --- Hero-Bild: https://www.fuer-gruender.de/fileadmin/blog/fal/106134.jpg---
st.markdown("""
<style>
.hero-about {
    position: relative;
    width: 100%;
    height: 700px;
    background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)),
    url('https://raw.githubusercontent.com/Reik98/Landingpage/main/Workshop.jpg');
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
    margin-bottom: 5.5rem;
}
.hero-about p {
    font-size: 1.3rem;
    margin-bottom: 2.5rem;
}
</style>
<div class="hero-about">
    <h1>KI-Framing Workshops</h1>
    <p>Wie muss KI kommunizieren, um akzeptiert zu werden? Narrative & Tonalitätsdesign.</p>
</div>
""", unsafe_allow_html=True)

# --- Catchfrase / Vorstellung ---
st.markdown("""
<div class="catchfrase">
    <h3>Akzeptanz beginnt mit Sprache. Und Haltung.</h3>
    <h1>Im Zeitalter der Künstlichen Intelligenz reicht es nicht aus, Systeme technisch zu integrieren – sie müssen verstanden, gefühlt und akzeptiert werden.<h1>
    <h1>Der Schlüssel liegt in der Art der Kommunikation.<h1>
</div>
""", unsafe_allow_html=True)

# --- Divider ---
st.markdown('<div class="divider"><span>Analyse Ihrer bestehenden Veränderungslogik</span></div>', unsafe_allow_html=True)

st.markdown("""
Viele Organisationen setzen nach wie vor auf klassische Methoden zur Steuerung von Wandel – häufig inspiriert von linearen Modellen wie denen von Kotter, Senge oder Luhmann. Doch die Frage ist nicht, ob sich Ihre Organisation verändert, sondern wie.

In unserem Analysemodul untersuchen wir u. a.:

- Anpassungsfähigkeit: Wie kontinuierlich und proaktiv reagiert Ihre Organisation auf interne und externe Veränderungen? Wird Wandel als Projekt verstanden – oder als integraler Teil des Systems?

- Systemisches Verhalten: Wird Ihre Organisation als lebendiges, lernendes System betrachtet, das auf neue Impulse adaptiv reagiert? Oder überwiegen starre Strukturen, klare Hierarchien und festgelegte Rollen?

- Veränderungsstrategie: Gibt es einen langfristig gedachten Change-Fahrplan, der auf Selbststeuerung, Mitarbeiterpartizipation und iteratives Lernen setzt?

👉 Ziel: Wir machen sichtbar, wie reif, anschlussfähig und anpassungsfähig Ihre aktuelle Veränderungslogik im Kontext von KI tatsächlich ist.

""")

# --- Divider ---
st.markdown('<div class="divider"><span>Bewertung aktueller Modelle auf Zukunftstauglichkeit</span></div>', unsafe_allow_html=True)

st.markdown("""
Unsere Organisationsentwickler:innen haben in einer interdisziplinären Studie klassische OE-Modelle systematisch auf ihre Tauglichkeit für eine KI-getriebene Zukunft hin untersucht. Dabei wurden unter anderem folgende Fragen betrachtet:

- Unterstützt das Modell dynamisches Lernen und Selbstorganisation?

- Fördert es interdisziplinäre Zusammenarbeit und mensch-maschinelle Rollenvielfalt?

- Wie flexibel ist es in Bezug auf komplexe, datengetriebene Umwelten?

Die Erkenntnis: Viele Modelle bieten weiterhin wertvolle Impulse – aber nur in Kombination mit systemischen, iterativen und KI-kompatiblen Denkweisen sind sie wirklich zukunftsfähig.

🔧 Gemeinsam mit Ihnen wählen wir das passende Modell oder kombinieren mehrere Denkansätze zu einer maßgeschneiderten Transformationslogik für Ihre Organisation.
""")

# --- Divider ---
st.markdown('<div class="divider"><span>Team-Workshop zur kollektiven Reflexion</span></div>', unsafe_allow_html=True)

st.markdown("""
Veränderung beginnt nicht auf dem Papier, sondern in den Köpfen. Deshalb integrieren wir einen Team-Workshop, der Ihre Führungskräfte und Schlüsselpersonen aktiviert:

- Reflexion über bestehende Paradigmen und ihre Wirkung

- Austausch über gewünschte Zukunftsbilder und kollektive Werte

- Bewertung interner Spannungsfelder & Chancen im Umgang mit KI

- Entwicklung erster Hypothesen für ein neues Veränderungsnarrativ

📌 Ergebnis: Ein geteiltes Verständnis darüber, was Veränderung in Ihrer Organisation bedeutet – heute, morgen und im Zeitalter von KI.
""")

# --- Footer ---
st.markdown('<footer style="margin-top: 5rem; text-align: center; font-size: 0.9rem; color: #888;">&copy; 2025 Aicura Consulting – DSGVO-konform · Impressum · Datenschutz</footer>', unsafe_allow_html=True)

