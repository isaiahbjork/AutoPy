# AutoPy

Self-improving python code writer and error checker.

⚠️ AutoPy works but may crash or not write complete code yet for all requests.

- Write python code until error-free.
- Auto-installs necessary packages during testing.
- Use langchain and vector database to write more robust python code. (In-Progress)
- Get package information from PyPi and Github to make sure code is written correctly. (In-Progress)

## Run AutoPy

1. Install Requirements

```python
pip install -r requirements.txt 
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
python output.py
```

Note: if you need an API for your generated code give the key in the prompt and it will add it in the code for you. Some packages won't install properly so you may have to run this in a python environment.

## Example Video

[![Watch the video](https://i.ytimg.com/vi/-o1XOOskJ6k/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLAbh3IHU0jVXRtogqlznUhTZLWxVQ)](https://youtu.be/-o1XOOskJ6k)
