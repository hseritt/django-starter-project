from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from .models import Event


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            "url",
            "username",
            "email",
            "is_staff",
        ]


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "description",
            "created",
            "modified",
            "active",
        ]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    http_method_names = [
        u"get",
        u"post",
        u"put",
        u"patch",
        u"delete",
        u"head",
        u"options",
        u"trace",
    ]
