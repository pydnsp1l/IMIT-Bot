import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard
#импорт библиотек, необходимых для работы программы

vk_session = vk_api.VkApi(token='vk1.a.dJaSqDgqiObrNGVk7-XS3_sR7nEuF0L2bN0YNJ4bcmAZtWAdsukxsnuN1BAc_ozVoeqhBrzHZZ2tLIm83SyI2pwnz9YNmTJqOi5xOnHdiM_1m7sBO_YTnmX5TGLVHnu5WkAgAEUvYsQGzId7cS6klYFfPdWDDgD0vZ7z5htQjGc-L42MZGG8vaQ4mpf8vNFSd4GPfJUE9F4lqkastPzLHA')
session_api = vk_session.get_api()
longpool = VkLongPoll(vk_session)
#подключение через LongPoll API к сообществу ВКонтакте с помощью заранее сгенерированного токена


def send_msg(id, some_text, keyboard=None): #функция отправки сообщений
  post = {
      "user_id":id,
      "message":some_text,
      "random_id":0,
      }
      #объект, сохраняющий параметры, необходимые для отправки сообщения: id пользователя, текст и id сообщения

  if keyboard != None:
    post["keyboard"] = keyboard.get_keyboard()
  else:
    pass
  #создание клавиатуры в случае необходимости

  vk_session.method("messages.send", post)
  #отправка сообщения

for event in longpool.listen():
  #цикл прослушивания событий longpoll
    if event.type == VkEventType.MESSAGE_NEW:
      #реакция программы только на событие "новое сообщение"
      if event.to_me:
        msg = event.text.lower()
        id = event.user_id
        #обработка ввода пользователя
        if msg == "начать":
          keyboard = VkKeyboard(one_time = True)
          keyboard.add_button("Контакты дирекции")
          keyboard.add_button("Связаться с приемной комиссией")
          keyboard.add_button("Нужна помощь!")
          keyboard.add_line()
          keyboard.add_button("Списки первого курса")
          keyboard.add_line()
          keyboard.add_button("Заявка на справку об обучении")
          #генерация клавиатуры для пользователя
          send_msg(id, "Какая информация вас интересует сегодня?", keyboard)
        if msg == "нужна помощь!":
          send_msg(id, "Обратитесь к @pydnsp1l, моему создателю", keyboard)
        if msg == "контакты дирекции":
          send_msg(id, "Адрес: г. Барнаул, ул. Ленина, 61 (корпус Л), каб. 406 \n\nТелефон: (3852) 29-81-37", keyboard)
        if msg == "связаться с приемной комиссией":
          send_msg(id, "Telegram-канал для поступающих на бакалавриат: https://vk.cc/coPoFv \n\nПолезные контакты: \nДронов Вадим Сергеевич, ответственный секретарь отборочной комиссии ИМИТ, +7-906-940-19-75, planeswalker@rambler.ru \nЖуравлева Вера Владимировна, ответственный по профориентации (бакалавриат) ИМИТ, 8-913-273-07-35, vvzhuravleva@mail.ru", keyboard)
        if msg == "списки первого курса":
          send_msg(id, "Ознакомиться можно тут: https://vk.cc/coP5q4", keyboard)
        if msg == "заявка на справку об обучении":
          send_msg(id, "Запросить справку можно тут: https://vk.cc/coPfci", keyboard)



