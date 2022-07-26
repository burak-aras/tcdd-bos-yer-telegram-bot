from driver import driver
from bosYer import yer
from message import telegram
if __name__ == "__main__":
    path = "YOUR CHROME WEB DRIVER PATH DIRECTORY"
    nereden = input("Kalkış istasyonu :")
    nereye = input("Varış İstasyonu :")
    zaman = input("Tarih :")
    chatId = "YOUR CHAT ID AS INT"
    apiKey = "YOUR API KEY"
    sourceCode = driver(path, nereden, nereye, zaman).sourceCode()
    sozluk = yer(sourceCode=sourceCode).soup()
    telegram(nereye, nereden, sozluk, apiKey, chatId).mesaj()
