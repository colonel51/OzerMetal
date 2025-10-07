from django.conf import settings

def business_info(request):
    """Global business bilgilerini template'lere ekler"""
    return {
        'BUSINESS_INFO': getattr(settings, 'BUSINESS_INFO', {})
    }