from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

import pandas as pd

import datetime
import time

"""
Realiza Web Scraping del grupo deseado en facebook
"""
service = Service()
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")

page_to_scrape = str(input("Ingrese la pagina a scrapear: ",))
datos_deseados = int(input("Datos deseados a analizar: ",))
search_item = str(input("Que producto desea buscar: ",))
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
driver.get('https://www.facebook.com')

#group = 'https://www.facebook.com/groups/881454116030717'
user = '@gmail.com'
passsword = ''

user_input = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="email"]'))) 
user_input.send_keys(user)
passsword_input = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="pass"]'))) 
passsword_input.send_keys(passsword)
passsword_input.send_keys(Keys.RETURN)

time.sleep(15)

driver.get(page_to_scrape)

driver.execute_script(f"window.scrollBy(0,600)") 
time.sleep(10)

comentarios_list = []
article_list = []
result = []
seller_list = []
title = driver.find_element(By.XPATH, '//a[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xt0b8zv x1xlr1w8"]')
title = title.text

a = 0
def scrape(a):
    comments = driver.find_elements(By.XPATH, '//div[@class="x6s0dn4 xi81zsa x78zum5 x6prxxf x13a6bvl xvq8zen xdj266r xktsk01 xat24cr x1d52u69 x889kno x4uap5 x1a8lsjc xkhd6sd xdppsyt"]/div[2]/div[2]')
    
    z = len(comments)
    print("Datos encontrados: ",z)
    if a == z:
        driver.execute_script(f"window.scrollBy(0,800)") 
    time.sleep(5)
    for _ in range(a, z):
        try:
            comments[_].click()
            time.sleep(5)
            try:
                comentarosdestacados = driver.find_element(By.XPATH, '//div[@class="x6s0dn4 x78zum5 xdj266r x11i5rnm xat24cr x1mh8g0r xe0p6wg"]')
                comentarosdestacados.click()
                time.sleep(2)
                todoscomentarios = driver.find_element(By.XPATH, '//div[@class="xb57i2i x1q594ok x5lxg6s x6ikm8r x1ja2u2z x1pq812k x1rohswg xfk6m8 x1yqm8si xjx87ck xx8ngbg xwo3gff x1n2onr6 x1oyok0e x1odjw0f x1e4zzel x1qjc9v5 x9f619 x78zum5 xdt5ytf xkhd6sd x4uap5 x1ten1a2 xz7cn9q x168biu4"]//div[3]')
                todoscomentarios.click()
                time.sleep(5)
            except:
                continue
            try:
                comentarios = driver.find_element(By.XPATH, '//div[@class="x78zum5 xdt5ytf x1iyjqo2 x1n2onr6 x1jxyteu x1mfppf3 xqbnct6 xga75y6"]//div[@class="x1jx94hy"]/ul')
                comentarios_list = comentarios.text
                j = len(comentarios_list)

            except:
                comentarios_list = ["sin comentarios"]

            vendedor = driver.find_elements(By.XPATH, '//span[@class="xt0psk2"]/a/strong/span')
            for i in range(len(vendedor)):
                seller = vendedor[i].text
                seller_list.append(seller)
            
            try:
                articulos = driver.find_element(By.XPATH, '//div[@class="x78zum5 xdt5ytf x1iyjqo2 x1n2onr6 x1jxyteu x1mfppf3 xqbnct6 xga75y6"]//div[@class="xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs x126k92a"]')
                article = articulos.text
                article = article.replace("\n", "")
                article_list.append(article)

            except:      
                article = ["sin articulo"]
            try:
                result.append({
                            "Usuario" : seller,
                            "Articulo" : article_list[_],
                            "Comentarios" : comentarios_list[0:j]
                        })
            except:
                result.append({
                            "Usuario" : seller,
                            "Articulo" : article,
                            "Comentarios" : comentarios_list
                        })
            try:
                close = driver.find_element(By.XPATH, '//div[@aria-label="Cerrar"]')
                close.click()

            except:
                continue
            time.sleep(5)
            driver.execute_script(f"window.scrollBy(0,800)") 
        except:
            print("Error al cargar la pagina")
    a = z
    return result, a

def search(search_item,a):
    comments = driver.find_elements(By.XPATH, '//div[@class="x6s0dn4 xi81zsa x78zum5 x6prxxf x13a6bvl xvq8zen xdj266r xktsk01 xat24cr x1d52u69 x889kno x4uap5 x1a8lsjc xkhd6sd xdppsyt"]/div[2]/div[2]')
    z = len(comments)
    print("Datos encontrados: ",z)
    if a == z:
        driver.execute_script(f"window.scrollBy(0,800)") 
    time.sleep(5)
    for _ in range(a,z):
        try:
            comments[_].click()
            time.sleep(5)
            try:
                comentarosdestacados = driver.find_element(By.XPATH, '//div[@class="x6s0dn4 x78zum5 xdj266r x11i5rnm xat24cr x1mh8g0r xe0p6wg"]')
                comentarosdestacados.click()
                time.sleep(2)
                todoscomentarios = driver.find_element(By.XPATH, '//div[@class="xb57i2i x1q594ok x5lxg6s x6ikm8r x1ja2u2z x1pq812k x1rohswg xfk6m8 x1yqm8si xjx87ck xx8ngbg xwo3gff x1n2onr6 x1oyok0e x1odjw0f x1e4zzel x1qjc9v5 x9f619 x78zum5 xdt5ytf xkhd6sd x4uap5 x1ten1a2 xz7cn9q x168biu4"]//div[3]')
                todoscomentarios.click()
                time.sleep(5)
            except:
                continue
            try:
                articulos = driver.find_element(By.XPATH, '//div[@class="x78zum5 xdt5ytf x1iyjqo2 x1n2onr6 x1jxyteu x1mfppf3 xqbnct6 xga75y6"]//div[@class="xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs x126k92a"]')
                article = articulos.text
                article = article.replace("\n", "")

            except:  
                article = ["sin articulo"]

            if article == search_item:
                article_list.append(article)

                comentarios = driver.find_element(By.XPATH, '//div[@class="x78zum5 xdt5ytf x1iyjqo2 x1n2onr6 x1jxyteu x1mfppf3 xqbnct6 xga75y6"]//div[@class="x1jx94hy"]/ul')
                comentarios_list = comentarios.text        
                c = len(comentarios_list)

                vendedor = driver.find_elements(By.XPATH, '//span[@class="xt0psk2"]/a/strong/span')
                for j in range(len(vendedor)):
                    seller = vendedor[j].text
                    seller_list.append(seller)          

                result.append({
                                "Usuario" : seller,
                                "Articulo" : article,
                                "Comentarios" : comentarios_list[0:c]
                            })
                break
            time.sleep(3)
            try:
                close = driver.find_element(By.XPATH, '//div[@aria-label="Cerrar"]')
                close.click()
            except:
                continue
            time.sleep(5)
            driver.execute_script(f"window.scrollBy(0,800)") 
        except:
            print("Error al cargar la pagina")
    a = z        
    return result, a

if search_item == "":
    while a < datos_deseados:
        result, a = scrape(a)
else:
    try:
        while True:
            result, a = search(search_item,a)
    except:
        print("listo")

current_date_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
df = pd.DataFrame(result)
#df['Comentarios'] = df['Comentarios'].replace(['\nSeguir','.'], '', regex=True)
df['Comentarios'] = df['Comentarios'].replace(['\nSeguir','\n  .','\nAutor','\nMe gusta', '\nResponder'], '', regex=True)
df['Comentarios'] = df['Comentarios'].replace(['\nCompartir'], '\n', regex=True)
df = df[~df['Comentarios'].apply(lambda x: x == ['sin comentarios'])]
df['Comentarios'] = df['Comentarios'].str.split('\n')
df_new = df.explode('Comentarios')
df_new = df_new.dropna(subset=['Comentarios'])
df_new.to_csv(f'{title} - {current_date_time}.csv', index=False)
print(df_new)
