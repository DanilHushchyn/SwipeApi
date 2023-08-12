from rest_framework import serializers

from builder.models import *


class ComplexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complex
        fields = "__all__"


class CorpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corp
        fields = "__all__"


class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = "__all__"


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = "__all__"


class SewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sewer
        fields = "__all__"


class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flat
        fields = "__all__"


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = "__all__"


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = "__all__"


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"
