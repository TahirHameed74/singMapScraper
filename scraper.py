# -*- coding: utf-8 -*-

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from datetime import datetime
import os
import time
import re
import glob
import shutil
from pathlib import Path
from bs4 import BeautifulSoup

print("Scraping Script Starting...")
print("During some phases of the script it will use the mouse pointer, please do not use it when Firefox comes to foreground")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
  
driver = webdriver.Chrome(chrome_options=chrome_options)  



def connect():
    driver.get("https://app.singmap.com/")
    
    while(len(driver.find_elements_by_xpath("//input[@class='van-field__control']"))==0):
        time.sleep(2)
    time.sleep(3)
    li = driver.find_elements_by_xpath("//input[@class='van-field__control']")
    li[0].click()
    li[0].send_keys("shapsp@gmail.com")
    li[1].click()
    li[1].send_keys("newlaunch18")
    driver.find_element_by_xpath("//button[@class='weui-btn login_btn weui-btn_warn']").click()
    time.sleep(2)

    while(len(driver.find_elements_by_xpath("//span[@class='search_icon_rt']"))==0):
        time.sleep(2)
    time.sleep(3)
    driver.find_element_by_xpath("//span[@class='search_icon_rt']").click()

    while(len(driver.find_elements_by_xpath("//div[contains(text(), 'Singapore')]"))==0):
        time.sleep(2)
    singa = driver.find_element_by_xpath("//div[contains(text(), 'Singapore')]")
    if(singa.get_attribute("class") != 'vux-checker-item vux-tap-active checker-item checker-item-selected'):
        singa.click()
    time.sleep(1)
    driver.find_element_by_xpath("//button[@class='searchBtn van-button van-button--default van-button--normal']").click()
    


    soup = BeautifulSoup(driver.page_source,'lxml')

    ul = soup.find("ul",{"class":"project_div_box"})

    # test = ul.find("div",{"class":"cardBox_bom"})
    print(test)


if __name__== "__main__":

    connect()
# filtr()
# liste = listeproj()

# print(liste)   


# def getdata():
#     while(len(driver.find_elements_by_xpath("//div[@class='vux-flexbox info_box vux-flex-row']"))==0):
#         time.sleep(2)
#     time.sleep(4)
#     name = driver.find_element_by_xpath("//h1[@class='vux-header-title']").text
#     li = driver.find_elements_by_xpath("//div[@class='vux-flexbox info_box vux-flex-row']")
#     dicte = {}
#     dicte = {
#         'Developer':None,
#         'Type':None,
#         'Total Units':None,
#         'Exp TOP':None,
#         'Address':None,
#         'Location':None,
#         'Gallery Address':None,
#         'Country':None,
#         'Tenure':None}
    
#     for i in li:
#         txt = i.text.split('\n')
#         if(txt[0] in dicte):
#             try:                #A RETIRER
#                 dicte[txt[0]] = txt[1]
#             except ValueError:
#                 print(" ")
#     count = 0
#     li = driver.find_elements_by_xpath("//div[@class='flex-demo']")
#     for i in li:
#         if("/" in i.text):
#             s = i.text.split('/')
#             if(s[0].isnumeric()):
#                 count += int(s[0])
#     return [name, dicte, count]
    
# def units():
#     while(len(driver.find_elements_by_xpath("//div[@class='vux-tab-item nav_bar']"))==0):
#         time.sleep(2)
#     time.sleep(2)
#     driver.find_elements_by_xpath("//div[@class='vux-tab-item nav_bar']")[9].click() #summary
#     while(len(driver.find_elements_by_xpath("//div[@class='Summary']"))==0):
#         time.sleep(2)
#     time.sleep(2)
#     azeq = driver.page_source
#     time.sleep(2)
    
#     error = driver.find_elements_by_class_name('text_err')
#     dicte = []
#     dacte = []
#     if(len(error)==0):
#         while(len(driver.find_elements_by_xpath("//div[@class='table']"))==0):
#             time.sleep(2)
#         li = driver.find_elements_by_xpath("//div[@class='table']")
#         for i in li:
#             if(i.text.split('\n')[0] == '#UNITS BY TYPE'):
#                 table = i.text.split('\n')[6:]
#                 row_num = len(table)/5
#                 a = 0
#                 for j in range(round(row_num)):
#                     if(j!=round(row_num)-1):
#                         temp = [table[a],table[a+1],table[a+2],table[a+3],table[a+4]]
#                         dicte.append(temp)
#                         a += 5
#                     else:   #parfois derniere ligne sans titre
#                         temp = ['',table[a],table[a+1],table[a+2],table[a+3]]
#                         dicte.append(temp)
#             if(i.text.split('\n')[0] == '#UNITS BY FLOOR PLAN'):
#                 table = i.text.split('\n')[6:]
#                 row_num = len(table)/5
#                 a = 0
#                 for j in range(round(row_num)):
#                     if(j!=round(row_num)-1):
#                         temp = [table[a],table[a+1],table[a+2],table[a+3],table[a+4]]
#                         dacte.append(temp)
#                         a += 5
#                     else:   #parfois derniere ligne sans titre
#                         temp = ['',table[a],table[a+1],table[a+2],table[a+3]]
#                         dacte.append(temp)
#     return [dicte, dacte]

# def moveFile(projname, i, now, doss): #folder already created
#     #move
#     list_of_files = glob.glob(str(Path.home() / "Downloads")+'\\*.png')
#     original = max(list_of_files, key=os.path.getctime)
#     target = str(Path().absolute())+"/"+now+"/"+projname+'/'+doss
#     shutil.move(original, target)
    
#     #Rename the file
#     target = target+"/"+original.split('\\')[len(original.split('\\'))-1]
#     targ = str(Path().absolute())+"/"+now+"/"+projname+'/'+doss+"/"+doss+"-"+str(i)+".png"
#     os.rename(target, targ)
#     return projname+'/'+doss+"/"+doss+"-"+str(i)+".png"

# def siteplan(now, projname):
#     pathliste = []
#     li=[]
#     driver.find_elements_by_xpath("//div[@class='vux-tab-item nav_bar']")[1].click() #site plan
#     os.makedirs(str(Path().absolute())+"/"+now+"/"+projname+'/'+'balance-units')
#     while(len(driver.find_elements_by_xpath("//div[@class='SitePlan']"))==0):
#         time.sleep(3)
#     time.sleep(2)
#     error = driver.find_elements_by_class_name('text_err')
#     time.sleep(2)
#     if(len(error)==0):
#         li = driver.find_elements_by_xpath("//label[@class='vux-label']")
#         for i in range(1,len(li)):
#             li[i].click()
            
#             while(len(driver.find_elements_by_class_name("UpLaod"))==0):
#                 time.sleep(3)
#             time.sleep(5)
#             driver.find_element_by_class_name("UpLaod").click()
            
#             while(len(driver.find_elements_by_class_name("img-box"))==0):
#                 time.sleep(3)
#             time.sleep(2)
#             dl = driver.find_elements_by_class_name("img-box")    #download
#             ok = False
#             while(ok == False):
#                 try:
#                     dl = driver.find_elements_by_class_name("img-box")
#                     time.sleep(1)
#                     dl[int(len(dl)-2)].click()
#                     ok=True
#                 except Exception:
#                     ok = False
#                     pass
            
#             dow = gw.getWindowsWithTitle('APP')[0]
#             dow.minimize()
#             dow.maximize()
#             dow.activate()
#             pyautogui.click(821, 455)
#             pyautogui.click(821, 455)
#             time.sleep(2)
#             pyautogui.press('down')
#             pyautogui.press('tab')
#             pyautogui.press('tab')
#             pyautogui.press('space')
#             pyautogui.press('enter')
#             time.sleep(2)
#             driver.back()
            
#             path = moveFile(projname, i, now, 'balance-units')
#             pathliste.append(path)
#     return [pathliste, error]
    
# def summary(now, projname):
#     li = []
#     os.makedirs(str(Path().absolute())+"/"+now+"/"+projname+'/'+'distribution-charts')
#     time.sleep(2)
    
#     num = 0
    
#     clickon = driver.find_elements_by_class_name('tab_div')
#     if(len(clickon)!=0):
#         clickon[0].click()
#         WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.CLASS_NAME, "tableList_lf_icon")))
#         time.sleep(2)
#         driver.find_element_by_class_name('tableList_lf_icon').click() #download
#         time.sleep(5)
            
#         while(len(driver.find_elements_by_class_name('pswp__img')) == 0):
#             driver.find_element_by_class_name('tableList_lf_icon').click() #download
#             time.sleep(5)
            
        
#         path = download(now, projname, 'distribution-charts', 'distribution-charts-'+str(1))
#         li.append(path)
            
#         #check num of files
#         aze = driver.page_source
#         num = int(re.findall(r'"pswp__counter">\d+ \/ \d+', aze)[0].split('>')[1][len(re.findall(r'"pswp__counter">\d+ \/ \d+', aze)[0].split('>')[1])-1:])
#         continuke = True
#         if(num>1):
#             for i in range(num-1):
#                 if(continuke):
#                     try:
#                         driver.find_elements_by_xpath("//button[@class='pswp__button pswp__button--arrow--right']")[1].click()
#                     except Exception:
#                         continuke = False
#                         pass
#                     if(continuke):
#                         WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH, "//img[@class='pswp__img']")))
#                         time.sleep(5)
                        
#                         path = download(now, projname, 'distribution-charts', 'distribution-charts-'+str(i+1))
#                         li.append(path)
#                         #moveFile(projname, i+1, now, 'distribution-charts')
#     return li

# def download(now, projname, doss, name):
#     time.sleep(2)
#     dl = driver.find_elements_by_class_name("img-box") #download
#     time.sleep(2)
#     dl[int(len(dl)-2)].click()
#     time.sleep(1)
    
#     driver.switch_to.window(driver.window_handles[-1])
#     while(len(driver.find_elements_by_tag_name('img'))==0):
#         time.sleep(2)
        
#     img = driver.find_elements_by_tag_name('img')[0]
#     src = img.get_attribute('src')
#     path = str(Path().absolute())+"/"+now+"/"+projname+'/'+doss+'/'+name+'.png'
#     urllib.request.urlretrieve(src, path)
#     driver.close()
#     driver.switch_to.window(driver.window_handles[0])
#     return projname+'/'+doss+'/'+name+'.png'

# def info(now, projname):
#     offliste =  []
#     #go back and click again on Unit Table List
#     driver.back()
#     time.sleep(2)
    
#     clickon = driver.find_elements_by_class_name('tab_div')
#     if(len(clickon)!=0):
        
#         clickon[0].click()
#         os.makedirs(str(Path().absolute())+"/"+now+"/"+projname+'/'+'floor-plans')

#         while(len(driver.find_elements_by_xpath("//div[@class='vux-tab-wrap']/div/div/div")) == 0):
#             time.sleep(3)
#         time.sleep(4)
        
#         blocs = driver.find_elements_by_xpath("//div[@class='vux-tab-wrap']/div/div/div")[1:]
        
#         for i in blocs:
#             i.click()
#             while(len(driver.find_elements_by_xpath("//div[@class='table_td_body']"))==0):
#                 time.sleep(2)
               
#             time.sleep(4)
            
#             cases = driver.find_elements_by_xpath("//div[@class='table_td-box SOLD']")
#             cases += driver.find_elements_by_xpath("//div[@class='table_td-box AVAILABLE']")
#             for j in cases:
               
#                 time.sleep(3)
#                 j.click()
#                 count = 0
#                 while((len(driver.find_elements_by_xpath("//img[@class='unitImg']")) == 0 or len(driver.find_elements_by_xpath("//div[@class='vux-flexbox unitInfoTab-box vux-flex-row']")) == 0) and count<7):
#                     time.sleep(3)
                    
#                     count += 1
#                 while(len(driver.find_elements_by_xpath("//div[@class='vux-flexbox unitInfoTab-box vux-flex-row']"))==0):
#                     time.sleep(2)
                        
                
#                 time.sleep(2)
                
#                 li = driver.find_elements_by_xpath("//div[@class='vux-flexbox unitInfoTab-box vux-flex-row']")
#                 dicte = {}
#                 dicte = {'Project':None,
#                          'Unit':None,
#                          'Status':None,
#                          'Area(Sqft/Sqm)':None,
#                          'PSF':None,
#                          'Bedrooms':None,
#                          'Bathrooms':None,
#                          'Plan':None,
#                          'Floor':None,
#                          'Type':None,
#                          'Block':None,
#                          'Selling Price':None,
#                          'Image':None}
#                 dicte['Unit'] = driver.find_element_by_xpath("//h1[@class='vux-header-title']").text
#                 for k in li:
#                     txt = k.text.split('\n')
#                     if(txt[0] in dicte):
#                         dicte[txt[0]] = txt[1]
                        
#                 if(dicte['Area(Sqft/Sqm)'] != None):
#                     dicte['Area(Sqft/Sqm)'] = dicte['Area(Sqft/Sqm)'].split("/")[0]
#                 #If available
#                 li = driver.find_elements_by_xpath("//div[@class='vux-flexbox unitInfoTab-box vux-flex-row padding-top']")
#                 lowest_price = -1
#                 for z in li:
#                     txt = z.text.split('\n')
#                     if(txt[0] == 'Selling Price' or txt[0]=='After Rental Subsidy'):
#                         if(int(txt[1][1:].replace(',','')) < lowest_price):
#                             lowest_price = int(txt[1][1:].replace(',',''))
#                 dicte['Selling Price'] = lowest_price
#                 if(dicte['PSF'] != None):
#                     dicte['PSF'] = int(dicte['PSF'][1:].replace(',',''))
                
#                 filename = 'default'
#                 if(dicte['Plan']==None and dicte['Floor']==None):
#                     filename = "default"
#                 else:
#                     filename = dicte['Floor']+'-'+dicte['Plan']
                
#                 if(len(driver.find_elements_by_xpath("//img[@class='unitImg']"))!=0):
#                     srcimg = str(driver.find_elements_by_xpath("//img[@class='unitImg']")[0].get_attribute("src"))
#                     driver.execute_script('''window.open("'''+srcimg+'''","_blank");''')
#                     driver.switch_to.window(driver.window_handles[-1])
                
#                     while(len(driver.find_elements_by_tag_name('img')) == 0):
#                         time.sleep(3)
                    
#                     path = str(Path().absolute())+"/"+now+"/"+projname+'/'+'floor-plans'+'/'+filename+'.png'
#                     img = driver.find_elements_by_tag_name('img')[0]
#                     src = img.get_attribute('src')
#                     urllib.request.urlretrieve(src, path)
#                     dicte['Image'] = projname+'/'+'floor-plans'+'/'+filename+'.png'
#                     time.sleep(1)
#                     driver.close()
#                     driver.switch_to.window(driver.window_handles[0])
                
#                 dicte['Project'] = projname
#                 offliste.append(dicte)
#                 driver.back()
#     return offliste

# def minu(a,b):
#     if(a!=None):
#         a = float(a)
#     if(b!=None):
#         b = float(b)
#     if(a==None):
#         return b
#     if(b==None):
#         return a
#     if(a<b):
#         return a
#     if(b<a):
#         return b
#     if(a==b):
#         return a

# def maxu(a,b):
#     if(a!=None):
#         a = float(a)
#     if(b!=None):
#         b = float(b)
#     if(a==None):
#         return b
#     if(b==None):
#         return a
#     if(a>b):
#         return a
#     if(b>a):
#         return b
#     if(a==b):
#         return a

# def u(X, Y, xpath):  #To scroll down page
#     bo = True
#     value = 0
#     while(bo):
#         bo = False
#         dow = gw.getWindowsWithTitle('APP')[0]
#         dow.activate()
        
#         time.sleep(2)
#         pyautogui.click(x=X, y=Y)
#         time.sleep(0.5)
#         pyautogui.click(x=X, y=Y)
#         time.sleep(2)
#         if(value<len(driver.find_elements_by_xpath(xpath))):
#             bo = True
#             value = len(driver.find_elements_by_xpath(xpath))

# def final(now, projname):
#     if(os.path.isdir(str(Path().absolute())+"/"+now+"/"+projname+'/'+'floor-plans'==False)):
#         os.makedirs(str(Path().absolute())+"/"+now+"/"+projname+'/'+'floor-plans')
#     offliste = []
#     count = 0
#     while(len(driver.find_elements_by_xpath("//div[@class='vux-tab-item nav_bar']"))<5):
#         time.sleep(3)
#     time.sleep(3)
#     driver.find_elements_by_xpath("//div[@class='vux-tab-item nav_bar']")[3].click()
#     while(len(driver.find_elements_by_class_name('Units_box_bom'))==0):
#         time.sleep(2)
#     driver.maximize_window()
#     u(1885, 893, "//div[@class='vux-flexbox units_row vux-flex-row']")
#     lite = driver.find_elements_by_xpath("//div[@class='vux-flexbox units_row vux-flex-row']")
#     for i in range(len(lite)):
#         while(len(driver.find_elements_by_xpath("//div[@class='vux-flexbox units_row vux-flex-row']"))==0):
#             time.sleep(3)
#         time.sleep(3)
#         lite[i].click()
#         while(len(driver.find_elements_by_xpath("//div[@class='vux-flexbox unitInfoTab-box vux-flex-row']"))==0):
#             time.sleep(2)
#         li = driver.find_elements_by_xpath("//div[@class='vux-flexbox unitInfoTab-box vux-flex-row']")
#         dicte = {}
#         dicte = {'Project':None,
#                  'Unit':None,
#                  'Status':None,
#                  'Area(Sqft/Sqm)':None,
#                  'PSF':None,
#                  'Bedrooms':None,
#                  'Bathrooms':None,
#                  'Plan':None,
#                  'Floor':None,
#                  'Type':None,
#                  'Block':None,
#                  'Selling Price':None,
#                  'Image':None}
#         for k in li:
#             txt = k.text.split('\n')
#             if(txt[0] in dicte):
#                 dicte[txt[0]] = txt[1]
#         name = driver.find_element_by_xpath("//h1[@class='vux-header-title']").text
#         dicte['Unit'] = name
#         if(dicte['Area(Sqft/Sqm)'] != None):
#             dicte['Area(Sqft/Sqm)'] = dicte['Area(Sqft/Sqm)'].split("/")[0]
       
#         #If available
#         li = driver.find_elements_by_xpath("//div[@class='vux-flexbox unitInfoTab-box vux-flex-row padding-top']")
#         lowest_price = -1
#         for z in li:
#             txt = z.text.split('\n')
#             if(txt[0] == 'Selling Price' or txt[0]=='After Rental Subsidy'):
#                 if(int(txt[1][1:].replace(',','')) < lowest_price):
#                     lowest_price = int(txt[1][1:].replace(',',''))
#         dicte['Selling Price'] = lowest_price
#         if(dicte['PSF'] != None):
#             dicte['PSF'] = int(dicte['PSF'][1:].replace(',',''))
            
#         filename = 'default'
#         if(dicte['Plan']==None and dicte['Floor']==None):
#             filename = "default"
#         else:
#             filename = dicte['Floor']+'-'+dicte['Plan']
            
#         if(len(driver.find_elements_by_xpath("//img[@class='unitImg']"))!=0):
#             srcimg = str(driver.find_elements_by_xpath("//img[@class='unitImg']")[0].get_attribute("src"))
#             driver.execute_script('''window.open("'''+srcimg+'''","_blank");''')
#             driver.switch_to.window(driver.window_handles[-1])
        
#             while(len(driver.find_elements_by_tag_name('img')) == 0):
#                 time.sleep(3)
            
#             path = str(Path().absolute())+"/"+now+"/"+projname+'/'+'floor-plans'+'/'+filename+'.png'
#             img = driver.find_elements_by_tag_name('img')[0]
#             src = img.get_attribute('src')
#             urllib.request.urlretrieve(src, path)
#             dicte['Image'] = projname+'/'+'floor-plans'+'/'+filename+'.png'
#             time.sleep(1)
#             driver.close()
#             driver.switch_to.window(driver.window_handles[0])
            
#         dicte['Project'] = projname
#         offliste.append(dicte)
        
#         driver.back()
#     return offliste


# def search(li):
    
#     now = str(datetime.now()).replace(":",'-')
#     os.makedirs(str(Path().absolute())+"\\"+now) #create script folder
#     listefin = []
#     tab_1 = []
#     tab_2 = []
#     tab_3 = []
#     tab_4 = []
#     tab_5 = []
#     tab_6 = []
#     tab_9 = []
#     driver.back()
#     driver.back()
#     while(len(driver.find_elements_by_class_name('search_div_lf'))==0):
#         time.sleep(2)
#     #WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.CLASS_NAME, "search_div_lf")))
    
#     driver.find_element_by_class_name('search_div_lf').click()
#     while(len(driver.find_elements_by_tag_name('input')) == 0):
#         driver.find_element_by_class_name('search_div_lf').click()
#         time.sleep(3)
#     for i in li:    #pour chaque proj
#         time.sleep(6)
#         oup = driver.find_elements_by_tag_name('input')
#         while(len(oup) == 0): 
#             time.sleep(3)
#             oup = driver.find_elements_by_tag_name('input')
        
#         oup = oup[0]
#         oup.click()
#         oup.send_keys(Keys.CONTROL,'a')
#         oup.send_keys(Keys.DELETE)
#         oup.send_keys(i)
#         oup.send_keys(Keys.RETURN)
#         elem = driver.find_elements_by_xpath("//div[@class='cardBox_bom_hint']/h3")
#         count = 0
#         while(len(elem)==0 and count<8):
#             time.sleep(2)
#             elem = driver.find_elements_by_xpath("//div[@class='cardBox_bom_hint']/h3")
#             count += 1
#         if(len(driver.find_elements_by_xpath("//p[@class='van-empty__description']"))==0):
#             time.sleep(5)
#             elemun = driver.find_elements_by_xpath("//div[@class='cardBox_bom_hint']/h3")
#             elemun[0].click()
            
#             numerouno = getdata()
#             numerodos = units()
            
#             os.makedirs(str(Path().absolute())+"\\"+now+"\\"+numerouno[0])
            
#             path_un = siteplan(now, numerouno[0])
#             tres = []
#             path_deux = []
#             if(len(path_un[1])==0):
#                 path_deux = summary(now, numerouno[0])
#                 tres = info(now, numerouno[0])
#                 driver.back()
#                 fin = final(now, numerouno[0])
#             else:
                
#                 fin = final(now, numerouno[0])
#                 driver.back()
                
            
#             if(len(tres)!=0 or len(path_deux)!=0):
#                  driver.back()
#             if(len(tres)!=0):
#                 tab_6 += tres
#             if(len(fin)!=0):
#                 tab_9 += fin
            
#             tab_1.append(numerouno)  #[name, dicte, count]
#             tab_2.append([numerouno[0],numerodos[0]])  #projname, liste
#             tab_3.append([numerouno[0],numerodos[1]])
#             tab_4.append(path_un[0])
#             tab_5.append(path_deux)
            
        
    

#     ''' Summary by Type '''
#     #tab_6 = [{'Project': 'Royal Hallmark', 'Unit': '#05-01', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '2077', 'PSF': None, 'Bedrooms': '5', 'Plan': 'D1-P', 'Floor': '05', 'Type': '5 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#05-02', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1130', 'PSF': None, 'Bedrooms': '4', 'Plan': 'C1-A', 'Floor': '05', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#05-03', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '797', 'PSF': None, 'Bedrooms': '3', 'Plan': 'A1', 'Floor': '05', 'Type': '3 Bedroom Classic', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#05-04', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '915', 'PSF': None, 'Bedrooms': '3', 'Plan': 'B1-A', 'Floor': '05', 'Type': '3 Bedroom Premium', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#05-05', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '915', 'PSF': None, 'Bedrooms': '3', 'Plan': 'B1-A', 'Floor': '05', 'Type': '3 Bedroom Premium', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#05-06', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '797', 'PSF': None, 'Bedrooms': '3', 'Plan': 'A1', 'Floor': '05', 'Type': '3 Bedroom Classic', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#05-07', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1130', 'PSF': None, 'Bedrooms': '4', 'Plan': 'C1-A', 'Floor': '05', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#05-08', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '2077', 'PSF': None, 'Bedrooms': '5', 'Plan': 'D1-P', 'Floor': '05', 'Type': '5 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#04-01', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1292', 'PSF': None, 'Bedrooms': '4', 'Plan': 'C2', 'Floor': '04', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#04-02', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1130', 'PSF': None, 'Bedrooms': '4', 'Plan': 'C1-A', 'Floor': '04', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#04-03', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '797', 'PSF': None, 'Bedrooms': '3', 'Plan': 'A1', 'Floor': '04', 'Type': '3 Bedroom Classic', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#04-04', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '915', 'PSF': None, 'Bedrooms': '3', 'Plan': 'B1-A', 'Floor': '04', 'Type': '3 Bedroom Premium', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#04-05', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '915', 'PSF': None, 'Bedrooms': '3', 'Plan': 'B1-A', 'Floor': '04', 'Type': '3 Bedroom Premium', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#04-06', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '797', 'PSF': None, 'Bedrooms': '3', 'Plan': 'A1', 'Floor': '04', 'Type': '3 Bedroom Classic', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#04-07', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1130', 'PSF': None, 'Bedrooms': '4', 'Plan': 'C1-A', 'Floor': '04', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#04-08', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1292', 'PSF': None, 'Bedrooms': '4', 'Plan': 'C2', 'Floor': '04', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#03-01', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1292', 'PSF': None, 'Bedrooms': '4', 'Plan': 'C2', 'Floor': '03', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#03-02', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1130', 'PSF': None, 'Bedrooms': '4', 'Plan': 'C1-A', 'Floor': '03', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#03-03', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '797', 'PSF': None, 'Bedrooms': '3', 'Plan': 'A1', 'Floor': '03', 'Type': '3 Bedroom Classic', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#03-04', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '915', 'PSF': None, 'Bedrooms': '3', 'Plan': 'B1-A', 'Floor': '03', 'Type': '3 Bedroom Premium', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#03-05', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '915', 'PSF': None, 'Bedrooms': '3', 'Plan': 'B1-A', 'Floor': '03', 'Type': '3 Bedroom Premium', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#03-06', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '797', 'PSF': None, 'Bedrooms': '3', 'Plan': 'A1', 'Floor': '03', 'Type': '3 Bedroom Classic', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#03-07', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1130', 'PSF': None, 'Bedrooms': '4', 'Plan': 'C1-A', 'Floor': '03', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#03-08', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1292', 'PSF': None, 'Bedrooms': '4', 'Plan': 'C2', 'Floor': '03', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#02-01', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1292', 'PSF': None, 'Bedrooms': '4', 'Plan': 'C2', 'Floor': '02', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#02-02', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1163', 'PSF': None, 'Bedrooms': '4', 'Plan': 'C1-B', 'Floor': '02', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#02-04', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '936', 'PSF': None, 'Bedrooms': '3', 'Plan': 'B1-B', 'Floor': '02', 'Type': '3 Bedroom Premium', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#02-05', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '936', 'PSF': None, 'Bedrooms': '3', 'Plan': 'B1-B', 'Floor': '02', 'Type': '3 Bedroom Premium', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#02-07', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1163', 'PSF': None, 'Bedrooms': '4', 'Plan': 'C1-B', 'Floor': '02', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#02-08', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1292', 'PSF': None, 'Bedrooms': '4', 'Plan': 'C2', 'Floor': '02', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#01-01', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1658', 'PSF': None, 'Bedrooms': '5', 'Plan': 'E1', 'Floor': '01', 'Type': '5 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#01-08', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1658', 'PSF': None, 'Bedrooms': '5', 'Plan': 'E1', 'Floor': '01', 'Type': '5 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}]
    
#     summ = []  #projname, type, minsize, maxsize, min psf, max psf, min price, max pri, available, total units
#     types = [] #[projname, type]
#     for j in tab_6: 
#         if([j['Project'], j['Type']] in types):  #Meme type et project
#             index = types.index([j['Project'], j['Type']])
#             if(j['Status']=='AVAILABLE'):
#                 summ[index][2] = minu(summ[index][2], j['Area(Sqft/Sqm)'])
#                 summ[index][3] = maxu(summ[index][3], j['Area(Sqft/Sqm)'])
#                 summ[index][4] = minu(summ[index][4], j['PSF'])
#                 summ[index][5] = maxu(summ[index][5], j['PSF'])
#                 summ[index][6] = minu(summ[index][6], j['Selling Price'])
#                 summ[index][7] = maxu(summ[index][7], j['Selling Price'])
#                 summ[index][8] = summ[index][8] + 1
#             summ[index][9] = summ[index][9] + 1
            
#         else:
#             types.append([j['Project'], j['Type']])
#             if(j['Status'] == 'AVAILABLE'):
#                 summ.append([j['Project'], j['Type'], j['Area(Sqft/Sqm)'], j['Area(Sqft/Sqm)'], j['PSF'], j['PSF'], j['Selling Price'], j['Selling Price'], 1, 1])
#             else:
#                 summ.append([j['Project'], j['Type'], 0, 0, 0, 0, 0, 0, 0, 1])

#     '''Summary By Plan '''
#     summun = []  #projname, type, plan, minsize, maxsize, min psf, max psf, min price, max pri, available, total units
#     plan = [] #[projname, type, plan]
#     for j in tab_6: 
#         if([j['Project'], j['Type'], j['Plan']] in plan):  #Meme type et project et meme plan
#             index = plan.index([j['Project'], j['Type'], j['Plan']])
#             if(j['Status']=='AVAILABLE'):
#                 summun[index][3] = minu(summun[index][3], j['Area(Sqft/Sqm)'])
#                 summun[index][4] = maxu(summun[index][4], j['Area(Sqft/Sqm)'])
#                 summun[index][5] = minu(summun[index][5], j['PSF'])
#                 summun[index][6] = maxu(summun[index][6], j['PSF'])
#                 summun[index][7] = minu(summun[index][7], j['Selling Price'])
#                 summun[index][8] = maxu(summun[index][8], j['Selling Price'])
#                 summun[index][9] = summun[index][9] + 1
#             summun[index][10] = summun[index][10] + 1
            
#         else:
#             plan.append([j['Project'], j['Type'], j['Plan']])
#             if(j['Status']=='AVAILABLE'):
#                 summun.append([j['Project'], j['Type'],j['Plan'], j['Area(Sqft/Sqm)'], j['Area(Sqft/Sqm)'], j['PSF'], j['PSF'], j['Selling Price'], j['Selling Price'], 1, 1])
#             else:
#                 summun.append([j['Project'], j['Type'],j['Plan'], 0, 0, 0, 0, 0, 0, 0, 1])
    
    
#     #tab_9 = [{'Project': 'Royal Hallmark', 'Unit': None, 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1292', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C2', 'Floor': '02', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/02-C2.png'}, {'Project': 'Royal Hallmark', 'Unit': None, 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1292', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C2', 'Floor': '03', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/03-C2.png'}, {'Project': 'Royal Hallmark', 'Unit': None, 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1292', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C2', 'Floor': '04', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/04-C2.png'}, {'Project': 'Royal Hallmark', 'Unit': None, 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '2077', 'PSF': None, 'Bedrooms': '5', 'Bathrooms': None, 'Plan': 'D1-P', 'Floor': '05', 'Type': '5 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/05-D1-P.png'}, {'Project': 'Royal Hallmark', 'Unit': None, 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1163', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C1-B', 'Floor': '02', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/02-C1-B.png'}, {'Project': 'Royal Hallmark', 'Unit': None, 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1130', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C1-A', 'Floor': '03', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/03-C1-A.png'}, {'Project': 'Royal Hallmark', 'Unit': None, 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1130', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C1-A', 'Floor': '04', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/04-C1-A.png'}, {'Project': 'Royal Hallmark', 'Unit': None, 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1130', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C1-A', 'Floor': '05', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/05-C1-A.png'}, {'Project': 'Royal Hallmark', 'Unit': None, 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '797', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'A1', 'Floor': '03', 'Type': '3 Bedroom Classic', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/03-A1.png'}, {'Project': 'Royal Hallmark', 'Unit': None, 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '797', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'A1', 'Floor': '04', 'Type': '3 Bedroom Classic', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/04-A1.png'}, {'Project': 'Royal Hallmark', 'Unit': None, 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '797', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'A1', 'Floor': '05', 'Type': '3 Bedroom Classic', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/05-A1.png'}, {'Project': 'Royal Hallmark', 'Unit': None, 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '936', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'B1-B', 'Floor': '02', 'Type': '3 Bedroom Premium', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/02-B1-B.png'}, {'Project': 'Royal Hallmark', 'Unit': None, 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '915', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'B1-A', 'Floor': '03', 'Type': '3 Bedroom Premium', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/03-B1-A.png'}, {'Project': 'Royal Hallmark', 'Unit': None, 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '915', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'B1-A', 'Floor': '04', 'Type': '3 Bedroom Premium', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/04-B1-A.png'}, {'Project': 'Royal Hallmark', 'Unit': None, 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '915', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'B1-A', 'Floor': '05', 'Type': '3 Bedroom Premium', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/05-B1-A.png'}, {'Project': 'Royal Hallmark', 'Unit': None, 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '936', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'B1-B', 'Floor': '02', 'Type': '3 Bedroom Premium', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/02-B1-B.png'}, {'Project': 'Royal Hallmark', 'Unit': None, 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '915', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'B1-A', 'Floor': '03', 'Type': '3 Bedroom Premium', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/03-B1-A.png'}, {'Project': 'Royal Hallmark', 'Unit': None, 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '915', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'B1-A', 'Floor': '04', 'Type': '3 Bedroom Premium', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/04-B1-A.png'}, {'Project': 'Royal Hallmark', 'Unit': None, 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '915', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'B1-A', 'Floor': '05', 'Type': '3 Bedroom Premium', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/05-B1-A.png'}, {'Project': 'Royal Hallmark', 'Unit': None, 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '797', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'A1', 'Floor': '03', 'Type': '3 Bedroom Classic', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/03-A1.png'}, {'Project': 'Royal Hallmark', 'Unit': None, 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '797', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'A1', 'Floor': '04', 'Type': '3 Bedroom Classic', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/04-A1.png'}, {'Project': 'Royal Hallmark', 'Unit': None, 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '797', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'A1', 'Floor': '05', 'Type': '3 Bedroom Classic', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/05-A1.png'}, {'Project': 'Royal Hallmark', 'Unit': None, 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1163', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C1-B', 'Floor': '02', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/02-C1-B.png'}, {'Project': 'Royal Hallmark', 'Unit': None, 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1130', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C1-A', 'Floor': '03', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/03-C1-A.png'}, {'Project': 'Royal Hallmark', 'Unit': None, 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1130', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C1-A', 'Floor': '04', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/04-C1-A.png'}, {'Project': 'Royal Hallmark', 'Unit': None, 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1130', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C1-A', 'Floor': '05', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/05-C1-A.png'}, {'Project': 'Royal Hallmark', 'Unit': None, 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1292', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C2', 'Floor': '02', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/02-C2.png'}, {'Project': 'Royal Hallmark', 'Unit': None, 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1292', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C2', 'Floor': '03', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/03-C2.png'}, {'Project': 'Royal Hallmark', 'Unit': None, 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1292', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C2', 'Floor': '04', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/04-C2.png'}, {'Project': 'Royal Hallmark', 'Unit': None, 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '2077', 'PSF': None, 'Bedrooms': '5', 'Bathrooms': None, 'Plan': 'D1-P', 'Floor': '05', 'Type': '5 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/05-D1-P.png'}]
    
#     '''Unit summary by type '''
#     summdeux = []  #projname, type, minsize, maxsize, min psf, max psf, min price, max pri, available, total units
#     typesun = [] #[projname, type]
#     for j in tab_6: 
#         if([j['Project'], j['Type']] in typesun):  #Meme type et project
#             index = typesun.index([j['Project'], j['Type']])
#             if(j['Status']=='AVAILABLE'):
#                 summdeux[index][2] = minu(summdeux[index][2], j['Area(Sqft/Sqm)'])
#                 summdeux[index][3] = maxu(summdeux[index][3], j['Area(Sqft/Sqm)'])
#                 summdeux[index][4] = minu(summdeux[index][4], j['PSF'])
#                 summdeux[index][5] = maxu(summdeux[index][5], j['PSF'])
#                 summdeux[index][6] = minu(summdeux[index][6], j['Selling Price'])
#                 summdeux[index][7] = maxu(summdeux[index][7], j['Selling Price'])
#                 summdeux[index][8] = summdeux[index][8] + 1
#             summdeux[index][9] = summdeux[index][9] + 1
            
#         else:
#             typesun.append([j['Project'], j['Type']])
#             if(j['Status'] == 'AVAILABLE'):
#                 summdeux.append([j['Project'], j['Type'], j['Area(Sqft/Sqm)'], j['Area(Sqft/Sqm)'], j['PSF'], j['PSF'], j['Selling Price'], j['Selling Price'], 1, 1])
#             else:
#                 summdeux.append([j['Project'], j['Type'], 0, 0, 0, 0, 0, 0, 0, 1])


#     '''Unit Summary By Plan '''
#     summtrois = []  #projname, type, plan, minsize, maxsize, min psf, max psf, min price, max pri, available, total units
#     planun = [] #[projname, type, plan]
#     for j in tab_6: 
#         if([j['Project'], j['Type'], j['Plan']] in planun):  #Meme type et project et meme plan
#             index = planun.index([j['Project'], j['Type'], j['Plan']])
#             if(j['Status']=='AVAILABLE'):
#                 summtrois[index][3] = minu(summtrois[index][3], j['Area(Sqft/Sqm)'])
#                 summtrois[index][4] = maxu(summtrois[index][4], j['Area(Sqft/Sqm)'])
#                 summtrois[index][5] = minu(summtrois[index][5], j['PSF'])
#                 summtrois[index][6] = maxu(summtrois[index][6], j['PSF'])
#                 summtrois[index][7] = minu(summtrois[index][7], j['Selling Price'])
#                 summtrois[index][8] = maxu(summtrois[index][8], j['Selling Price'])
#                 summtrois[index][9] = summtrois[index][9] + 1
#             summtrois[index][10] = summtrois[index][10] + 1
            
#         else:
#             planun.append([j['Project'], j['Type'], j['Plan']])
#             if(j['Status']=='AVAILABLE'):
#                 summtrois.append([j['Project'], j['Type'],j['Plan'], j['Area(Sqft/Sqm)'], j['Area(Sqft/Sqm)'], j['PSF'], j['PSF'], j['Selling Price'], j['Selling Price'], 1, 1])
#             else:
#                 summtrois.append([j['Project'], j['Type'],j['Plan'], 0, 0, 0, 0, 0, 0, 0, 1])
    
    
#     populate(tab_1, tab_2, tab_3, tab_4, tab_5, tab_6, summ, summun, tab_9, summdeux, summtrois)
    
    



# def populate(tab_1, tab_2, tab_3, tab_4, tab_5, tab_6, summ, summun, tab_9, summdeux, summtrois):
    
    
#     wb = Workbook()
#     ws1 = wb.active
#     ws1.title = "Info"
#     ws2 = wb.create_sheet(title="Summary - Units By Type")
#     ws3 = wb.create_sheet(title="Summary - Units By Floor Plan")
#     ws4 = wb.create_sheet(title="Site Plan - Balance Units")
#     ws5 = wb.create_sheet(title="Site Plan - Distribution Charts")
#     ws6 = wb.create_sheet(title="Site Plan - Units Info")
#     ws7 = wb.create_sheet(title="Site Plan - Summary - By Type")
#     ws8 = wb.create_sheet(title="Site Plan - Summary - By Plan")
#     ws9 = wb.create_sheet(title="Units - Units Info")
#     ws10 = wb.create_sheet(title="Units - Summary - By Type")
#     ws11 = wb.create_sheet(title="Units - Summary - By Plan")
    
#     ws1["A1"]="Project Name"
#     ws1["B1"]="Developer"
#     ws1["C1"]="Type"
#     ws1["D1"]="Total Units"
#     ws1["E1"]="Exp TOP"
#     ws1["F1"]="Address"
#     ws1["G1"]="Location"
#     ws1["H1"]="Gallery Address"
#     ws1["I1"]="Country"
#     ws1["J1"]="Tenure"
#     ws1["K1"]="Available units"
    
#     alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N"]
#     key1 = ["Developer","Type","Total Units","Exp TOP","Address","Location","Gallery Address","Country","Tenure"]
    
#     for i in range(len(tab_1)):
#         if(tab_1[i][0]==None):
#             temp = 'None'
#         else:
#             temp = tab_1[i][0]
#         ws1["A"+str(i+2)] = tab_1[i][0]
        
#         if(tab_1[i][2]==None):
#             temp = 'None'
#         else:
#             temp = tab_1[i][2]
#         ws1["K"+str(i+2)] = tab_1[i][2]
        
#         for j in range(len(key1)):
#             if(tab_1[i][1][key1[j]]==None):
#                 temp = 'None'
#             else:
#                 temp = tab_1[i][1][key1[j]]
#             ws1[alpha[j+1]+str(i+2)] = temp
            

    
#     ws2["A1"]="Project Name"
#     ws2["B1"]="Type"
#     ws2["C1"]="Reserved"
#     ws2["D1"]="Sold"
#     ws2["E1"]="Available"
#     ws2["F1"]="Total"
    
#     compt = 1
#     for i in range(len(tab_2)):    
#         if(len(tab_2[i][1])!=0):
#             for j in range(len(tab_2[i][1])):
#                 compt += 1
#                 ws2["A"+str(compt)] = tab_2[i][0]
#                 for k in range(len(tab_2[i][1][j])):
#                     if(tab_2[i][1][j][k]==None):
#                         temp = 'None'
#                     else:
#                         temp = tab_2[i][1][j][k]
#                     if(temp == '-'):
#                         temp = 0
#                     ws2[alpha[k+1]+str(compt)] = temp
                    
   
#     ws3["A1"]="Project Name"
#     ws3["B1"]="Plan"
#     ws3["C1"]="Reserved"
#     ws3["D1"]="Sold"
#     ws3["E1"]="Available"
#     ws3["F1"]="Total"
    
    
#     compt = 1
#     for i in range(len(tab_3)):    
#         if(len(tab_3[i][1])!=0):
#             for j in range(len(tab_3[i][1])):
#                 compt += 1
#                 ws3["A"+str(compt)] = tab_3[i][0]
#                 for k in range(len(tab_3[i][1][j])):
#                     if(tab_3[i][1][j][k]==None):
#                         temp = 'None'
#                     else:
#                         temp = tab_3[i][1][j][k]
#                     if(temp == '-'):
#                         temp = 0
#                     ws3[alpha[k+1]+str(compt)] = temp
                    
    
    
#     ws4["A1"]="Project Name"
#     ws4["B1"]="Balance Units"
#     compt = 1
#     for i in range(len(tab_4)):
#         if(len(tab_4[i])!=0 and len(tab_4[i][0])!=0):
#             compt +=1
#             if(tab_4[i][0]==None):
#                 temp = 'None'
#                 temp1 = 'None'
#             else:
#                 temp = tab_4[i][0].split('/')[0]
#                 temp1 = tab_4[i][0]
#             ws4["A"+str(compt)] = temp
#             ws4["B"+str(compt)] = '/'+temp1
    
#     ws5["A1"]="Project Name"
#     ws5["B1"]="Balance Units"
    
#     compt= 1
#     for i in range(len(tab_5)):
#         if(len(tab_5[i])!=0):
#             compt += 1
#             if(tab_5[i][0]==None):
#                 temp = 'None'
#                 temp1 = 'None'
#             else:
#                 temp = tab_5[i][0].split('/')[0]
#                 temp1 = tab_5[i][0]
#             ws5["A"+str(compt)] = temp
#             ws5["B"+str(compt)] = '/'+temp1
    
#     ws6["A1"]="Project Name"
#     ws6["B1"]="Unit #"
#     ws6["C1"]="Status"
#     ws6["D1"]="Area (sqft)"
#     ws6["E1"]="Selling Price"
#     ws6["F1"]="PSF"
#     ws6["G1"]="Bedrooms"
#     ws6["H1"]="Bathrooms"
#     ws6["I1"]="Plan"
#     ws6["J1"]="Floor"
#     ws6["K1"]="Type"
#     ws6["L1"]="Bloc"
#     ws6["M1"]="Image"
    
#     key6 = ['Project','Unit','Status','Area(Sqft/Sqm)','Selling Price','PSF','Bedrooms','Bathrooms','Plan','Floor','Type','Block','Image']
    
#     for i in range(len(tab_6)):
#         for j in range(len(key6)):
#             if(tab_6[i][key6[j]]==None):
#                 temp = 'None'
#             else:
#                 temp = tab_6[i][key6[j]]
#                 if(key6[j]=="Image"):
#                     temp = '/'+temp
#                 if(key6[j]=="Selling Price" and temp == -1):
#                     temp =  'None'
#                 if(key6[j]=="Floor"):
#                     temp =  int(temp)
#             ws6[alpha[j]+str(i+2)] = temp

#     ws7["A1"]="Project Name"
#     ws7["B1"]="Type"
#     ws7["C1"]="Min Size"
#     ws7["D1"]="Max Size"
#     ws7["E1"]="Min PSF"
#     ws7["F1"]="Max PSF"
#     ws7["G1"]="Min Price"
#     ws7["H1"]="Max Price"
#     ws7["I1"]="Available"
#     ws7["J1"]="Total Units"
    
#     for i in range(len(summ)):
#         for j in range(len(summ[i])):
#             if(summ[i][j]==None):
#                 temp='None'
#             else:
#                 temp = summ[i][j]
#                 if(temp == -1):
#                     temp = 'None'
#             ws7[alpha[j]+str(i+2)] = temp

#     ws8["A1"]="Project Name"
#     ws8["B1"]="Type"
#     ws8["C1"]="Plan"
#     ws8["D1"]="Min Size"
#     ws8["E1"]="Max Size"
#     ws8["F1"]="Min PSF"
#     ws8["G1"]="Max PSF"
#     ws8["H1"]="Min Price"
#     ws8["I1"]="Max Price"
#     ws8["J1"]="Available"
#     ws8["K1"]="Total Units"
    
#     for i in range(len(summun)):
#         for j in range(len(summun[i])):
#             if(summun[i][j]==None):
#                 temp='None'
#             else:
#                 temp = summun[i][j]
#                 if(temp == -1):
#                     temp = 'None'
#             ws8[alpha[j]+str(i+2)] = temp
    
#     ws9["A1"]="Project Name" 
#     ws9["B1"]="Unit #"
#     ws9["C1"]="Status"
#     ws9["D1"]="Area (sqft)"
#     ws9["E1"]="Selling Price"
#     ws9["F1"]="PSF"
#     ws9["G1"]="Bedrooms"
#     ws9["H1"]="Bathrooms"
#     ws9["I1"]="Plan"
#     ws9["J1"]="Floor"
#     ws9["K1"]="Type"
#     ws9["L1"]="Bloc"
#     ws9["M1"]="Image"
    
#     key9 = ['Project','Unit','Status','Area(Sqft/Sqm)','Selling Price','PSF','Bedrooms','Bathrooms','Plan','Floor','Type','Block','Image']
    
#     for i in range(len(tab_9)):
#         for j in range(len(key9)):
#             if(tab_9[i][key9[j]]==None):
#                 temp = 'None'
#             else:
#                 temp = tab_9[i][key9[j]]
#                 if(key9[j]=="Image"):
#                     temp = '/'+temp
#                 if(key9[j]=="Selling Price" and temp == -1):
#                     temp =  'None'
#                 if(key9[j]=="Floor"):
#                     temp =  int(temp)
#             ws9[alpha[j]+str(i+2)] = temp

    
#     ws10["A1"]="Project Name"
#     ws10["B1"]="Type"
#     ws10["C1"]="Min Size"
#     ws10["D1"]="Max Size"
#     ws10["E1"]="Min PSF"
#     ws10["F1"]="Max PSF"
#     ws10["G1"]="Min Price"
#     ws10["H1"]="Max Price"
#     ws10["I1"]="Available"
#     ws10["J1"]="Total Units"
    
#     for i in range(len(summdeux)):
#         for j in range(len(summdeux[i])):
#             if(summdeux[i][j]==None):
#                 temp='None'
#             else:
#                 temp = summdeux[i][j]
#                 if(temp == -1):
#                     temp = 'None'
#             ws10[alpha[j]+str(i+2)] = temp
    
#     ws11["A1"]="Project Name"
#     ws11["B1"]="Type"
#     ws11["C1"]="Plan"
#     ws11["D1"]="Min Size"
#     ws11["E1"]="Max Size"
#     ws11["F1"]="Min PSF"
#     ws11["G1"]="Max PSF"
#     ws11["H1"]="Min Price"
#     ws11["I1"]="Max Price"
#     ws11["J1"]="Available"
#     ws11["K1"]="Total Units"
    
#     for i in range(len(summtrois)):
#         for j in range(len(summtrois[i])):
#             if(summtrois[i][j]==None):
#                 temp='None'
#             else:
#                 temp = summtrois[i][j]
#                 if(temp == -1):
#                     temp = 'None'
#             ws11[alpha[j]+str(i+2)] = temp
    
     
#     wb.save('sample_book.xlsx')    
    



# #liste = liste[:4]
# boum = search(liste)

'''
tab_1 = [['Piccadilly Grand', {'Developer': 'CDL / MCL', 'Type': 'Mixed Development', 'Total Units': '407', 'Exp TOP': 'TBC', 'Address': 'Northumberland Rd', 'Location': 'D08 - Farrer Park / Serangoon Road', 'Gallery Address': None, 'Country': 'Singapore', 'Tenure': '99 Years'}, 0], ['Royal Hallmark', {'Developer': 'H Homes Pte Ltd', 'Type': 'Residential Lowrise', 'Total Units': '32', 'Exp TOP': 'Nov 2025', 'Address': '1 Haig Lane', 'Location': 'D15 - East Coast / Marine Parade', 'Gallery Address': None, 'Country': 'Singapore', 'Tenure': 'Freehold'}, 32], ['The Arden 雅诗轩', {'Developer': 'CNQC REALTY (PHOENIX) PTE LTD', 'Type': 'Residential Lowrise', 'Total Units': '105', 'Exp TOP': 'TBC', 'Address': '24 Phoenix Rd', 'Location': 'D23 - Bukit Batok / Bukit Panjang', 'Gallery Address': None, 'Country': 'Singapore', 'Tenure': '99 Years'}, 0]]
tab_2 = [['Piccadilly Grand', []], ['Royal Hallmark', [['3 Bedroom Classic', '-', '-', '6', '6'], ['3 Bedroom Premium', '-', '-', '8', '8'], ['4 Bedroom', '-', '-', '14', '14'], ['5 Bedroom', '-', '-', '4', '4'], ['', '-', '-', '32', '32']]], ['The Arden 雅诗轩', []]]
tab_3 = [['Piccadilly Grand', []], ['Royal Hallmark', [['A1', '-', '-', '6', '6'], ['B1-A', '-', '-', '6', '6'], ['B1-B', '-', '-', '2', '2'], ['C1-A', '-', '-', '6', '6'], ['C1-B', '-', '-', '2', '2'], ['C2', '-', '-', '6', '6'], ['D1-P', '-', '-', '2', '2'], ['E1', '-', '-', '2', '2'], ['', '-', '-', '32', '32']]], ['The Arden 雅诗轩', []]]
tab_4 = [[], ['Royal Hallmark/balance-units/balance-units-1.png'], []]
tab_5 = [[], ['Royal Hallmark/distribution-charts/distribution-charts-1.png'], []]
tab_6 = [{'Project': 'Royal Hallmark', 'Unit': '#05-01', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '2077', 'PSF': None, 'Bedrooms': '5', 'Bathrooms': None, 'Plan': 'D1-P', 'Floor': '05', 'Type': '5 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#05-02', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1130', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C1-A', 'Floor': '05', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#05-03', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '797', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'A1', 'Floor': '05', 'Type': '3 Bedroom Classic', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#05-04', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '915', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'B1-A', 'Floor': '05', 'Type': '3 Bedroom Premium', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#05-05', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '915', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'B1-A', 'Floor': '05', 'Type': '3 Bedroom Premium', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#05-06', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '797', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'A1', 'Floor': '05', 'Type': '3 Bedroom Classic', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#05-07', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1130', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C1-A', 'Floor': '05', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#05-08', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '2077', 'PSF': None, 'Bedrooms': '5', 'Bathrooms': None, 'Plan': 'D1-P', 'Floor': '05', 'Type': '5 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#04-01', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1292', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C2', 'Floor': '04', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#04-02', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1130', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C1-A', 'Floor': '04', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#04-03', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '797', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'A1', 'Floor': '04', 'Type': '3 Bedroom Classic', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#04-04', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '915', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'B1-A', 'Floor': '04', 'Type': '3 Bedroom Premium', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#04-05', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '915', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'B1-A', 'Floor': '04', 'Type': '3 Bedroom Premium', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#04-06', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '797', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'A1', 'Floor': '04', 'Type': '3 Bedroom Classic', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#04-07', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1130', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C1-A', 'Floor': '04', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#04-08', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1292', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C2', 'Floor': '04', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#03-01', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1292', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C2', 'Floor': '03', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#03-02', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1130', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C1-A', 'Floor': '03', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#03-03', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '797', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'A1', 'Floor': '03', 'Type': '3 Bedroom Classic', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#03-04', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '915', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'B1-A', 'Floor': '03', 'Type': '3 Bedroom Premium', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#03-05', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '915', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'B1-A', 'Floor': '03', 'Type': '3 Bedroom Premium', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#03-06', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '797', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'A1', 'Floor': '03', 'Type': '3 Bedroom Classic', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#03-07', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1130', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C1-A', 'Floor': '03', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#03-08', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1292', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C2', 'Floor': '03', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#02-01', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1292', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C2', 'Floor': '02', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#02-02', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1163', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C1-B', 'Floor': '02', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#02-04', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '936', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'B1-B', 'Floor': '02', 'Type': '3 Bedroom Premium', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#02-05', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '936', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'B1-B', 'Floor': '02', 'Type': '3 Bedroom Premium', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#02-07', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1163', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C1-B', 'Floor': '02', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#02-08', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1292', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C2', 'Floor': '02', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#01-01', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1658', 'PSF': None, 'Bedrooms': '5', 'Bathrooms': None, 'Plan': 'E1', 'Floor': '01', 'Type': '5 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#01-08', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1658', 'PSF': None, 'Bedrooms': '5', 'Bathrooms': None, 'Plan': 'E1', 'Floor': '01', 'Type': '5 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}]
summ = [['Royal Hallmark', '5 Bedroom', 1658.0, 2077.0, None, None, -1.0, -1.0, 4, 4], ['Royal Hallmark', '4 Bedroom', 1130.0, 1292.0, None, None, -1.0, -1.0, 14, 14], ['Royal Hallmark', '3 Bedroom Classic', 797.0, 797.0, None, None, -1.0, -1.0, 6, 6], ['Royal Hallmark', '3 Bedroom Premium', 915.0, 936.0, None, None, -1.0, -1.0, 8, 8]]
summun = [['Royal Hallmark', '5 Bedroom', 'D1-P', 2077.0, 2077.0, None, None, -1.0, -1.0, 2, 2], ['Royal Hallmark', '4 Bedroom', 'C1-A', 1130.0, 1130.0, None, None, -1.0, -1.0, 6, 6], ['Royal Hallmark', '3 Bedroom Classic', 'A1', 797.0, 797.0, None, None, -1.0, -1.0, 6, 6], ['Royal Hallmark', '3 Bedroom Premium', 'B1-A', 915.0, 915.0, None, None, -1.0, -1.0, 6, 6], ['Royal Hallmark', '4 Bedroom', 'C2', 1292.0, 1292.0, None, None, -1.0, -1.0, 6, 6], ['Royal Hallmark', '4 Bedroom', 'C1-B', 1163.0, 1163.0, None, None, -1.0, -1.0, 2, 2], ['Royal Hallmark', '3 Bedroom Premium', 'B1-B', 936.0, 936.0, None, None, -1.0, -1.0, 2, 2], ['Royal Hallmark', '5 Bedroom', 'E1', 1658.0, 1658.0, None, None, -1.0, -1.0, 2, 2]]
tab_9 = [{'Project': 'Royal Hallmark', 'Unit': '#01-01', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1658', 'PSF': None, 'Bedrooms': '5', 'Bathrooms': None, 'Plan': 'E1', 'Floor': '01', 'Type': '5 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#02-01', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1292', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C2', 'Floor': '02', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/02-C2.png'}, {'Project': 'Royal Hallmark', 'Unit': '#03-01', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1292', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C2', 'Floor': '03', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/03-C2.png'}, {'Project': 'Royal Hallmark', 'Unit': '#04-01', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1292', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C2', 'Floor': '04', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/04-C2.png'}, {'Project': 'Royal Hallmark', 'Unit': '#05-01', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '2077', 'PSF': None, 'Bedrooms': '5', 'Bathrooms': None, 'Plan': 'D1-P', 'Floor': '05', 'Type': '5 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/05-D1-P.png'}, {'Project': 'Royal Hallmark', 'Unit': '#02-02', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1163', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C1-B', 'Floor': '02', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/02-C1-B.png'}, {'Project': 'Royal Hallmark', 'Unit': '#03-02', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1130', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C1-A', 'Floor': '03', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/03-C1-A.png'}, {'Project': 'Royal Hallmark', 'Unit': '#04-02', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1130', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C1-A', 'Floor': '04', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/04-C1-A.png'}, {'Project': 'Royal Hallmark', 'Unit': '#05-02', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1130', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C1-A', 'Floor': '05', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/05-C1-A.png'}, {'Project': 'Royal Hallmark', 'Unit': '#03-03', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '797', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'A1', 'Floor': '03', 'Type': '3 Bedroom Classic', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/03-A1.png'}, {'Project': 'Royal Hallmark', 'Unit': '#04-03', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '797', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'A1', 'Floor': '04', 'Type': '3 Bedroom Classic', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/04-A1.png'}, {'Project': 'Royal Hallmark', 'Unit': '#05-03', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '797', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'A1', 'Floor': '05', 'Type': '3 Bedroom Classic', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/05-A1.png'}, {'Project': 'Royal Hallmark', 'Unit': '#02-04', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '936', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'B1-B', 'Floor': '02', 'Type': '3 Bedroom Premium', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/02-B1-B.png'}, {'Project': 'Royal Hallmark', 'Unit': '#03-04', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '915', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'B1-A', 'Floor': '03', 'Type': '3 Bedroom Premium', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/03-B1-A.png'}, {'Project': 'Royal Hallmark', 'Unit': '#04-04', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '915', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'B1-A', 'Floor': '04', 'Type': '3 Bedroom Premium', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/04-B1-A.png'}, {'Project': 'Royal Hallmark', 'Unit': '#05-04', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '915', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'B1-A', 'Floor': '05', 'Type': '3 Bedroom Premium', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/05-B1-A.png'}, {'Project': 'Royal Hallmark', 'Unit': '#02-05', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '936', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'B1-B', 'Floor': '02', 'Type': '3 Bedroom Premium', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/02-B1-B.png'}, {'Project': 'Royal Hallmark', 'Unit': '#03-05', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '915', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'B1-A', 'Floor': '03', 'Type': '3 Bedroom Premium', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/03-B1-A.png'}, {'Project': 'Royal Hallmark', 'Unit': '#04-05', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '915', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'B1-A', 'Floor': '04', 'Type': '3 Bedroom Premium', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/04-B1-A.png'}, {'Project': 'Royal Hallmark', 'Unit': '#05-05', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '915', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'B1-A', 'Floor': '05', 'Type': '3 Bedroom Premium', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/05-B1-A.png'}, {'Project': 'Royal Hallmark', 'Unit': '#03-06', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '797', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'A1', 'Floor': '03', 'Type': '3 Bedroom Classic', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/03-A1.png'}, {'Project': 'Royal Hallmark', 'Unit': '#04-06', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '797', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'A1', 'Floor': '04', 'Type': '3 Bedroom Classic', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/04-A1.png'}, {'Project': 'Royal Hallmark', 'Unit': '#05-06', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '797', 'PSF': None, 'Bedrooms': '3', 'Bathrooms': None, 'Plan': 'A1', 'Floor': '05', 'Type': '3 Bedroom Classic', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/05-A1.png'}, {'Project': 'Royal Hallmark', 'Unit': '#02-07', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1163', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C1-B', 'Floor': '02', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/02-C1-B.png'}, {'Project': 'Royal Hallmark', 'Unit': '#03-07', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1130', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C1-A', 'Floor': '03', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/03-C1-A.png'}, {'Project': 'Royal Hallmark', 'Unit': '#04-07', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1130', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C1-A', 'Floor': '04', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/04-C1-A.png'}, {'Project': 'Royal Hallmark', 'Unit': '#05-07', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1130', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C1-A', 'Floor': '05', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/05-C1-A.png'}, {'Project': 'Royal Hallmark', 'Unit': '#01-08', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1658', 'PSF': None, 'Bedrooms': '5', 'Bathrooms': None, 'Plan': 'E1', 'Floor': '01', 'Type': '5 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': None}, {'Project': 'Royal Hallmark', 'Unit': '#02-08', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1292', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C2', 'Floor': '02', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/02-C2.png'}, {'Project': 'Royal Hallmark', 'Unit': '#03-08', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1292', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C2', 'Floor': '03', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/03-C2.png'}, {'Project': 'Royal Hallmark', 'Unit': '#04-08', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '1292', 'PSF': None, 'Bedrooms': '4', 'Bathrooms': None, 'Plan': 'C2', 'Floor': '04', 'Type': '4 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/04-C2.png'}, {'Project': 'Royal Hallmark', 'Unit': '#05-08', 'Status': 'AVAILABLE', 'Area(Sqft/Sqm)': '2077', 'PSF': None, 'Bedrooms': '5', 'Bathrooms': None, 'Plan': 'D1-P', 'Floor': '05', 'Type': '5 Bedroom', 'Block': 'Royal Hallmark', 'Selling Price': -1, 'Image': 'Royal Hallmark/floor-plans/05-D1-P.png'}]
summdeux  = [['Royal Hallmark', '5 Bedroom', 1658.0, 2077.0, None, None, -1.0, -1.0, 4, 4], ['Royal Hallmark', '4 Bedroom', 1130.0, 1292.0, None, None, -1.0, -1.0, 14, 14], ['Royal Hallmark', '3 Bedroom Classic', 797.0, 797.0, None, None, -1.0, -1.0, 6, 6], ['Royal Hallmark', '3 Bedroom Premium', 915.0, 936.0, None, None, -1.0, -1.0, 8, 8]]
summtrois = [['Royal Hallmark', '5 Bedroom', 'D1-P', 2077.0, 2077.0, None, None, -1.0, -1.0, 2, 2], ['Royal Hallmark', '4 Bedroom', 'C1-A', 1130.0, 1130.0, None, None, -1.0, -1.0, 6, 6], ['Royal Hallmark', '3 Bedroom Classic', 'A1', 797.0, 797.0, None, None, -1.0, -1.0, 6, 6], ['Royal Hallmark', '3 Bedroom Premium', 'B1-A', 915.0, 915.0, None, None, -1.0, -1.0, 6, 6], ['Royal Hallmark', '4 Bedroom', 'C2', 1292.0, 1292.0, None, None, -1.0, -1.0, 6, 6], ['Royal Hallmark', '4 Bedroom', 'C1-B', 1163.0, 1163.0, None, None, -1.0, -1.0, 2, 2], ['Royal Hallmark', '3 Bedroom Premium', 'B1-B', 936.0, 936.0, None, None, -1.0, -1.0, 2, 2], ['Royal Hallmark', '5 Bedroom', 'E1', 1658.0, 1658.0, None, None, -1.0, -1.0, 2, 2]]
populate(tab_1, tab_2, tab_3, tab_4, tab_5, tab_6, summ, summun, tab_9, summdeux, summtrois)

#####                   LIGNE 226
'''











