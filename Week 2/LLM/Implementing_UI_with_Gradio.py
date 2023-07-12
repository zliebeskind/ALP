import gradio as gr
from huggingface_hub.inference_api import InferenceApi
key = "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"
inference = InferenceApi(repo_id="gpt2-large", token=key)

def Prompt(prompt, max_length):
  topP = {'max_length': max_length, 'top_p': 0.95, 'do_sample': True}
  topK = {'max_length': max_length, 'top_k': 4, 'do_sample': True}
  ConS = {'max_length': max_length, 'penalty_alpha': 0.6, 'top_p': 0.95, 'do_sample': True}
  result1 = inference(prompt, topP)
  result2 = inference(prompt, topK)
  result3 = inference(prompt, ConS)
  return result1, result2, result3
demo = gr.Interface(fn = Prompt, inputs=[gr.Textbox(lines=1, placeholder="Type prompt here"), gr.Slider(1, 499)], outputs=["text", "text", "text"])
    
demo.launch(share = True)