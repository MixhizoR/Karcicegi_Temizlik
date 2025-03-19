from django.urls import path
from . import views, forms

urlpatterns = [
    path("", views.index, name="index"),
    path("hakkimizda.html", views.hakkimizda, name="hakkimizda"),
    path("iletisim.html", views.iletisim, name="iletisim"),
    path("galeri.html", views.galeri, name="galeri"),
    path("ev-temizligi.html", views.ev_temizligi, name="ev_temizligi"),
    path("ofis-temizligi.html", views.ofis_temizligi, name="ofis_temizligi"),
    path("insaat-sonrasi-temizligi.html", views.insaat_sonrasi_temizligi, name="insaat_sonrasi_temizligi"),
    path("hastane-temizligi.html", views.hastane_temizligi, name="hastane_temizligi"),
    path("dezenfeksiyon.html", views.dezenfeksiyon, name="dezenfeksiyon"),
    path("yurt-temizligi.html", views.yurt_temizligi, name="yurt_temizligi"),
    path("fabrika-temizligi.html", views.fabrika_temizligi, name="fabrika_temizligi"),
    path("isyeri-temizligi.html", views.isyeri_temizligi, name="isyeri_temizligi"),
    path("idari-bina-temizligi.html", views.idari_bina_temizligi, name="idari_bina_temizligi"),
    path("dis-cephe-temizligi.html", views.dis_cephe_temizligi, name="dis_cephe_temizligi"),
    path("villa-temizligi.html", views.villa_temizligi, name="villa_temizligi"),
    path("referanslarimiz.html", views.referanslarimiz, name="referanslarimiz"),
    path("musteri-gorusleri.html", views.musteri_gorusleri, name="musteri_gorusleri"),
    path("yerinde-hali-yikama.html", views.yerinde_hali_yikama, name="yerinde_hali_yikama"),
]
