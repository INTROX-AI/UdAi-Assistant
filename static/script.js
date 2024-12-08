// Add event listener for Enter key
document.getElementById('user-input').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        sendMessage();
    }
});

function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    if (!userInput.trim()) return; // Prevent empty messages
    
    fetch('/send_message', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userInput }),
    })
    .then(response => response.json())
    .then(data => {
        const chatBox = document.getElementById('chat-box');
        chatBox.innerHTML += `<p><strong>You:</strong> ${userInput}</p>`;
        chatBox.innerHTML += `<hr>`;
        
        if (data.response.startsWith('play_')) {
            const videoType = data.response.replace('play_', '');
            playVideo(videoType);
        } else {
            chatBox.innerHTML += `<p><strong>Assistant:</strong> ${data.response}</p>`;
            document.getElementById('user-input').value = '';
            chatBox.scrollTop = chatBox.scrollHeight;
            
            document.getElementById('status-gif').src = 'static/speaking.gif';
            const audio = new Audio(`static/response.mp3?${Date.now()}`);
            audio.play();
            audio.onended = () => {
                document.getElementById('status-gif').src = 'static/listening.gif';
            };
        }
    });
}

// Single function to handle all video playback
function playVideo(videoType) {
    const videoContainer = document.getElementById('video-container');
    videoContainer.innerHTML = `<video id="${videoType}-video" src="static/${videoType}.mp4" controls autoplay></video>`;
    const video = document.getElementById(`${videoType}-video`);
    video.requestFullscreen();
    video.onended = () => {
        document.exitFullscreen();
        videoContainer.innerHTML = '<img id="status-gif" src="static/listening.gif" alt="Listening">';
    };
}

// Voice recognition
const voiceButton = document.getElementById('voice-button');
voiceButton.addEventListener('click', () => {
    startVoiceRecognition();
});

function startVoiceRecognition() {
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = 'en-US';
    recognition.start();

    recognition.onresult = function(event) {
        const voiceInput = event.results[0][0].transcript;
        document.getElementById('user-input').value = voiceInput;
        sendMessage();
    };

    recognition.onerror = function(event) {
        console.error(event.error);
    };

    recognition.onend = function() {
        console.log("Voice recognition ended.");
    };
}

// Fullscreen toggle
document.addEventListener('keydown', (event) => {
    if (event.key === 'F11') {
        event.preventDefault();
        toggleFullScreen();
    }
});

function toggleFullScreen() {
    if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen();
    } else {
        if (document.exitFullscreen) {
            document.exitFullscreen();
        }
    }
}