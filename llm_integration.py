import os
from langchain.llms import OpenAI

class LlmIntegration:

    def __init__(self) -> None:
        
        f = open('configs/key.txt')
        os.environ["OPENAI_API_KEY"] = f.read()
        self.llm = OpenAI()
    

    def get_results(self, prompt):
        
        if type(prompt) == str:
            result = self.llm(prompt)
        else:
            result = self.llm.generate(prompt)

        return result



if __name__=="__main__":

    obj = LlmIntegration()
    prompt = "Generate a funny quaote about the sun"
    print("Text Promt: ", obj.get_results(prompt))

    p2 = ["tell a fact about india", "tell a fact about Kollam"]
    result = obj.get_results(p2)

    for i in result.generations:
        print(i[0].text)
