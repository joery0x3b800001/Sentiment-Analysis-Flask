from flask import Flask, request, render_template
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Initialize Flask app
app = Flask(__name__)

# Define the model and tokenizer
MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

# Define sentiment labels (these are usually mapped in the model config)
LABELS = {
    0: "Negative",
    1: "Neutral",
    2: "Positive"
}

# Define colors for sentiments
COLORS = {
    "Negative": "#f8d7da",  # Red
    "Neutral": "#d1ecf1",   # Blue
    "Positive": "#d4edda"    # Green
}

# Define a function to perform sentiment analysis
def analyze_sentiment(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    predicted_class_id = logits.argmax().item()
    confidence_scores = torch.softmax(logits, dim=-1).squeeze().tolist()
    sentiment = LABELS.get(predicted_class_id, "Unknown")
    confidence = confidence_scores[predicted_class_id]
    color = COLORS.get(sentiment, "#ffffff")  # Default to white if unknown
    return sentiment, confidence, color

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None
    confidence = None
    color = "#ffffff"  # Default color
    if request.method == 'POST':
        review = request.form.get('review')
        if review:
            sentiment, confidence, color = analyze_sentiment(review)
    return render_template('index.html', sentiment=sentiment, confidence=confidence, color=color)

if __name__ == '__main__':
    app.run(debug=True)