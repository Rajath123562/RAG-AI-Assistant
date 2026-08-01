# RAG AI Assistant

A simple chatbot that answers questions based on whatever text you feed it. Built this to experiment with retrieval-augmented generation using Google's Gemini API and Streamlit.

The idea is pretty straightforward — you paste some text (docs, policies, notes, whatever) into the sidebar, and the model only uses that context to answer your questions. If the answer isn't in the text, it'll tell you it doesn't know instead of making stuff up.

## What it does

- Takes any text you paste into the sidebar as its knowledge base
- Answers questions strictly from that context
- Keeps chat history so you can have a back-and-forth conversation
- Shows a clear error if the API key is missing or something goes wrong

## Setup

You'll need Python 3.9+ and a Gemini API key (free tier works fine).

```bash
# install dependencies
pip install -r requirements.txt

# set up your API key
cp .env.example .env
# open .env and paste your key from https://aistudio.google.com/apikey

# run it
python -m streamlit run app.py
```

App should open at `http://localhost:8501`.

## Files

```
├── app.py              # all the app logic lives here
├── requirements.txt    # streamlit, google-genai, python-dotenv
├── .env.example        # template for your API key
└── .gitignore
```

## Stack

- **Streamlit** for the UI
- **google-genai** SDK to talk to Gemini (using gemini-2.0-flash)
- **python-dotenv** to load the API key from `.env`

## Notes

- The free Gemini API tier has rate limits (~15 req/min), so if you get a 429 error just wait a minute.
- `.env` is gitignored so your key won't get committed. Only `.env.example` is tracked.
- The dummy context is a fake company policy handbook — replace it with whatever you actually want to query.

## License

MIT
