from django.urls import path
from Admin import views


urlpatterns = [
    path('users/', views.ShowUsers.as_view()),
    path('admins/', views.ShowAdminUsers.as_view()),
    path('addAdmin/', views.AddAdmin.as_view()),
    path('removeAdmin/', views.RemoveAdmin.as_view()),
    path('coversations/', views.ShowAllConversations.as_view()),
    path('tickets/', views.ShowAllTickets.as_view()),
    path('sendTicket/', views.SendTicket.as_view()),   
]
