from django.urls import path
from actiscribe import views


urlpatterns = [
    path('residents/', views.get_all_residents),
    path('residents/archived/', views.get_archived_residents),
    path('residents/<id>/', views.get_resident_by_id),
    path('residents/<id>/notes/', views.get_notes_by_resident),
    path('residents/<id>/assessment/', views.assessments),
    path('residents/<id>/participation/',views.resident_participation),
    path('notes/<note_id>/', views.get_notes_by_id),
    path('activities/', views.get_all_activities),
    path('activities/archived/', views.get_archived_activities),
    path('activities/<id>/', views.edit_activities),
    path('activities/<id>/participation/', views.activity_participation),
    path('<dow>/', views.activities_by_dow),
    path('participation/<id>/', views.manage_participation),
    
]