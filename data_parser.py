import requests, re
from bs4 import BeautifulSoup

class Parser:
    def __init__(self, id):
        self.url = "https://info.braude.ac.il/yedion/fireflyweb.aspx"\
                    "?APPNAME=&PRGNAME=S_LOOK_FOR_NOSE&ARGUMENTS=SubjectCode&"\
                    "SubjectCode=" + str(id)
        self.html = self.get_html()
        self.types_list = self.get_types()
        self.data_list = self.get_data()

    def get_html(self):
        response = requests.get(self.url)
        return BeautifulSoup(response.text, "html.parser")
    
    def get_name(self):
        topic_string = self.html.find("h1", class_="TextAlignCenter")
        name = str(topic_string.text.split("שנה")[0].split("קורס")[1])
        return name[1:len(name) - 1]

    def get_types(self):
        types_list = self.html.find_all(string=re.compile("קורס מסוג"))
        for index, type_string in enumerate(types_list):
            types_list[index] = re.sub(r'\s+', '', type_string).replace("קורסמסוג",'')
        return types_list
        
    def get_data(self):
        data_list = self.html.find_all("tbody")
        last_index = len(data_list)

        for index in range(len(data_list)):
            child = data_list[index].findChildren("tr")
            if child == []:
                last_index = index
                break
            
        return data_list[0:last_index]
    
        
    