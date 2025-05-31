import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

custom_stopwords = set(STOPWORDS)
custom_stopwords.update(["enter", "sentence", "word", "cloud", "h"])

text = """
Python is a high-level interpreted programming language that's easy to learn 
and versatile in its applications. Python supports various libraries for 
machine learning, data analysis, and web development.
"""

wordcloud = WordCloud(
    width=1000,
    height=500,
    background_color='black',
    colormap='cool',
    stopwords=custom_stopwords,
    max_words=100
).generate(text)

plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("LexiViz – Word Frequency Visualization", fontsize=20, color='white', pad=20)
plt.tight_layout(pad=0)

wordcloud.to_file("lexiviz_wordcloud.png")

plt.show()
