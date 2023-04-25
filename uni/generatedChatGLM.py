from transformers import AutoTokenizer, AutoModel
import torch
print(torch.cuda.is_available())
torch.backends.cuda.max_split_size_bytes = 1024 * 1024 * 10  # 设置最大分割大小为10MB
torch.backends.cuda.split_kernel_size = 1024 * 1024 * 1  # 设置分割内核大小为1MB


tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True)
torch.cuda.empty_cache()
model = AutoModel.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True)

response, history = model.chat(tokenizer, "你好", history=[])
print(response)
# response, history = model.chat(tokenizer, "晚上睡不着应该怎么办", history=history)
# print(response)
