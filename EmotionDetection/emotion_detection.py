"""
Simple emotion detection application using the Watson NLP library
"""
import json      # Import json to parse JSON responses
import requests  # Import the requests library to handle HTTP requests

def emotion_detector(text_to_analyse):
    """Call the remote Watson EmotionPredict service and return its raw text response.

    This function sends ``text_to_analyse`` to the EmotionPredict endpoint and
    returns the raw response body as a string when the HTTP status code is 200.

    Behavior:
    - On success (HTTP 200): returns ``response.text`` (the JSON payload as a
      string). 
    Args:
        text_to_analyse (str): Text to be analyzed for emotions.

    Returns:
        Optional[str]: The raw JSON response as a string on success, or ``None``
        if the request did not return HTTP 200.
    """
    # URL of the Watson EmotionPredict service
    url = (
        "https://sn-watson-emotion.labs.skills.network"
        "/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    # Define the required headers, including the model ID
    headers = {
        "grpc-metadata-mm-model-id": (
            "emotion_aggregated-workflow_lang_en_stock"
        )
    }
    # create the input JSON payload
    input_json = {"raw_document": {"text": text_to_analyse}}

    response = requests.post(url, headers=headers, json=input_json, timeout=10)

    if response.status_code != 200:
        return None

    # Convert the response text into a dictionary using the json library functions.
    response_dict = json.loads(response.text)

    # Extract emotion data from emotionPredictions array
    emotion_predictions = response_dict.get("emotionPredictions", [])
    if not emotion_predictions:
        return None

    emotion_data = emotion_predictions[0].get("emotion", {})

    # Extract the required emotions and their scores
    anger_score = emotion_data.get("anger", 0)
    disgust_score = emotion_data.get("disgust", 0)
    fear_score = emotion_data.get("fear", 0)
    joy_score = emotion_data.get("joy", 0)
    sadness_score = emotion_data.get("sadness", 0)

    # Find the dominant emotion
    dominant_emotion = max(
        [("anger", anger_score), ("disgust", disgust_score), ("fear", fear_score),
         ("joy", joy_score), ("sadness", sadness_score)],
        key=lambda x: x[1]
    )

    # Return the formatted output
    return {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
        "dominant_emotion": dominant_emotion[0]
    }
