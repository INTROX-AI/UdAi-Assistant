# UdAi Assistant 🤖

UdAi Assistant is an intelligent AI-driven tool designed to streamline and enhance school assemblies. Powered by Google's Gemini 1.5 Flash model, UdAi offers both text and voice interaction capabilities, making it an ideal companion for educational environments. Whether it's guiding prayer sessions, announcing achievements, or playing instructional videos, UdAi ensures seamless and engaging assembly experiences.

![UdAi Interface](https://github.com/INTROX-AI/INTROX-AI/blob/eceefd0da19781bd943052b117ad97ed3fea77e1/assets/screenshotudai.jpeg)

## 🌟 Features

- **Dual Interaction Modes**: Communicate via text input or voice commands.
- **Automated Video Playback**: Plays specific videos based on user commands (e.g., prayers, news, yoga).
- **Real-time AI Responses**: Instantaneous responses powered by Google Gemini.
- **Responsive Design**: Optimized for both desktop and mobile devices.
- **Voice Recognition**: Utilizes SpeechRecognition API for voice inputs.
- **Text-to-Speech**: Converts AI responses to audio using pyttsx3.
- **Full-Screen Playback**: Automatically enters full-screen mode for video presentations.

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Flask
- **AI Model**: Google Gemini 1.5 Flash
- **Speech Processing**:
  - **Text-to-Speech**: pyttsx3
  - **Speech Recognition**: SpeechRecognition
- **Others**:
  - Google Generative AI API
  - Bootstrap (optional for enhanced UI components)

## 🚀 Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/udai-assistant.git
   cd udai-assistant
   ```

2. **Create a Virtual Environment (Optional but Recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Required Packages**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Google API Key**

   - Obtain your Google Generative AI API key.
   - Create a `.env` file in the root directory and add your API key:

     ```env
     GOOGLE_API_KEY=your_google_api_key_here
     ```

   - Ensure that your `main.py` reads the API key from the environment variable.

5. **Run the Application**

   ```bash
   python main.py
   ```

6. **Access the Application**

   - Open your browser and navigate to `http://localhost:5000`.

## 📋 Requirements

Ensure you have Python installed (preferably Python 3.7 or higher).

Dependencies are listed in the `requirements.txt` file:
