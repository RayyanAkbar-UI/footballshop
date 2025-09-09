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

2. Bagan Alur Request-Response Django

    Gambar bagan: https://drive.google.com/file/d/1uEXDBgd1tRCNFbizFnJWKuXbwprkAawf/view?usp=sharing

    Penjelasan Bagan:

        - Request Client: Pengguna mengakses sebuah URL. Browser mengirimkan HTTP Request ke server.

        - settings.py: Sebelum request diproses lebih jauh, Django menggunakan konfigurasi dari settings.py untuk hal-hal seperti middleware yang akan memproses request dan response.

        - urls.py: Django menerima request dan memberikannya ke URL resolver. proyek/urls.py (berkas URL utama) akan mencari pola URL yang cocok. Jika pola tersebut didelegasikan ke aplikasi lain (misalnya main/), maka main/urls.py akan mengambil alih untuk menemukan pola yang lebih spesifik.

        - views.py: Setelah pola URL ditemukan, urls.py akan memanggil fungsi view yang terkait yang ada di views.py. Fungsi inilah yang berisi logika utama untuk memproses request tersebut.

        - models.py: Jika view memerlukan interaksi dengan database (misalnya, mengambil daftar produk), ia akan menggunakan class model yang didefinisikan di models.py. Django ORM (Object-Relational Mapper) akan menerjemahkan perintah Python menjadi query SQL ke database.

        - Template HTML: Setelah mendapatkan data yang diperlukan, view akan memanggil template engine dan meneruskan data tersebut sebagai "konteks".

        - Render & Response: Template engine akan mengisi berkas .html dengan data dari konteks, menghasilkan sebuah halaman HTML final. Halaman HTML inilah yang dikemas dalam sebuah HTTP Response dan dikirim kembali ke browser pengguna.

3. Peran settings.py dalam Proyek Django

    Berkas settings.py adalah pusat kendali atau "otak" dari sebuah proyek Django. Berkas ini tidak berisi logika aplikasi, melainkan konfigurasi global yang menentukan bagaimana proyek berjalan. Peran utamanya meliputi:

        - Konfigurasi Database: Mendefinisikan database engine yang digunakan (PostgreSQL, SQLite, dll.), nama database, serta kredensial untuk mengaksesnya.

        - Pendaftaran Aplikasi (INSTALLED_APPS): Memberi tahu Django aplikasi mana saja yang aktif dalam proyek. Tanpa didaftarkan di sini, model, URL, dan komponen lain dari sebuah aplikasi tidak akan dikenali oleh Django.

        - Pengelolaan Aset Statis (STATIC_URL, STATICFILES_DIRS): Mengatur bagaimana Django menangani berkas statis seperti CSS, JavaScript, dan gambar.

        - Konfigurasi Middleware (MIDDLEWARE): Middleware adalah lapisan-lapisan pemrosesan yang dilewati oleh setiap request dan response. Contohnya adalah middleware untuk otentikasi sesi dan keamanan CSRF.

        - Konfigurasi Template: Menentukan di mana Django harus mencari berkas-berkas template HTML.

        - Kunci Rahasia (SECRET_KEY): Sebuah kunci unik yang digunakan untuk cryptographic signing dan keamanan.

        - Mode Debug (DEBUG): Mengaktifkan atau menonaktifkan mode debug. Ketika DEBUG = True, Django akan menampilkan halaman error yang detail, yang sangat berguna saat pengembangan.

4. Cara Kerja Migrasi Database di Django
    Sistem migrasi Django adalah fitur canggih yang berfungsi untuk menjaga skema database tetap sinkron dengan definisi model (models.py) secara terstruktur dan terkontrol versinya. Proses ini bekerja dalam dua langkah utama:

        A. makemigrations:

            - Ketika kita menjalankan perintah python manage.py makemigrations, Django akan membandingkan kondisi model saat ini (di dalam semua berkas models.py) dengan kondisi terakhir yang tercatat dalam berkas migrasi sebelumnya.

            - Jika Django mendeteksi adanya perubahan (misalnya, penambahan field, penghapusan model, atau modifikasi tipe data), ia akan membuat sebuah berkas Python baru di dalam direktori migrations/ pada aplikasi terkait.

            - Berkas ini bukanlah query SQL, melainkan sebuah deskripsi perubahan dalam format Python. Ia berisi instruksi tentang operasi apa yang harus dilakukan pada database untuk mencerminkan perubahan pada model.

        B. migrate:

            - Perintah python manage.py migrate berfungsi sebagai eksekutor. Django akan melihat tabel django_migrations di database untuk mengetahui migrasi mana yang sudah pernah diterapkan.

            - Kemudian, ia akan mengambil semua berkas migrasi yang belum diterapkan dan menjalankannya secara berurutan.

            - Untuk setiap berkas migrasi, Django akan menerjemahkan deskripsi perubahan dalam Python menjadi query SQL yang sesuai dengan dialek database yang dikonfigurasi di settings.py.

            - Query SQL ini kemudian dieksekusi pada database, yang akhirnya mengubah struktur tabel, kolom, dan lain-lain.

    Dengan sistem ini, perubahan skema database menjadi bagian dari codebase proyek, sehingga dapat dilacak menggunakan sistem kontrol versi seperti Git dan mudah diterapkan secara konsisten di lingkungan pengembangan, pengujian, maupun produksi.

5. Mengapa Django Menjadi Pilihan Awal yang Baik untuk Pengembangan Perangkat Lunak?

    Menurut pandangan saya, Django adalah framework yang sangat ideal sebagai titik awal pembelajaran pengembangan perangkat lunak, terutama dalam konteks web, karena beberapa alasan kuat berikut:

        - Filosofi "Batteries-Included": Django hadir dengan banyak sekali fitur bawaan yang siap pakai, seperti sistem otentikasi pengguna, panel admin yang fungsional, ORM yang kuat, dan sistem routing. Hal ini memungkinkan pemula untuk fokus pada pemahaman konsep inti pengembangan web (seperti alur request-response dan arsitektur MVT) tanpa harus pusing memilih dan mengintegrasikan banyak pustaka eksternal untuk fungsionalitas dasar.

        - Struktur yang Jelas dan Terorganisir (MVT): Arsitektur Model-View-Template (MVT) yang diusung Django mendorong adanya separation of concerns (pemisahan tanggung jawab) yang sangat jelas. Pemula diajarkan sejak dini untuk memisahkan logika data (Model), logika bisnis (View), dan logika presentasi (Template). Ini adalah fondasi penting dalam rekayasa perangkat lunak yang akan sangat berguna di framework atau bahasa apa pun di masa depan.

        - ORM yang Mengabstraksi Kerumitan SQL: Berinteraksi langsung dengan database menggunakan SQL mentah bisa menjadi penghalang besar bagi pemula. Django ORM (Object-Relational Mapper) memungkinkan developer untuk berinteraksi dengan database menggunakan objek dan metode Python yang intuitif. Ini tidak hanya mempercepat pengembangan tetapi juga mengurangi risiko SQL injection dan membuat kode lebih mudah dibaca.

        - Keamanan Bawaan: Django sangat serius dalam hal keamanan. Banyak celah keamanan web umum seperti Cross-Site Scripting (XSS), Cross-Site Request Forgery (CSRF), dan SQL Injection sudah ditangani secara default. Ini menanamkan praktik pengembangan yang aman sejak awal.

        - Dokumentasi dan Komunitas yang Luar Biasa: Django memiliki salah satu dokumentasi terbaik di dunia open-source. Dokumentasinya sangat lengkap, terstruktur, dan penuh dengan contoh. Ditambah dengan komunitas global yang besar dan aktif, pemula dapat dengan mudah menemukan solusi untuk hampir setiap masalah yang mereka hadapi.

6. Feedback terhadap asdos

    Materi serta langkah-langkah dalam tutorial mudah dipahami, terutama untuk saya sebagai seorang pemula.