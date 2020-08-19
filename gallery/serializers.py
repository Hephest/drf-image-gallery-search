from rest_framework import serializers

from gallery.models import Picture


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = (
            'picture_id',
            'author',
            'camera',
            'cropped_picture',
            'full_picture',
            'tags'
        )
