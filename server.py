'''Executing this function initiates the application of emotion
   analysis to be executed over the Flask channel and deployed on
   localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : TODO
from flask import Flask, request, render_template

# Import the emotion_detector function from the package created: TODO
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app : TODO
app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_analyzer():
    ''' This code receives the text from the HTML interface and
        runs emotion analysis over it using emotion_detector()
        function. The output returned shows the label and its confidence
        score for the provided text.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get("textToAnalyze", "")
    
    # Call the emotion_detector function and get the result
    result = emotion_detector(text_to_analyze)
    
    # Check if result is valid or if dominant_emotion is None
    if result is None or result['dominant_emotion'] is None:
        return "Invalid text! Please try again!.", 400
    
    # Format the output as required
    formatted_result = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )

    return formatted_result

@app.route("/")
def index():
    ''' This code renders the main HTML interface for the emotion
        analysis application.
    '''
    return render_template("index.html")

if __name__ == "__main__":

    # Run the Flask app on host
    app.run(host="0.0.0.0", port=5000)
