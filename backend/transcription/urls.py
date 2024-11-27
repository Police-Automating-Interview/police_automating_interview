from django.urls import path
from .views import transcribe_audio, update_transcription

urlpatterns = [
    path('transcribe/', transcribe_audio, name='transcribe_audio'),
    path('transcribe/<int:transcription_id>/', update_transcription, name='update_transcription'),
]
