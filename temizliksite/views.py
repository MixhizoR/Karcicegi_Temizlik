from django.shortcuts import render, redirect
from .models import Comment, Photo
from .forms import CommentForm

def index(request):
    comments = Comment.objects.all()
    star_range = range(1,6)
    photos = Photo.objects.all().order_by('-date')[:6]
    return render(request, 'temizliksite/index.html',
    {'comments': comments, 'star_range': star_range, 'photos': photos})
    

def dezenfeksiyon(request):
    return render(request, 'temizliksite/dezenfeksiyon.html')

def dis_cephe_temizligi(request):
    return render(request, 'temizliksite/dis-cephe-temizligi.html')

def ev_temizligi(request):
    return render(request, 'temizliksite/ev-temizligi.html')

def ofis_temizligi(request):
    return render(request, 'temizliksite/ofis-temizligi.html')

def fabrika_temizligi(request):
    return render(request, 'temizliksite/fabrika-temizligi.html')

def hastane_temizligi(request):
    return render(request, 'temizliksite/hastane-temizligi.html')

def idari_bina_temizligi(request):
    return render(request, 'temizliksite/idari-bina-temizligi.html')

def insaat_sonrasi_temizligi(request):
    return render(request, 'temizliksite/insaat-sonrasi-temizligi.html')

def isyeri_temizligi(request):
    return render(request, 'temizliksite/isyeri-temizligi.html')

def musteri_gorusleri(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('musteri_gorusleri')  # Redirect to musteri_gorusleri
    else:
        form = CommentForm()
    
    comments = Comment.objects.all()
    star_range = range(1,6)
    return render(request, 'temizliksite/musteri-gorusleri.html',
    {'comments': comments, 'star_range': star_range, 'form': form})

def ofis_temizligi(request):
    return render(request, 'temizliksite/ofis-temizligi.html')

def villa_temizligi(request):
    return render(request, 'temizliksite/villa-temizligi.html')

def yerinde_hali_yikama(request):
    return render(request, 'temizliksite/yerinde-hali-yikama.html') 

def yurt_temizligi(request):
    return render(request, 'temizliksite/yurt-temizligi.html')

def hakkimizda(request):
    return render(request, 'temizliksite/hakkimizda.html')

def iletisim(request):
    return render(request, 'temizliksite/iletisim.html')

def galeri(request):
    photos = Photo.objects.all()
    return render(request, 'temizliksite/galeri.html', {'photos': photos})

def referanslarimiz(request):
    return render(request, 'temizliksite/referanslarimiz.html')
