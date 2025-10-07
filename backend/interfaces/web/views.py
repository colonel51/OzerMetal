from django.shortcuts import render

def home_view(request):
    """Ana sayfa view'ı"""
    return render(request, 'home.html')

def about_view(request):
    """Hakkımızda sayfası view'ı"""
    return render(request, 'about.html')

def contact_view(request):
    """İletişim sayfası view'ı"""
    return render(request, 'contact.html')