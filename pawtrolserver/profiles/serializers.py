from django.db import transaction

from rest_framework import serializers

from profiles.models import (
    OwnerProfile,
    User,
    UserProfile,
    WalkerProfile,
    ServiceBusiness,
)


from rest_framework.fields import empty


class ServiceBusinessSerializer(serializers.ModelSerializer):
    business_owner = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
    )

    class Meta:
        model = ServiceBusiness
        fields = ('pk', 'uuid', 'business_name', 'business_owner', 'subscription_status', 'subscription_expiration_date', )
        read_only_fields = ('pk', 'uuid', 'subscription_status', 'subscription_expiration_date')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('pk', 'address', 'avatar', )
        read_only_fields = ('pk', )


class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ('pk', 'username', 'password', 'email', 'first_name', 'last_name', 'phone_number', 'userprofile', )
        read_only_fields = ('pk', 'username', )
        extra_kwargs = {'password': {'write_only': True}}

    def to_representation(self, obj):
        serialized_dict = super(UserSerializer, self).to_representation(obj)

        for key, value in serialized_dict['userprofile'].items():
            if key != 'pk':
                serialized_dict[key] = value

        serialized_dict.pop('userprofile')

        return serialized_dict

    def to_internal_value(self, data):
        userprofile_data = {}

        for field in UserProfileSerializer.Meta.fields:
            if data.has_key(field) and field != 'pk':
                userprofile_data[field] = data.pop(field)

        data['userprofile'] = userprofile_data

        return super(UserSerializer, self).to_internal_value(data)

    def create(self, validated_data):
        profile_data = validated_data.pop('userprofile')
        password = validated_data.pop('password')
        with transaction.atomic():
            user = User.objects.create(**validated_data)
            user.set_password(password)
            user.save()
            UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('userprofile')
        try:
            userprofile = instance.userprofile
        except UserProfile.DoesNotExist:
            raise serializers.ValidationError('User is missing user profile')

        if validated_data.get('password', None):
            instance.set_password(validated_data.get('password'))
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.save()

        userprofile.address = profile_data.get('address', userprofile.address)
        userprofile.avatar = profile_data.get('avatar', userprofile.avatar)
        userprofile.save()

        return instance


class OwnerProfileSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
    )

    class Meta:
        model = OwnerProfile
        fields = ('pk', 'user')
        read_only_fields = ('pk',)


class WalkerProfileSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
    )
    businesses = serializers.SlugRelatedField(
        many=True,
        queryset=ServiceBusiness.objects.all(),
        required=False,
        slug_field='uuid',
    )

    class Meta:
        model = WalkerProfile
        fields = ('pk', 'user', 'businesses', 'default_rate_per_hour_walked')
        read_only_fields = ('pk',)
