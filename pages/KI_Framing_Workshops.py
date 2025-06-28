

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
/* ---------- HERO ---------- */
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
    <h1>KI-Framing Workshops</h1>
    <p>Wie muss KI kommunizieren, um akzeptiert zu werden? Narrative & Tonalitätsdesign.</p>
</div>
""", unsafe_allow_html=True)

# --- Catchfrase / Vorstellung ---
st.markdown("""
<div class="catchfrase">
    <h3>Akzeptanz beginnt mit Sprache. Und Haltung.</h3>
    <p>Im Zeitalter der Künstlichen Intelligenz reicht es nicht aus, Systeme technisch zu integrieren – sie müssen verstanden, gefühlt und akzeptiert werden.<p>
    <p>Der Schlüssel liegt in der Art der Kommunikation.<p>
</div>
""", unsafe_allow_html=True)

# --- Divider ---
st.markdown('<div class="divider"><span>Entwicklung akzeptanzfördernder Narrative</span></div>', unsafe_allow_html=True)

st.markdown("""
Narrative formen unser Denken. Sie definieren, wie wir Technologie sehen – als Bedrohung oder Chance, als Werkzeug oder als Partner. In unseren Workshops helfen wir Ihnen, zielgruppenspezifische Geschichten zu entwickeln, die Vertrauen schaffen:

- Welche Werte und Bilder verknüpfen Ihre Mitarbeitenden mit KI?

- Welche Geschichten lösen Widerstand aus – welche öffnen Perspektiven?

- Wie kann KI als unterstützender Begleiter statt als Kontrollinstanz erscheinen?

📌 Wir entwickeln mit Ihnen organisationsspezifische Narrative, die emotional andocken, Ängste entkräften und ein gemeinsames Zukunftsbild transportieren.

""")

# --- Divider ---
st.markdown('<div class="divider"><span>Gestaltung emotionaler Tonalitäten</span></div>', unsafe_allow_html=True)

st.markdown("""
Kommunikation mit KI ist mehr als Inhalt – sie ist Stimmung, Stimme und Zwischenraum.
Wir untersuchen mit Ihnen:

- Welche Tonalität passt zu Ihrer Kultur? Förmlich, kollegial, inspirierend?

- Wie spricht KI mit Führungskräften vs. operativen Teams?

- Welche Worte fördern Autonomie, welche erzeugen Reaktanz?

Mithilfe von Tonalitätsprototypen und Sprachstil-Simulationen arbeiten wir an einem Stil, der Vertrauen schafft – ohne Künstlichkeit, ohne Entfremdung.

📣 Ergebnis: Eine Tonalität, die KI greifbar macht – und Ihre Organisation darin wiedererkennbar lässt.
""")

# --- Divider ---
st.markdown('<div class="divider"><span>Abgrenzung zu zwischenmenschlicher Kommunikation</span></div>', unsafe_allow_html=True)

st.markdown("""
KI darf nicht vorgeben, menschlich zu sein – sie muss einen eigenen Kommunikationsraum erhalten: transparent, unterstützend, aber niemals vermenschlichend.

In unseren Workshops klären wir gemeinsam:

- Wo verläuft die Grenze zwischen Authentizität und Täuschung?

- Wie kann KI klar und wertschätzend kommunizieren – ohne Empathie zu imitieren?

- Wann hilft es, der KI eine „Stimme“ zu geben – und wann nicht?

🧩 Ziel ist eine klare Rollendefinition der KI als Dialogpartnerin, deren Kommunikation strukturiert, aber nicht emotional übergriffig ist.
""")

# --- Footer ---
st.markdown('<footer style="margin-top: 5rem; text-align: center; font-size: 0.9rem; color: #888;">&copy; 2025 Aicura Consulting – DSGVO-konform · Impressum · Datenschutz</footer>', unsafe_allow_html=True)

