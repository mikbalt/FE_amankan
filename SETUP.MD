# Panduan Setup Django Admin Dashboard

Dokumen ini berisi instruksi detail untuk menyiapkan dan menjalankan aplikasi Django Admin Dashboard dari awal hingga siap digunakan.

## Prasyarat

Sebelum memulai, pastikan sistem Anda telah memenuhi prasyarat berikut:

1. **Python 3.8 atau lebih tinggi** - [Unduh Python](https://www.python.org/downloads/)
2. **pip** (Python package manager)
3. **git** - [Unduh Git](https://git-scm.com/downloads)
4. **Backend API Django** yang sudah berjalan

## Langkah 1: Clone Repositori

```bash
git clone https://github.com/yourusername/django-admin-dashboard.git
cd django-admin-dashboard
```

## Langkah 2: Persiapan Lingkungan Virtual

### Untuk Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Untuk macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## Langkah 3: Install Dependensi

```bash
pip install -r requirements.txt
```

Jika file `requirements.txt` belum ada, buat dengan konten berikut:

```
django==4.2.9
requests==2.31.0
python-dotenv==1.0.0
```

## Langkah 4: Konfigurasi Lingkungan

Buat file `.env` di direktori root proyek dengan konten berikut:

```
DEBUG=True
SECRET_KEY=change-this-to-a-secure-random-string
API_BASE_URL=http://your-backend-api-url
```

Pastikan untuk mengganti `SECRET_KEY` dengan string random yang aman dan `API_BASE_URL` dengan URL API backend Anda.

## Langkah 5: Jalankan Migrasi Database

Meskipun proyek ini terutama berperan sebagai frontend, Django masih memerlukan beberapa tabel database dasar:

```bash
python manage.py migrate
```

## Langkah 6: Jalankan Server Pengembangan

```bash
python manage.py runserver
```

Aplikasi sekarang dapat diakses di http://127.0.0.1:8000/login/

## Langkah 7: Verifikasi Koneksi ke Backend API

Pastikan bahwa backend API Anda berjalan dan dapat diakses dari aplikasi frontend. Anda dapat menguji koneksi dengan mencoba login menggunakan kredensial yang valid.

## Konfigurasi Tambahan

### Mengubah Port Server

Jika port 8000 sudah digunakan, Anda dapat menjalankan server di port lain:

```bash
python manage.py runserver 8080
```

### Mengakses dari Perangkat Lain di Jaringan

Untuk mengakses server dari perangkat lain di jaringan yang sama:

```bash
python manage.py runserver 0.0.0.0:8000
```

Kemudian akses melalui IP komputer Anda, misalnya: http://192.168.1.100:8000

### Mengkonfigurasi Static Files untuk Produksi

Untuk environment produksi, jalankan:

```bash
python manage.py collectstatic
```

## Struktur Database API Backend yang Diperlukan

Backend API harus menyediakan endpoint berikut:

1. **Autentikasi**
   - POST `/auth/login/` - Untuk login (menerima username dan password, mengembalikan token)
   - POST `/auth/logout/` - Untuk logout (opsional)

2. **Data Dashboard**
   - GET `/dashboard/data/` - Untuk mendapatkan data dashboard utama

Setiap endpoint API harus mengembalikan respons dalam format JSON.

## Troubleshooting

### Masalah Koneksi API

Jika Anda mengalami masalah koneksi ke backend API:

1. Periksa apakah URL API benar di file `.env`
2. Pastikan backend API berjalan
3. Periksa apakah ada masalah CORS dengan mengaktifkan CORS di backend

### Masalah Static Files

Jika file statis tidak dimuat dengan benar:

1. Periksa konfigurasi STATIC_URL dan STATICFILES_DIRS di `settings.py`
2. Pastikan file ada di lokasi yang benar
3. Jalankan `python manage.py collectstatic`

### Error "ModuleNotFoundError"

Jika Anda melihat error ini, pastikan semua dependensi telah diinstal:

```bash
pip install -r requirements.txt
```

## Deployment ke Produksi

Untuk deployment produksi, tambahan langkah-langkah berikut direkomendasikan:

1. Ubah `DEBUG=False` di file `.env`
2. Gunakan server WSGI seperti Gunicorn:
   ```bash
   pip install gunicorn
   gunicorn admin_dashboard.wsgi:application
   ```
3. Konfigurasikan Nginx atau Apache sebagai reverse proxy
4. Aktifkan HTTPS menggunakan sertifikat SSL
5. Konfigurasi file statis untuk dilayani oleh web server

## Sumber Daya Tambahan

- [Dokumentasi Django](https://docs.djangoproject.com/)
- [Dokumentasi Django REST framework](https://www.django-rest-framework.org/) (untuk backend)
- [Dokumentasi Bootstrap](https://getbootstrap.com/docs/)

## Kontak Bantuan

Jika Anda mengalami masalah yang tidak tercakup dalam panduan ini, silakan hubungi:

- Email: support@example.com
- GitHub Issues: Buat issue baru di repositori