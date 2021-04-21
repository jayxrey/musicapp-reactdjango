from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UsersSerializer, ArtistsSerializer, RatingsSerializer, PriceSerializer
from .models import Users, Artists, Ratings, Price
from django.template import loader


def createuser(request):
    template = loader.get_template('createuser.html')

    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('password'):
            user = Users()
            user.username = request.POST.get('username')
            user.password = request.POST.get('password')
            user.save()

            return HttpResponse(render(request, 'createuser.html'))

        else:
            return render(request, 'createuser.html', {'ERROR':'Input field is empty'})

    if request.method == 'GET':
        if request.GET.get('user'):
            user = str(request.GET.get('user'))
            ratings = Ratings.objects.filter(username_id = user)
            if not ratings:
                return HttpResponse(render(request, 'createuser.html', {'ERROR': 'no ratings'}))
            else:
                return HttpResponse(render(request, 'createuser.html', {'ratings' : ratings}))


        if request.GET.get('song'):
            song = str(request.GET.get('song'))
            price = Price.objects.filter(song_id = song)
            if not price:
                return HttpResponse(render(request, 'createuser.html', {'ERROR': 'no pricing'}))
            else:
                return HttpResponse(render(request, 'createuser.html', {'price' : price}))

        else:
            return HttpResponse(render(request, 'createuser.html', {'ERROR':'Input field(s) is empty'}))

class UsersView(viewsets.ModelViewSet):       # add this
  serializer_class = UsersSerializer          # add this
  queryset = Users.objects.all()              # add this

class ArtistsView(viewsets.ModelViewSet):       # add this
  serializer_class = ArtistsSerializer          # add this
  queryset = Artists.objects.all()              # add this

class RatingsView(viewsets.ModelViewSet):       # add this
  serializer_class = RatingsSerializer          # add this
  queryset = Ratings.objects.all()              # add this

class PriceView(viewsets.ModelViewSet):       # add this
  serializer_class = PriceSerializer          # add this
  queryset = Price.objects.all()              # add this
