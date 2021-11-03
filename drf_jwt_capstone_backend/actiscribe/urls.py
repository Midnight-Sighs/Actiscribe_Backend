from django.urls import path
from actiscribe import views

# urlpatterns = [
#     path('', views.ResidentList.as_view())
# ]

urlpatterns = [
    path('residents/', views.get_all_residents),
    path('residents/archived/', views.get_archived_residents),
    path('residents/<id>/', views.get_resident_byId)
]