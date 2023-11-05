from wordcloud import WordCloud
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
file=input("Enter your text below here... \n")
def calculate_frequencies(file_contents):
    
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any","the", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    file_contents = file_contents.lower()
    for i in punctuations:
        file_contents=file_contents.replace(i, "")
    words=file_contents.split()
    alpha_words=[]
    result={}
    for word in words:
        if word.isalpha() == True:
            alpha_words.append(word)
    for word in alpha_words :
        if word not in result.keys() and word not in uninteresting_words:
            result[word]=alpha_words.count(word)
    wordcloud = WordCloud(background_color='white')
    print(result)
    content= " ".join(list(result.keys()))
    wordcloud.generate(content)
    return wordcloud.to_array()
myimage = calculate_frequencies(file)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
