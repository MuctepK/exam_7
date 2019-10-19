from django.contrib import admin
from django.urls import path
from webapp.views import PollListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PollListView.as_view(), name='index')
]
