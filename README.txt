# IQ Aptitude Test Web App (Per Nomor)

## Cara jalanin
**Disarankan pakai server lokal** (karena index.html fetch JSON).
- VS Code: install extension **Live Server** → klik "Go Live"
- atau Python:
  - Windows: `py -m http.server 8000`
  - Mac/Linux: `python3 -m http.server 8000`
  - lalu buka: http://localhost:8000

## Struktur folder
- index.html
- questions.json
- answer_key.json
- soal.pdf
- pages/page-1.png ... page-7.png

## Catatan soal bergambar (rapi & scalable)
Saat ini soal bergambar menampilkan **gambar halaman penuh**.
Kalau mau auto-zoom ke area soal tertentu, tambahkan `bbox` pada item soal di questions.json:

"bbox": { "x": 120, "y": 420, "w": 1650, "h": 620 }

Koordinat mengikuti pixel di file pages/page-X.png.
