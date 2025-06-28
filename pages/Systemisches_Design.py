


import streamlit as st
from shared.header import show_header  # Gemeinsamer Header

st.set_page_config(
    page_title="Aicura – Systemisches_Design",
    layout="wide",
    initial_sidebar_state="collapsed"
)

show_header()

# --- Hero-Bild: https://www.iis.fraunhofer.de/de/ff/lv/net/jcr:content/stage/stageParsys/stage_slide/image.img.png/1643987344631/20211018-Vernetzung-AdobeStock-285478116-v4-WEB.png---
st.markdown("""
<style>
/* ---------- HERO ---------- */
.hero-about {
    position: relative;
    width: 100%;
    height: 700px;
    background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)),
                      url('https://raw.githubusercontent.com/Reik98/Landingpage/main/Systemdesign_1.png');
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

/* ---------- TEXT ---------- */
.hero-about h1 {
    font-size: 3rem;
    margin-bottom: 0.5rem;
}
.hero-about p {
    font-size: 1.3rem;
    margin-top: 5.5rem;
}

/* ---------- DIVIDER ---------- */
.divider {
            display: flex; flex-wrap: nowrap; align-items: center; text-align: center;
            margin: 2rem 0;
        }
        .divider::before, .divider::after {
            content: ''; flex: 1; border-bottom: 2.5px solid #008B92;
        }
        .divider:not(:empty)::before { margin-right: 0.75em; }
        .divider:not(:empty)::after { margin-left: 0.75em; }
        .divider span {
            color: #444; font-weight: 600; font-size: 2.5rem;
        }



/* ---------- CATCHFRASE ---------- */
.catchfrase {
    background-color: #ffffff;
    padding: 2rem;
    margin-top: 2rem;
    text-align: center;
    border-radius: 12px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
}

/* ---------- DARKMODE ---------- */
@media (prefers-color-scheme: dark) {
    body {
        background-color: #121212;
        color: #ffffff;
    }
    .catchfrase {
        background-color: #1f1f1f;
        color: #ffffff;
        box-shadow: 0 2px 6px rgba(0,0,0,0.4);
    }
.divider span {
        color: #ffffff !important;
    }
    .divider::before,
    .divider::after {
        border-bottom: 2.5px solid #fddb3a !important;
    }

    .hero-about {
        text-shadow: none;
    }
    h1, h2, h3, h4 {
        color: #00c6d2;
    }
    footer {
        color: #aaa;
    }
}

/* ---------- MEDIA QUERY ---------- */
@media (max-width: 768px) {
    .hero-about {
        height: auto;
        aspect-ratio: 3 / 2;
        padding: 6rem 1rem 2rem 1rem;
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
    }
    .hero-about h1 {
        font-size: 1.3rem;
        margin-bottom: 0rem;
        margin-top: 0rem;
    }
    .hero-about p {
        font-size: 0.9rem;
        margin-top: 0rem;
        margin-bottom: 1rem;
    }
    .catchfrase {
        padding: 1.2rem;
    }
    .catchfrase h3 {
        font-size: 1.5rem;
    }
    .catchfrase p {
        font-size: 1rem;
    }
.divider {
    flex-direction: row;
    margin: 1.5rem 0;
}

.divider::before,
.divider::after {
    border-bottom: 2.5px solid #008B92;  /* etwas dünner auf Mobil */
}

.divider:not(:empty)::before {
    margin-right: 0.0em;
}

.divider:not(:empty)::after {
    margin-left: 0.0em;
}

.divider span {
    font-size: 1.3rem;  /* 👈 kleiner auf Mobil */
    font-weight: 600;
    line-height: 1.2;
    display: inline-block;
    max-width: 90%;
}

    footer {
        font-size: 0.8rem;
        padding: 1rem;
    }
    h1, h2, h3, h4 {
        font-size: 1.4rem;
    }
    p, li {
        font-size: 1rem;
        line-height: 1.6;
    }
}
</style>
<div class="hero-about">
    <h1>Systemisches Design</h1>
    <p>Neuausrichtung systemischer Ansätze im Zusammenspiel mit lernenden Maschinen.</p>
</div>
""", unsafe_allow_html=True)

# --- Catchfrase / Vorstellung ---
st.markdown("""
<div class="catchfrase">
    <h3>Organisationen als lebendige Systeme neu denken – mit und für KI.</h3>
    <p>Künstliche Intelligenz verändert nicht nur Prozesse, sondern das Fundament, auf dem Organisationen funktionieren: Kommunikation, Steuerung, Beziehung.<p>
    <p>Systemisches Design betrachtet Organisationen nicht als Maschinen, sondern als dynamische Netzwerke – und genau hier setzt unser Ansatz an.<p>
</div>
""", unsafe_allow_html=True)

# --- Divider ---
st.markdown('<div class="divider"><span>Analyse und Weiterentwicklung systemischer Logiken</span></div>', unsafe_allow_html=True)

st.markdown("""
Wie „funktioniert“ Ihre Organisation – im Inneren?
Wir analysieren, welche systemischen Prinzipien heute Ihre Zusammenarbeit, Entscheidungswege und Kommunikation prägen. Dabei gehen wir Fragen nach wie:

- Welche impliziten Regeln steuern Verhalten?

- Wie zirkulär oder linear verlaufen Entscheidungsprozesse?

- Wie wird Wissen geteilt – explizit, implizit, selektiv?

- Wo entstehen Muster, Schleifen, blinde Flecken?

Gemeinsam identifizieren wir systemische Engpässe, die den produktiven Umgang mit KI behindern – und entwickeln neue Denk- und Handlungsmuster, die auf Verknüpfung statt Kontrolle, Wirkung statt Anweisung, und Selbstorganisation statt Top-Down setzen.

""")

# --- Divider ---
st.markdown('<div class="divider"><span>Übersetzung auf lernende Maschinen</span></div>', unsafe_allow_html=True)

st.markdown("""
Systemisches Denken endet nicht beim Menschen – es bezieht KI als Akteur ein.

Wir helfen Ihnen, systemische Prinzipien auf KI zu übertragen, z. B.:

- Welche Beobachtungslogiken muss KI abbilden können?

- Wie können Feedbackschleifen mit KI sinnvoll gestaltet werden?

- Welche „Bedeutung“ erhalten Daten im sozialen Kontext?

- Wie differenziert eine Organisation zwischen menschlicher und maschineller Kommunikation?

Durch diese Übersetzung wird KI nicht als Fremdkörper erlebt, sondern als Teil des organisationalen Systems – mit klaren Rollen und wirksamer Anschlussfähigkeit.
""")

# --- Divider ---
st.markdown('<div class="divider"><span>Design neuer Interaktionsmuster mit KI</span></div>', unsafe_allow_html=True)

st.markdown("""
Veränderung beginnt nicht bei der Technologie, sondern bei der Beziehung zur Technologie.

Wir gestalten mit Ihnen neue Interaktionsmuster, in denen KI als kollegiale Ressource wirkt – z. B.:

- Welche Aufgaben übernimmt KI – und wie werden sie übergeben?

- Wie sehen dialogische Schnittstellen aus, die Vertrauen schaffen?

- Wie verändert sich die Teamdynamik, wenn KI mitarbeitet?

- Welche Regeln und Rituale unterstützen produktives Mensch-KI-Zusammenspiel?

Dazu entwickeln wir Prototypen, testen sie in Pilot-Settings und begleiten ihre kulturelle Integration.
""")

# --- Footer ---
st.markdown('<footer style="margin-top: 5rem; text-align: center; font-size: 0.9rem; color: #888;">&copy; 2025 Aicura Consulting – DSGVO-konform · Impressum · Datenschutz</footer>', unsafe_allow_html=True)

