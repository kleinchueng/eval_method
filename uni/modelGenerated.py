import json
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the dataset
with open("F:\dataset\\1.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Initialize the GPT-2 tokenizer and modeluer/gpt2-chinese-cluecorpussmall
tokenizer = AutoTokenizer.from_pretrained("uer/gpt2-chinese-cluecorpussmall")
model = AutoModelForCausalLM.from_pretrained("uer/gpt2-chinese-cluecorpussmall")

# Move the model to the GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
print(device)

torch.backends.cuda.max_split_size_bytes = 1024 * 1024 * 10  # 设置最大分割大小为10MB
torch.backends.cuda.split_kernel_size = 1024 * 1024 * 1  # 设置分割内核大小为1MB
# Generate text using GPT-2 and prepare the generated texts
generated_texts = []
src_list = []
context_list = []
# reference_texts = []
i = 1
# generated text
with torch.no_grad():
    for item in data:
        prompt = item["instruction"] + item["input"]
        src_list.append(item["instruction"])
        context_list.append(item["input"])
        expected_output = item["output"]
        input_ids = tokenizer.encode(prompt, return_tensors='pt').to(device)
        attention_mask = torch.ones_like(input_ids)
        attention_mask[input_ids == tokenizer.pad_token_id] = 0
        generated_text = model.generate(input_ids=input_ids, max_length=128, num_beams=5, no_repeat_ngram_size=2,
                                        early_stopping=True, pad_token_id=tokenizer.pad_token_id,
                                        attention_mask=attention_mask, temperature=0.7)
        generated_text = tokenizer.decode(generated_text[0], skip_special_tokens=True)

        # Preprocess the generated texts and reference texts
        generated_text = generated_text.replace(" ", "")
        # print(generated_text)
        # expected_output = expected_output.replace(" ", "")
        generated_texts.append(generated_text)
        # reference_texts.append(expected_output)
        print("已完成generated：" + str(i))
        i = i + 1

# 使用 zip 将三个列表中的元素配对
combined = list(zip(generated_texts, src_list, context_list))

# 将结果转换为字典对象
result = {"data": []}
for item in combined:
    result["data"].append({
        "generated": item[0],
        "src": item[1],
        "context": item[2]
    })
print(result)
# 导出为 JSON 文件
with open("F:\dataset\output.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=4)

