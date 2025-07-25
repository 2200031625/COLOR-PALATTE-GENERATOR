from django.http import JsonResponse
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(text):
    """Analyze sentiment of text and return a category."""
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)["compound"]

    if score >= 0.05:
        return "positive"
    elif score <= -0.05:
        return "negative"
    else:
        return "neutral"

def sentiment_analysis(request):
    """Django view to analyze sentiment from user input."""
    text = request.GET.get("text", "")  # Get text from query parameter
    if not text:
        return JsonResponse({"error": "No text provided"}, status=400)

    sentiment = analyze_sentiment(text)
    return JsonResponse({"text": text, "sentiment": sentiment})
