# AutoPy

Self-improving python code writer and error checker.

⚠️ AutoPy works but may crash or not write complete code yet for all requests.

- Write python code until error-free.
- Auto-installs necessary packages during testing.
- Use langchain and vector database to write more robust python code. (In-Progress)

## Run AutoPy

1. Install OpenAI Python SDK

```python
pip install openai
```
2. Create .env file and add your API Key & Model
```env
OPEN_AI_API_KEY=
MODEL=
```

3. Run Code

```bash
python main.py
```

4. Enter Desired Code

```
What do you want AutoPy to build:
```

5. Test Code

```bash
python code.py
```

Note: if you need an API for your generated code give the key in the prompt and it will add it in the code for you.

## Example Video

[![Watch the video](https://i.ytimg.com/vi/-o1XOOskJ6k/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLAbh3IHU0jVXRtogqlznUhTZLWxVQ)](https://youtu.be/-o1XOOskJ6k)
