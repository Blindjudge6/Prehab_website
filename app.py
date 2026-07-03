import os

import streamlit as st

st.set_page_config(page_title="Prien Aktiv PreHab", page_icon="🩺", layout="wide")

APP_TITLE = "Prien Aktiv PreHab"
DEFAULT_APP_PASSWORD = "Prien0107!"


def get_configured_password() -> str:
    configured_password = os.environ.get("APP_PASSWORD", "").strip()
    if configured_password:
        return configured_password

    try:
        configured_password = st.secrets.get("APP_PASSWORD", "").strip()
    except Exception:
        configured_password = ""

    if configured_password:
        return configured_password

    return DEFAULT_APP_PASSWORD


def require_password() -> bool:
    configured_password = get_configured_password()
    if not configured_password or configured_password in {"CHANGE_ME", "SET_YOUR_PASSWORD_HERE"}:
        return True

    if st.session_state.get("password_ok", False):
        return True

    st.markdown("<h1 style='font-size:2rem; margin-bottom:0.4rem;'>Prien Aktiv PreHab</h1>", unsafe_allow_html=True)
    st.markdown("Bitte geben Sie das Passwort ein, um die Anwendung zu öffnen.")

    with st.form("password_form"):
        password = st.text_input("Passwort", type="password")
        submitted = st.form_submit_button("Öffnen")

    if submitted:
        if password == configured_password:
            st.session_state.password_ok = True
            st.rerun()
            return True
        st.error("Passwort nicht korrekt.")

    return False


def inject_styles() -> None:
    st.markdown(
        """
        <style>
        :root {
            --bg: #ffffff;
            --card: #f9f9f9;
            --text: #1a1a1a;
            --muted: #666666;
            --line: #e0e0e0;
            --accent: #0066cc;
            --accent-light: #e6f0ff;
        }
        .stApp {
            background: var(--bg) !important;
            color: var(--text);
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Helvetica Neue", sans-serif;
        }
        .stApp p, .stApp span, .stApp li {
            color: var(--text) !important;
        }
        .stMarkdown, .stMarkdown p, .stMarkdown span {
            color: var(--text) !important;
        }
        [data-testid="stSidebar"] {
            background: var(--card) !important;
            border-right: 1px solid var(--line) !important;
        }
        [data-testid="stSidebar"] p, [data-testid="stSidebar"] span {
            color: var(--text) !important;
        }
        .hero-card, .info-card, .role-card {
            background: var(--card);
            border: 1px solid var(--line);
            border-radius: 6px;
            padding: 20px;
            margin-bottom: 16px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.08);
        }
        .hero-card h1, .info-card h2, .role-card h3 {
            margin-top: 0;
            color: var(--accent) !important;
            font-weight: 600;
        }
        .hero-card p, .info-card p, .info-card li, .info-card a {
            color: var(--text) !important;
        }
        .muted {
            color: var(--muted) !important;
        }
        .pill {
            display: inline-block;
            border-radius: 4px;
            padding: 6px 12px;
            background: var(--accent-light);
            color: var(--accent);
            font-size: 0.85rem;
            font-weight: 500;
            margin-right: 8px;
            margin-bottom: 8px;
            border: 1px solid #ccddff;
        }
        [data-testid="stRadio"] label p,
        [data-testid="stRadio"] label span {
            color: var(--text) !important;
        }
        [data-testid="stCheckbox"] label p,
        [data-testid="stCheckbox"] label span {
            color: var(--text) !important;
        }
        [data-testid="stAlert"] {
            background-color: var(--accent-light) !important;
            border-color: #ccddff !important;
            border-left: 4px solid var(--accent) !important;
        }
        [data-testid="stAlert"] p,
        [data-testid="stAlert"] span,
        [data-testid="stAlert"] div {
            color: var(--text) !important;
        }
        details {
            background-color: var(--card) !important;
            border: 1px solid var(--line) !important;
            border-radius: 6px !important;
            padding: 12px !important;
            margin-bottom: 8px !important;
        }
        summary {
            color: var(--text) !important;
            font-weight: 600 !important;
            cursor: pointer;
        }
        summary:hover {
            color: var(--accent) !important;
        }
        [data-testid="stFormSubmitButton"] button {
            background-color: var(--accent) !important;
            color: white !important;
            border: none !important;
            border-radius: 4px !important;
            font-weight: 600 !important;
        }
        [data-testid="stFormSubmitButton"] button:hover {
            background-color: #0052a3 !important;
        }
        [data-testid="stSidebar"] [data-testid="stRadio"] {
            background-color: var(--bg) !important;
            border: 1px solid var(--line) !important;
            border-radius: 6px !important;
            padding: 12px !important;
        }
        h1 {
            color: var(--accent) !important;
        }
        h2, h3 {
            color: var(--accent) !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_home() -> None:
    st.markdown(
        """
        <div class="hero-card">
            <h1>Prien Aktiv – Ihre Vorbereitung auf die Operation</h1>
            <p class="muted">
                Präoperative Vorbereitung (PreHab) bedeutet, sich gezielt auf Ihre Operation vorzubereiten. 
                Forschungen zeigen: Menschen, die sich gut vorbereiten, haben weniger Komplikationen und genesen schneller.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("""
    ## Was ist Prä-Rehabilitation (PreHab)?

    PreHab ist ein strukturiertes Programm **vor Ihrer Operation**, um Ihre körperliche und mentale Fitness zu verbessern. 
    Dies hilft Ihnen, die Operation besser zu bewältigen und schneller wieder in Ihren Alltag zurückzukehren.
    """)

    st.markdown(
        """
        <div class="info-card">
            <strong>Die 5 Säulen von PreHab:</strong><br>
            <span class="pill">💪 Bewegung & Kraft</span>
            <span class="pill">🥗 Ernährung</span>
            <span class="pill">🚭 Risikofaktoren</span>
            <span class="pill">📚 Information</span>
            <span class="pill">🧠 Mentale Vorbereitung</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("""
    ## Warum PreHab wirkt
    
    **Wissenschaftliche Evidenz zeigt:**
    - **Weniger Infektionen** – Gute Vorbereitung reduziert Infektionen um bis zu 50%
    - **Weniger Komplikationen** – Gekräftigte Muskeln und bessere Fitness reduzieren Schwellungen und Schmerzen
    - **Schnellere Genesung** – Personen mit PreHab sind durchschnittlich 2-3 Wochen schneller mobil
    - **Bessere Outcomes** – Langfristig bessere Funktion und Beweglichkeit nach der Operation
    """)

    st.markdown(
        """
        <div class="info-card" style="background: var(--accent-light); border-left: 4px solid var(--accent); padding: 14px 16px;">
            <p style="color: #1a1a1a; margin: 0; font-size: 0.95rem;">
                <strong style="color: var(--accent);">💡 Hinweis:</strong> Diese Seite speichert <strong>keine personenbezogenen Daten</strong> dauerhaft. 
                Sie bekommen hier Informationen und einen persönlichen Planungsüberblick – alles dient nur Ihrer Information und Vorbereitung.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("""
    ## Wie funktioniert diese Website?
    
    Diese Seite bietet **drei Bereiche** je nach Ihrer Rolle:
    """)

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="info-card" style="text-align: center;">
            <h3 style="color: var(--accent); margin-top: 0;">👨‍⚕️ Für Hausärzt:innen</h3>
            <p>Evidenzbasierte Empfehlungen zur Optimierung der Vorbereitung vor der OP</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="info-card" style="text-align: center;">
            <h3 style="color: var(--accent); margin-top: 0;">🏥 Für Therapeut:innen</h3>
            <p>Konkrete Trainingsprogramme und Übungsanleitungen für Prehab</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="info-card" style="text-align: center;">
            <h3 style="color: var(--accent); margin-top: 0;">👤 Für Patient:innen</h3>
            <p>Persönliche Checkliste und konkrete Tipps zur Vorbereitung</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("""
    ## Die ideale Timeline
    
    **4-8 Wochen vor der Operation** ist die optimale Zeit für PreHab.
    Je früher Sie beginnen, desto besser der Effekt.
    
    - **Woche 1-2:** Grundlagen: Gespräche, erste Bewegung, Rauchen
    - **Woche 3-5:** Training: Kraft, Ausdauer, Balance
    - **Woche 6-8:** Intensivieren und optimieren
    - **1 Woche vor OP:** Finale Vorbereitung und Entspannung
    """)

    st.markdown(
        """
        <div class="info-card" style="border-top: 3px solid var(--accent); padding: 14px 16px;">
            <strong>Datenschutz:</strong> Diese Seite ist eine Demo-Anwendung ohne Datenspeicherung. 
            Alle Eingaben sind nur lokal im Browser sichtbar. Teilen Sie persönliche Daten (wie Namen, Geburtsdatum) 
            <strong>nicht</strong> auf dieser Seite. Bei Veröffentlichung im echten Betrieb werden vollständige 
            Datenschutzrichtlinien implementiert.
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_hausarzt() -> None:
    st.markdown("<div class='role-card'><h3>Empfehlungen für Hausärzt:innen</h3></div>", unsafe_allow_html=True)
    st.write("""
    Die präoperative Optimierung vor Knie- und Hüftendoprothetik hat sich als wirksam zur Verringerung von Komplikationen und Verbesserung der Genesung erwiesen.
    Folgende medizinisch evidenzbasierte Bereiche sollten angesprochen werden:
    """)

    with st.expander("🚭 Rauchen und Nikotinentwöhnung"):
        st.markdown("""
        **Evidenz:** Rauchen erhöht das Infektionsrisiko um 4-fach, verzögert die Wundheilung und erhöht Komplikationen.
        
        **Empfehlungen:**
        - Rauchstopp mindestens 4 Wochen vor OP anstreben (ideal: 8+ Wochen)
        - Motivationsgespräch und Ressourcen zur Raucherentwöhnung bereitstellen
        - Nikotinersatztherapie erwägen
        - Passivrauchen vermeiden
        - Follow-up in den Wochen vor OP
        
        **Fragen zur Motivation:** Kennt die betroffene Person die Risiken? Ist sie bereit, mit dem Rauchen aufzuhören?
        """)

    with st.expander("⚖️ Gewicht und Adipositas"):
        st.markdown("""
        **Evidenz:** BMI > 30 kg/m² erhöht Komplikationen; sogar kleine Gewichtsreduktionen (5-10%) verbessern Outcomes.
        
        **Empfehlungen:**
        - BMI berechnen und dokumentieren
        - Bei BMI > 30: Überweisung zu Adipositaszentrum oder Ernährungsberatung
        - Realistisches Ziel: 5-10% Gewichtsreduktion vor OP
        - Kombination aus Ernährung und Bewegung
        - Ggf. strukturiertes Gewichtsverlust-Programm
        """)

    with st.expander("🩸 Diabetes und Blutzuckereinstellung"):
        st.markdown("""
        **Evidenz:** Schlecht eingestellter Diabetes (HbA1c > 8%) erhöht Infektionsrisiko und verzögert Wundheilung.
        
        **Empfehlungen:**
        - HbA1c prüfen (Ziel: < 7%, bei OP < 8%)
        - Blutzuckerkontrolle optimieren
        - Medikamentenanpassung mit Diabetologie erwägen
        - Perioperativ engmaschige Überwachung
        - Die betroffene Person über veränderte Einnahmeregeln aufklären
        """)

    with st.expander("💊 Blutdruckkontrolle"):
        st.markdown("""
        **Evidenz:** Unkontrollierter Bluthochdruck erhöht kardiovaskuläre Komplikationen.
        
        **Empfehlungen:**
        - Blutdruck regelmäßig prüfen (Ziel: < 140/90 mmHg)
        - Medikamenteneinstellung überprüfen und ggf. anpassen
        - Salzreduktion und Bewegung empfehlen
        - In den letzten 4 Wochen vor OP regelmäßig kontrollieren
        """)

    with st.expander("🥗 Ernährung und Proteinzufuhr"):
        st.markdown("""
        **Evidenz:** Ausreichende Proteinzufuhr (mindestens 1,2 g/kg KG pro Tag) verbessert Muskelerhalt und Wundheilung.
        
        **Empfehlungen:**
        - Ernährungsstatus prüfen (Körpergewicht, Albumin ggf.)
        - Bei Mangelernährung: Ernährungsberatung vor OP
        - Proteinreiche Ernährung empfehlen (Fleisch, Fisch, Eier, Milchprodukte)
        - Ausreichende Flüssigkeitszufuhr
        - Vitamin D und Calcium sicherstellen
        """)

    with st.expander("🏥 Kardiovaskuläre Optimierung"):
        st.markdown("""
        **Empfehlungen:**
        - Basale kardiovaskuläre Fitness prüfen
        - EKG erwägen (je nach Alter und Risiko)
        - Medikamentöse Anpassung durchsprechen
        - Bewegung vor OP fördern (siehe Physiotherapie-Bereich)
        """)

    with st.expander("💉 Infektionsprävention"):
        st.markdown("""
        **Empfehlungen:**
        - Aktuelle Impfungen prüfen (insbesondere Influenza, Pneumokokken)
        - Zahnhygiene und eventuelle Zahnbehandlungen vorher klären
        - Haut vor OP mit antiseptischem Shampoo reinigen (Octenisan oder Chlorhexidin)
        """)

    st.info("**Hinweis:** Diese Empfehlungen folgen internationalen ERAS-Richtlinien und Cochrane-Evidenz. Individuelle Anpassungen je nach Person sind notwendig.")


def render_physio() -> None:
    st.markdown("<div class='role-card'><h3>Physiotherapie-Anleitungen</h3></div>", unsafe_allow_html=True)
    st.write("""
    Ein wirksames Prä-Habilitationsprogramm basiert auf Evidenz zu Knie- und Hüftendoprothetik. 
    Die Übungen sollten 4-8 Wochen vor der Operation durchgeführt werden.
    """)

    st.markdown("""
    **Trainingsfrequenz:** 3-5x pro Woche  
    **Dauer pro Einheit:** 30-45 Minuten  
    **Intensität:** Symptomgesteuert – kein Schmerz über 4/10 auf der Schmerzskala
    """)

    with st.expander("📋 Aufwärmen (5-10 Minuten)"):
        st.markdown("""
        **1. Gehen oder Radfahren**
        - 5-10 Minuten lockeres Gehen oder Heimtrainer
        - Ziel: Gelenke mobilisieren, Puls erhöhen
        
        **2. Dynamische Hüftmobilisation**
        - Stehen, ein Bein pendeln vor und zurück (10x pro Seite)
        - Seitliches Beinheben (10x pro Seite)
        - Hüftkreisen (8x pro Richtung)
        """)

    with st.expander("💪 Krafttraining (15-20 Minuten)"):
        st.markdown("""
        **Fokus: Quadrizeps, Glutaeus, Hamstrings – diese Muskeln stabilisieren das Gelenk nach OP**
        
        **1. Quadrizeps-Kontraktion im Sitz**
        - Sitz auf Stuhl, Rücken an Lehne
        - Oberschenkelmuskel anspannen und 5-10 Sekunden halten
        - 15-20 Wiederholungen, 2-3 Sätze
        - Fortgeschritten: Mit Gewichtsweste oder Widerstandsband
        
        **2. Sitz-auf-Stand (chair stands)**
        - Stabiler Stuhl ohne Armlehnen
        - Arme gekreuzt oder zur Seite
        - Aufstehen und langsam wieder Hinsetzen
        - 2-3 Sekunden in der Luft halten
        - 10-15 Wiederholungen, 2-3 Sätze
        - Wichtig: Knie nicht über die Zehen hinaus
        
        **3. Bridging (Glutaeus-Kräftigung)**
        - Rückenlage, Füße aufgestellt
        - Becken anheben, Schultern-Hüfte-Knie in einer Linie
        - 2-3 Sekunden oben halten
        - 12-15 Wiederholungen, 2 Sätze
        
        **4. Seitliches Beinheben im Stand**
        - Mit Stuhl zur Unterstützung
        - Ein Bein langsam zur Seite heben (ca. 45°)
        - 2 Sekunden oben halten
        - 12-15 Wiederholungen pro Seite, 2 Sätze
        
        **5. Isometrische Hüftabduktion (liegend)**
        - Seitenlage, Kissen zwischen den Knien
        - Kissen zusammendrücken und 5-10 Sekunden halten
        - 15 Wiederholungen, 2 Sätze
        """)

    with st.expander("⚖️ Balance und Propriozeption (10 Minuten)"):
        st.markdown("""
        **Ziel: Sturzprävention und verbesserte Gelenkkontrolle**
        
        **1. Gewichtsverlagerung**
        - Standhüftbreit
        - Gewicht langsam von links nach rechts verlagern
        - 30-45 Sekunden, ruhig atmen
        
        **2. Einbeinstand (mit Halt)**
        - Mit Stuhl oder Wand zur Unterstützung
        - Ein Bein leicht anheben
        - 20-30 Sekunden halten, dann Seite wechseln
        - 2-3 Sätze pro Seite
        
        **3. Tandemstand**
        - Ein Fuß vor den anderen (Ferse vor Spitze)
        - Mit Stuhl zur Unterstützung
        - 20-30 Sekunden halten
        - Schwierigkeit: Hände loslassen oder Augen schließen
        
        **4. Marschieren auf der Stelle**
        - Gerade Position
        - Knie bis zur Hüfthöhe anheben
        - 30-45 Sekunden
        """)

    with st.expander("🚶 Gehen/Ausdauer (10-15 Minuten)"):
        st.markdown("""
        **Ziel: Kardiorespiratorische Ausdauer und funktionale Mobilität**
        
        **Woche 1-2:** 15-20 Minuten täglich gehen  
        **Woche 3-4:** 25-30 Minuten täglich gehen  
        **Woche 5-8:** 30-45 Minuten 3-5x pro Woche, ggf. mit Steigungen
        
        - Tempo: Sprechen sollte noch möglich sein (ca. 60-70% maximale HR)
        - Indoor (Laufband) oder outdoor
        - Feste Schuhe
        - Bei Schmerz > 4/10 Pause machen
        
        **Zusatz: Treppen steigen** (wenn verfügbar)
        - Langsam und kontrolliert
        - Gleich viele Treppen ab- und aufwärts
        """)

    with st.expander("🫁 Atem- und Entspannungsübungen (5 Minuten)"):
        st.markdown("""
        **1. Tiefe Bauchatmung**
        - Sitz, Rücken entspannt
        - Durch Nase 4 Sekunden einatmen
        - Durch Mund 6 Sekunden ausatmen
        - 10-12 Wiederholungen, 2x täglich
        
        **2. Zwerchfellatemtechnik (für Schmerzkontrolle post-OP)**
        - Diese Atemtechnik sollte vor der OP trainiert werden
        - Liegt in Rückenlage
        - Hand auf Bauch
        - Bewusst in den Bauch atmen
        - 10 Zyklen
        """)

    with st.expander("🔍 Range of Motion Übungen"):
        st.markdown("""
        **Hüfte:**
        - Knie zur Brust ziehen (10x, 2 Sekunden halten)
        - Hüftbeugung in Seitenlage (10x pro Seite)
        - Oberschenkelstreckung (10x)
        
        **Knie:**
        - Kniebeugen mit Stuhl (10-15x)
        - Kniestreckung im Sitz (10x)
        - Fersengang (10x pro Seite)
        """)

    st.success("**Wichtig:** Alle Übungen sollten schmerzarm sein. Bei Schmerzen > 4/10 oder Schwellungen Trainier-Intensität reduzieren und die behandelnde Fachkraft konsultieren.")
    st.info("**Progression:** Übungen können wöchentlich intensiviert werden (Wiederholungen +2-3, Widerstand erhöhen, Pausen verkürzen).")


def render_patient() -> None:
    st.markdown("<div class='role-card'><h3>Ihre persönliche Vorbereitung</h3></div>", unsafe_allow_html=True)
    st.write("""
    Diese Seite hilft Ihnen, sich optimal auf Ihre Operation vorzubereiten. Eine gute Vorbereitung reduziert Komplikationen und beschleunigt die Genesung.
    """)

    st.markdown("<div class='info-card' style='background: var(--accent-light); border: 1px solid #ccddff; padding: 14px 16px;'><p style='color: #1a1a1a; margin: 0; font-size: 0.95rem;'><strong style='color: #0066cc;'>Wie funktioniert diese Seite?</strong><br>Beantworten Sie zuerst die Fragen zu Ihren Risikofaktoren. Dann erhalten Sie eine persönliche Checkliste mit konkreten Aufgaben, die Sie vor der Operation abhaken können.</p></div>", unsafe_allow_html=True)

    with st.form("patient_assessment"):
        st.markdown("**Ihre Situation einschätzen:**")
        smoking = st.radio("Rauchen Sie derzeit?", ["Nein", "Ja, aber ich möchte versuchen aufzuhören", "Ja, und ich plane keine Änderung"], horizontal=False)
        diabetes = st.radio("Haben Sie Diabetes (Zuckerkrankheit)?", ["Nein", "Ja, gut eingestellt", "Ja, aber nicht optimal kontrolliert"], horizontal=False)
        adipositas = st.radio("Wie beschreiben Sie Ihr Gewicht?", ["Normal", "Leicht übergewichtig", "Übergewichtig/Adipositas"], horizontal=False)
        hypertension = st.radio("Haben Sie Bluthochdruck?", ["Nein", "Ja, behandelt und kontrolliert", "Ja, aber nicht optimal kontrolliert"], horizontal=False)
        submitted = st.form_submit_button("Meine Checkliste erstellen")

    if submitted:
        st.session_state.patient_summary = {
            "smoking": smoking,
            "diabetes": diabetes,
            "adipositas": adipositas,
            "hypertension": hypertension,
        }
        st.session_state.patient_summary_ready = True

    if st.session_state.get("patient_summary_ready", False):
        summary = st.session_state.patient_summary
        risks = []
        risk_level = 0

        if "Ja" in summary["smoking"]:
            risks.append("**Rauchen** – Das wichtigste Thema: Rauchstopp reduziert Infektionen um 75%")
            risk_level += 2
        if "nicht optimal" in summary["diabetes"]:
            risks.append("**Diabetes** – Schlechte Einstellung erhöht Infektionsrisiko erheblich")
            risk_level += 2
        elif "Ja" in summary["diabetes"]:
            risks.append("**Diabetes** – Gute Kontrolle ist wichtig, regelmäßige Messungen")
            risk_level += 1
        if summary["adipositas"] in ["Übergewichtig/Adipositas"]:
            risks.append("**Gewicht** – Kleine Gewichtsreduktion (5-10%) hilft schon")
            risk_level += 1
        if "nicht optimal" in summary["hypertension"]:
            risks.append("**Blutdruck** – Sollte vor OP gut eingestellt sein")
            risk_level += 1

        st.markdown("<div class='info-card'><h2>Ihre persönliche Übersicht</h2></div>", unsafe_allow_html=True)
        
        if risks:
            if risk_level >= 3:
                st.warning(f"**Mehrere Risikofaktoren gefunden** – Diese Bereiche sind für Sie besonders wichtig:\n\n" + "\n\n".join(risks))
            else:
                st.info(f"**Optimierungsbereiche gefunden:**\n\n" + "\n\n".join(risks))
        else:
            st.success("✓ Keine der genannten Risikofaktoren markiert. Das ist ein gutes Zeichen!")

        st.markdown("---")

    st.markdown("<div class='info-card'><h2>📋 Ihre Checkliste zur Vorbereitung</h2></div>", unsafe_allow_html=True)
    st.write("Haken Sie die erledigten Punkte ab und nutzen Sie diese Übersicht bei Gesprächen mit den Fachleuten:")

    checklist = [
        ("🚭 Gespräch mit Hausärzt:in: Rauchen", "Falls Sie rauchen, besprechen Sie einen Entwöhnungsplan mit Ihrer Hausärztin oder Ihrem Hausarzt."),
        ("⚖️ Gewicht und Ernährung überprüft", "Ausreichend Protein essen (Fleisch, Fisch, Eier, Milchprodukte). Bei Übergewicht mit der Ärztin oder dem Arzt besprechen."),
        ("🩸 Blutzucker kontrolliert", "Falls Diabetes: Blutzuckermessungen durchführen und dokumentieren. Werte zum Arzt mitbringen."),
        ("💊 Blutdruck überwacht", "Regelmäßig Blutdruck messen (idealerweise täglich die letzte Woche vor OP)."),
        ("🏋️ Mit Bewegung begonnen", "Mindestens 3x pro Woche 20-30 Minuten gehen oder Übungen machen."),
        ("💪 Kraft- und Balanceübungen gemacht", "2-3x pro Woche einfache Übungen durchführen (siehe Physio-Seite)."),
        ("🦷 Zahnhygiene kontrolliert", "Zahnbürste verwenden, Flossspülung durchführen. Zahnprobleme vorher klären."),
        ("🧼 Desinfektionsshampoo besorgt", "Octenisan oder Chlorhexidin-Shampoo kaufen für die Reinigung vor OP."),
        ("📋 Medikamentenliste zusammengestellt", "Alle regelmäßigen Medikamente aufschreiben und zum Gespräch mitbringen."),
        ("❓ Fragen notiert", "Fragen für den Chirurgen und Anästhesisten aufschreiben."),
    ]

    completed = 0
    for idx, (title, hint) in enumerate(checklist):
        key = f"checklist_item_{idx}"
        checked = st.checkbox(title, value=st.session_state.get(key, False), key=key)
        st.caption(hint)
        if checked:
            completed += 1
        st.divider()

    progress = int(completed / len(checklist) * 100) if checklist else 0
    st.progress(progress / 100)
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write(f"**{completed} von {len(checklist)} Punkte erledigt**")
    
    st.markdown("---")
    st.markdown("<div class='info-card'><h2>💡 Konkrete Tipps für die nächsten Wochen</h2></div>", unsafe_allow_html=True)

    with st.expander("Woche 1-2: Grundlagen schaffen"):
        st.markdown("""
        - Erstes Gespräch mit Hausärzt:in: Alle Risikofaktoren besprechen
        - Mit täglichen Spaziergängen beginnen (15-20 Minuten)
        - Ernährung überprüfen: Ausreichend Eiweiß?
        - Rauchen: Falls Sie rauchen, jetzt ist der beste Zeitpunkt zu beginnen
        """)

    with st.expander("Woche 3-4: Trainieren und optimieren"):
        st.markdown("""
        - Kraft- und Balanceübungen (siehe Physio) 2-3x pro Woche
        - Spazierganglänge auf 25-30 Minuten erhöhen
        - Blutzucker/Blutdruck regelmäßig messen (falls relevant)
        - Medikamenten-Check: Alle aktuellen Medikamente notieren
        """)

    with st.expander("Woche 5-8: Intensivieren und finalisieren"):
        st.markdown("""
        - Training weiterführen und leicht intensivieren
        - Zahnhygiene verbessern
        - Alle Untersuchungen abschließen (Blutdruck, Blutzucker)
        - Fragen sammeln für Chirurg und Anästhesist
        - Desinfektionsshampoo kaufen (vor OP verwenden)
        """)

    with st.expander("3-5 Tage vor OP: Letzte Vorbereitung"):
        st.markdown("""
        - Mit Desinfektionsshampoo duschen (wenn vom Chirurgen empfohlen)
        - Viel trinken (Wasser, Tee)
        - Gut schlafen
        - Alle Medikamentenlisten und Fragen mitnehmen
        - Entspannen und positiv denken – Sie sind gut vorbereitet!
        """)

    st.markdown("---")
    st.markdown("<div class='info-card'><h2>📓 Mein Tagebuch</h2></div>", unsafe_allow_html=True)
    st.write("Nutzen Sie dieses Feld, um Ihre Fortschritte, Fragen oder Gedanken festzuhalten:")
    
    st.text_area(
        "Meine Notizen (nicht dauerhaft gespeichert)",
        value=st.session_state.get("patient_diary", ""),
        key="patient_diary",
        height=120,
        placeholder="z.B. Trainingsfortschritt, Fragen, Gedanken zur OP, Erfolge...",
    )

    st.info("**Wichtig:** Diese App speichert Ihre Einträge nicht dauerhaft. Speichern Sie wichtige Informationen selbst ab oder schreiben Sie sie auf Papier.")


def main() -> None:
    inject_styles()
    if not require_password():
        return

    st.title(APP_TITLE)

    role = st.sidebar.radio(
        "Ich bin",
        ["Start", "Hausärzt:innen", "Physio", "Patient:innen"],
        index=0,
        horizontal=False,
    )

    if role == "Start":
        render_home()
    elif role == "Hausärzt:innen":
        render_hausarzt()
    elif role == "Physio":
        render_physio()
    else:
        render_patient()


if __name__ == "__main__":
    main()
