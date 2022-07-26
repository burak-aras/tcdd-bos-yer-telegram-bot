from bs4 import BeautifulSoup
import re
import json


class yer():
    def __init__(self, sourceCode):
        self.sourceCode = sourceCode

    def soup(self):
        self.sozluk = {}
        soup = BeautifulSoup(self.sourceCode, "html.parser")
        for i in soup.find_all("tr", {"class": "ui-widget-content ui-datatable-even"}):
            tarihZaman11 = (i.td.text.replace("\t", ""))
            tarihZaman21 = tarihZaman11.replace("\n", " ")
            liste0 = []
            bosYer = i.find("div", {
                            "class": "ui-selectonemenu ui-widget ui-state-default ui-corner-all ui-helper-clearfix vagonTipiCombo"}).text
            for segment in re.findall("[(][^)]*[)]", bosYer):
                if re.findall(r"^\(\d+\)", segment):
                    bosYersayiCift1 = re.findall(r"^\(\d+\)", segment)[0]
                    bosYersayiCift2 = re.findall('\d+', bosYersayiCift1)[0]
                    liste0.append(bosYersayiCift2)
            self.sozluk[tarihZaman21] = liste0[:-1]

        for tek in soup.find_all("tr", {"class": "ui-widget-content ui-datatable-odd"}):
            tarihZaman = (tek.td.text.replace("\t", ""))
            tarihZaman2 = tarihZaman.replace("\n", " ")
            liste = []
            bosYer = tek.find("div", {
                              "class": "ui-selectonemenu ui-widget ui-state-default ui-corner-all ui-helper-clearfix vagonTipiCombo"}).text
            for segment in re.findall("[(][^)]*[)]", bosYer):
                if re.findall(r"^\(\d+\)", segment):
                    bosYersayiTek1 = re.findall(r"^\(\d+\)", segment)[0]
                    bosYersayiTek2 = re.findall('\d+', bosYersayiTek1)[0]
                    liste.append(bosYersayiTek2)
            self.sozluk[tarihZaman2] = liste[:-1]
        return self.sozluk
