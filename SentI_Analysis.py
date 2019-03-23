from textblob import TextBlob

text_sample=TextBlob("Cyberattacks on Ukarine spread a new variant of the Petya malware (ransom note pictured) around the world and cause severe disruptions.")

if text_sample.sentiment.polarity > 1:
    print("POSITIVE")
elif text_sample.polarity==0:
    print("NUETRAL")
else:
    print("NEGATIVE")
