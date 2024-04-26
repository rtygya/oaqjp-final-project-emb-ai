import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = obj, headers=header)
    formatted_response = json.loads(response.text)
    emotions= formatted_response['emotionPredictions'][0]['emotion']
    
    v = list(emotions.values())
    k = list(emotions.keys())
 
    dominant_emotion = k[v.index(max(v))]

    res = {
        'anger': emotions["anger"],
        'disgust': emotions["disgust"],
        'fear': emotions["fear"],
        'joy': emotions["joy"],
        'sadness': emotions["sadness"],
        'dominant_emotion': dominant_emotion
        }

    return res
