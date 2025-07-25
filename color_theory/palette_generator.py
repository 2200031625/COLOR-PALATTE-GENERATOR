from builtins import len

import matplotlib.pyplot as plt
import numpy as np

# Define color palettes for different sentiment categories
PALETTES = {
    "positive": ["#FFD700", "#FFA500", "#FF6347"],  # Warm, happy colors
    "neutral": ["#A9A9A9", "#808080", "#696969"],  # Neutral grays
    "negative": ["#483D8B", "#2F4F4F", "#000000"],  # Dark, sad colors
}


def generate_palette(sentiment):
    """Generate a color palette based on sentiment."""
    colors = PALETTES.get(sentiment, PALETTES["neutral"])

    # Create a gradient of colors for better display
    gradient = np.linspace(0, 1, 256).reshape(1, -1)
    gradient = np.vstack([gradient] * len(colors))

    # Display the palette
    fig, ax = plt.subplots(figsize=(8, 2))
    ax.imshow(gradient, aspect="auto", cmap=plt.cm.colors.ListedColormap(colors))
    ax.set_xticks([])  # Remove x-ticks
    ax.set_yticks([])  # Remove y-ticks
    ax.set_title(f"Color Palette for {sentiment.capitalize()} Sentiment", fontsize=14)
    plt.show()


if __name__ == "__main__":
    generate_palette("positive")  # Example: Generate a positive sentiment palette

