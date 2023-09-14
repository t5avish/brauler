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
        try:
            response = requests.get(self.url)
        except Exception as e:
            print("Some problem with getting course data.")
            return
        return  BeautifulSoup(response.text, "html.parser")
    
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
    
        
    