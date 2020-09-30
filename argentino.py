import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


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



def main():
    updater = Updater("1316967775:AAGKQ8zgp5mYNJ9cy5aAKhBj9cw5cI-yxWI", use_context=True)

    #Para llamar a todas las acciones utilizo esto
    llamada = updater.dispatcher.add_handler

    #Start
    llamada(CommandHandler("start", start))

    #Help
    llamada(CommandHandler("help", help))

    #Conversacion
    llamada(MessageHandler(Filters.text, respuestas))

    #Empieza el bot
    updater.start_polling()

    #Se queda esperando
    updater.idle()


if __name__ == '__main__':
    main()

