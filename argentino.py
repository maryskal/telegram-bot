import logging
import sys
from crypt import methods
from http import server

import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
import telebot
from flask import Flask, request

server = Flask(__name__)

#Nuestro Bot
TOKEN = "1316967775:AAGKQ8zgp5mYNJ9cy5aAKhBj9cw5cI-yxWI"
bot = telegram.Bot(token = TOKEN)
updater = Updater(bot.token, use_context=True)


#Configurar Loggin
logging.basicConfig(
    level = logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)")

logger = logging.getLogger()

#Solicitar datos
TOKEN = os.getenv("TOKEN")
mode = os.getenv("MODE")


#Segun el modo
if mode == "local":
    def run(updater):
        updater.start_polling() #Activa el bot
        print("Bot activo")
        updater.idle() #Finaliza el bot cuando damos Ctrl + C

elif mode == "heroku":
    def run(updater):
        #Definimos el puerto y la aplicacion
        PORT = int(os.environ.get("PORT", "5000"))
        HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")

        #Encendemos el servidor
        server.run(host="0, 0, 0, 0", port=PORT)

        #Creamos el webhook
        updater.bot.remove_webhook()
        updater.bot.set_webhook(url="https://{HEROKU_APP_NAME}.herokuapp.com/{TOKEN}")
else:
    logger.info("No se especificó el mode")
    sys.exit()



#FUNCIONES
def start (update, context):
    #print(update.message)
    name = update.message.from_user.first_name
    update.message.reply_text("Hola! " + name + ", este es el bot de Maria")

def help (update, context):
    update.message.reply_text("Soy un bot que reconoce ciertas palabras, "
                              "si mencionas alguna palabra de mi limitado vocabulario te contestaré, sino paso de ti")

#Para la búsqueda y respuesta de palabras, se llama posteriormente desde respuestas
def encontrar_palabra (palabra, respuesta, update, context):
    if (update.message.text.lower().find(palabra) != -1):
        update.message.reply_text(respuesta)


#Todas las palabras que busca y las respuestas que da
def respuestas (update, context):
    try:
        encontrar_palabra("fiesta", "Eso, salgamos de fiesta", update, context)
        encontrar_palabra("comida", "mmm... comida", update, context)
        encontrar_palabra("hola", "Hola bebé, se que contigo no sirve la labia", update, context)
        encontrar_palabra("tal?", "Yo bien, ¿y tú?", update, context)
        encontrar_palabra("sexo", "mmm... sexo...", update, context)
        encontrar_palabra("follar", "Te lo comía toh", update, context)
        encontrar_palabra("cuentame", "Soy la mejor bot del mundo primo", update, context)
        encontrar_palabra("puta", "Puta tu madre eh...", update, context)
        encontrar_palabra("hambre", "Yo siempre tengo hambre... :(", update, context)
        encontrar_palabra("te llamas", "Mi nombre es maryskal, el bot de Rolli", update, context)
    except:
        encontrar_palabra("", "", update, context)



#MAIN
def main():


    #Para llamar a todas las acciones utilizo esto
    llamada = updater.dispatcher.add_handler

    #Start
    llamada(CommandHandler("start", start))

    #Help
    llamada(CommandHandler("help", help))

    #Conversacion
    llamada(MessageHandler(Filters.text, respuestas))

    run(updater)


if __name__ == '__main__':
    main()

