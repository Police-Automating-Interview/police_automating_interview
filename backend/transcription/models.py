from django.db import models

class Transcription(models.Model):
    audio_file = models.CharField(max_length=255)  
    transcription_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

