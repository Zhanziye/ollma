from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_community.llms.tongyi import Tongyi
example_template = PromptTemplate.from_template("单词：{word}，反义词：{antonym}")

example_data = [
    {"word": "happy", "antonym": "sad"},
    {"word": "hot", "antonym": "cold"},
    {"word": "big", "antonym": "small"}
    ]

few_shot_template = FewShotPromptTemplate(
    example_prompt=example_template,
    examples=example_data,
    prefix="give me the antonym of the word based on the following examples:",
    suffix="the antonym of the word {input_word} is",
    input_variables=['input_word']     
)

prompt_text = few_shot_template.invoke(input={"input_word": "left"}).to_string()
print(prompt_text)


model = Tongyi(model="qwen-max")
print(model.invoke(input = prompt_text))