from django.db.models import Prefetch
from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from services.models import Subscription
from services.serializers import SubscriptionSerializer

from services.models import Client


class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.all().prefetch_related(

        Prefetch('client', queryset=Client.objects.all().select_related('user').only('company_name',                                                              'user__email'))
        )
    serializer_class = SubscriptionSerializer
