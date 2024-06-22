import requests
import json

def emotion_detection(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = myobj, headers = header)
    response_frmt = json.loads(response.text)

    if response.status_code == 400:
        emotions = {
            'anger' : None, 
            'disgust' : None, 
            'fear' : None,
            'joy' : None, 
            'sadness' : None,
            'dominant_emotion' : None
        }
    elif response.status_code == 200:
        emotions = response_frmt['emotionPredictions'][0]['emotion']

        score = 0
        for emotion in emotions:
            if emotions[emotion] > score:
                score = emotions[emotion]
                emotion_dom = emotion

        emotions['dominant_emotion'] = emotion_dom        
        
    return emotions

