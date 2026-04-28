from llama_cpp import Llama
from huggingface_hub import hf_hub_download

from pathlib import Path

class Chatboot:
    def __init__(self, cache_dir: Path = Path("cache-dir")):

        cache_dir.mkdir(exist_ok=True, parents=True)

        model_file = Path("cache-dir/Phi-3-mini-4k-instruct-q4.gguf")

        if not model_file.exists():
            hf_hub_download(
                    repo_id="microsoft/Phi-3-mini-4k-instruct-gguf",
                    filename="Phi-3-mini-4k-instruct-q4.gguf",
                    local_dir="cache-dir")

        self.model = Llama(model_path=str(model_file), n_ctx=4096, 
                           n_threads=8, n_gpu_layers=35, verbose=False)

        self.messages = []

    def __call__(self, question: str):
        self.messages.append({"role": "user", "content": question})

        output = self.model.create_chat_completion(messages=self.messages,
                                                   max_tokens=200,
                                                   temperature=0.7,
                                                   top_p=0.9,
                                                   stop=[". "])
        
        response = output["choices"][0]["message"]["content"]

        self.messages.append({"role": "assistant", "content": response})

        return response
