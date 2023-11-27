from langchain import HuggingFaceHub
import os
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
llm = HuggingFaceHub(repo_id="google/flan-t5-xl", model_kwargs={"temperature":0, "max_length":64})

prompt = """Question: Can Barack Obama have a conversation with George Washington?

Let's think step by step.

Answer: """
llm(prompt)