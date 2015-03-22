from django.db import transaction

from rest_framework import serializers

from profiles.models import (
    OwnerProfile,
    User,
    UserProfile,
    WalkerProfile,
)


from rest_framework.fields import empty


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
        with transaction.atomic():
            user = User.objects.create(**validated_data)
            UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('userprofile')
        try:
            userprofile = instance.userprofile
        except UserProfile.DoesNotExist:
            raise serializers.ValidationError('User is missing user profile')

        instance.password = validated_data.get('password', instance.password)
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
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = OwnerProfile
        fields = ('pk', 'user')
        read_only_fields = ('pk',)


class WalkerProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = WalkerProfile
        fields = ('pk', 'user', 'subscription_status', 'subscription_expiration_date', 'default_rate_per_hour_walked')
        read_only_fields = ('pk',)


# class OwnerSerializer(UserSerializer):
#     def __init__(self, *args, **kwargs):
#         # Instantiate the superclass normally
#         super(OwnerSerializer, self).__init__(*args, **kwargs)

#         self.fields['ownerprofile'] = OwnerProfileSerializer()

#     # def to_representation(self, obj):
#     #     serialized_dict = super(OwnerSerializer, self).to_representation(obj)

#     #     try:
#     #         profile_dict = OwnerProfileSerializer(user.ownerprofile)
#     #     except OwnerProfile.DoesNotExist:
#     #         raise serializers.ValidationError('User is missing owner profile')

#     #     # The profile is selected before the user so that the user's pk is left as the pk (not the profile pk)
#     #     serialized_dict = profile_dict.copy()
#     #     serialized_dict.update(user_dict)

#     #     return serialized_dict

#     def to_internal_value(self, data):
#     #     user_data = {}
#     #     user_fields = UserSerializer.Meta.fields

#     #     for field in user_fields:
#     #         if data.has_key(field) and field != 'pk':
#     #             user_data[field] = data.pop(field)

#     #     data['user'] = user_data

#         ownerprofile

#         return super(OwnerSerializer, self).to_internal_value(data)


# from profiles.serializers import *
# owner = OwnerProfile.objects.first()
# serializer = OwnerProfileSerializer(owner)
# serializer.data

# class UserSerializer(serializers.Serializer):
#     pk = serializers.IntegerField(read_only=True)
#     # url = serializers.URLField(read_only=True)
#     email = serializers.EmailField(required=True)
#     username = serializers.UUIDField(read_only=True)
#     password = serializers.CharField(write_only=True, required=False, allow_blank=False, max_length=128)
#     first_name = serializers.CharField(required=False, allow_blank=True, max_length=30)
#     last_name = serializers.CharField(required=False, allow_blank=True, max_length=30)
#     phone_number = serializers.RegexField(r'^[\d]+$', max_length=11, min_length=1, allow_blank=False)

#     def create(self, validated_data):
#         return User.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.email = validated_data.get('email', instance.email)
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.phone_number = validated_data.get('phone_number', instance.phone_number)

#         instance.save()
#         return instance


# class OwnerProfileSerializer(serializers.Serializer):
#     pk = serializers.IntegerField(read_only=True)
#     user = UserSerializer(read_only=True)
#     address = serializers.CharField(required=False, allow_blank=True)
#     avatar = serializers.ImageField(required=False)

#     def create(self, validated_data):

#         user_validated_data = {}
#         for field in ['email', 'username', 'password', 'first_name', 'last_name', 'phone_number']:
#             if validated_data.has_key(field):
#                 user_validated_data[field] = validated_data[field]

#         owner_validated_data = {}
#         for field in ['address', 'avatar']:
#             if validated_data.has_key(field):
#                 owner_validated_data[field] = validated_data[field]

#         with transaction.atomic():
#             user = User.objects.create(**user_validated_data)
#             owner_validated_data['user'] = user
#         owner_profile = OwnerProfile.objects.create(**owner_validated_data)

#         return owner_profile

#     def update(self, instance, validated_data):
#         instance.email = validated_data.get('email', instance.email)
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.phone_number = validated_data.get('phone_number', instance.phone_number)

#         instance.save()
#         return instance
