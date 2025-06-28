
import streamlit as st
from shared.header import show_header  # Gemeinsamer Header

st.set_page_config(
    page_title="Aicura – Kulturdiagnostik_Integrationsstrategie",
    layout="wide",
    initial_sidebar_state="collapsed"
)

show_header()

# --- Hero-Bild: https://www.engagement-in-der-kultur.de/wp-content/uploads/EidK_Homepage_Kultur_Angebote_Bild.jpg---
st.markdown("""
<style>
/* ---------- HERO ---------- */
.hero-about {
    position: relative;
    width: 100%;
    height: 700px;
    background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)),
                      url('https://raw.githubusercontent.com/Reik98/Landingpage/main/Kultur.jpg');
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
            content: ''; flex: 1; border-bottom: 2px solid #fddb3a;
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
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
    }
    .hero-about h1 {
        font-size: 2rem;
        margin-bottom: 1rem;
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
    border-bottom: 1.5px solid #fddb3a;  /* etwas dünner auf Mobil */
}

.divider:not(:empty)::before {
    margin-right: 0.5em;
}

.divider:not(:empty)::after {
    margin-left: 0.5em;
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
    <h1>Kulturdiagnostik & Integrationsstrategie</h1>
    <p>Tool-gestützte Analyse Ihrer aktuellen kulturellen Reife zur Integration von KI.</p>
</div>
""", unsafe_allow_html=True)

# --- Catchfrase / Vorstellung ---
st.markdown("""
<div class="catchfrase">
    <h3>Künstliche Intelligenz braucht kulturelle Intelligenz.</h3>
    <p>Viele KI-Initiativen scheitern nicht an Technologie – sondern an Haltung, Strukturen und fehlender kultureller Anschlussfähigkeit.<p>
    <p>Mit unserem Ansatz identifizieren wir kulturelle Reifegrade und machen Ihre Organisation fit für echte Transformation.<p>
</div>
""", unsafe_allow_html=True)

# --- Divider ---
st.markdown('<div class="divider"><span>Tool-gestützte Ist-Erhebung kultureller Reife</span></div>', unsafe_allow_html=True)

st.markdown("""
Unsere eigens entwickelten Diagnoseinstrumente messen, wie offen Ihre Organisation für den produktiven Einsatz von KI ist – kulturell, strukturell und kommunikativ.

Dabei analysieren wir unter anderem:

- Wie werden Entscheidungen getroffen – datenbasiert oder erfahrungsgetrieben?

- Wie hoch ist das Vertrauen in technologische Systeme im Alltag?

- Welche Narrative, Werte und Grundhaltungen prägen die Zusammenarbeit?

- Wie adaptiv ist Ihre Organisation bei Veränderungen?

🔍 Mithilfe von standardisierten Fragebögen, kulturellen Metriken und qualitativen Interviews erhalten Sie ein klares Bild über Ihre KI-Kultur – nicht als Zustand, sondern als Entwicklungspotenzial.

""")

# --- Divider ---
st.markdown('<div class="divider"><span>Entwicklung von Rollenmodellen für „KI im Team“</span></div>', unsafe_allow_html=True)

st.markdown("""
KI verändert nicht nur Prozesse – sie verändert Beziehungen und Rollen.

Wir entwickeln mit Ihnen konkrete Rollenmodelle, die beschreiben:

- Wie und wo KI im Team eingebunden wird (Assistenz, Entscheidungsvorbereitung, Automatisierung)

- Welche Verantwortung beim Menschen bleibt – und welche nicht

- Wie Führung neu gedacht werden muss, wenn Maschinen mitdenken

Dabei stehen Transparenz, Akzeptanz und psychologische Sicherheit im Vordergrund: Wer KI versteht, vertraut ihr auch.

📌 Ergebnis ist ein Modell, das Mensch und Maschine als komplementäre Partner positioniert – nicht als Konkurrenten.
""")

# --- Divider ---
st.markdown('<div class="divider"><span>Integrationsstrategie inkl. kulturellem Re-Design</span></div>', unsafe_allow_html=True)

st.markdown("""
Basierend auf Ihrer Ausgangslage entwickeln wir eine passgenaue Strategie zur kulturellen Integration von KI. Diese umfasst:

- Kulturelle Entwicklungsfelder & Wachstumsachsen

- Empfehlungen für konkrete Maßnahmen (z. B. Kommunikationsinitiativen, Führungskräftetrainings, Rituale)

- Change-Kommunikation, die Haltung und Richtung gibt

- Architekturen für Pilotprojekte & prototypische Teams

Zusätzlich gestalten wir ein kulturelles Re-Design, das nicht bei Werten und Postern endet, sondern sich in Verhalten, Systemlogiken und Entscheidungsstrukturen niederschlägt.
""")


# --- Footer ---
st.markdown('<footer style="margin-top: 5rem; text-align: center; font-size: 0.9rem; color: #888;">&copy; 2025 Aicura Consulting – DSGVO-konform · Impressum · Datenschutz</footer>', unsafe_allow_html=True)
