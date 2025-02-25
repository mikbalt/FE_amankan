# Django Admin Dashboard

Sebuah aplikasi frontend untuk admin dashboard yang dibuat dengan Django, terhubung ke API backend Django untuk pengelolaan data.

## Deskripsi

Django Admin Dashboard adalah aplikasi web yang dirancang untuk memberikan antarmuka admin yang ramah pengguna. Aplikasi ini dibangun dengan Django sebagai framework frontend dan terhubung ke API backend Django terpisah untuk pengelolaan data. Dashboard ini menyediakan tampilan yang intuitif untuk manajemen sistem, melihat data statistik, dan melakukan operasi CRUD.

## Fitur

- **Sistem Autentikasi**: Halaman login yang aman dengan validasi input
- **Dashboard Interaktif**: Tampilan utama dengan statistik dan ringkasan data
- **Desain Responsif**: Tampilan yang menyesuaikan dengan berbagai ukuran perangkat
- **Koneksi API**: Integrasi dengan backend Django API
- **UI Modern**: Antarmuka pengguna yang bersih dan intuitif menggunakan Bootstrap 5
- **Keamanan**: Pengelolaan sesi dan token otentikasi

## Screenshot

![Login Page](static/images/login-screenshot.png)
![Dashboard Page](static/images/dashboard-screenshot.png)

## Teknologi yang Digunakan

- Django 4.x
- Bootstrap 5
- JavaScript
- HTML5 & CSS3
- Python Requests (untuk komunikasi API)
- python-dotenv (untuk variabel lingkungan)

## Prasyarat

- Python 3.8 atau versi lebih baru
- pip (Python package manager)
- Backend Django API yang berjalan

## Instalasi dan Pengaturan

1. Clone repositori ini:
   ```bash
   git clone https://github.com/yourusername/django-admin-dashboard.git
   cd django-admin-dashboard
   ```

2. Buat dan aktifkan virtual environment:
   ```bash
   python -m venv venv
   
   # Untuk Windows
   venv\Scripts\activate
   
   # Untuk Linux/Mac
   source venv/bin/activate
   ```

3. Install dependensi:
   ```bash
   pip install -r requirements.txt
   ```

4. Buat file `.env` di direktori root dengan konten berikut:
   ```
   DEBUG=True
   SECRET_KEY=your-secret-key-here
   API_BASE_URL=http://your-backend-api-url
   ```

5. Jalankan migrasi:
   ```bash
   python manage.py migrate
   ```

6. Jalankan server pengembangan:
   ```bash
   python manage.py runserver
   ```

7. Buka browser dan akses `http://127.0.0.1:8000/login/`

## Penggunaan

1. Masuk menggunakan kredensial yang valid melalui halaman login
2. Setelah otentikasi berhasil, Anda akan diarahkan ke dashboard utama
3. Gunakan sidebar untuk navigasi ke berbagai bagian aplikasi
4. Logout saat selesai menggunakan sistem

## Struktur Proyek

```
admin_dashboard/
│
├── admin_dashboard/        # Direktori utama proyek Django
│   ├── __init__.py
│   ├── settings.py         # Konfigurasi Django
│   ├── urls.py             # Konfigurasi URL utama
│   └── wsgi.py             # Konfigurasi WSGI
│
├── dashboard/              # Aplikasi dashboard
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py             # URL untuk aplikasi dashboard
│   └── views.py            # View untuk aplikasi dashboard
│
├── static/                 # File statis (CSS, JS, gambar)
│   ├── css/
│   │   ├── login.css
│   │   └── dashboard.css
│   ├── js/
│   │   ├── login.js
│   │   └── dashboard.js
│   └── images/
│
├── templates/              # Template HTML
│   └── dashboard/
│       ├── login.html
│       └── home.html
│
├── .env                    # Variabel lingkungan
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

## Pengembangan

### Menambahkan Halaman Baru

1. Buat template HTML baru di `templates/dashboard/`
2. Tambahkan view baru di `dashboard/views.py`
3. Tambahkan URL baru di `dashboard/urls.py`
4. Tambahkan link ke halaman baru di sidebar navigasi

### Mengubah Tampilan

1. Edit file CSS di direktori `static/css/`
2. Jika perlu, tambahkan file CSS baru dan impor di template

### Mengubah Koneksi API

Edit fungsi `call_api()` di `dashboard/views.py` untuk mengubah cara aplikasi berkomunikasi dengan API backend.

## Deployment

Untuk deployment ke server produksi:

1. Ubah `DEBUG=False` di file `.env`
2. Gunakan server WSGI seperti Gunicorn
3. Konfigurasikan Nginx atau Apache sebagai reverse proxy
4. Pindahkan file statis menggunakan `python manage.py collectstatic`

## Kontribusi

Silakan berkontribusi pada proyek ini dengan mengikuti langkah-langkah berikut:

1. Fork repositori
2. Buat branch fitur (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan Anda (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buka Pull Request

## Lisensi

Didistribusikan di bawah lisensi MIT. Lihat `LICENSE` untuk informasi lebih lanjut.

## Kontak

Nama Anda - [@twitter_handle](https://twitter.com/twitter_handle) - email@example.com

Link Proyek: [https://github.com/yourusername/django-admin-dashboard](https://github.com/yourusername/django-admin-dashboard)