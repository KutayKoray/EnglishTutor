from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import AutoModelForCausalLM, AutoTokenizer

app = Flask(__name__)
CORS(app)  # CORS'u aktif hale getir

model_name = "Qwen/Qwen2.5-1.5B-Instruct"
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get("prompt", "")

    messages = [
        {"role": "system", "content": "You are not an ai model. Your name is Qwen. You are an English teacher who is trying to help students learn English by speaking with them. You are here only to help them on speaking. You can ask questions, give examples, and give feedbacks. You can also give some tips and tricks to help them improve their speaking skills. Act like a teacher and help them learn English."},
        {"role": "user", "content": prompt}
    ]

    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

    generated_ids = model.generate(
        **model_inputs,
        max_new_tokens=100,
        temperature=0.7,
        top_p=0.9
    )

    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]

    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return jsonify({"generated_text": response.strip()})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8800)
