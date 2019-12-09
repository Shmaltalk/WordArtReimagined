from picamera import PiCamera
from PIL import Image
import time
import os
import pytesseract
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def camera_setup():
    camera = PiCamera() 
    return camera

def read_file(camera):
    with open("init.txt", "r", encoding='utf8') as text_file:
        lines = text_file.readlines()
    cleaned = []
    camera.start_preview()
    camera.rotation = 90
    time.sleep(3)
    
    camera.capture('/home/pi/Desktop/image.jpg')
    camera.stop_preview()
    image = Image.open('/home/pi/Desktop/image.jpg')
    image.rotate(90)

    lines = pytesseract.image_to_string(image).split('\n')
    os.remove('/home/pi/Desktop/image.jpg')
    print(lines)
    for line in lines:
        if line == '':
            continue
        if line.strip():
            cleaned.append(line.strip())
    text_file.close()
    return cleaned



def get_sentinalysis(camera):
    analyzer = SentimentIntensityAnalyzer()

    cleaned = read_file(camera)

    final_scores = []
    for line in cleaned:
        score = analyzer.polarity_scores(line)
        p = score['pos']
        n = score['neg']
        u = score['neu']
        final_scores.append((p, n, u))
    return final_scores
