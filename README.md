
# 🚀 Django Blog & Portfolio Project (Hyperspace)

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-4.2+-092E20.svg?style=for-the-badge&logo=django&logoColor=white)](https://djangoproject.com)

Bu proje, Django MVT (Model-View-Template) mimarisi kullanılarak geliştirilmiş; dinamik içerik yönetimi, gelişmiş sayfalama (pagination) ve doğrudan SMTP entegrasyonlu bir iletişim yapısına sahip modern bir blog ve portfolyo web uygulamasıdır. Frontend tarafında HTML5 UP (Hyperspace) şablonu entegre edilerek modern ve duyarlı (responsive) bir arayüz sunulmuştur.

---

## ✨ Öne Çıkan Özellikler

*   **📰 Dinamik İçerik Yönetimi:** Blog yazıları, hizmetler (services) ve portfolyo ögeleri veritabanından dinamik olarak çekilir ve listelenir.
*   **🔗 SEO Dostu URL Yapısı:** Blog detay sayfaları için benzersiz `slug` routing yapısı kullanılmıştır.
*   **📄 Akıllı Sayfalama (Pagination):** Blog listesinde, sunucu tarafında çalışan ve sayfa yüklenme performansını optimize eden sayfalama sistemi entegre edilmiştir.
*   **✉️ SMTP Entegrasyonlu İletişim Formu:** Ziyaretçilerin gönderdiği mesajlar veritabanını şişirmeden, Django'nun  `send_mail` altyapısı kullanılarak doğrudan belirlenen e-posta adresine SMTP üzerinden anlık olarak fırlatılır.
*   **🛡️ Güvenli Altyapı:** CSRF koruması ve güvenli form doğrulama mekanizmaları aktif edilmiştir.

---

## 🛠️ Kullanılan Teknolojiler & Kütüphaneler

*   **Backend:** Python, Django
*   **Database:** SQLite (Geliştirme aşaması için)
*   **Frontend:** HTML5, CSS3, JavaScript, Jinja (Django Template Language)
*   **Tasarım:** HTML5 UP - Hyperspace

---

## 🚀 Kurulum ve Çalıştırma

Projeyi lokalinizde ayağa kaldırmak için aşağıdaki adımları sırasyle takip edebilirsiniz:

### 1. Depoyu Klonlayın
```bash
git clone [https://github.com/Yigoboz/DjangoBlogExample.git](https://github.com/Yigoboz/DjangoBlogExample.git)cd proje-adi
```

### 2. Sanal Ortam Oluşturun ve Aktif Edin

```bash
python -m venv venv

# Windows için:
venv\Scripts\activate

# macOS/Linux için:
source venv/bin/activate
```

### 3. Gerekli Paketleri Yükleyin

```bash
pip install -r requirements.txt
```

### 4. Veritabanı Göçlerini (Migrations) Tamamlayın

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Süper Kullanıcı (Admin) Oluşturun

```bash
python manage.py createsuperuser
```

### 6. Sunucuyu Başlatın

```bash
python manage.py runserver
```

Uygulamaya tarayıcınızdan `http://127.0.0.1:8000/` adresinden erişebilirsiniz. Admin paneline ise `http://127.0.0.1:8000/admin/` üzerinden giriş yapabilirsiniz.

---


