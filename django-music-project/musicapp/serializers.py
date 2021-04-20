from rest_framework import serializers
from .models import Artists

# The serializer translates a Todo object into a format that
# can be stored in our database. We use the Todo model.
class ArtistsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Artists
    fields = ('song', 'artist', 'album','genre','year')
