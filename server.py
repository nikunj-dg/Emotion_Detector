''' Executing this function initiates the application of emotion detector to be executed over the 
    Flask channel and deployed on localhost:5000.
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detection

#Initiate the flask app :
app = Flask('Emotion Detector')

@app.route('/emotionDetector')
def emotion_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detector over it using emotion_detection()
        function. The output returned shows the emotions and their
        scores.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detection(text_to_analyze)
    if result['dominant_emotion'] is None:
        result_str = "Invalid text! Please try again!"
    else:
        result_str = f"For the given statement, the system response is 'anger': {result['anger']} 'disgust': {result['disgust']} 'fear': {result['fear']} 'joy': {result['joy']} and 'sadness': {result['sadness']}. The dominant emption is {result['dominant_emotion']}."
    
    return result_str

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
