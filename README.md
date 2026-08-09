# 📚 Book Crawler App — UAS Information Retrieval (SIF502)

## Identitas
- **Nama:** M. Ridhal Maulana
- **NIM:** 24146099P
- **Mata Kuliah:** Information Retrieval (SIF502)
- **Dosen Pengampu:** Teuku Rizky Noviandy, S.Kom., M.Kom.
- **Tahun Ajaran:** Genap 2025/2026

## Deskripsi
Aplikasi ini merupakan hasil pengembangan web crawler menggunakan **Scrapy** untuk mengumpulkan data
buku dari situs [books.toscrape.com](http://books.toscrape.com), yang kemudian ditampilkan melalui
antarmuka pencarian interaktif berbasis **Streamlit**.

## Link Akses
- **Streamlit App:** [https://mwfo64r3vwsc2wgwzyglxn.streamlit.app/ ]
- **Repository GitHub:** [https://github.com/ridhalmaulana/-book-crawler-app ]

## Struktur Proyek
```
book_crawler_app/
├── app.py              ← Aplikasi Streamlit
├── data/
│   └── books.json      ← Data hasil crawl
├── requirements.txt    ← Dependensi
└── README.md
```

## Cara Menjalankan Lokal
1. Clone repository ini:
   ```
   git clone [LINK_GITHUB]
   cd book_crawler_app
   ```
2. Install dependensi:
   ```
   pip install -r requirements.txt
   ```
3. Jalankan aplikasi:
   ```
   streamlit run app.py
   ```

## Sumber Data
Data buku diperoleh melalui proses web scraping menggunakan Scrapy terhadap situs
`books.toscrape.com`, mencakup atribut: judul, harga, ketersediaan stok, rating, dan tautan detail buku.
