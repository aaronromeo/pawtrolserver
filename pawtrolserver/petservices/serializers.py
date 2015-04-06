from django.db import transaction

from rest_framework import serializers

from petservices.models import (
    Dog,
)


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = (
            'pk',
            'avatar',
            'coat_pattern',
            'date_joined',
            'description',
            'dob',
            'is_dob_estimated',
            'microchip_number',
            'name',
            'ownerprofile',
            'primary_breed',
            'primary_coat_color',
            'secondary_breed',
            'secondary_coat_color',
            'vet_name',
            'vet_number',
            'weight',
        )
        read_only_fields = ('pk', 'date_joined', )
