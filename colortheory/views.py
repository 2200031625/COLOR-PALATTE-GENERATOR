from django.shortcuts import render
from django.http import JsonResponse
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.colors import ListedColormap
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import io
import base64
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# Define color palettes for different sentiment categories
PALETTES = {
    "positive": ["#FFD700", "#FFA500", "#FF6347"],  # Warm, happy colors
    "neutral": ["#A9A9A9", "#808080", "#696969"],  # Neutral grays
    "negative": ["#483D8B", "#2F4F4F", "#000000"],  # Dark, sad colors
}

# Function to analyze sentiment
def analyze_sentiment(text):
    """Analyze sentiment of text and return a category."""
    analyzer = SentimentIntensityAnalyzer()

    # Split the sentence based on conjunctions or keywords that might indicate a shift in sentiment
    segments = re.split(r'\b(But|and|or|although|however|yet)\b', text, flags=re.IGNORECASE)

    sentiments = []
    for segment in segments:
        score = analyzer.polarity_scores(segment)["compound"]
        if score >= 0.05:
            sentiments.append("positive")
        elif score <= -0.05:
            sentiments.append("negative")
        else:
            sentiments.append("neutral")

    # Combine the sentiments of all segments to determine the overall sentiment
    if "negative" in sentiments:
        return "negative"
    elif "positive" in sentiments:
        return "positive"
    else:
        return "neutral"


# Home View with Input Form
def home(request):
    """Home page with form for sentiment analysis."""
    if request.method == "POST":
        text = request.POST.get("text", "")
        sentiment = analyze_sentiment(text)
        return render(request, "home.html", {"text": text, "sentiment": sentiment})

    return render(request, "home.html")

# View for sentiment analysis (JSON response)
def sentiment_analysis(request):
    """Django view to analyze sentiment from user input via GET request."""
    text = request.GET.get("text", "")
    if not text:
        return JsonResponse({"error": "No text provided"}, status=400)

    sentiment = analyze_sentiment(text)
    return JsonResponse({"text": text, "sentiment": sentiment})

# Function to generate image as base64
def generate_image(fig):
    """Convert a Matplotlib figure to a base64-encoded PNG image."""
    buffer = io.BytesIO()
    fig.savefig(buffer, format="png", bbox_inches="tight")
    buffer.seek(0)
    encoded_image = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return f"data:image/png;base64,{encoded_image}"

# View for color palette
def sentiment_palette(request, sentiment):
    """View to generate and return a color palette image based on sentiment."""
    colors = PALETTES.get(sentiment, PALETTES["neutral"])
    gradient = np.linspace(0, 1, 256).reshape(1, -1)
    gradient = np.vstack([gradient] * 20)

    fig, ax = plt.subplots(figsize=(8, 2))
    cmap = ListedColormap(colors)
    ax.imshow(gradient, aspect="auto", cmap=cmap)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(f"Color Palette for {sentiment.capitalize()} Sentiment", fontsize=14)

    image_data = generate_image(fig)
    return render(request, "sentiment_palette.html", {"image_data": image_data, "sentiment": sentiment})

# View for artwork creation
def artwork_creation(request, sentiment):
    """View for generating and displaying artwork based on sentiment."""
    fig, ax = plt.subplots(figsize=(6, 6))
    np.random.seed(42)
    colors = PALETTES.get(sentiment, PALETTES["neutral"])
    ax.scatter(np.random.randn(100), np.random.randn(100), color=colors[0], alpha=0.7)
    ax.set_title(f"Artwork for {sentiment.capitalize()} Sentiment")

    image_data = generate_image(fig)
    return render(request, "artwork_creation.html", {"image_data": image_data, "sentiment": sentiment})

# View for sentiment analysis visualization
def analysis_tools(request, sentiment):
    """View for generating a sentiment analysis bar chart."""
    sentiments = ["Positive", "Neutral", "Negative"]
    scores = [75, 50, 25] if sentiment == "positive" else [50, 60, 40]  # Example scores

    colors = ["#FFD700", "#A9A9A9", "#483D8B"]

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(sentiments, scores, color=colors)
    ax.set_xlabel("Sentiment")
    ax.set_ylabel("Score")
    ax.set_title("Sentiment Analysis Results")

    image_data = generate_image(fig)
    return render(request, "analysis_tools.html", {"image_data": image_data, "sentiment": sentiment})
