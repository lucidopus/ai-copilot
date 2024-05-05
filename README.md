# AI Copilot

This AI Copilot is an intelligent system that provides real-time conversational guidance and insights to sales professionals during live customer interactions. It leverages large language models and natural language processing to dynamically analyze ongoing dialogues, identify potential objections or areas requiring clarification, and generate contextually relevant suggestions to steer the conversation towards a successful close.

## Features

- Real-time conversation analysis using state-of-the-art natural language processing models
- Dynamic generation of relevant suggestions, rebuttals, and talking points
- Seamless integration with existing CRM and communication platforms
- Continuous learning and adaptation to improve suggestion quality
- RESTful API for easy integration with various applications

## Tech Stack

- Python
- FastAPI
- Groq AI (For utilizing models hosted on LPUs)
- Uvicorn (ASGI server)
- Jinja2 (Templating)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/lucidopus/ai-copilot.git
```

2. Navigate to the project directory:

```bash
cd ai-copilot
```

3. Create a virtual environment and install the required dependencies:

```bash
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
pip install -r requirements.txt
```

4. Create a .env file in the project root directory and add your API keys and model configurations:

```bash
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=your_groq_model
API_KEY=your_api_key
```

## Usage

1. Start the FastAPI server:

```bash
uvicorn main:app --reload
```

2. The API will be available at http://localhost:8000. You can use tools like Postman or cURL to interact with the API endpoints.

3. To get suggestions for a conversation, send a POST request to /get_suggestions with the following payload:

```json
{
  "conversation_history": "The history of the conversation goes here.",
  "calling_purpose": "Purpose of the call as an additional piece of context for the model goes here."
}
```

## Interact with the hosted API

You can interact with the AI Copilot API using tools like cURL or Postman. Here's an example of how to get suggestions for a conversation:

```bash
curl -X 'POST' \
  'https://convodroid.onrender.com/get_suggestions' \
  -H 'accept: application/json' \
  -H "X-API-Key: $CONVODROID_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
  'conversation_history': 'The history of the conversation goes here.',
  'calling_purpose': 'Purpose of the call as an additional piece of context for the model goes here.'
}'
```

For access to the Copilot API, please send a request for an API key to [send a request for an API key](mailto:harshilpatel30402@gmail.com?subject=[Request for an API Key for AI Copilot]).
