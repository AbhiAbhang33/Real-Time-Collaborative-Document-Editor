from django.urls import path
from . import views

urlpatterns = [
    # Dashboard home
    path('', views.dashboard, name='dashboard'),

    # Create new document
    path('create/', views.create_document, name='create-document'),

    # Edit existing document
    path('editor/<int:doc_id>/', views.editor_view, name='editor'),

    # Delete document
    path('editor/<int:doc_id>/delete/', views.delete_document, name='delete-document'),

    # AI grammar suggestions API
    path('api/grammar-check/', views.ai_suggestions, name='grammar-check'),
]
