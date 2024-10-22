from collections import Counter
fileWithResult = open("result.txt", "w")
file = input("Enter the name of the file you would like to analyze: ")
def openFileAndStoreText():
    fileToRead = open(file, "r")
    textToAnalyze = fileToRead.read()
    fileToRead.close()
    return textToAnalyze

textToAnalyze = openFileAndStoreText()

def countWords():
        words = textToAnalyze.split()
        wordCount = Counter(words)
        sortedWordCount = dict(sorted(wordCount.items(), key=lambda item: item[1], reverse = True))
        fileWithResult.write("The number of words in the text is: " + str(len(words)) + "\n")
        uniqueWords = set(words)
        fileWithResult.write("The number of unique words in the text is: " + str(len(uniqueWords)) + "\n")
        for word, count in sortedWordCount.items():
            if count >= 1:
                fileWithResult.write(f"{word} - {count} \n")
        fileWithResult.close()
        print("All counted words are stored in result.txt")

countWords()