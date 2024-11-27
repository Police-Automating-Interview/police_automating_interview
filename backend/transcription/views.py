from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Transcription
import whisper
import os

# Load Whisper model once to avoid reloading for every request
model = whisper.load_model("base")

@api_view(['POST'])
def transcribe_audio(request):
    """
    Endpoint to upload an audio file, transcribe it, and save the result in the database.
    """
    try:
        # Ensure the request has a file
        if 'audio_file' not in request.FILES:
            return Response({'detail': 'Audio file is required'}, status=status.HTTP_400_BAD_REQUEST)

        audio_file = request.FILES['audio_file']  # Get uploaded audio file

        # Save the file to a temporary location for processing
        file_path = f"temp/{audio_file.name}"
        os.makedirs('temp', exist_ok=True)  # Ensure temp directory exists
        with open(file_path, 'wb') as f:
            for chunk in audio_file.chunks():
                f.write(chunk)

        # Process the audio file with Whisper
        result = model.transcribe(file_path)
        transcription_text = result["text"]

        # Save the transcription to the database
        transcription = Transcription.objects.create(
            # user=request.user if request.user.is_authenticated else None,
            audio_file=audio_file,
            transcription_text=transcription_text
        )

        # Delete the temporary file after processing
        os.remove(file_path)

        return Response({
            'id': transcription.id,
            'audio_file': transcription.audio_file.url,
            'transcription_text': transcription_text,
        }, status=status.HTTP_201_CREATED)

    except Exception as e:
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
