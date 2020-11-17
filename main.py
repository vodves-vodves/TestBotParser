import requests
import telebot


token = '' #bot token
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def main(message):
    url = message.text
    if "https://www.instagram.com/" in url:
        r = requests.get(url)
        try:
            user_name = r.text.split('"instagram://user?username=')[1].split('"')[0]
            subscribers = r.text.split('"edge_followed_by":{"count":')[1].split('}')[0]
            publ = r.text.split('"edge_owner_to_timeline_media":{"count":')[1].split(',')[0]
            podpisok = r.text.split('"edge_follow":{"count":')[1].split('}')[0]
            image = r.text.split('<meta property="og:image" content="')[1].split('"')[0]
            
            text = f"{user_name}:\n"
            text += f"{subscribers} подписчиков\n"
            text += f"{publ} публикации\n"
            text += f"{podpisok} подписок"
            bot.send_message(message.chat.id, text)
            bot.send_photo(message.chat.id, image)
        except Exception:
            likes = r.text.split('"userInteractionCount":"')[1].split('"')[0]
            image = r.text.split('<meta property="og:image" content="')[1].split('"')[0]
            bot.send_message(message.chat.id, likes)
            bot.send_photo(message.chat.id, image)

if __name__ == '__main__':
    bot.polling(none_stop=True)
    # test()