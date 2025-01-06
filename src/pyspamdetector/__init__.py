## Welcome to the Humans Library
########################################
## by: Praise Chiedozie Sunday

########################################
## Project: Spam Detector
########################################

########################################
## Date Created: 2025-01-06
########################################

########################################
## License: GPL-3.0
########################################

import pickle
import os
import json


class PySpamDetector:
    """
    PySpamDetector is a class that provides methods to classify text as spam or not spam.

    Users can call:
    - read_text(text): Returns True if the text is spam, otherwise False.
    - describe_text(text): Returns a JSON-style description of the message.
    """

    def __init__(self):
        """
        Initializes the PySpamDetector by loading the pre-trained model and vectorizer.
        """
        # Locate the .pkl files relative to this file's directory
        base_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(base_dir, 'spam_model.pkl')
        vectorizer_path = os.path.join(base_dir, 'vectorizer.pkl')

        # Load the pre-trained model and vectorizer
        self.model = self._load_pickle_file(model_path)
        self.vectorizer = self._load_pickle_file(vectorizer_path)

    @staticmethod
    def _load_pickle_file(file_path: str):
        """
        Loads a pickle file.

        Args:
            file_path (str): The path to the pickle file.

        Returns:
            object: The loaded pickle object.
        """
        with open(file_path, 'rb') as file:
            return pickle.load(file)

    def read_text(self, text: str) -> bool:
        """
        Classifies the given text as Spam or Not Spam.

        Args:
            text (str): The input text to classify.

        Returns:
            bool: True if the text is classified as Spam, False otherwise.
        """
        features = self.vectorizer.transform([text])
        prediction = self.model.predict(features)
        return prediction[0] == 0  # 0 indicates Spam

    def describe_text(self, text: str) -> dict:
        """
        Provides a JSON-style general description of the message.

        Args:
            text (str): The input text to classify.

        Returns:
            dict: A dictionary with the description of the text.
        """
        is_spam = self.read_text(text)
        return {
            "message": text,
            "classification": "Spam" if is_spam else "Not Spam",
            "advice": (
                "Be cautious! This message appears to be spam. Avoid clicking on links or providing sensitive information."
                if is_spam
                else "This message may appear legitimate. However, always verify unexpected messages."
            ),
        }