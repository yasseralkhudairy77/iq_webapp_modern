# Recruitment Test Suite (IQ + Pauli/Kraeplin + Typing + DISC + Working Style)

## Cara Jalan
- Jalankan server lokal dari folder project:
  - `python -m http.server 8000`
  - atau `py -m http.server 8000`
- Buka `http://localhost:8000`

## Alur Wajib Kandidat
1. Mulai dari **IQ Test** (`apps/iq/index.html`).
2. Isi identitas di IQ saja:
   - Nama lengkap
   - No. WhatsApp format `08xxxxxxxxxx`
   - Posisi dilamar
   - Token saat ini dinonaktifkan sementara (mode testing)
3. Setelah klik **Mulai Tes** di IQ, profil kandidat otomatis disimpan.
4. Lanjut ke tes lain tanpa isi ulang identitas:
   - `apps/koran/index.html`
   - `apps/typing/index.html`
   - `apps/disc/index.html`
   - `apps/working-style/index.html`

## Struktur Folder
- `index.html` → launcher suite
- `apps/iq/` → modul IQ + assets
- `apps/koran/` → modul Pauli/Kraeplin
- `apps/typing/` → modul Typing
- `apps/disc/` → modul DISC
- `apps/working-style/` → modul Working Style

## Catatan Integrasi
- Shared identity key: `berani_suite_profile_v1` (localStorage).
- Tes non-IQ membaca profil dari query string + localStorage.
- Field identitas di tes non-IQ dikunci agar tidak perlu input ulang.
