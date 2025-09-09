Link: https://rayyan-akbar-footballshop.pbp.cs.ui.ac.id/

1. Implementasi Checklist Proyek

    Berikut adalah penjelasan step-by-step mengenai proses implementasi yang saya lakukan untuk menyelesaikan proyek ini.

    - Inisialisasi Proyek dan Aplikasi:

        Langkah pertama adalah membuat fondasi proyek. Saya menggunakan perintah django-admin startproject nama_proyek . untuk menginisialisasi proyek Django di direktori saat ini. Setelah itu, saya membuat aplikasi utama dengan nama main menggunakan perintah python manage.py startapp main. Aplikasi main ini akan menjadi pusat dari seluruh logika bisnis proyek.

    - Konfigurasi Proyek untuk Aplikasi main:

        Agar proyek mengenali aplikasi main yang baru dibuat, saya mendaftarkannya ke dalam list INSTALLED_APPS pada berkas settings.py. Selanjutnya, saya mengatur routing utama pada proyek/urls.py. Saya menggunakan include('main.urls') untuk mendelegasikan semua request yang masuk ke path tertentu agar ditangani oleh berkas urls.py di dalam aplikasi main. Ini adalah praktik terbaik untuk menjaga agar aplikasi tetap modular.

    - Pembuatan Model Product:

        Sesuai dengan kebutuhan, saya mendefinisikan struktur data produk pada main/models.py. Saya membuat sebuah class bernama Product yang mewarisi models.Model. Di dalamnya, saya mendefinisikan setiap atribut yang diminta:

            name: CharField untuk teks singkat.

            price: IntegerField untuk bilangan bulat.

            description: TextField untuk teks yang lebih panjang.

            thumbnail: URLField untuk menyimpan tautan gambar.

            category: CharField untuk kategori produk.

            is_featured: BooleanField untuk status True/False.
            Setelah model didefinisikan, saya menjalankan python manage.py makemigrations untuk membuat skrip migrasi dan python manage.py migrate untuk menerapkan skema model ini ke database.

    - Pembuatan View dan Template:

        Saya membuat sebuah fungsi sederhana pada main/views.py. Fungsi ini bertugas untuk me-render sebuah template HTML dan mengirimkan konteks data. Konteks yang saya kirimkan berisi nama aplikasi, nama saya, dan kelas saya. Template HTML-nya sendiri saya buat di dalam direktori main/templates/main/nama_template.html, yang isinya hanya menampilkan data dari konteks tersebut menggunakan sintaks template Django ({{ nama_variabel }}).

    - Routing di Tingkat Aplikasi:

        Agar fungsi view yang telah dibuat dapat diakses melalui URL, saya membuat berkas urls.py di dalam direktori main. Di dalamnya, saya mendefinisikan sebuah path (misalnya, path('', show_main, name='show_main')) yang memetakan URL root dari aplikasi ke fungsi show_main yang ada di views.py.

    - Deployment ke Platform as a Service (PWS):

        Proses deployment adalah tahap akhir untuk membuat aplikasi dapat diakses secara publik. Saya memilih salah satu PWS yang kompatibel dengan Python/Django. Langkah-langkah umumnya meliputi: menghubungkan repository Git saya ke PWS, mengonfigurasi variabel lingkungan (environment variables) jika ada, dan memastikan PWS menjalankan perintah yang benar untuk menginstal dependensi (pip install -r requirements.txt) dan menjalankan server (gunicorn nama_proyek.wsgi).