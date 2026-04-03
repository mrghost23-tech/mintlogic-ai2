import streamlit as st

st.set_page_config(page_title="MintLogic AI", page_icon="💰", layout="wide")

st.markdown("<style>.stApp { background-color: #0e1117; color: white; } .stMetric { background-color: #1e2130; padding: 15px; border-radius: 10px; border: 1px solid #3EB489; }</style>", unsafe_allow_index=True)

st.sidebar.markdown("<h1 style='color: #3EB489;'>MintLogic AI</h1>", unsafe_allow_index=True)
st.sidebar.caption("Sistem Durumu: Aktif 🟢")

st.title("💰 MintLogic AI Canlı Panel")
st.write("Yapay zeka analiz motoru başarıyla başlatıldı. Piyasalar izleniyor...")

# Demo Görsel Metrikler
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Güncel Fiyat (BTC)", "64,230 $")
with col2:
    st.metric("AI Tahmini", "YÜKSELİŞ (AL)")
with col3:
    st.metric("Model Doğruluğu", "%68.5")

st.divider()
st.caption("© 2026 MintLogic AI - Tüm hakları saklıdır.")
