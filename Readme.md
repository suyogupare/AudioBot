# Speech-Enabled Chatbot with GPT-2 and Streamlit

This project implements a speech-enabled chatbot using Streamlit for the user interface, GPT-2 for text generation, and Google Text-to-Speech (gTTS) for converting text responses to speech.

## 🚀 Overview
The application provides a chat interface where users can type messages, and the AI responds with both text and speech. The conversation history is maintained throughout the session.

## ✨ Features
- 🤖 **Interactive chat interface**  
- 🔊 **Text-to-speech responses**  
- 💬 **Conversation history**  
- 🧠 **Powered by GPT-2 language model**  
- 🌐 **No API keys required**  

## ⚙️ How It Works

### Code Explanation

#### Setup and Initialization:
- The application uses Streamlit for the web interface  
- Session state is used to maintain chat history  
- The GPT-2 model is loaded once and cached using `@st.cache_resource`  

#### Text-to-Speech Functionality:
- The `text_to_speech()` function converts text to speech using Google's TTS service  
- It creates a temporary audio file, encodes it to base64, and embeds it in an HTML audio element  
- The audio plays automatically when rendered  

#### LLM Response Generation:
- The `get_llm_response()` function formats the user's prompt and sends it to GPT-2  
- It extracts the AI's response from the generated text  
- The response is cleaned and formatted for better readability  
- Error handling ensures the user always gets a response  

#### User Interface:
- The chat history is displayed at the top  
- User input is captured via a chat input field  
- Responses are displayed with a spinner while the model is thinking  
- Both text and audio responses are presented to the user  

## 🔧 Technical Details

### Model
- Uses the pre-trained **GPT-2 model**, which is a free and open-source language model  

### Text Generation Parameters
- `max_length=100`: Limits the length of generated text  
- `temperature=0.7`: Controls randomness (higher = more random)  
- `top_p=0.9`: Nucleus sampling parameter for more diverse responses  
- `do_sample=True`: Enables sampling for more natural text  

### Response Processing
- Extracts the assistant's response from the generated text  
- Limits response length to avoid overly long messages  
- Provides fallback responses when needed  

## 🛠️ Installation

### Clone the repository:
```bash
git clone https://github.com/suyogupare/AudioBot.git
cd speech-chatbot
```

### Install the required packages:
```bash
pip install -r requirements.txt
```

### Run the application:
```bash
streamlit run app.py
```

## 📦 Requirements
```
altair==5.5.0  
attrs==25.3.0  
blinker==1.9.0  
cachetools==5.5.2  
certifi==2025.1.31  
charset-normalizer==3.4.1  
click==8.1.8  
colorama==0.4.6  
filelock==3.18.0  
fsspec==2025.3.0  
gitdb==4.0.12  
GitPython==3.1.44  
gTTS==2.5.4  
huggingface-hub==0.29.3  
idna==3.10  
Jinja2==3.1.6  
jsonschema==4.23.0  
jsonschema-specifications==2024.10.1  
MarkupSafe==3.0.2  
mpmath==1.3.0  
narwhals==1.32.0  
networkx==3.4.2  
numpy==2.2.4  
packaging==24.2  
pandas==2.2.3  
pillow==11.1.0  
protobuf==5.29.4  
pyarrow==19.0.1  
pydeck==0.9.1  
pygame==2.6.1  
python-dateutil==2.9.0.post0  
pytz==2025.2  
PyYAML==6.0.2  
referencing==0.36.2  
regex==2024.11.6  
requests==2.32.3  
rpds-py==0.23.1  
safetensors==0.5.3  
six==1.17.0  
smmap==5.0.2  
streamlit==1.43.2  
sympy==1.13.1  
tenacity==9.0.0  
tokenizers==0.21.1  
toml==0.10.2  
torch==2.6.0  
tornado==6.4.2  
tqdm==4.67.1  
transformers==4.50.0  
typing_extensions==4.12.2  
tzdata==2025.2  
urllib3==2.3.0  
watchdog==6.0.0  
```

## ⚠️ Limitations
- The GPT-2 model may sometimes generate responses that are not directly related to the input  
- The first run may be slow as it downloads the model  
- Audio playback requires browser support for HTML5 audio  
- The model runs locally, so performance depends on your hardware  

## 🙏 Acknowledgments
- **Hugging Face** for providing the transformers library and pre-trained models  
- **Google** for the Text-to-Speech API  
- **Streamlit** for the easy-to-use web interface framework and deployment  

