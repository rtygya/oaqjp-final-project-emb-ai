'''Deploying web application using Flask, importing emotion_detector function'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    '''Display webpage'''
    return render_template('index.html')

@app.route('/emotionDetector')
def emot_detector():
    '''Displays results on webpage'''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    # Handle blank entry
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    return f'''For the given statement, the system response is 'anger': {response['anger']},
'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and 
'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}.'''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
