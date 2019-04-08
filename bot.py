import time, uuid
import telebot
from telebot import apihelper
import constants
from workToDB import *

bot = telebot.TeleBot(constants.tlgToken)


@bot.message_handler(commands=['start'])
def startСommand(message):
    if chekUser(message.chat.id) is True:
        bot.send_message(message.chat.id,
                         'Добро пожаловать, для того чтобы добавить ссылку на ресурс выберите командку(/add_link)'
                         ' если вы хотите добавить файлик, воспользуйтесь командой(/add_file)')
    elif chekUser(message.chat.id) is None:
        try:
            name = str(message.chat.username)
            addUser(message.chat.id, name)
            bot.send_message(message.chat.id,
                             'Пользователь успешно зарегистрирован, ожидайте подтверждения личности')
            bot.send_message(constants.adminId,
                             'Пользователь @{} успешно зарегистрирован'.format(name))
        except Exception as e:
            print(e)
    else:
        bot.send_message(message.chat.id,
                         'Вы зарегистрированны, но не подтверждены, пожалуйста дождить подтверждения вашей личности))')


@bot.message_handler(commands=['add_link'])
def addLinkCommand(message):
    if chekUser(message.chat.id) is True:
        bot.send_message(message.chat.id,
                         "Введите тег статьи(например тестирование)")
        idArticle = uuid.uuid4()
        addArticle(idArticle, message.chat.id)
        setCurrentidArticle(message.chat.id, idArticle)
        setCurrentState(message.chat.id, constants.StatusAddLink.s_addTag.value)
    else:
        bot.send_message(message.chat.id,
                         'Вы зарегистрированны, но не подтверждены, пожалуйста дождить подтверждения вашей личности))')


@bot.message_handler(
    func=lambda message: getCurrentState(message.chat.id) == constants.StatusAddLink.s_addTag.value)
def addTag(message):
    updateArticle(getCurrentidArticle(message.chat.id), 'tag', message.text)
    bot.send_message(message.chat.id, "Добавтьте описание")
    setCurrentState(message.chat.id, constants.StatusAddLink.s_addDescription.value)


@bot.message_handler(
    func=lambda message: getCurrentState(message.chat.id) == constants.StatusAddLink.s_addDescription.value)
def addDescription(message):
    updateArticle(getCurrentidArticle(message.chat.id), 'description', message.text)
    bot.send_message(message.chat.id, "А теперь вашу ссылочку")
    setCurrentState(message.chat.id, constants.StatusAddLink.s_addLink.value)


@bot.message_handler(
    func=lambda message: getCurrentState(message.chat.id) == constants.StatusAddLink.s_addLink.value)
def addLink(message):
    updateArticle(getCurrentidArticle(message.chat.id), 'link', message.text)
    article = getAllArticle((getCurrentidArticle(message.chat.id)))
    bot.send_message(constants.idChatArchive, str('Теги: ' + article[1]) + '\n' + 'Описание: ' + str(
        article[2]) + '\n' + 'Полезные ссылочки: ' + str(article[3]))
    bot.send_message(message.chat.id, "Спасибо! Ссылка успешно добавлена в архив")
    setCurrentState(message.chat.id, constants.StatusAddLink.s_start.value)


while True:
    try:
        apihelper.proxy = constants.proxy
        bot.polling(none_stop=True, interval=0)
    except Exception as e:
        print(e)
        time.sleep(5)
