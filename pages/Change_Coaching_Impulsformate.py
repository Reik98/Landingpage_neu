
import streamlit as st
from shared.header import show_header  # Gemeinsamer Header

st.set_page_config(
    page_title="Aicura – Change-Coaching_Impulsformate",
    layout="wide",
    initial_sidebar_state="collapsed"
)

show_header()

# --- Hero-Bild: https://lacobe.de/wp-content/uploads/2019/06/Coaching-Beratung.jpg---
st.markdown("""
<style>
/* ---------- HERO ---------- */
.hero-about {
    position: relative;
    width: 100%;
    height: 700px;
    background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)),
                      url('https://raw.githubusercontent.com/Reik98/Landingpage/main/Coaching.jpg');
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
    <h1>Change-Coaching & Impulsformate</h1>
    <p>Begleitung Ihrer Führungskräfte beim Wandel zur KI-kompatiblen Unternehmenskultur.</p>
</div>
""", unsafe_allow_html=True)

# --- Catchfrase / Vorstellung ---
st.markdown("""
<div class="catchfrase">
    <h3>Führung neu denken – im Dialog mit der Künstlichen Intelligenz.</h3>
    <p>Künstliche Intelligenz verändert nicht nur Tools und Prozesse – sie fordert eine neue Haltung in der Führung.
    <p>Wie führt man Teams, in denen Maschinen mitdenken?<p>
    <p>Wie bleibt man handlungsfähig in einem Umfeld, das sich täglich wandelt?<p>
    <p>Unsere Formate geben Orientierung, schaffen Reflexionsräume und begleiten Führungskräfte dabei, den Wandel nicht nur zu managen, sondern zu gestalten.<p>
</div>
""", unsafe_allow_html=True)

# --- Divider ---
st.markdown('<div class="divider"><span>„KI verändert Führung“ – Impulsvortrag</span></div>', unsafe_allow_html=True)

st.markdown("""
Ein provokanter, inspirierender Einstieg in das Thema:

- Warum klassische Führungslogiken (Planung, Kontrolle, Hierarchie) an Grenzen stoßen

- Welche neuen Anforderungen KI an Leadership stellt (z. B. Kontextsensibilität, Datenethik, Vertrauen in emergente Prozesse)

- Welche Haltung heute zukunftsfähig macht: Orientierung statt Ansage, Verantwortung statt Kontrolle, Dialog statt Durchgriff

Der Vortrag verbindet Forschung, Praxis und persönliche Geschichten – perfekt für interne Veranstaltungen, Strategieklausuren oder Leadership-Days.

""")

# --- Divider ---
st.markdown('<div class="divider"><span>„Systemisches Denken im Zeitalter von KI“ – Teamworkshop</span></div>', unsafe_allow_html=True)

st.markdown("""
„Nicht die stärkste Organisation überlebt, sondern die anpassungsfähigste.“

In diesem Workshop erleben Teams, wie systemisches Denken hilft, KI nicht nur technisch, sondern auch kulturell zu integrieren.

Inhalte & Übungen:

- Eigene Muster erkennen: Wie reagiert unsere Organisation auf Wandel?

- Umgang mit Komplexität & Nichtwissen (statt Scheinlösungen und Aktionismus)

- Resonanz mit Maschinen? – Wie Systeme kommunizieren, beobachten und lernen

- Entwicklung eines systemischen Blicks auf Führung, Rolle, Verantwortung

Der Workshop schafft ein gemeinsames Verständnis und legt die Grundlage für weitere Veränderungsschritte.


""")

# --- Divider ---
st.markdown('<div class="divider"><span>„Framing & Narrative für KI-Kommunikation“ – Kommunikationsstrategie</span></div>', unsafe_allow_html=True)

st.markdown("""
Technische Systeme brauchen kulturelle Erzählungen.
Akzeptanz entsteht nicht durch Technik – sondern durch Bedeutung.

In diesem Modul arbeiten wir gemeinsam mit Führungskräften und Kommunikator:innen an einer narrativen Strategie, die KI sinnvoll in die Organisation integriert:

- Welche Erzählungen über KI existieren bereits im Unternehmen?

- Welche Ängste, Hoffnungen oder Widerstände sind daran geknüpft?

- Wie gestalten wir ein Narrativ, das Vertrauen, Sinn und Orientierung gibt?

- Wie differenzieren wir zwischen interner Kommunikation, Employer Branding und Stakeholder-Ansprache?

Das Ergebnis: Eine klare, authentische Tonalität für Ihre KI-Initiativen – getragen von Ihren Führungskräften.
""")

# --- Footer ---
st.markdown('<footer style="margin-top: 5rem; text-align: center; font-size: 0.9rem; color: #888;">&copy; 2025 Aicura Consulting – DSGVO-konform · Impressum · Datenschutz</footer>', unsafe_allow_html=True)
