import gradio as gr
from transformers import AutoTokenizer, AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained("khotveer1/gpt2-medium-lora-finetuned-shakespeare")
tokenizer = AutoTokenizer.from_pretrained("khotveer1/gpt2-medium-lora-finetuned-shakespeare")

def generate_text(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        **inputs,
        max_length=80,
        do_sample=True,
        top_k=40,
        temperature=0.8,
        repetition_penalty=1.15,
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

gr.Interface(fn=generate_text, inputs="text", outputs="text", title="Shakespeare GPT-2").launch()
