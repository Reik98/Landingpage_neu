



import streamlit as st
from shared.header import show_header  # Gemeinsamer Header

st.set_page_config(
    page_title="Aicura – Prototypische_Teams",
    layout="wide",
    initial_sidebar_state="collapsed"
)

show_header()

# --- Hero-Bild: https://www.studio-gong.de/blog/wp-content/uploads/2025/03/Beitragsbild_Vermeide-diese-7-Fehler-KI.jpg---
st.markdown("""
<style>
/* ---------- HERO ---------- */
.hero-about {
    position: relative;
    width: 100%;
    height: 700px;
    background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)),
                      url('https://raw.githubusercontent.com/Reik98/Landingpage/main/Prototyp.jpg');
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
    margin-top: 2.0rem;
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
        margin-top: 1rem;
    }
    .hero-about h1 {
        font-size: 1.3rem;
        margin-bottom: 0rem;
        margin-top: 0rem;
    }
    .hero-about p {
        font-size: 0.9rem;
        margin-top: 0rem;
        margin-bottom: 0rem;
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
    <h1>Prototypische Teams</h1>
    <p>Begleitung von Pilotteams mit echten KI-Agenten im Arbeitsalltag.</p>
</div>
""", unsafe_allow_html=True)

# --- Catchfrase / Vorstellung ---
st.markdown("""
<div class="catchfrase">
    <h3>KI nicht nur testen – sondern erleben. Im echten Alltag.</h3>
    <p>Der kulturelle Wandel gelingt nicht im Labor.<p>
    <p>Er gelingt in der echten Arbeit mit echten Teams – dort, wo KI auf Prozesse, Rollen, Verantwortung und Kommunikation trifft.<p>
    <p>Mit unseren „Prototypischen Teams“ begleiten wir Organisationen auf dem Weg zu echter Integration: nicht als Tool-Rollout, sondern als kulturelles Experiment mit Haltung.<p>
</div>
""", unsafe_allow_html=True)

# --- Divider ---
st.markdown('<div class="divider"><span>Identifikation geeigneter Pilotbereiche</span></div>', unsafe_allow_html=True)

st.markdown("""
Bevor ein KI-Agent sinnvoll eingeführt werden kann, identifizieren wir mit Ihnen gemeinsam:

- Arbeitsbereiche mit hohem Potenzial für KI-Integration (z. B. datengetriebene Prozesse, repetitive Aufgaben, Entscheidungsunterstützung)

- Teams mit der nötigen Offenheit und Stabilität, um Veränderungen nicht nur zu tragen, sondern aktiv zu gestalten

- Führungskräfte, die als Kultur-Multiplikatoren agieren können

Ziel: Ein Pilotbereich, der technisch geeignet, kulturell offen und strategisch relevant ist.

""")

# --- Divider ---
st.markdown('<div class="divider"><span>Begleitung interdisziplinärer Teams</span></div>', unsafe_allow_html=True)

st.markdown("""
Sobald das Pilotszenario definiert ist, startet die eigentliche Arbeit:

- Co-Creation der Zielsetzung: Was soll der KI-Agent leisten – und was nicht?

- Definition der Mensch-KI-Interaktion: Welche Rolle übernimmt der Agent im Team? Welche Verantwortung bleibt beim Menschen?

- Lernschleifen & Reflexion: In regelmäßigen Sessions reflektieren wir mit dem Team ihre Erfahrungen – technisch, emotional und strukturell.

- Begleitendes Coaching für Führung & Teammitglieder zur Navigation durch Unsicherheit, Erwartungen & Rollenverschiebung

Dabei stehen nicht nur technische Kennzahlen im Fokus, sondern vor allem: Kultur, Akzeptanz und emergente Dynamiken.


""")

# --- Divider ---
st.markdown('<div class="divider"><span>Evaluation von Akzeptanz & kulturellem Impact</span></div>', unsafe_allow_html=True)

st.markdown("""
Am Ende des Pilotprojekts steht nicht nur ein Erfahrungsbericht, sondern ein kulturelles Lernmomentum.

Wir evaluieren:

- Wie wurde die KI akzeptiert? (z. B. Vertrauen, Nutzung, Rollenklärung)

- Welche Muster im Umgang mit der KI haben sich gebildet?

- Welche kulturellen Spannungen wurden sichtbar?

- Welche Narrative über die KI haben sich im Team entwickelt?

- Welche systemischen Auswirkungen zeigten sich über das Team hinaus?

Ergebnis: Eine tiefe, qualitative Einsicht, wie KI in Ihrer Organisation wirkt – als Kulturveränderer, nicht nur als Tool.

""")

# --- Footer ---
st.markdown('<footer style="margin-top: 5rem; text-align: center; font-size: 0.9rem; color: #888;">&copy; 2025 Aicura Consulting – DSGVO-konform · Impressum · Datenschutz</footer>', unsafe_allow_html=True)

