from django.contrib import admin
from django.urls import path
from webapp.views import PollListView, PollDetailView, PollCreateView, PollUpdateView, PollDeleteView, ChoiceUpdateView, \
    ChoiceDeleteView, ChoiceCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PollListView.as_view(), name='index'),
    path('poll/<int:pk>', PollDetailView.as_view(), name='view_poll'),
    path('poll/create/', PollCreateView.as_view(), name='create_poll'),
    path('poll/update/<int:pk>', PollUpdateView.as_view(), name='update_poll'),
    path('poll/delete/<int:pk>', PollDeleteView.as_view(), name='delete_poll'),
    path('choice/update/<int:pk>',ChoiceUpdateView.as_view(), name='update_choice'),
    path('choice/delete/<int:pk>', ChoiceDeleteView.as_view(), name='delete_choice'),
    path('choice/create/<int:pk>', ChoiceCreateView.as_view(), name='create_choice')
]
