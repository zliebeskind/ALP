Api_key = "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"

from huggingface_hub.inference_api import InferenceApi

inference = InferenceApi(repo_id="gpt2-large", token=Api_key)

prompt = input("Prompt: ")
topP = {'max_length': 128, 'top_p': 0.95, 'do_sample': True}

result = inference(prompt, topP)
print("This is the top p result ----  ", result)
print("  ")
topK = {'max_length': 128, 'top_k': 4, 'do_sample': True}
result2 = inference(prompt, topK)
print("This is the top k result ----  ", result2)

ConS = {'max_length': 128, 'penalty_alpha': 0.6, 'top_k': 4, 'do_sample': True}
print("  ")

topK = {'max_length': 128, 'top_p': 0.95, 'do_sample': True}
result3 = inference(prompt, topK)
print("This is the constrastive search with top-P result ----  ", result3)
