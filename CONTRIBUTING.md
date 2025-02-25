# Panduan Kontribusi

Terima kasih atas minat Anda untuk berkontribusi pada proyek Django Admin Dashboard! Dokumen ini berisi informasi penting tentang cara Anda dapat berkontribusi pada proyek ini.

## Cara Berkontribusi

1. **Fork Repositori**
   
   Mulailah dengan melakukan fork pada repositori ini ke akun GitHub Anda.

2. **Clone Repositori**
   
   ```bash
   git clone https://github.com/yourusername/django-admin-dashboard.git
   cd django-admin-dashboard
   ```

3. **Buat Branch Baru**
   
   ```bash
   git checkout -b feature/nama-fitur
   ```
   atau
   ```bash
   git checkout -b fix/nama-bug
   ```

4. **Lakukan Perubahan**
   
   Lakukan perubahan yang diperlukan dan pastikan kode Anda mengikuti pedoman gaya kode proyek.

5. **Commit Perubahan**
   
   ```bash
   git commit -m "Deskripsi perubahan yang dilakukan"
   ```

6. **Push ke Branch**
   
   ```bash
   git push origin feature/nama-fitur
   ```

7. **Buat Pull Request**
   
   Buka halaman GitHub repositori yang Anda fork dan klik tombol "New Pull Request".

## Pedoman Kode

- Ikuti [PEP 8](https://www.python.org/dev/peps/pep-0008/) untuk gaya kode Python
- Gunakan indentasi 4 spasi (bukan tab)
- Berikan nama yang deskriptif untuk fungsi, variabel, dan kelas
- Tambahkan komentar yang jelas untuk kode yang kompleks
- Pisahkan logika bisnis dari kode tampilan

## Proses Pull Request

1. **Review Kode**
   
   Setiap pull request akan ditinjau oleh maintainer proyek. Mereka mungkin akan memberikan masukan atau meminta perubahan.

2. **CI/CD Checks**
   
   Pull request harus lolos semua pemeriksaan CI/CD yang dikonfigurasi.

3. **Merging**
   
   Setelah ditinjau dan disetujui, pull request Anda akan digabungkan ke branch utama.

## Jenis Kontribusi

### Fitur Baru

Jika Anda ingin menambahkan fitur baru:

1. Diskusikan fitur dengan maintainer terlebih dahulu dengan membuat issue
2. Berikan deskripsi rinci tentang fitur yang diusulkan
3. Jelaskan mengapa fitur ini berguna untuk proyek

### Perbaikan Bug

Untuk memperbaiki bug:

1. Periksa apakah bug sudah dilaporkan di issues
2. Jika belum, buat issue baru dengan langkah-langkah untuk mereproduksi bug
3. Jelaskan perilaku yang diharapkan vs. perilaku aktual

### Dokumentasi

Kontribusi dokumentasi sangat dihargai:

1. Perbaiki kesalahan ketik atau informasi yang tidak akurat
2. Tambahkan contoh atau penjelasan yang lebih jelas
3. Tingkatkan kejelasan dan kelengkapan dokumentasi

## Setup Pengembangan

1. **Persiapan Lingkungan**
   
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   ```

2. **Setup Database**
   
   ```bash
   python manage.py migrate
   ```

3. **Jalankan Server**
   
   ```bash
   python manage.py runserver
   ```

## Pengujian

- Tulis unit test untuk setiap fitur baru atau perbaikan
- Jalankan pengujian sebelum membuat pull request:
  ```bash
  python manage.py test
  ```

## Laporan Bug

Jika Anda menemukan bug, mohon buat issue dengan informasi berikut:

- Deskripsi singkat dan jelas tentang bug
- Langkah-langkah untuk mereproduksi bug
- Perilaku yang diharapkan
- Tangkapan layar (jika memungkinkan)
- Informasi lingkungan (OS, browser, versi Python, versi Django)

## Kontak

Jika Anda memiliki pertanyaan yang tidak tercakup dalam dokumen ini, silakan hubungi:

- Nama Maintainer: email@example.com
- Discord: Server Link/Channel
- Slack: Workspace/Channel

Terima kasih telah berkontribusi pada Django Admin Dashboard!