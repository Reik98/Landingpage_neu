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
/* ---------- HERO ---------- */
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
    }
    .hero-about p {
        font-size: 0.9rem;
        margin-top: 0rem;
        margin-bottom: 3rem;
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
    <h1> </h1>
    <p>Bewertung klassischer OE-Modelle wie Luhmann, Kotter oder Senge in Bezug auf KI-Fähigkeit.</p>
</div>
""", unsafe_allow_html=True)

# --- Catchfrase / Vorstellung ---
st.markdown("""
<div class="catchfrase">
    <h3>Können Ihre bisherigen Denkmodelle den Wandel mit KI wirklich tragen?</h3>
    <p>Künstliche Intelligenz verändert nicht nur Tools – sie verändert die Logik von Organisationen.<p>
    <p>Was gestern noch als Best Practice galt, ist heute vielleicht hinderlich.<p>
    <p>Mit unserer Paradigmenanalyse überprüfen wir, ob Ihre organisationale Veränderungslogik dem Zeitalter der KI gewachsen ist – und helfen Ihnen, blinde Flecken zu erkennen und neue Wege zu denken.<p>
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
