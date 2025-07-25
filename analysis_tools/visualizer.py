from builtins import print, input
import matplotlib.pyplot as plt
from sentiment_analysis.sentiment_analyzer import analyze_sentiment

def visualize_sentiment(sentence):
    """Analyze a single sentence and display its sentiment without a bar chart."""
    sentiment = analyze_sentiment(sentence)

    # Display the sentiment result as text in the console
    print(f"The sentiment of the sentence: '{sentence}' is {sentiment.capitalize()}")

    # Create a simple plot to display the sentiment result as text
    fig, ax = plt.subplots(figsize=(6, 4))  # Adjust size as needed
    ax.text(0.5, 0.5, f"Sentiment: {sentiment.capitalize()}", fontsize=16, ha='center', va='center', transform=ax.transAxes)
    ax.axis('off')  # Hide the axes for a clean view
    plt.title(f"Sentiment Analysis for: '{sentence}'", fontsize=16)
    plt.show()

if __name__ == "__main__":
    # Get a single sentence from user input
    sentence = input("Enter a sentence for sentiment analysis: ")

    # Visualize the sentiment of the input sentence
    visualize_sentiment(sentence)
