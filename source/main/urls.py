from django.contrib import admin
from django.urls import path
from webapp.views import PollListView, PollDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PollListView.as_view(), name='index'),
    path('poll/<int:pk>', PollDetailView.as_view(), name='view_poll')
]
