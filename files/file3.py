import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

def analyze_word_frequency(text):
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word.isalpha()]
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in tokens if word not in stop_words]
    
    word_freq = Counter(filtered_words)
    
    return word_freq

if __name__ == "__main__":
    text = """
    Это текст, проверка текста, текст, крутой текст-текст, текст!! Текст.
    """
    
    freq = analyze_word_frequency(text)
    for word, count in freq.most_common():
        print(f"{word}: {count}")
