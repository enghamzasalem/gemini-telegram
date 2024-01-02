# gemini-telegram

Gemini Pro Bot is an AI-powered chatbot designed to generate content based on user inputs.

## Requirements

- Python 3.6+
- `telepot` library (`pip install telepot`)
- `google.generativeai` library (`pip install -q -U google-generativeai`)

## Installation

1. **Clone the Repository**
    ```
    git clone https://github.com/enghamzasalem/gemini-telegram.git
    cd gemini-pro-bot
    ```

2. **Install Dependencies**
    ```
    pip install telepot
    pip install -q -U google-generativeai
    ```

3. **Setup Google API Key**
    - Obtain a Google API key from the [Google Cloud Console](https://console.cloud.google.com/).
    - Replace `'YOUR_GOOGLE_API_KEY'` in the code with your API key:
        ```python
        genai.configure(api_key="YOUR_GOOGLE_API_KEY")
        ```

4. **Run the Bot**
    - Execute the script:
        ```
        python main.py
        ```
    - The bot will start listening for messages.

## Bot Usage

1. **Interacting with the Bot**
    - Start a conversation with the bot on Telegram.
    - Input any text message to generate content.

2. **Bot Responses**
    - The bot will respond with content generated based on your input.

---
