import pickle
import feedparser
import telegram
from time import sleep

feed_list =["https://zaufanatrzeciastrona.pl/feed/",
            "http://feeds.feedburner.com/niebezpiecznik/",
            "http://feeds.feedburner.com/sekurak",
            "http://www.cyberdefence24.pl/rss/zagrozenia" ]

last_feeds = pickle.load(open("db.p", 'rb'))
fee_links = []

bot = telegram.Bot(token='YOUR_TOKEN')


def feederek():
    for i in feed_list:
        fee = feedparser.parse(i)
        fee_title = fee.feed.title
        for x in range(10):
            fee_links.append(fee['entries'][x]['id'])
            if fee['entries'][x]['id'] in last_feeds:
                print("Nothing new - " + fee_title)
            else:

                sleep(5)
                entry_title = fee['entries'][x]['title']
                entry_id = fee['entries'][x]['id']
                print("Update - " + fee_title)


                message = str(fee_title +"\n" + entry_title +"\n" + entry_id)
                bot.sendMessage(chat_id="@CyberSecPL", text=message)

    pickle.dump(fee_links, open("db.p", 'wb'))
    return

feederek()