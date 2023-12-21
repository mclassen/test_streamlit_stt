import streamlit as st
import streamlit.components.v1 as components

# JavaScript for speech recognition
js = """
<button id="start">Start Recognition</button>
<script>
    var startButton = document.getElementById('start');
    var recognition = new webkitSpeechRecognition();
    recognition.continuous = false;
    recognition.interimResults = false;
    
    recognition.onresult = function(event) {
        var text = event.results[0][0].transcript;
        Streamlit.setComponentValue(text);
    };

    recognition.onend = function() {
        recognition.stop();
    }

    startButton.onclick = function() {
        recognition.start();
    };
</script>
"""

# Embed the JavaScript in the app
components.html(js, height=100) #, key="speech_recognition")

# Callback to handle text updates
def on_text_update():
    if "data" in st.session_state:
        text.text("You said: " + st.session_state["data"])
    else:
        text.text("I heard nothing")

# Display recognized text
text = st.empty()
on_text_update()