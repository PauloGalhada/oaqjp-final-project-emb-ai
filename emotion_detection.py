"""
Simple emotion detection application using the Watson NLP library
"""

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

    if response.status_code == 200:
        return response.text

    return None
