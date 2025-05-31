import matplotlib.pyplot as plt
from wordcloud import WordCloud

text = input("Enter sentence for word cloud : ")

wordcloud = WordCloud().generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Turn off the axis
plt.show()


