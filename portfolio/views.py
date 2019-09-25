from django.shortcuts import render, redirect

# Create your views here.
from portfolio.models import Photo, PhotoCategory

# Create your views here.
def portfolio_view (request):
    from django.utils.datastructures import MultiValueDictKeyError
    try:
        category_id = int(request.GET['category'])
    except MultiValueDictKeyError:
            category_id = 1
    photos = Photo.objects.filter(category_id=category_id)
    category = PhotoCategory.objects.all()
    context = {
            'category': category,
            'photos': photos,
            'category_id': category_id,
    }
    return render(request, 'portfolio.html', context)

def about_view (request):
    return render(request, 'about.html')

def contact_view (request):
    return render(request, 'contact.html')

def site_notice_view (request):
    return render(request, 'site_notice.html')

def faq_view (request):
    return render(request, 'faq.html')

def special_view (request):
    return render(request, 'special_thanks.html')

def view_404(request, *args, **kwargs):
    return redirect('portfolio_view')
