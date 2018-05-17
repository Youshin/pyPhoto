from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from .models import Photo

# Create your views here.

def hello(request):
    return HttpResponse('Hi')

def detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    msg = (
        '<p>{pk}번 사진입니다'.format(pk=photo.pk),
        '<p>주소는 {url}</p>'.format(url=photo.image.url),
        '<p><img src="{url}" /></p>'.format(url=photo.image.url),
        '<p>content = "{}"</p>'.format(photo.content)
    )
    return HttpResponse('\n'.join(msg))

def displayImageGrid(request):
    photos = Photo.objects.all()
    msg = []
    for photo in photos:
        msg.append('<img src="{url}" /><br><p>{content}</p>'.format(url=photo.image.url,content=photo.content))
        image1 = []
        image2 = []
    if len(msg) > 1:
        image1 = msg[:len(msg)//2]
        image2 = msg[len(msg)//2:]
        return render(request, 'pyPhoto/imageGrid.html', {'image1': image1 , 'image2': image2})
    else:
        return render(request, 'pyPhoto/imageGrid.html', {'image1': msg } )

