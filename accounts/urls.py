from django.urls import path

from .views import AccountList, AccountDetail

urlpatterns = [
    path("<int:pk>/", AccountDetail.as_view(), name="account_detail"),
    path("", AccountList.as_view(), name="account_list"),
]
