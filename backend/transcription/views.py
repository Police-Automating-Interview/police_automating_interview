from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Transcription
import whisper
import tempfile
from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError
import os

# Load Whisper model once to avoid reloading for every request
model = whisper.load_model("base")



@api_view(['POST'])
def transcribe_audio(request):
    try:
        if 'audio_file' not in request.FILES:
            return Response({'detail': 'Audio file is required'}, status=status.HTTP_400_BAD_REQUEST)

        audio_file = request.FILES['audio_file']

        # Use a temporary file to handle the uploaded file
        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{audio_file.name.split('.')[-1]}") as temp_audio_file:
            # Write the uploaded file to a temporary file
            for chunk in audio_file.chunks():
                temp_audio_file.write(chunk)
            temp_audio_file.flush()

            # Transcribe the audio file
            result = model.transcribe(temp_audio_file.name)
            transcription_text = result["text"]

        # Clean up the temporary file
        temp_audio_file.close()

        transcription = Transcription.objects.create(
            audio_file=audio_file.name,
            transcription_text=transcription_text
        )

        return Response({
            'id': transcription.id,
            'audio_file': transcription.audio_file,
            'transcription_text': transcription_text,
        }, status=status.HTTP_201_CREATED)

    except Exception as e:
        # It's generally a good idea to log the exception details here to understand what went wrong
        return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    

@api_view(['PUT'])
def update_transcription(request, transcription_id):
    """
    Endpoint to update a transcription's text.
    """
    try:
        transcription = Transcription.objects.get(id=transcription_id)
        transcription_text = request.data.get('transcription_text')
        
        if not transcription_text:
            return Response({'detail': 'Transcription text is required'}, status=status.HTTP_400_BAD_REQUEST)

        transcription.transcription_text = transcription_text
        transcription.save()

        return Response({'detail': 'Transcription updated successfully'}, status=status.HTTP_200_OK)
    except Transcription.DoesNotExist:
        return Response({'detail': 'Transcription not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
