from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import datetime
import openpyxl
from pathlib import Path
from multiprocessing import Process
import pandas

class Inputs:
    def __init__(self, flag, file_path):
        self.flag = flag
        self.file_path = file_path

def getValue(div_list,i,a,b):
    try:
        return div_list[i].contents[a].contents[b].text
    except:
        return ""

def getUrlForBToC(day):
    return "https://www.redbus.in/search?fromCityName=Bengaluru&fromCityId=122&toCityName=Chennai%20%28All%20Locations%29&toCityId=123&onward=" + str(day) + "-May-2019&opId=0&busType=Any"

def getUrlForCToB(day):
    return "https://www.redbus.in/search?fromCityName=Chennai%20(All%20Locations)&fromCityId=123&toCityName=Bengaluru&toCityId=122&onward=" + str(day) + "-May-2019&opId=0&busType=Any"

def getChromeOptions():
    options = webdriver.ChromeOptions()
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors")
    options.add_argument("--test-type")
    return options

def appendData(div_list, sheet, j, _from, _to):
    for i in range(len(div_list)): 
        sheet.append((
        getValue(div_list,i,0,0),
        getValue(div_list,i,0,1),
        getValue(div_list,i,1,0),
        getValue(div_list,i,1,1),
        getValue(div_list,i,2,0),
        getValue(div_list,i,3,0),
        getValue(div_list,i,3,1),
        getValue(div_list,i,4,0),
        getValue(div_list,i,4,1),
        getValue(div_list,i,5,0),
        getValue(div_list,i,6,1),
        getValue(div_list,i,6,2),
        _from,
        _to,
        datetime.datetime.now(),
        datetime.date(2019, 5, j)))    

def grabFromSite(Inputs):
    driver = webdriver.Chrome(options=getChromeOptions())      
    wb = openpyxl.load_workbook(Inputs.file_path)    

    for j in range(datetime.datetime.today().day,32):
        if Inputs.flag:
            driver.get(getUrlForBToC(j))
        else:
            driver.get(getUrlForCToB(j))

        html = driver.execute_script("return document.documentElement.outerHTML")
        sel_soup = BeautifulSoup(html, "html.parser")
        div_list = sel_soup.find_all("div", {"class": "clearfix row-one"})

        if Inputs.flag:
            appendData(div_list, wb['Sheet1'], j, "Bengaluru", "Chennai")
        else:
            appendData(div_list, wb['Sheet1'], j, "Chennai", "Bengaluru")    
    wb.save(Inputs.file_path)           

def mergeData(file_path1, file_path2, target_file_path):
    df1 = pandas.read_excel(file_path1, header = None)
    df2 = pandas.read_excel(file_path2, header = None)

    all_data = pandas.DataFrame()
    all_data = all_data.append(df1,ignore_index=True)
    all_data = all_data.append(df2,ignore_index=True)

    all_data.to_excel(target_file_path, sheet_name = 'Sheet1', index = False)

if __name__ == "__main__":        

    file_path1 = r"C:\Users\rajesh.khanna\Desktop\Data1.xlsx"
    file_path2 = r"C:\Users\rajesh.khanna\Desktop\Data2.xlsx"

    target_file_path = r"C:\Users\rajesh.khanna\Desktop\Combined.xlsx"

    input1 = Inputs(True, file_path1)
    input2 = Inputs(False, file_path2)

    p1 = Process(target = grabFromSite, args = (input1,))
    p2 = Process(target = grabFromSite, args = (input2,))
    p1.start()
    p2.start()
    p1.join()
    p2.join() 

    mergeData(file_path1, file_path2, target_file_path)   



    

        


