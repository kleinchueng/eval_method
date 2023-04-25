import json

from transformers import AutoTokenizer, AutoModelForCausalLM

from utils import convert_to_json
from metric.evaluator import get_evaluator
import torch

# task = 'data2text'
# # a list of model outputs to be evaluataed
# output_list = ['You would like to search financial district ?']
# # a list of human-annotated reference texts
# ref_list = ['You are looking near the financial district , right ?']
#
# # Prepare data for pre-trained evaluators
# data = convert_to_json(output_list=output_list, ref_list=ref_list)
# # Initialize evaluator for a specific task
# evaluator = get_evaluator(task)
# # Get multi-dimensional evaluation scores
# eval_scores = evaluator.evaluate(data, print_result=True)


# Example for dialogue response generation
task = 'dialogue'

# a list of dialogue histories
src_list = ["我想让你做一名记者。您将报道突发新闻，撰写专题报道和评论文章，验证信息，发现来源，遵守新闻道德，并使用您自己独特的风格提供准确的报道。我的第一个请求是:我需要帮助写一篇关于世界主要城市空气污染的文章。"]
# a list of additional context that should be included into the generated response
context_list = [""]
# a list of model outputs to be evaluated
output_list = ["好的，我可以帮助您写一篇关于世界主要城市空气污染的文章。空气污染是当前全球最严重的环境问题之一，世界上主要城市的空气污染尤为严重。根据评估，全球有超过3万名城市，其中约有2000"
               "名城市的空气污染水平超过国家标准，这些城市的居民面临各种健康风险。世界上最污染的城市之一是印度泛尔巴尼市，其空气污染水平普遍高。其次是印度南印度尼西亚的印度尼西亚市，以及印度印布玛罗纳市。其他发达国家的城市也存在污染问题，如中国上海、美国德克萨斯州的坦帕市、墨西哥城市等。空气污染的主要来源是工业、交通和建筑等领域的排放。工业排放主要包括燃烧厂、厂房、油田等，其中燃烧厂是最大的排放单位，其排放的二氧化碳和有害气体对人体健康造成巨大的威胁。交通排放主要包括汽车尾气和航空尾气，其中汽车尾气是最大的排放单位，占据了大部分空气污染的份额。建筑排放主要包括建筑燃烧和冷却等，其中建筑燃烧是最大的排放单位，其排放的二氧化碳和有害气体对人体健康造成巨大的威胁。为了应对空气污染，政府和国际组织已经采取了一系列措施。其中包括加强环境监管、推广绿色出行和可持续能源等。但这些措施的实施还有待提高，需要全球共同努力，才能真正解决空气污染问题。总之，空气污染是一个全球性的问题，需要全球共同努力解决。政府和国际组织应该加强环境监管，推广绿色出行和可持续能源等措施，以保护人类健康和环境安全。"]

# # Load the dataset
# with open("F:\dataset\\output.json", "r", encoding="utf-8") as f:
#     data = json.load(f)
#

# Prepare data for pre-trained evaluators

data = convert_to_json(output_list=output_list,
                       src_list=src_list, context_list=context_list)

# Initialize evaluator for a specific task
evaluator = get_evaluator(task)
# Get multi-dimensional evaluation scores
eval_scores = evaluator.evaluate(data, print_result=True)

'''
# Example for summarization
task = 'summarization'

# a list of source documents
src_list = ['Peter and Elizabeth took a taxi to attend the night party in the city. \
             While in the party, Elizabeth collapsed and was rushed to the hospital.']
# a list of human-annotated reference summaries
ref_list = ['Elizabeth was hospitalized after attending a party with Peter.']
# a list of model outputs to be evaluataed
output_list = ['Peter and Elizabeth attend party city. Elizabeth rushed hospital.']

# Prepare data for pre-trained evaluators
data = convert_to_json(output_list=output_list, 
                       src_list=src_list, ref_list=ref_list)
# Initialize evaluator for a specific task
evaluator = get_evaluator(task)
# Get multi-dimensional evaluation scores
eval_scores = evaluator.evaluate(data, print_result=True)
# eval_scores = evaluator.evaluate(data, dims=['coherence', 'consistency', 'fluency'], 
#                                  overall=False, print_result=True)






# Example for factual consistency detection
task = 'fact'

# a list of source documents
src_list = ['Peter and Elizabeth took a taxi to attend the night party in the city. \
             While in the party, Elizabeth collapsed and was rushed to the hospital.']
# a list of model outputs (claims) to be evaluataed
output_list = ['Tom was rushed to hospital.']

# Prepare data for pre-trained evaluators
data = convert_to_json(output_list=output_list, src_list=src_list)
# Initialize evaluator for a specific task
evaluator = get_evaluator(task)
# Get factual consistency scores
eval_scores = evaluator.evaluate(data, print_result=True)
'''
