from django.urls import path
from Chat import views


urlpatterns = [
    path('Conversation/', views.ConversationView.as_view()),
    path('Ticket/', views.TicketView.as_view()),

]
