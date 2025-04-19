from textblob import TextBlob
import re

def parse_whatsapp_chat(text):
    pattern = re.compile(r'^(\d{1,2}/\d{1,2}/\d{2,4}), (\d{1,2}:\d{2}) - ([^:]+): (.+)$')
    messages = []
    for line in text.split('\n'):
        match = pattern.match(line)
        if match:
            date, time, sender, message = match.groups()
            sentiment = TextBlob(message).sentiment.polarity
            if sentiment > 0:
                mood = 'Positive'
            elif sentiment < 0:
                mood = 'Negative'
            else:
                mood = 'Neutral'
            messages.append({
                'date': date,
                'time': time,
                'sender': sender,
                'message': message,
                'sentiment': mood
            })
    return messages

def handle_uploaded_chat_file(file_content):
    try:
        text = file_content.decode('utf-8')
    except UnicodeDecodeError:
        text = file_content.decode('latin-1')
    return parse_whatsapp_chat(text)
