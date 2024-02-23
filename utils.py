import os
from langchain_experimental.agents import create_pandas_dataframe_agent
import pandas as pd
# from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain.agents.agent_types import AgentType

def query_agent(data, query):
    df = pd.read_csv(data)

    llm = OpenAI(temperature=0)

    #agent = create_pandas_dataframe_agent(OpenAI(temperature=0), df, verbose=False)

    agent = create_pandas_dataframe_agent(
        ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613"),
                    df,
                    verbose=False,
                    agent_type=AgentType.OPENAI_FUNCTIONS,
            )

    return agent.run(query)
