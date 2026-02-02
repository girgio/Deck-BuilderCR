"""
GUI Clash Royale Deck Builder
"""
import streamlit as st
import sys
import os
import pandas as pd
from datetime import datetime
import json

# Aggiungi path per import
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from Dati.DatabaseCarte import DatabaseCarte
from Dati.Mazzo import Mazzo
from Algoritmi.GA.Algoritmo import algoritmo_genetico
from Algoritmi.HillClimbing.HillClimbing import hill_climbing, costruisci_mazzo_random_valido

# ==================== CONFIGURAZIONE ====================

st.set_page_config(
    page_title="Deck Builder CR",
    page_icon="👑",
    layout="wide"
)

# CSS Minimalista
st.markdown("""
<style>
    .main {background: linear-gradient(135deg, #1e1e2e 0%, #2d2d3a 100%);}
    h1 {color: #ffd700; text-align: center;}
    h2 {color: #ff6b6b; border-bottom: 2px solid #ffd700; padding-bottom: 10px;}
    h3 {color: #4ecdc4;}
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white; font-weight: bold; border-radius: 10px;
        padding: 12px 24px; border: none;
    }
</style>
""", unsafe_allow_html=True)

# ==================== FUNZIONI ====================

@st.cache_resource
def carica_database():
    """Carica database carte"""
    db_path = os.path.join(parent_dir, 'Dati', 'database_carte.json')
    return DatabaseCarte(db_path)

def mostra_mazzo(mazzo, titolo="Mazzo", carte_fisse=None):
    """Mostra un mazzo con immagini"""
    st.subheader(titolo)

    cols = st.columns(8)
    for i, carta in enumerate(mazzo.carte):
        with cols[i]:
            st.image(carta.image_url, use_container_width=True)
            badge = "🔒" if carte_fisse and carta.nome in carte_fisse else ""
            st.caption(f"**{carta.nome}** {badge}")
            st.caption(f"⚡ {carta.costo}")

    # Statistiche
    st.markdown("---")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("Costo Medio", f"{mazzo.get_costo_medio():.2f}")
    with col2:
        st.metric("Danno Medio", f"{mazzo.get_danno_medio():.0f}")
    with col3:
        st.metric("Vita Media", f"{mazzo.get_vita_medio():.0f}")
    with col4:
        st.metric("Incantesimi", mazzo.get_incantesimi())
    with col5:
        st.metric("Fitness", f"{mazzo.calcola_fitness():.2f}")

def salva_storico(esecuzione_data):
    """Salva esecuzione nello storico"""
    storico_path = os.path.join(parent_dir, 'GUI', 'storico.json')

    try:
        with open(storico_path, 'r', encoding='utf-8') as f:
            storico = json.load(f)
    except:
        storico = []

    storico.append(esecuzione_data)

    # Mantieni solo ultime 50 esecuzioni
    storico = storico[-50:]

    with open(storico_path, 'w', encoding='utf-8') as f:
        json.dump(storico, f, indent=2, ensure_ascii=False)

def carica_storico():
    """Carica storico esecuzioni"""
    storico_path = os.path.join(parent_dir, 'GUI', 'storico.json')
    try:
        with open(storico_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []

# ==================== HEADER ====================

st.title("👑 CLASH ROYALE DECK BUILDER")
st.markdown("### Ottimizza i tuoi mazzi con algoritmi AI")

# ==================== TABS ====================

tab1, tab2 = st.tabs(["🚀 Ottimizzazione", "📊 Storico Esecuzioni"])

# ==================== TAB 1: OTTIMIZZAZIONE ====================

with tab1:
    st.markdown("---")

    # ==================== CARICAMENTO ====================

    try:
        db = carica_database()
        tutte_carte = db.get_tutte_le_carte()
        st.success(f"✅ Database caricato: {len(tutte_carte)} carte disponibili")
    except Exception as e:
        st.error(f"❌ Errore caricamento database: {e}")
        st.stop()

    # ==================== SIDEBAR: CONFIGURAZIONE ====================

    st.sidebar.header("⚙️ Configurazione Algoritmo")

    # Scelta algoritmo
    algoritmo = st.sidebar.selectbox(
        "Seleziona Algoritmo",
        ["Algoritmo Genetico (GA)", "Hill Climbing (HC)"],
        help="Scegli l'algoritmo di ottimizzazione"
    )

    st.sidebar.markdown("---")

    # Carte fisse
    st.sidebar.markdown("### 🔒 Carte Fisse (opzionale)")

    if 'num_carte_fisse' not in st.session_state:
        st.session_state.num_carte_fisse = 0

    nomi_carte = db.get_nomi_carte()

    if st.session_state.num_carte_fisse < 4:
        st.sidebar.info(f"📝 Selezionate: {st.session_state.num_carte_fisse}/4 carte")
    else:
        st.sidebar.warning("⚠️ **Limite raggiunto** (4/4)\n\nRimuovi una carta per cambiarne un'altra.")

    carte_fisse = st.sidebar.multiselect(
        "Seleziona max 4 carte da fissare",
        options=nomi_carte,
        max_selections=4,
        help="Queste carte saranno sempre presenti nel mazzo",
        key='carte_fisse'
    )

    st.session_state.num_carte_fisse = len(carte_fisse)

    st.sidebar.markdown("---")

    # Parametri specifici per algoritmo
    if "Genetic" in algoritmo:
        st.sidebar.markdown("### 🧬 Parametri GA")

        size_pop = st.sidebar.slider("Dimensione Popolazione", 0, 1000, 100, 10)
        size_mating = st.sidebar.slider("Dimensione Mating Pool", 0, 1000, 80, 5)
        p_mutation = st.sidebar.slider("Prob. Mutazione", 0.0, 1.0, 0.8, 0.05)
        p_crossover = st.sidebar.slider("Prob. Crossover", 0.0, 1.0, 1.0, 0.05)

    else:  # Hill Climbing
        st.sidebar.markdown("### 🏔️ Parametri HC")

        max_iter = st.sidebar.slider("Max Iterazioni", 50, 500, 200)
        neighbors = st.sidebar.slider("Vicini per Iterazione", 10, 840, 840)
        max_stalli = st.sidebar.slider("Max Stalli", 10, 50, 30)
        usa_restart = st.sidebar.checkbox("Usa Random Restart", value=True)

    # ==================== ESECUZIONE ====================

    st.header("🚀 Genera Mazzo Ottimale")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        bottone_avvia = st.button("▶️ AVVIA OTTIMIZZAZIONE", type="primary", use_container_width=True)

    if bottone_avvia:

        fisse_set = set(carte_fisse)

        progress_bar = st.progress(0)
        status = st.empty()

        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            status.info("⏳ Esecuzione in corso...")

            # ========== ALGORITMO GENETICO ==========
            if "Genetic" in algoritmo:
                progress_bar.progress(25)
                status.info("🧬 Esecuzione Algoritmo Genetico...")

                mazzo_best, fitness_best = algoritmo_genetico(
                    size_popolazione=size_pop,
                    size_mating_pool=size_mating,
                    p_mutazione=p_mutation,
                    p_crossover=p_crossover,
                    db=db,
                    fisse=fisse_set,
                )

                progress_bar.progress(100)

                # Salva nello storico
                esecuzione = {
                    "timestamp": timestamp,
                    "algoritmo": "GA",
                    "parametri": {
                        "popolazione": size_pop,
                        "mating_pool": size_mating,
                        "mutazione": p_mutation,
                        "crossover": p_crossover
                    },
                    "carte_fisse": list(carte_fisse),
                    "fitness_finale": fitness_best,
                    "mazzo": [c.nome for c in mazzo_best.carte]
                }
                salva_storico(esecuzione)

            # ========== HILL CLIMBING ==========
            else:
                progress_bar.progress(10)
                status.info("🏗️ Generazione mazzo iniziale...")

                # Genera mazzo iniziale
                mazzo_iniziale = costruisci_mazzo_random_valido(db, fisse_set)

                progress_bar.progress(25)
                status.info("🏔️ Esecuzione Hill Climbing...")

                mazzo_best, fitness_best = hill_climbing(
                    mazzo_iniziale=mazzo_iniziale,
                    db=db,
                    fisse=fisse_set,
                    max_iter=max_iter,
                    neighbors_per_iter=neighbors,
                    max_stalli=max_stalli,
                    usa_restart=usa_restart,
                    stampa_finale=False  # non stampare su console
                )

                progress_bar.progress(100)

                # Salva nello storico
                esecuzione = {
                    "timestamp": timestamp,
                    "algoritmo": "HC",
                    "parametri": {
                        "max_iter": max_iter,
                        "neighbors": neighbors,
                        "max_stalli": max_stalli,
                        "restart": usa_restart
                    },
                    "carte_fisse": list(carte_fisse),
                    "fitness_finale": fitness_best,
                    "mazzo": [c.nome for c in mazzo_best.carte]
                }
                salva_storico(esecuzione)

            status.success("✅ Ottimizzazione completata!")

            # ========== MOSTRA RISULTATO ==========
            st.markdown("---")

            # Box informativo
            st.info(f"🎯 **Algoritmo utilizzato:** {algoritmo}\n\n"
                    f"🔒 **Carte fisse:** {len(carte_fisse)}\n\n"
                    f"⭐ **Fitness finale:** {fitness_best:.2f}\n\n"
                    f"🕒 **Salvato alle:** {timestamp}")

            st.markdown("---")

            # Mostra mazzo
            mostra_mazzo(mazzo_best, titolo="🏆 Mazzo Ottimale Generato", carte_fisse=carte_fisse)

            # Dettagli carte
            st.markdown("---")
            st.subheader("📋 Dettaglio Carte")

            for carta in mazzo_best.carte:
                col1, col2, col3, col4, col5 = st.columns([3, 1, 1, 1, 2])

                with col1:
                    badge = "🔒" if carta.nome in carte_fisse else ""
                    st.write(f"**{carta.nome}** {badge}")
                with col2:
                    st.write(f"💧 {carta.costo}")
                with col3:
                    st.write(f"❤️ {carta.punti_vita}")
                with col4:
                    st.write(f"⚔️ {carta.danno_s}")
                with col5:
                    st.write(f"📦 {carta.tipologia}")

            progress_bar.empty()
            status.empty()

        except ValueError as e:
            st.error(f"❌ Errore di validazione: {e}")
            progress_bar.empty()
            status.empty()

        except Exception as e:
            st.error(f"❌ Errore durante l'esecuzione: {e}")
            st.code(str(e))
            import traceback
            st.code(traceback.format_exc())
            progress_bar.empty()
            status.empty()

# ==================== TAB 2: STORICO ====================

with tab2:
    st.header("📊 Storico Esecuzioni")
    st.markdown("Visualizza e confronta le esecuzioni precedenti degli algoritmi")
    st.markdown("---")

    storico = carica_storico()

    if not storico:
        st.info("📭 **Nessuna esecuzione salvata**\n\nAvvia un'ottimizzazione nel tab principale per popolare lo storico!")
    else:
        st.success(f"✅ Trovate **{len(storico)}** esecuzioni salvate")

        # Statistiche generali
        col1, col2, col3 = st.columns(3)

        with col1:
            num_ga = sum(1 for e in storico if e["algoritmo"] == "GA")
            st.metric("Esecuzioni GA", num_ga)

        with col2:
            num_hc = sum(1 for e in storico if e["algoritmo"] == "HC")
            st.metric("Esecuzioni HC", num_hc)

        with col3:
            best_fitness = max(e["fitness_finale"] for e in storico)
            st.metric("Miglior Fitness", f"{best_fitness:.2f}")

        st.markdown("---")

        # Tabella riepilogo
        st.subheader("📋 Riepilogo Esecuzioni")

        df_data = []
        for i, exec in enumerate(reversed(storico)):
            df_data.append({
                "#": len(storico) - i,
                "Data": exec["timestamp"],
                "Algoritmo": exec["algoritmo"],
                "Fitness": f"{exec['fitness_finale']:.2f}",
                "Carte Fisse": len(exec.get("carte_fisse", []))
            })

        df = pd.DataFrame(df_data)
        st.dataframe(df, use_container_width=True, hide_index=True)

        # Selezione esecuzione da visualizzare
        st.markdown("---")
        st.subheader("🔍 Dettaglio Esecuzione")

        exec_num = st.selectbox(
            "Seleziona esecuzione da visualizzare",
            options=list(range(len(storico), 0, -1)),
            format_func=lambda x: f"#{x} - {storico[x-1]['timestamp']} - {storico[x-1]['algoritmo']} (Fitness: {storico[x-1]['fitness_finale']:.2f})"
        )

        exec_selezionata = storico[exec_num - 1]

        # Info esecuzione
        col1, col2 = st.columns(2)

        with col1:
            st.metric("🤖 Algoritmo", exec_selezionata["algoritmo"])
            st.metric("⭐ Fitness Finale", f"{exec_selezionata['fitness_finale']:.2f}")
            st.metric("🔒 Carte Fisse", len(exec_selezionata.get("carte_fisse", [])))

            if exec_selezionata.get("carte_fisse"):
                st.write("**Carte fisse usate:**")
                for carta in exec_selezionata["carte_fisse"]:
                    st.write(f"• {carta}")

        with col2:
            st.write("**📝 Parametri utilizzati:**")
            st.json(exec_selezionata["parametri"])

        # Mazzo risultante
        st.markdown("---")
        st.subheader("🃏 Mazzo Risultante")

        cols = st.columns(8)
        for i, nome_carta in enumerate(exec_selezionata["mazzo"]):
            carta = db.get_carta(nome_carta)
            if carta:
                with cols[i]:
                    st.image(carta.image_url, use_container_width=True)
                    badge = "🔒" if nome_carta in exec_selezionata.get("carte_fisse", []) else ""
                    st.caption(f"**{carta.nome}** {badge}")
                    st.caption(f"💧 {carta.costo}")

        # Statistiche mazzo
        st.markdown("---")

        # Ricostruisci mazzo per statistiche
        carte_mazzo = [db.get_carta(nome) for nome in exec_selezionata["mazzo"]]
        if all(carte_mazzo):
            mazzo_storico = Mazzo(carte_mazzo)

            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.metric("Costo Medio", f"{mazzo_storico.get_costo_medio():.2f}")
            with col2:
                st.metric("Danno Medio", f"{mazzo_storico.get_danno_medio():.0f}")
            with col3:
                st.metric("Vita Media", f"{mazzo_storico.get_vita_medio():.0f}")
            with col4:
                st.metric("Incantesimi", mazzo_storico.get_incantesimi())
            with col5:
                st.metric("Edifici", mazzo_storico.get_edifici())

        # Bottoni azioni
        st.markdown("---")
        col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 2])

        with col_btn1:
            if st.button("🗑️ Elimina Questa", type="secondary"):
                storico.pop(exec_num - 1)
                storico_path = os.path.join(parent_dir, 'GUI', 'storico.json')
                with open(storico_path, 'w', encoding='utf-8') as f:
                    json.dump(storico, f, indent=2, ensure_ascii=False)
                st.success("✅ Esecuzione eliminata!")
                st.rerun()

        with col_btn2:
            if st.button("🗑️ Pulisci Tutto", type="secondary"):
                storico_path = os.path.join(parent_dir, 'GUI', 'storico.json')
                with open(storico_path, 'w', encoding='utf-8') as f:
                    json.dump([], f)
                st.success("✅ Storico eliminato!")
                st.rerun()

# ==================== FOOTER ====================

st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #888;'>"
    "🎮 <b>Deck Builder CR</b> - Progetto Universitario | Algoritmi di Ottimizzazione | Con Storico"
    "</div>",
    unsafe_allow_html=True
)
