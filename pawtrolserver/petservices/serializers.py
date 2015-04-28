from django.db import transaction

from rest_framework import serializers

from petservices.models import (
    Dog,
)

from profiles.models import (
    OwnerProfile,
)


class DogSerializer(serializers.ModelSerializer):
    ownerprofile = serializers.SlugRelatedField(
        queryset=OwnerProfile.objects.all(),
        slug_field='user__username',
    )

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
