from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import datetime
import openpyxl
from pathlib import Path

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
        "05-"+ str(j)+"-2019"))    

def grabFromSite(flag):
    for j in range(2,32):
        if flag:
                driver.get(getUrlForBToC(j))
        else:
                driver.get(getUrlForCToB(j))
        html = driver.execute_script("return document.documentElement.outerHTML")
        sel_soup = BeautifulSoup(html, "html.parser")
        div_list = sel_soup.find_all("div", {"class": "clearfix row-one"})
        sheet = wb['Sheet1']
        if flag:
                appendData(div_list, sheet, j, "Bengaluru", "Chennai")
        else:
                appendData(div_list, sheet, j, "Chennai", "Bengaluru")        

if __name__ == "__main__":
        file_path = r"C:\Users\rajesh.khanna\Desktop\Data2.xlsx"
        wb = openpyxl.load_workbook(file_path)

        driver = webdriver.Chrome(options=getChromeOptions())        
        
        grabFromSite(True)
        grabFromSite(False)            

        wb.save(file_path)

