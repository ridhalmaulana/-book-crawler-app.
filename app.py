# app.py
import streamlit as st
import json
import os

DATA_PATH = "data/books.json"

st.set_page_config(page_title="Web Crawler Search", layout="wide")
st.title("📚 Book Search (Scraped via Scrapy)")

# Load data
if os.path.exists(DATA_PATH):
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
else:
    st.warning("Data belum tersedia. Jalankan crawler terlebih dahulu.")
    st.stop()

# Input pencarian
query = st.text_input("Cari judul buku:", "")

# Filter data
if query:
    filtered = [
        item for item in data
        if query.lower() in item["title"].lower()
    ]
    st.markdown(f"### ✨ Ditemukan {len(filtered)} hasil")
else:
    filtered = data
    st.markdown(f"### ✨ Ditemukan {len(filtered)} hasil")

# Tampilkan hasil
for item in filtered:
    st.markdown(f"**[{item['title']}]({item['link']})**")
    st.markdown(
        f"Price: `{item['price']}` | Rating: `{item['rating']}` | "
        f"Availability: `{item['availability']}`"
    )
    st.markdown("---")
