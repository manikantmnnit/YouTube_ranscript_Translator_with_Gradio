from youtube_transcript_api import YouTubeTranscriptApi

from extract_youtube_link import extract_youtube_IDs

def extract_transcript(topic:str,languages: list[str]=['en'])->str:
    IDs=extract_youtube_IDs(topic=topic)

    ytt_api = YouTubeTranscriptApi()
    fetched_transcript=ytt_api.fetch(IDs[0],languages= languages)

    transcript_text=[' '.join([s.text for s in fetched_transcript])]
    return transcript_text

if __name__=='__main__':
    topic='langchain'
    transcript=extract_transcript(topic,languages=['en'])
    print(type(transcript))






