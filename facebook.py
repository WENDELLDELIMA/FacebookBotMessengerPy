#importar as lib
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from datetime import date
import re
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
#Navegar ate sistema
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.facebook.com/')

usuario =['seuemail@gmail.com', 'suasenha']
friendTabs = 'https://www.facebook.com/your.perfil/friends?lst=100002508176851%3A100002508176851%3A1600258624&source_ref=pb_friends_tl'
def logar(usuario):
    time.sleep(3)

    user =  driver.find_element_by_name('email')
    user.click()
    user.send_keys(usuario[0])
    time.sleep(1)
    senha =  driver.find_element_by_name('pass')
    senha.click()
    senha.send_keys(usuario[1])
    time.sleep(1)
    senha.send_keys(Keys.RETURN)
    time.sleep(3)

    driver.get(friendTabs)


    
   # chave.send_keys(Keys.ENTER)
   
#forcando o scroll da pagina até 200x para conseguir coletar o maximo de perfis possiveis.
    for i in range(200):
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    print('finalizou o Scroll')

    time.sleep(4)
    pegarLinks()

def pegarLinks():
    print('iniciando pegar links')
    hrefs = driver.find_elements_by_tag_name('a')  
    links = [elem.get_attribute('href') for elem in hrefs]
    print('removendo repetidos')


#criando uma lista sem url repetidas    
    lista = remove_repetidos(links)
   

    for link in lista:
#garantindo que será uma url de amigo da pagina!        
        if re.search('profile_friend', link, re.IGNORECASE) :
            print(link)
            time.sleep(2)
            driver.get(link)
            btn =  driver.find_element_by_xpath('//a[@class="_42ft _4jy0 _4jy4 _517h _51sy"]')
            
            btn.click()
            try:

                time.sleep(2)
                btn2 =  driver.find_elements_by_xpath('//div[@class="_1mf _1mj"]')
                btn2[1].click()
                btn2[1].send_keys('Salve Galera!!!')
                btn2[1].send_keys(Keys.SHIFT + Keys.ENTER)
                btn2[1].send_keys(Keys.SHIFT + Keys.ENTER)
                btn2[1].send_keys('Lançou o EPISODIO 27 DO BADAROSKA LIVE SESSIONS')
                btn2[1].send_keys(Keys.SHIFT + Keys.ENTER)
                btn2[1].send_keys('Onde tivemos a honra de ser convidados!')
                btn2[1].send_keys(Keys.SHIFT + Keys.ENTER)
                btn2[1].send_keys(Keys.SHIFT + Keys.ENTER)
                btn2[1].send_keys('Dá uma conferida pra fortalecer: ')
                btn2[1].send_keys(Keys.SHIFT + Keys.ENTER)
                btn2[1].send_keys('https://www.youtube.com/watch?v=xzwzy06tOVU&t=2s')
                btn2[1].send_keys(Keys.SHIFT + Keys.ENTER)
                btn2[1].send_keys(Keys.SHIFT + Keys.ENTER)
                btn2[1].send_keys(Keys.SHIFT + Keys.ENTER)
                time.sleep(2)

                
                btn2[1].send_keys(Keys.ENTER)

                #a = driver.find_elements_by_xpath('//*[@data-tooltip-content="Fechar guia""]')
                #a[0].click()
                btnSalvar =  driver.find_element_by_xpath('//*[contains(@class, "_7jbw _4vu4 button")]')
                btnSalvar.click()
               
            
                
            
                
            
                time.sleep(1)
            except IndexError:
                print("deu ruim nesse usuario")
            except ElementClickInterceptedException:
                print("deu ruim nesse usuario")  
            except StaleElementReferenceException:
                print("deu ruim nesse usuario") 
            
            except ElementNotInteractableException:
                print('elemento sem interação')
                pass
            except NoSuchElementException:
                print("deu ruim nesse usuario")
                pass  
           
        else:
#informando que não é uma url de friends
            print("Não contem profile_friend na url")


#removendo urls repetidas   
def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    
    return l    
logar(usuario)


