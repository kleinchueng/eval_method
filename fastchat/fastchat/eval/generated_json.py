import os
import json

i = 0
with open('F:\dataset\chatglm.json', "r", encoding="utf-8") as f:
    data = json.load(f)
f.close()
print(data)
with open('F:\毕设模型评估\FastChat\\fastchat\eval\output.jsonl', 'r', encoding="utf-8") as f1:
    json_list = []
    for line in f1:
        json_list.append(json.loads(line))

print(json_list)
while i < len(json_list):
    json_list[i]["text"] = data[i]["generated"]
    json_list[i]["model_id"] = "chatglm-6B"
    i = i + 1
print(json_list)
with open('F:\毕设模型评估\FastChat\\fastchat\eval\chatglm_output.jsonl', 'w', encoding="utf-8") as f:
    table = [json.dumps(ans, ensure_ascii=False) for ans in json_list]
    f.write('\n'.join(table))