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