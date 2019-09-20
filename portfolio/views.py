from django.shortcuts import render

# Create your views here.
from portfolio.models import Photo

# Create your views here.
def portfolio_view (request):
    from django.utils.datastructures import MultiValueDictKeyError
    try:
        category_id = request.POST['category']
    except MultiValueDictKeyError:
            category_id = 1
    photos = Photo.objects.filter(category_id=category_id)
    context = {
            'photos': photos,
            'category_id': category_id,
    }
    return render(request, 'portfolio.html', context)
