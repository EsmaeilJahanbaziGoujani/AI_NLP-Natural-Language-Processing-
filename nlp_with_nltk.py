# Import the nltk library for natural language processing tasks
import nltk



# Import the list of English stopwords from nltk.corpus
from nltk.corpus import stopwords

# Import Counter from collections to count word frequencies
from collections import Counter

# Import matplotlib.pyplot for plotting the word frequencies
import matplotlib.pyplot as plt

# Download the stopwords dataset from nltk (run once)
nltk.download('stopwords')

# Define a sample list of comments (replace with your own comments if needed)
comments = [
    "This product is great and very useful",
    "I did not like the product at all",
    "Great value for the price",
    "The product is not good",
    "Very useful and good quality"
]

# Get the set of English stopwords from nltk
stop_words = set(stopwords.words('english'))

# Initialize an empty list to store processed words
processed_words = []

# Loop through each comment in the list
for comment in comments:
    # Convert the comment to lowercase and split it into words
    words = comment.lower().split()
    # Remove stopwords from the list of words
    filtered = [word for word in words if word not in stop_words]
    # Add the filtered words to the processed_words list
    processed_words.extend(filtered)

# Count the frequency of each word using Counter
word_counts = Counter(processed_words)

# Print the most common words and their frequencies
print("Most common words:", word_counts.most_common())

# Get the 10 most common words and their counts
most_common = word_counts.most_common(10)

# Separate the words and their counts for plotting
words, counts = zip(*most_common)

# Create a bar chart of the most frequent words
plt.bar(words, counts)

# Add a label to the x-axis
plt.xlabel('Words')

# Add a label to the y-axis
plt.ylabel('Frequency')

# Add a title to the plot
plt.title('Most Frequent Words in Comments')

# Show the plot
plt.show()
