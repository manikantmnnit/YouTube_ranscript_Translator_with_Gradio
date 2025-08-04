from langchain_community.tools import YouTubeSearchTool
import pandas as pd
from typing import List
import re

def extract_youtube_IDs(topic: str) -> List[str]:
    """
    Uses LangChain's YouTubeSearchTool to get a list of YouTube links ID for a given topic.
    
    Args:
        topic (str): The search topic.
    
    Returns:
        List[str]: A list of YouTube video IDs.
    """
    tool = YouTubeSearchTool()
    links = tool.run(topic)   
    ids=re.findall(r'(?<=v=)[\w-]{11}',links)
    return ids

if __name__=='__main__':
    topic='langchain'
    ids=extract_youtube_IDs(topic)
    print(ids)