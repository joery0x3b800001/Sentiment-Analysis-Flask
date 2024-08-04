# Sentiment Analysis with Flask and Hugging Face

## Overview

This project is a web application that performs sentiment analysis on user-provided text using a Hugging Face transformer model. Built with Flask, it allows users to enter text (such as product reviews), analyze its sentiment, and view the result along with a confidence score. The application dynamically changes the background color of the result display based on the sentiment of the text.

## Features

- **Sentiment Analysis:** Uses a pre-trained sentiment analysis model from Hugging Face to classify text into positive, neutral, or negative sentiments.
- **Dynamic UI:** Changes the background color of the result display based on the sentiment analysis outcome.
- **Confidence Score:** Displays the confidence level of the sentiment classification.

## Requirements

- Python 3.8 or higher
- Flask
- Transformers library
- Torch

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/joery0x3b800001/Sentiment-Analysis-Flask.git
    cd Sentiment-Analysis-Flask
    ```

2. **Create and Activate a Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Create a `requirements.txt` File:**

    ```plaintext
    scipy
    flask
    transformers
    torch
    ```

## Usage

1. **Run the Application:**

    ```bash
    python app.py
    ```

2. **Access the Web Application:**

    Open your web browser and go to `http://127.0.0.1:5000/`.

3. **Analyze Sentiment:**

    - Enter your text (e.g., a product review) into the textarea and click "Analyze Sentiment."
    - The application will display the sentiment (Positive, Neutral, or Negative) and the confidence score.
    - The background color of the result will change based on the sentiment:
      - Green for Positive
      - Blue for Neutral
      - Red for Negative

## Code Explanation

- **app.py**: Contains the Flask application and the logic for sentiment analysis using the Hugging Face model.
- **templates/index.html**: The HTML template for the web interface. It includes form input, dynamic result display, and CSS styling.

## Example Output

- **Positive Review:** "I absolutely love this oatmeal! It has a fantastic texture and is so easy to prepare."
- **Neutral Review:** "This oatmeal is okay. It cooks quickly and has a decent flavor, but it's nothing special."
- **Negative Review:** "I was disappointed with this oatmeal. The texture was a bit mushy, and the flavor was bland."

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE.md) file for details.

## Acknowledgments

- **Hugging Face:** For providing the transformer models.
- **Flask:** For creating a lightweight web framework.