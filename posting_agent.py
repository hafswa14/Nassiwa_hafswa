import requests
import schedule
import time


token = ""
chat_id = -1002000945804

url = f"https://api.telegram.org/bot{token}/getUpdates"

response = requests.get(url)
print(response.text)

#TOPIC LIST
topics = [
    "#1 :  And whoever fears Allah, He will make for him a way out. (Quran 65:2)",
    "#2 : The best among you are those who have the best manners and character.(Bukhari)",
    "#3 : Do good deeds properly, sincerely and in moderation. (Muslim)",
    "#4 : Allah does not burden a soul beyond what it can bear. (Quran 2:286)",
    "#5 :The strong believer is better and more beloved to Allah than the weak believer. (Ibn Majah)",
]

# to track which topic was sent last)
current_index = 0

#to generate message(topic)
def generate_message(topic):
    return f"Today's motivation is: {topic}"

# send message to the platform(telegram)
def send_message(message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {"chat_id": chat_id, "text": message}
    response = requests.get(url, params=params)
    print(f"Status: {response.status_code}, Response: {response.text}")
    return response.json()

#to post te next topic 
def post_next_topic():
    global current_index
    topic = topics[current_index]
    message = generate_message(topic)
    send_message(message)
    
    current_index = (current_index + 1) % len(topics)  # Loop back to 0


def main():
    schedule.every().day.at("08:00").do(post_next_topic)
    print("HaphieAgent running. I will post a new topic every day at 08:00.")
    
    #send_message(generate_message(topics))
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
