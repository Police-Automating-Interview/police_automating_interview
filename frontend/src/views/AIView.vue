<template>
  <div class="transcription-page">
    <header class="header">
      <h1>AI Audio Transcription</h1>
    </header>

    <div class="upload-section">
      <input type="file" @change="handleFileUpload" accept="audio/*" />
      <button @click="submitAudio">Submit</button>
    </div>

    <div class="chat-box">
      <div v-for="(message, index) in messages" :key="index" class="message">
        <div class="user-bubble">Audio:</div>
        <div class="ai-bubble">
          <textarea v-model="messages[index]" rows="5"></textarea>
        </div>
      </div>
    </div>

    <div v-if="messages.length > 0" class="save-section">
      <button @click="saveTranscription">Save</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      file: null,
      messages: [], // Array to store transcription messages
      currentTranscriptionId: null, // To track the ID of the transcription for saving
    };
  },
  methods: {
    handleFileUpload(event) {
      this.file = event.target.files[0];
    },
    async submitAudio() {
      if (!this.file) {
        alert('Please select a file to upload');
        return;
      }

      const formData = new FormData();
      formData.append('audio_file', this.file);

      try {
        // Clear previous messages
        this.messages = [];
        this.currentTranscriptionId = null; // Reset transcription ID

        // Send the audio file to the server
        const response = await axios.post(
          'http://127.0.0.1:8000/api/transcribe/',
          formData,
          {
            headers: {
              'Content-Type': 'multipart/form-data',
            },
          }
        );

        // Display only the new transcription
        this.messages.push(response.data.transcription_text);
        this.currentTranscriptionId = response.data.id; // Store the transcription ID
      } catch (error) {
        console.error(error);
        alert('Error processing the audio file');
      }
    },
    async saveTranscription() {
      if (!this.currentTranscriptionId) {
        alert('No transcription to save.');
        return;
      }

      try {
        // Send the modified transcription back to the server
        await axios.put(`http://127.0.0.1:8000/api/transcribe/${this.currentTranscriptionId}/`, {
          transcription_text: this.messages[0],
        });

        alert('Transcription saved successfully!');
      } catch (error) {
        console.error(error);
        alert('Error saving the transcription.');
      }
    },
  },
};
</script>

<style>
/* General page styling */
.transcription-page {
  font-family: Arial, sans-serif;
  max-width: 800px;
  margin: 10% auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

/* Header styles */
.header {
  text-align: center;
  margin-bottom: 20px;
}

.header h1 {
  color: #333;
}

/* Upload section styles */
.upload-section {
  display: flex;
  gap: 10px;
  justify-content: center;
  margin-bottom: 20px;
}

.upload-section input[type="file"] {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.upload-section button {
  padding: 10px 20px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.save-section button {
  padding: 10px 20px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.upload-section button:hover {
  background-color: #0056b3;
}

.save-section button:hover {
  background-color: #0056b3;
}

/* Chat box styles */
.chat-box {
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 15px;
  max-height: 400px;
  overflow-y: auto;
}

.message {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.user-bubble,
.ai-bubble {
  max-width: 100%;
  padding: 10px;
  border-radius: 15px;
  margin: 5px;
}

.user-bubble {
  background-color: #007bff;
  color: #fff;
  align-self: flex-start;
  margin-right: auto;
}

.ai-bubble {
  background-color: #f1f1f1;
  min-width: 650px;
  color: #333;
  align-self: flex-end;
  margin: 0;
}

/* Scrollbar customization */
.chat-box::-webkit-scrollbar {
  width: 6px;
}

.chat-box::-webkit-scrollbar-thumb {
  background-color: #007bff;
  border-radius: 3px;
}

.chat-box::-webkit-scrollbar-track {
  background-color: #f1f1f1;
}

.ai-bubble textarea{
  width: 100%;

}
</style>
