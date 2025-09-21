Link: https://rayyan-akbar-footballshop.pbp.cs.ui.ac.id/

1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

    Kebutuhan akan data delivery merupakan konsekuensi logis dari evolusi arsitektur perangkat lunak modern yang beralih dari pola monolitik ke arsitektur terdistribusi, seperti microservices. Dalam arsitektur modern, komponen-komponen aplikasi seperti front-end (misalnya, aplikasi web berbasis JavaScript atau aplikasi seluler) dan back-end dikembangkan dan dijalankan secara terpisah. Agar komponen-komponen yang independen ini dapat saling berinteraksi, diperlukan sebuah mekanisme standar untuk pertukaran data. Di sinilah peran data delivery. Ia berfungsi sebagai jembatan komunikasi yang memungkinkan server (back-end) mengirimkan data kepada klien (front-end) dalam format yang terstruktur dan dapat dipahami oleh kedua belah pihak (contohnya JSON atau XML). Tanpa proses data delivery yang efektif, interoperabilitas antar-komponen tidak akan tercapai, dan platform tidak dapat berfungsi sebagai satu kesatuan yang kohesif.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

    Dalam konteks pengembangan aplikasi web modern, JSON (JavaScript Object Notation) secara umum dianggap lebih superior dibandingkan XML (eXtensible Markup Language).

    Popularitas JSON didorong oleh beberapa faktor teknis utama:

        - Efisiensi: Sintaksis JSON lebih ringkas karena tidak memerlukan tag pembuka dan penutup untuk setiap elemen data. Hal ini menghasilkan ukuran payload yang lebih kecil, sehingga proses transmisi data menjadi lebih cepat dan efisien.

        - Kinerja Parsing: Struktur JSON yang sederhana memungkinkan proses parsing (analisis data) di sisi klien berlangsung lebih cepat dan dengan konsumsi sumber daya yang lebih rendah dibandingkan XML.

        - Keterbacaan (Readability): Struktur key-value pair yang diadopsi oleh JSON cenderung lebih mudah dibaca dan dipahami oleh manusia (pengembang), yang menyederhanakan proses debugging dan pengembangan.

        - Representasi Data Alami: Format JSON secara langsung memetakan struktur data yang umum digunakan dalam banyak bahasa pemrograman, seperti objek, dictionary, dan array. Hal ini membuat proses serialisasi (konversi objek ke teks) dan deserialisasi (konversi teks ke objek) menjadi lebih intuitif dan efisien.

    Meskipun demikian, XML masih memiliki relevansi dalam kasus-kasus spesifik yang menuntut validasi skema yang sangat ketat melalui DTD (Document Type Definition) atau XSD (XML Schema Definition), seperti pada sistem konfigurasi enterprise atau layanan web berbasis SOAP.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

    Method is_valid() pada Django Forms merupakan sebuah fungsi krusial yang berfungsi sebagai gerbang validasi untuk semua data yang dikirimkan melalui formulir HTML. Fungsi utamanya adalah:

        - Menjalankan Validasi Data: Method ini mengeksekusi serangkaian aturan validasi yang telah didefinisikan pada kelas Form. Aturan ini mencakup pemeriksaan tipe data, validasi format (misalnya, email), pemenuhan batasan (seperti max_length), dan memastikan semua field yang wajib diisi telah terisi.

        - Membersihkan dan Menyiapkan Data: Jika semua data yang dikirimkan lolos dari proses validasi, is_valid() akan menempatkan versi data yang bersih, aman, dan telah dinormalisasi ke dalam sebuah dictionary bernama form.cleaned_data.

    Pemanfaatan method is_valid() bersifat esensial karena perannya dalam menjaga integritas data dan meningkatkan keamanan aplikasi. Dengan memastikan bahwa hanya data yang valid dan sesuai format yang diproses lebih lanjut (misalnya, disimpan ke basis data), method ini secara efektif mencegah korupsi data dan memitigasi risiko kerentanan yang disebabkan oleh input pengguna yang tidak valid atau berbahaya.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

    {% csrf_token %} adalah template tag yang digunakan di Django untuk mengimplementasikan proteksi terhadap serangan Cross-Site Request Forgery (CSRF). Serangan ini bertujuan untuk mengeksploitasi sesi terautentikasi seorang pengguna untuk melakukan tindakan yang tidak diinginkan atas nama pengguna tersebut.

    Risiko Tanpa csrf_token:
        Apabila sebuah formulir tidak dilindungi oleh csrf_token, seorang penyerang dapat membuat sebuah halaman web berbahaya yang berisi formulir tersembunyi yang menargetkan suatu aksi pada aplikasi kita (misalnya, transfer dana atau penghapusan akun). Jika pengguna yang sedang aktif sesinya di aplikasi kita mengunjungi halaman berbahaya tersebut, skrip di halaman itu dapat secara otomatis mengirimkan formulir palsu ke aplikasi kita. Karena peramban akan secara otomatis menyertakan cookie sesi yang valid dalam permintaan tersebut, server aplikasi kita akan menganggap permintaan itu sah dan mengeksekusinya.

    Mekanisme Proteksi csrf_token:
        Django menghasilkan sebuah token rahasia yang unik untuk setiap sesi pengguna. Dengan menyertakan {% csrf_token %}, token ini akan disisipkan sebagai input tersembunyi di dalam formulir. Ketika formulir dikirimkan, server akan memvalidasi apakah token yang dikirimkan sesuai dengan yang diharapkan untuk sesi pengguna tersebut. Permintaan yang berasal dari situs eksternal tidak akan memiliki akses ke token yang benar, sehingga server akan menolak permintaan tersebut dan serangan CSRF dapat digagalkan.

5.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

        Berikut adalah langkah-langkah yang saya lakukan untuk menyelesaikan tugas ini:

        1) Membuat View untuk Data Delivery (JSON/XML):

            - Pertama, saya buka views.py di aplikasi saya.

            - Saya import HttpResponse dari django.http dan serializers dari django.core.

            - Saya buat 4 fungsi view baru:

                - show_xml dan show_json:   Mengambil semua objek dari model (NamaModel.objects.all()), lalu men-serialize-nya ke format XML atau JSON. Hasilnya dimasukkan ke HttpResponse dengan content_type yang sesuai (application/xml atau application/json).

                - show_xml_by_id dan show_json_by_id: Sama seperti di atas, tapi fungsi ini menerima parameter id. Datanya diambil berdasarkan ID tersebut (NamaModel.objects.filter(pk=id)).

        2) Membuat Routing URL:

            - Saya buka urls.py di dalam direktori aplikasi.

            - Saya import semua view yang baru saya buat tadi dari views.py.

            - Saya tambahkan 4 baris path baru di dalam urlpatterns. Masing-masing path saya arahkan ke fungsi view yang bersesuaian, misalnya path('xml/', show_xml, name='show_xml') dan path('json/<int:id>/', show_json_by_id, name='show_json_by_id').

        3) Membuat Halaman Form Tambah Objek:

            - Saya buat file baru forms.py di dalam aplikasi. Di dalamnya, saya membuat sebuah kelas Form (misal NamaForm) yang merupakan turunan dari forms.ModelForm. Di dalam kelas Meta, saya hubungkan form ini dengan model yang sudah ada dan menentukan field mana saja yang mau ditampilkan.

            - Di views.py, saya buat view baru, misalnya add_item. View ini menangani dua kondisi:

                - request.method == 'GET': Menampilkan halaman dengan form yang masih kosong.

                - request.method == 'POST': Memproses data yang dikirim. Saya panggil form.is_valid(). Jika valid, saya simpan (form.save()) dan redirect user ke halaman utama.

            - Saya buat template HTML-nya (add_item.html). Di dalamnya ada tag <form> dengan method="POST". Yang terpenting, saya tambahkan {% csrf_token %} di dalamnya, lalu {{ form.as_p }} untuk me-render field-field form-nya, dan sebuah tombol submit.

        4) Membuat Halaman Utama (List Objek) dan Halaman Detail:

            - Untuk halaman utama, saya modifikasi view yang sudah ada untuk mengambil semua data dari model dan me-render sebuah template HTML.

            - Di template utama (main.html atau index.html), saya pakai template tag Django {% for item in items %} untuk menampilkan setiap data dalam bentuk tabel atau list.

            - Di setiap baris data, saya tambahkan tombol "Detail" yang link-nya mengarah ke URL detail dengan menyertakan ID objek (href="{% url 'nama_app:show_detail' item.pk %}"). Saya juga menambahkan satu tombol "Add" di luar loop yang mengarah ke halaman form.

            - Untuk halaman detail, saya buat view baru (show_detail) yang mengambil satu objek berdasarkan ID-nya. View ini kemudian me-render template detail.html sambil mengirimkan data objek tersebut.

            - Di template detail.html, saya cukup menampilkan semua atribut dari objek yang diterima dari view.

6. Feedback terhadap asdos

    Materi serta langkah-langkah dalam tutorial mudah dipahami, terutama untuk saya sebagai seorang pemula.

7. Hasil akses URL pada Postman

    - XML: https://drive.google.com/file/d/1y0WgLBHHxmHZ7e1M6pikEk-hWQmIvSI5/view?usp=sharing

    - JSON: https://drive.google.com/file/d/1AIGVez-7dAkKI7zL3QUso6cSPDxZDV_N/view?usp=sharing

    - XML by ID: https://drive.google.com/file/d/10FABSmdeUdhpBVa1jt0Vr-BEbrC42MnN/view?usp=sharing

    - JSON by ID: https://drive.google.com/file/d/13ZRshHZ_vcDB9IK0mCXQ-dNjjBJIfM6v/view?usp=sharing

------------------------------------------------------------------------------------------------------------------------------------------

TUGAS 4

1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.

    Django AuthenticationForm adalah sebuah form class bawaan dari modul django.contrib.auth.forms yang dirancang khusus untuk proses autentikasi (login) pengguna. Form ini tidak terikat langsung dengan model manapun (bukan ModelForm), karena tujuannya bukan untuk membuat atau mengubah data pengguna, melainkan hanya untuk memverifikasi kredensial yang dimasukkan.

    Form ini secara default memiliki dua field: username dan password. Ketika data di-submit, form akan melakukan validasi untuk memeriksa:

        - Apakah pengguna dengan username tersebut ada di database.

        - Apakah password yang dimasukkan cocok untuk pengguna tersebut.

        - Apakah akun pengguna tersebut aktif (is_active flag).

    Jika semua validasi berhasil, form akan mengembalikan objek User yang terautentikasi, yang kemudian bisa digunakan untuk proses login menggunakan fungsi login() dari Django.

    Kelebihan:

        - Keamanan Bawaan: Sudah menangani berbagai aspek keamanan dasar secara otomatis, seperti memeriksa status pengguna (apakah aktif atau tidak) dan validasi kredensial yang aman.

        - Cepat dan Mudah Digunakan: Sebagai bagian dari framework Django, AuthenticationForm sangat mudah diimplementasikan dan mempercepat proses pengembangan karena tidak perlu membuat logika validasi login dari nol.

        - Terintegrasi Penuh: Bekerja dengan mulus bersama sistem autentikasi Django lainnya (User model, views, dan middleware) tanpa  perlu konfigurasi tambahan yang rumit.

    Kekurangan:

        - Kustomisasi Terbatas: Secara default, form ini hanya menerima username dan password. Jika ingin login menggunakan email atau menambahkan fitur seperti "Remember Me", kita perlu membuat subclass dan memodifikasinya sendiri.

        - Tampilan Generik: Tampilan HTML yang dihasilkan sangat dasar. Perlu kustomisasi CSS lebih lanjut agar sesuai dengan desain website yang diinginkan.

        - Hanya untuk Login: Sesuai namanya, form ini hanya untuk autentikasi (login). Untuk registrasi pengguna baru, Django menyediakan form lain yaitu UserCreationForm.

2. Apa perbedaan antara autentikasi dan otorisasi? Bagaimana Django mengimplementasikan kedua konsep tersebut?

    Autentikasi dan Otorisasi adalah dua konsep fundamental dalam keamanan aplikasi, namun memiliki fungsi yang berbeda.

    - Autentikasi (Authentication): Siapa Anda?
    
        Ini adalah proses untuk memverifikasi identitas seorang pengguna. Tujuannya adalah untuk memastikan bahwa pengguna adalah benar-benar orang yang mereka klaim. Contoh paling umum adalah proses login menggunakan username dan password.

        Analogi: Menunjukkan KTP kepada petugas keamanan untuk membuktikan identitas Anda.

    - Otorisasi (Authorization): Apa yang Boleh Anda Lakukan?
    
        Ini adalah proses yang terjadi setelah autentikasi berhasil. Otorisasi menentukan hak akses atau izin yang dimiliki oleh pengguna yang sudah terverifikasi identitasnya. Ini mengatur apa saja yang boleh dan tidak boleh dilakukan oleh pengguna di dalam aplikasi.

        Analogi: Setelah petugas keamanan memverifikasi KTP Anda, ia akan memeriksa daftar tamu untuk melihat apakah Anda diizinkan masuk ke area VIP atau hanya area umum.

    Implementasi di Django:

        Autentikasi di Django:
        Django mengelola autentikasi melalui aplikasi django.contrib.auth. Fitur-fitur utamanya meliputi:

            - Model User: Model bawaan untuk menyimpan informasi pengguna (username, password yang di-hash, email, dll.).

            - Forms: AuthenticationForm untuk login dan UserCreationForm untuk registrasi.

            - Views: LoginView dan LogoutView bawaan untuk menangani proses login dan logout.

            - Session Framework: Untuk menjaga status login pengguna di setiap request. Saat login(request, user) dipanggil, Django akan membuat sesi untuk pengguna tersebut.

    Otorisasi di Django:

    Django memiliki sistem perizinan (permissions) yang sangat kuat:

        - Permissions: Setiap model Django secara otomatis membuat tiga izin dasar: add, change, dan delete. Izin kustom juga bisa ditambahkan.

        - Groups: Pengguna dapat dikelompokkan, dan izin dapat diberikan ke grup secara kolektif. Ini memudahkan manajemen hak akses untuk banyak pengguna.

        - Decorators & Mixins: Django menyediakan decorators seperti @login_required (untuk memastikan pengguna sudah terautentikasi) dan @permission_required (untuk memeriksa izin spesifik) yang bisa diterapkan pada views. Untuk Class-Based Views, tersedia LoginRequiredMixin dan PermissionRequiredMixin.

3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
Cookies dan Session adalah dua mekanisme untuk menyimpan state (informasi pengguna) di antara permintaan HTTP, yang pada dasarnya bersifat stateless.

COOKIES
Cookies adalah data kecil yang disimpan langsung di browser pengguna (sisi klien).

    Kelebihan:

        - Penyimpanan di Klien: Tidak membebani sumber daya server (memori atau database) karena data disimpan di browser pengguna.

        - Persisten: Cookies dapat diatur untuk bertahan dalam waktu yang lama, bahkan setelah browser ditutup, cocok untuk fitur seperti "Remember Me".

        - Sederhana: Mudah dibuat dan dibaca di sisi server.

    Kekurangan:

        - Ukuran Terbatas: Ukuran cookies sangat kecil (sekitar 4KB), tidak cocok untuk menyimpan data yang kompleks.

        - Keamanan Rendah: Karena disimpan di sisi klien, data di dalam cookies dapat dilihat dan dimanipulasi oleh pengguna. Tidak boleh digunakan untuk menyimpan data sensitif seperti password atau informasi pribadi.

        - Overhead Jaringan: Cookies dikirimkan pada setiap request ke server, yang dapat menambah sedikit beban pada bandwidth jika ukurannya besar atau jumlahnya banyak.

SESSION
Session menyimpan data di sisi server, dan hanya mengirimkan sebuah ID unik (Session ID) ke browser pengguna yang disimpan dalam sebuah cookie.

    Kelebihan:

        - Lebih Aman: Data sensitif disimpan di server, bukan di browser. Klien hanya memegang ID sesi yang acak dan sulit ditebak.

        - Kapasitas Lebih Besar: Dapat menyimpan data yang jauh lebih besar dan kompleks dibandingkan cookies.

        - Kontrol Penuh di Server: Pengembang memiliki kontrol penuh atas data sesi, termasuk kapan data tersebut akan kedaluwarsa atau dihapus.

    Kekurangan:

        - Membebani Server: Setiap sesi pengguna aktif akan menggunakan memori atau penyimpanan di server. Pada situs dengan trafik sangat tinggi, ini bisa menjadi masalah skalabilitas.

        - Kompleksitas Skalabilitas: Dalam arsitektur terdistribusi (misalnya, menggunakan beberapa server), manajemen sesi memerlukan solusi tambahan seperti shared session storage (misalnya Redis atau database) agar sesi pengguna konsisten di semua server.

4. Apakah penggunaan cookies aman secara default? Bagaimana Django menangani hal tersebut?

    Tidak, cookies tidak aman secara default. Cookies pada dasarnya hanyalah file teks biasa yang disimpan di browser, sehingga rentan terhadap beberapa risiko keamanan:

        - Pencurian (Hijacking): Jika seorang penyerang berhasil mendapatkan cookie sesi seorang pengguna (misalnya melalui jaringan Wi-Fi publik yang tidak aman), mereka dapat menggunakannya untuk meniru pengguna tersebut.

        - Cross-Site Scripting (XSS): Penyerang dapat menyuntikkan skrip berbahaya ke dalam situs web yang kemudian dapat membaca data dari cookies, termasuk ID sesi.

        - Cross-Site Request Forgery (CSRF): Penyerang menipu pengguna yang sudah login untuk melakukan tindakan yang tidak diinginkan di situs web. Browser secara otomatis akan mengirimkan cookie otentikasi bersama dengan permintaan palsu tersebut.

    Penanganan Keamanan Cookies oleh Django:

        Django menyediakan beberapa lapisan perlindungan untuk membuat penggunaan cookies jauh lebih aman:

            - CSRF Protection: Django memiliki middleware CSRF yang aktif secara default. Ini mengharuskan setiap permintaan POST menyertakan token rahasia ({% csrf_token %}). Hal ini memastikan bahwa permintaan tersebut berasal dari formulir di situs kita sendiri, bukan dari situs lain, sehingga efektif mencegah serangan CSRF.

            - Cryptographic Signing: Django secara kriptografis "menandatangani" banyak cookies yang ditetapkannya, termasuk cookie sesi. Tanda tangan digital ini memungkinkan Django untuk mendeteksi jika cookie telah diubah oleh pihak luar. Jika tanda tangan tidak valid, Django akan mengabaikan cookie tersebut.

            - HTTPOnly Flag: Cookie sesi Django diatur dengan atribut HttpOnly secara default. Atribut ini mencegah JavaScript di sisi klien untuk mengakses cookie, sehingga sangat efektif dalam mengurangi risiko pencurian cookie melalui serangan XSS.

            - Secure Flag: Pengembang dapat mengaktifkan pengaturan SESSION_COOKIE_SECURE = True di settings.py. Ini akan memastikan bahwa cookie sesi hanya dikirim melalui koneksi HTTPS yang terenkripsi, mencegah penyadapan di jaringan.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.

    Berikut adalah langkah-langkah yang saya lakukan untuk mengimplementasikan fungsionalitas autentikasi pada proyek ini:

        1. Membuat Aplikasi Baru untuk Autentikasi:

                Untuk menjaga struktur proyek tetap rapi, saya membuat aplikasi baru bernama authentication dengan perintah python manage.py startapp authentication. Aplikasi ini kemudian saya daftarkan di INSTALLED_APPS dalam file settings.py.

        2. Mengatur URL Routing:

                Saya mengkonfigurasi urls.py utama proyek untuk mengarahkan semua URL yang berawalan auth/ ke urls.py di dalam aplikasi authentication. Di dalam authentication/urls.py, saya mendefinisikan tiga path: register/, login/, dan logout/.

        3. Implementasi Fitur Registrasi:

                - View (views.py): Saya membuat fungsi register yang menangani permintaan GET dan POST. Untuk permintaan POST, saya menggunakan form bawaan Django UserCreationForm. Jika form valid, pengguna baru akan dibuat (form.save()) dan diarahkan ke halaman login.

                - Template (register.html): Saya membuat file HTML yang berisi sebuah form dengan metode POST. Di dalamnya, saya menyertakan {{ form.as_p }} untuk me-render field form dan {% csrf_token %} untuk keamanan.

        4. Implementasi Fitur Login dan Cookies:

                - View (views.py): Saya membuat fungsi login_user. Di sini, saya menggunakan AuthenticationForm. Jika form valid, saya mengambil objek pengguna dari form.get_user() lalu memanggil fungsi login(request, user) untuk membuat sesi.

                - Implementasi Cookie: Setelah login berhasil, saya membuat sebuah HttpResponseRedirect dan menggunakan metode .set_cookie('last_login', str(datetime.now())) pada respons tersebut untuk menyimpan waktu login terakhir pengguna.

                - Template (login.html): Mirip seperti registrasi, saya membuat template dengan form, {{ form.as_p }}, dan {% csrf_token %}.

        5. Implementasi Fitur Logout:

                View (views.py): Saya membuat fungsi logout_user yang sangat sederhana. Fungsi ini hanya memanggil logout(request) dari Django untuk menghapus sesi pengguna, lalu mengarahkannya kembali ke halaman login.

        6. Menghubungkan Model Product dengan User:

                - Saya membuka models.py dari aplikasi produk utama.

                - Pada model Product, saya menambahkan field baru: user = models.ForeignKey(User, on_delete=models.CASCADE). Ini menciptakan hubungan "one-to-many" di mana satu User dapat memiliki banyak Product.

                - Setelah mengubah model, saya menjalankan python manage.py makemigrations dan python manage.py migrate untuk menerapkan perubahan ke database.

        7. Membuat Akun dan Dummy Data:

                - Saya menggunakan python manage.py shell untuk masuk ke shell interaktif Django.

                - Saya membuat dua pengguna baru menggunakan User.objects.create_user(username='...', password='...').

                - Untuk setiap pengguna yang telah dibuat, saya membuat tiga objek Product dan mengaitkannya dengan pengguna tersebut, misalnya: Product.objects.create(name='...', user=user1, ...).

        8. Menampilkan Informasi Pengguna dan Cookie:

                - Pada view halaman utama, saya memodifikasi konteks yang dikirim ke template. Saya menambahkan username dari request.user.username dan nilai cookie last_login yang diambil dari request.COOKIES.get('last_login', 'Ini adalah login pertama Anda!').

                - Di template halaman utama, saya menggunakan tag {% if user.is_authenticated %}. Jika pengguna sudah login, halaman akan menampilkan pesan selamat datang dengan {{ user.username }}, waktu login terakhir dari {{ last_login }}, dan tombol logout. Jika tidak, halaman akan menampilkan tombol untuk login dan registrasi.