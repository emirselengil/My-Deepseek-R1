# My Deepseek R1

## Overview
`my-deepseek-r1.py` is a Streamlit-based chatbot interface that interacts with the `deepseek-r1:14b` model via a local API. The application allows users to input prompts and receive AI-generated responses in a chat-like format.

## Features
- Streamlit-based UI for an interactive chatbot experience.
- Stores chat messages in session state.
- Sends user prompts to a locally hosted Deepseek R1 model.

## Installation
### Prerequisites
- Python 3.8+
- Streamlit
- Requests library
- [Ollama](https://ollama.com) installed
- Deepseek R1 model installed and running via Ollama

### Setup
1. Install Ollama by following the instructions at [Ollama's website](https://ollama.com).
2. Install the Deepseek R1 model by running:
   ```sh
   ollama pull deepseek-r1:14b
   ```
3. Clone the repository or copy the script.
4. Install required dependencies:
   ```sh
   pip install streamlit requests
   ```
5. Ensure the Deepseek R1 model is running locally at `http://localhost:11434/api/generate`:
   ```sh
   ollama serve
   ```

## Usage
1. Run the Streamlit app:
   ```sh
   streamlit run my-deepseek-r1.py
   ```
2. Enter a prompt in the input field.
3. The AI generates a response and displays it in the chat interface.

## Author
Emir SELENGİL
