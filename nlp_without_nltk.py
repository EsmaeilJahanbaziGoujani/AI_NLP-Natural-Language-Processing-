# Import necessary libraries for text processing and visualization
from collections import Counter  # For counting word frequencies
import matplotlib.pyplot as plt  # For plotting the word frequencies




# Sample list of comments (replace with your own comments)
comments = [
    "This product is great and very useful",
    "I did not like the product at all",
    "Great value for the price",
    "The product is not good",
    "Very useful and good quality"
]  # Sample comments about a product


# Define a list of English stopwords
stopwords = set([
    "the", "is", "and", "at", "on", "in", "for", "to", "a", "of", "not", "did", "i", "all"
])  # Common stopwords to remove

# Preprocess the comments: lowercase and remove stopwords
processed_words = []  # List to store processed words
for comment in comments:  # Iterate over each comment
    words = comment.lower().split()  # Convert to lowercase and split into words
    filtered = [word for word in words if word not in stopwords]  # Remove stopwords
    processed_words.extend(filtered)  # Add filtered words to the list

# Count word frequencies (Bag of Words)
word_counts = Counter(processed_words)  # Count occurrences of each word

# Print the most common words
print("Most common words:", word_counts.most_common())  # Display word frequencies

# Plot the most frequent words
most_common = word_counts.most_common(10)  # Get top 10 most common words
words, counts = zip(*most_common)  # Separate words and their counts

plt.bar(words, counts)  # Create a bar chart
plt.xlabel('Words')  # Label for x-axis
plt.ylabel('Frequency')  # Label for y-axis
plt.title('Most Frequent Words in Comments')  # Title of the plot
plt.show()  # Display the plot
