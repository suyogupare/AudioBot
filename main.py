import streamlit as st
from transformers import pipeline
import time
from gtts import gTTS
import os
import tempfile
import base64

# Set page configuration
st.set_page_config(
    page_title="Speech-Enabled Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize the text generation model (only once)
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="gpt2")  # Using GPT-2 which is more reliable

# Function to convert text to speech
def text_to_speech(text):
    tts = gTTS(text=text, lang='en', slow=False)
    
    # Save the audio file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
        temp_filename = fp.name
        tts.save(temp_filename)
    
    # Read the audio file and encode it to base64
    with open(temp_filename, "rb") as audio_file:
        audio_bytes = audio_file.read()
    
    # Clean up the temporary file
    os.unlink(temp_filename)
    
    # Encode to base64 for HTML embedding
    audio_base64 = base64.b64encode(audio_bytes).decode('utf-8')
    
    # Create HTML audio element
    audio_html = f'<audio autoplay="true" src="data:audio/mp3;base64,{audio_base64}">'
    
    return audio_html

# Function to get response from the free LLM
def get_llm_response(prompt):
    try:
        generator = load_model()
        # Format the prompt to make it more conversational
        formatted_prompt = f"User: {prompt}\nAI Assistant:"
        
        # Generate response
        response = generator(
            formatted_prompt,
            max_length=100,
            num_return_sequences=1,
            temperature=0.7,
            top_p=0.9,
            do_sample=True
        )
        
        # Extract the generated text and clean it up
        generated_text = response[0]['generated_text']
        
        # Try to extract the assistant's response
        try:
            assistant_response = generated_text.split("AI Assistant:")[1].strip()
        except IndexError:
            # If splitting fails, just return everything after the prompt
            assistant_response = generated_text.replace(formatted_prompt, "").strip()
            
        # Clean up the response - limit to a reasonable length
        if len(assistant_response) > 200:
            assistant_response = assistant_response[:200] + "..."
            
        # If response is empty, provide a fallback
        if not assistant_response:
            assistant_response = "I'm not sure how to respond to that. Can you try asking something else?"
            
        return assistant_response
    except Exception as e:
        return f"Sorry, I encountered an error: {str(e)}"

# App title
st.title("🤖 Speech-Enabled Chatbot")
st.markdown("Chat with me and I'll respond with voice!")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("What would you like to talk about?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Display assistant response with a spinner
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = get_llm_response(prompt)
            st.markdown(response)
            
            # Convert response to speech and play it
            audio_html = text_to_speech(response)
            st.markdown(audio_html, unsafe_allow_html=True)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
