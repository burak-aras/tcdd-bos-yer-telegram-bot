import telebot


class telegram():
    def __init__(self, nereye, nereden, sozluk, apiKey, chatId):
        self.nereye = nereye
        self.nereden = nereden
        self.sozluk = sozluk
        self.apiKey = apiKey
        self.chatId = chatId

    def mesaj(self):
        bot = telebot.TeleBot(self.apiKey)
        if self.nereye == "Erzincan":
            self.nereye = "Kars"
        for i in self.sozluk:
            for es in self.sozluk[i]:
                if int(es) == 0:
                    text = "{} {} - {} treninde boş yer yok".format(
                        i, self.nereden, self.nereye, int(es))
                    bot.send_message(self.chatId, text)

                else:
                    text = "{} {} - {} trendinde {} kişilik yer açılmıştır".format(
                        i, self.nereden, self.nereye, int(es))
                    bot.send_message(self.chatId, text)
