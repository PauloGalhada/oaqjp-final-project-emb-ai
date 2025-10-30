"""
Simple emotion detection application using the Watson NLP library
"""

import requests  # Import the requests library to handle HTTP requests

def emotion_detector(text_to_analyse):
    """Send `text_to_analyse` to a remote emotion detection service and return result.

    Args:
        text_to_analyse (str): Text to be analyzed for emotions.

    Returns:
        str: Detected emotions in the text.
    """
    # URL do serviço de detecção de emoções
    url = (
        "https://sn-watson-emotion.labs.skills.network"
        "/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    # Define os headers necessários para a chamada (id do modelo)
    headers = {
        "grpc-metadata-mm-model-id": (
            "emotion_aggregated-workflow_lang_en_stock"
        )
    }
    # Cria o payload JSON com o texto a analisar
    input_json = {"raw_document": {"text": text_to_analyse}}

    response = requests.post(url, headers=headers, json=input_json, timeout=10)

    emotions = None

    if response.status_code == 200:
        emotions = response.json().get("text", "")
    else:
        emotions = "Error: Unable to detect emotions."

    return {"emotions": emotions}
