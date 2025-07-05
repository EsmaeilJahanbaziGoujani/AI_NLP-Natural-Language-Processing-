import nltk
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt

comments = [
    """
    his product is great and very useful 
    I did not like the product at all
    Great value for the price
    The product is not good
    Very useful and good quality
    """
]

stop_words = set(stopwords.words('english'))
print(stop_words)

processed_words = []

for comment in comments:
    words = comment.lower().split()
    filtered = [word for word in words if word not in stop_words]
    processed_words.extend(filtered)
    print("processed_words:", processed_words)

word_counts = Counter(processed_words)
most_common = word_counts.most_common(3)
print("Most Common Words:", most_common)

words, counts = zip(*most_common)
plt.bar(words, counts)
plt.title("Most Common Words In Comment")
plt.xlabel("words")
plt.ylabel("Frequently")
plt.show()

