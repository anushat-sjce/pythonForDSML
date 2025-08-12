import requests

def sentiment_analyzer(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = {"raw_document": {"text": text_to_analyse}}
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    response = requests.post(url, json = myobj, headers= header)
    return response.text


#to run .
#from sentiment_analysis import sentiment_analyzer
"""
sentiment_analyzer("I not love this new tech"
'{"documentSentiment":{"score":-0.917043, "label":"SENT_NEGATIVE", "mixed":false,
"sentimentMentions":[{"span":{"begin":0, "end":24, "text":"I not love this new tech"},
"sentimentprob":{"positive":0.08448495, "neutral":0.044717044, "negative":0.870798}}]}, 
"targetedSentiments":{"targetedSentiments":{}, "producerId":{"name":"Aggregated Sentiment Workflow", "version":"0.0.1"}}, 
"producerId":{"name":"Aggregated Sentiment Workflow", "version":"0.0.1"}}'
"""
