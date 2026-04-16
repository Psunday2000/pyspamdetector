# pyspamdetector

[![PyPI version](https://img.shields.io/pypi/v/pyspamdetector.svg)](https://pypi.org/project/pyspamdetector/)
[![Python versions](https://img.shields.io/pypi/pyversions/pyspamdetector.svg)](https://pypi.org/project/pyspamdetector/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

A Python library for detecting spam messages using machine learning. Install it, pass in text, get a prediction.

## Install

```
pip install pyspamdetector
```

## Quick start

```
from pyspamdetector import PySpamDetector

detector = PySpamDetector()

# Classify a message
is_spam = detector.readText("Congratulations, you've won a $1000 gift card! Click here to claim your prize.")
print(is_spam)  # True
```

## API

### readText(text: str) -> bool

Classifies a message as spam or not.

- Returns: True if spam, False if not.

### describeText(text: str) -> dict

Returns a dictionary with the classification result and a human-readable advice string.

```
detector.describeText("Congratulations, you've won a $1000 gift card! Click here to claim your prize.")

# Returns:
{
    "message": "Congratulations, you've won a $1000 gift card! Click here to claim your prize.",
    "classification": "Spam",
    "advice": "Be cautious! This message appears to be spam. Avoid clicking on links or providing sensitive information."
}
```

## How it works

pyspamdetector uses a **Logistic Regression** classifier trained on TF-IDF features extracted from text messages. The model ships pre-trained with the package, so there's nothing to train yourself. Just install and use.

### Performance

Evaluated on a held-out test set:

| Metric | Score |
|--------|-------|
| Test accuracy | 96.6% |
| Training accuracy | 96.7% |

The near-identical train and test accuracy indicates the model generalizes well without overfitting.

### Training details

- **Classifier:** Logistic Regression (scikit-learn)
- **Features:** TF-IDF vectorization
- **Dataset:** A public spam message dataset

The full training notebook is publicly available on Kaggle: [Spam Model notebook](https://www.kaggle.com/code/nwachipraises/spam-model).

## Requirements

- Python 3.0+
- scikit-learn

## License

Released under the GNU General Public License v3.0. See [LICENSE](LICENSE) for details.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

## Author

Built by **Praise Chiedozie Sunday**.

- Portfolio: [praise-chiedozie-sunday.vercel.app](https://praise-chiedozie-sunday.vercel.app)
- LinkedIn: [praise-sunday](https://www.linkedin.com/in/praise-sunday-179a86224)
- GitHub: [@Psunday2000](https://github.com/Psunday2000)

If you find this package useful, a star on [GitHub](https://github.com/Psunday2000/pyspamdetector) is appreciated.
