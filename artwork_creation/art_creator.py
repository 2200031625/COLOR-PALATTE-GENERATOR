import numpy as np
import matplotlib.pyplot as plt
from color_theory.palette_generator import generate_palette


def create_artwork(sentiment, intensity="medium"):
    """Create an abstract artwork based on sentiment and intensity."""
    colors = {
        "positive": ["yellow", "orange", "red"],
        "neutral": ["gray", "silver", "black"],
        "negative": ["blue", "darkblue", "black"]
    }

    # Adjust scatter plot properties based on sentiment intensity
    if intensity == "high":
        size = 300  # Larger dots for highly positive/negative
        alpha = 0.9  # More opacity for more vivid colors
    elif intensity == "low":
        size = 50  # Smaller dots for mild positive/negative
        alpha = 0.3  # Less opacity for subdued colors
    else:
        size = 100  # Standard size for medium intensity
        alpha = 0.6  # Medium opacity for balanced colors

    fig, ax = plt.subplots(figsize=(6, 6))
    x, y = np.random.rand(100), np.random.rand(100)

    # Use the color palette based on sentiment and intensity
    if sentiment == "positive":
        color_choice = np.random.choice(colors["positive"], size=100)
    elif sentiment == "negative":
        color_choice = np.random.choice(colors["negative"], size=100)
    else:  # Neutral
        color_choice = np.random.choice(colors["neutral"], size=100)

    ax.scatter(x, y, c=color_choice, s=size, alpha=alpha)
    ax.set_xticks([])  # Hide x-axis ticks
    ax.set_yticks([])  # Hide y-axis ticks
    plt.title(f"Abstract Artwork for {sentiment.capitalize()} Sentiment ({intensity.capitalize()} Intensity)")
    plt.show()


if __name__ == "__main__":
    create_artwork("positive", intensity="high")  # Highly Positive
    # Create different artworks with varying intensity
    create_artwork("positive", intensity="medium")  # Medium Positive
    create_artwork("negative", intensity="low")  # Mild Negative
    create_artwork("negative", intensity="high")  # Highly Negative
    create_artwork("neutral", intensity="medium")  # Neutral
