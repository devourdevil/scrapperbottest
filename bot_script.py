from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
from bs4 import BeautifulSoup

def scrape_website():
    url = "https://payments.cashfree.com/forms/donateme"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.title.string
        return title
    else:
        return "Failed to retrieve data"

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Welcome to the Website Scraper Bot!")

def scrape(update: Update, context: CallbackContext) -> None:
    data = scrape_website()
    update.message.reply_text(data)

def main():
    # Replace 'YOUR_API_TOKEN' with your bot's API token
    updater = Updater("7268944881:AAGD_cK5YsFrif4ZtNF2efpMyZN9o16ExRc", use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("scrape", scrape))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
