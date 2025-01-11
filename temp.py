import langchain
from langchain_huggingface import HuggingFaceEndpoint
import pandas as pd

repo_ids = [
    "PowerInfer/SmallThinker-3B-Preview",
    "mistralai/Mistral-Nemo-Instruct-2407",
    "microsoft/Phi-3-mini-4k-instruct",
    "Qwen/Qwen2.5-1.5B-Instruct",
    "meta-llama/Llama-3.2-1B",
    "google/gemma-2-2b-it",
    "microsoft/Phi-3.5-mini-instruct"
]

sec_key = "api token"

def test_llms():
    results = {"Input": []}

    for repo_id in repo_ids:
        results[repo_id] = []

    with open('query.txt', 'r') as file:
        prompts = file.readlines()


    results["Input"].extend(prompts)


    for repo_id in repo_ids:
        print(f"Testing model: {repo_id}")
        llm = HuggingFaceEndpoint(repo_id=repo_id, max_length=50, temperature=0.1, token=sec_key)

        for prompt in prompts:
            response = llm.invoke(prompt)
            print(f"Question: {prompt}")
            print(f"Answer: {response}")
            results[repo_id].append(response)


    df = pd.DataFrame(results)
    df.to_csv("llm_comp.csv", index=False)
    print("Results saved to llm_comp.csv")

test_llms()
