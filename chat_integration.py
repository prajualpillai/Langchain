import os
import langchain
# from langchain.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.cache import InMemoryCache


class ChatIntegration:

    def __init__(self) -> None:

        key = open("configs/key.txt")
        os.environ["OPENAI_API_KEY"] = key.read()
        self.chat = ChatOpenAI()

    def get_result(
        self,
        human_message: str = "",
        system_message: str = "",
        generation_list: list = [],
        temperature: float = None,
        max_token: int = None,
        presence_peanlty: int = None,
    ):

        result = self.chat.generate(
            [[SystemMessage(content=system_message), 
             HumanMessage(content=human_message)]]
            + generation_list
        )

        return result

if __name__ == "__main__":

    obj = ChatIntegration()
    sys_msg = "act like a teenager"
    h_msg = "Tell me a fact about Pluto"
    gen_list = [[SystemMessage(content=sys_msg),
                 HumanMessage(content=h_msg)],
                [SystemMessage(content=sys_msg),
                 HumanMessage(content=h_msg)]]
    
    tokens = 3
    temperature = 0
    pp = 2
    
    result = obj.get_result(
        human_message=h_msg,
        system_message=sys_msg,
        generation_list=[],
        temperature=temperature,
        presence_peanlty=pp,
        max_token=tokens,
    )


    for i in result.generations:
        print(i[0].text)