from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def read_file():
    text_file = open("init.txt", "r")
    lines = text_file.readlines()
    cleaned = []
    for line in lines:
        if line.strip():
            cleaned.append(line.strip())
    text_file.close()
    return cleaned



def get_sentinalysis():
    analyzer = SentimentIntensityAnalyzer()

    cleaned = read_file()

    final_scores = []
    for line in cleaned:
        score = analyzer.polarity_scores(line)
        p = score['pos']
        n = score['neg']
        u = score['neu']
        final_scores.append((p, n, u))
    return final_scores
