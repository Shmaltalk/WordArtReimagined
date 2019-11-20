from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


text_file = open("init.txt", "r")
lines = text_file.readlines()
cleaned = []
for line in lines:
    if line.strip():
        cleaned.append(line.strip())
print(cleaned)
text_file.close()

analyzer = SentimentIntensityAnalyzer()

#
# prev_pos = 0
# prev_neg = 0
# prev_neu = 0

print('{')
for line in cleaned:
    vs = analyzer.polarity_scores(line)
    # cur_p = 0
    # cur_n = 0
    # cur_u = 0
    # if vs['neu'] == 1:
    #     cur_p = prev_pos/2
    #     cur_n = prev_neg/2
    # else:
    p = vs['pos']
    n = vs['neg']
    u = vs['neu']
    # print('{' + str(int(cur_p*180)) + ',' + str(int(cur_n*120)) + '},')
    print('{' + str(int(p*100)) + ',' + str(int(n*100)) + ',' + str(int(u*100)) +'},')

if

 





    # prev_pos = cur_p
    # prev_neg = cur_n
    # prev_neu = cur_u
    #

print('}')
