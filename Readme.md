# **pyspamdetector**

`pyspamdetector` is a Python library that allows you to easily classify text messages as **Spam** or **Not Spam** using a pre-trained machine learning model. The library is designed to be simple and intuitive, with built-in methods to classify and describe text messages.

---

## **Table of Contents**

1. [Requirements](#requirements)  
2. [Usage](#usage)  
    - [Basic Usage](#basic-usage)  
    - [Method Descriptions](#method-descriptions)  
3. [License](#license)  
4. [Contributing](#contributing)  

---

## **Requirements**

The project has the following requirement:

- `scikit-learn`: Required to load and use the pre-trained model for classification.

Make sure `scikit-learn` is installed in your environment.

---

## **Usage**

Once you have the library installed, you can easily classify text messages. The main features are:

### **Basic Usage**

To classify a message as spam or not, you simply need to import `pyspamdetector` and call the `read_text()` method. Here's an example:

```python
from pyspamdetector import PySpamDetector

# Instantiate the classifier
detector = PySpamDetector()

# Classify a message
is_spam = detector.read_text("Congratulations, you've won a $1000 gift card! Click here to claim your prize.")

# Output classification result
print(is_spam)  # Output will be True (Spam) or False (Not Spam)
```

### **Method Descriptions**

1. **`read_text(text: str) -> bool`**  
   - **Purpose**: Classifies the provided text as Spam or Not Spam.  
   - **Arguments**: `text` (str) - The message you want to classify.  
   - **Returns**: `bool` - `True` for Spam, `False` for Not Spam.  

2. **`describe_text(text: str) -> dict`**  
   - **Purpose**: Provides a general description of the message without classifying it.  
   - **Arguments**: `text` (str) - The message you want to describe.  
   - **Returns**: `dict` - A JSON-like dictionary that includes:  
     - The original message.  
     - A classification (`Spam` or `Not Spam`).  
     - Advice or warning about the message's nature.  

Example:

```python
description = detector.describe_text("Congratulations, you've won a $1000 gift card! Click here to claim your prize.")

# Example output
{
    "message": "Congratulations, you've won a $1000 gift card! Click here to claim your prize.",
    "classification": "Spam",
    "advice": "Be cautious! This message appears to be spam. Avoid clicking on links or providing sensitive information."
}
```

---

## **License**

`pyspamdetector` is open-source and released under the GNU General Public License v3 (GPLv3). See the [LICENSE](LICENSE) file for more details.

---

## **Contributing**

If you'd like to contribute to the project, feel free to fork the repository and submit a pull request. We welcome improvements and fixes!

---