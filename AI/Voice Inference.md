---
type: ai-note
description: This is my ai template
---


# Voice Inference

### Objectives

- Learn to set up a local text-to-speech inference server.
- Understand how to clone and configure a GitHub repository for the server.
- Test and change voices using the local server.
- Add custom voices to the server using Piper.

### Instructions

1. **Clone the GitHub Repository**
   - Go to the open AI repository on GitHub.
   - Copy the repository link.
   - Open a terminal in an empty directory on your computer.
   - Type `git clone` and paste the repository link to clone it locally.

2. **Rename the Configuration File**
   - Navigate to the cloned repository.
   - Find the file named `sample.env`.
   - Rename `sample.env` to `speech.env`.

3. **Run Docker Compose**
   - Open a terminal in the repository directory.
   - Run the command `docker compose up`.
   - Wait for the container to download and set up.

4. **Test the Server**
   - Open a browser and go to `localhost:8000`.
   - Navigate to the `health` section and execute to check the status.
   - Go to the `models` section and execute to see available models.

5. **Configure Admin Settings**
   - Go to the admin panel under settings and click on `audio`.
   - Set the API URL to `localhost:8000`.
   - Set the text-to-speech voice to `Nova`.
   - Set the text-to-speech model to `tts1 HD`.
   - Save the settings.

6. **Change Voices**
   - Go back to the GitHub repository.
   - Select a different voice from the available options.
   - Save the new voice settings and test it out.

7. **Add Custom Voices**
   - Go to the Piper section in the GitHub repository.
   - Select a Piper voice and model from Piper samples.
   - Download the `.onnx` model file and `.onnx.json` config file for the selected voice.
   - Add the downloaded files to the repository.

8. **Test Custom Voices**
   - Go back to the admin panel and select the newly added custom voice.
   - Save the settings and test the new voice.
