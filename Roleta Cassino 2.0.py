from ast import parse
from requests.api import options
from selenium import webdriver
import selenium
import json
import pytest
import time
import telepot
import emoji
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from threading import Thread


def loginsenha(u, p):
    """
    -> Função para digitar o login e senha
    :param: u: seria o usuário
    :param: p: seria o password
    """
    username = browser.find_element_by_xpath('//*[@id="txtUsername"]')
    password = browser.find_element_by_xpath('//*[@id="txtPassword"]')
    username.send_keys(u)
    password.send_keys(p)
    btn = browser.find_element_by_xpath('/html/body/div[1]/div[2]/form/button')
    btn.click()
    time.sleep(20)


def lembramaistarde():
    browser.switch_to.frame(0)
    browser.find_element(By.ID, "remindLater").click()
    time.sleep(10)


def clickcontinuar():
    browser.switch_to.default_content()
    browser.find_element(
        By.CSS_SELECTOR, ".regulatory-last-login-modal__button").click()
    time.sleep(10)


def aumentajanela():
    # Voltar ao content original para não dar error
    browser.switch_to.default_content()
    browser.find_element(
        By.CSS_SELECTOR, ".inline-games-page-component__game-header-right").click()


def clickmaisjogos():
    browser.switch_to.frame(1)
    browser.switch_to.frame(1)
    browser.find_element(
        By.CSS_SELECTOR, ".header__more-games").click()  # Mais jogos
    # Clicar em BlackJack
    browser.find_element(
        By.CSS_SELECTOR, "div.lobby-category__slide:nth-child(3)").click()
    # Entra na primeira sala do BlackJack
    browser.find_element(
        By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(1)").click()
    time.sleep(10)
    # Mais jogos novamente
    browser.find_element(By.CSS_SELECTOR, ".header__more-games").click()
    browser.find_element(
        By.CSS_SELECTOR, "div.lobby-category__slide:nth-child(2)").click()


def bet365_premium_roulette():
    global lista01
    global cont01
    global quant
    cont_impar = []
    cont_par = []
    cont_par01 = []
    quant = 0
    if conf_lista[i] != conf_lista_compara[i]:
        print('Diferente')
        print(conf_lista[i])
        if conf_lista['bet365_premium_roulette'] != conf_lista_compara['bet365_premium_roulette']:
            parimpar((conf_lista['bet365_premium_roulette']))

            if resultado == 'Par':
                cont_par.append(0)
                cont_impar.clear()
                #print(f'Par {cont_par}')

            else:
                cont_impar.append(1)
                cont_par.clear()
                #print(f'Impar {cont_impar}')

            if conf_lista['bet365_premium_roulette'] == 0:
                cont_impar.clear()
                cont_par.clear()

            conf_lista_compara['bet365_premium_roulette'] = conf_lista['bet365_premium_roulette']
            print(f'bet365_premium_roulette - Par {cont_par}')
            print(f'bet365_premium_roulette - Impar {cont_impar}')


def bet365_roulette():
    global lista02
    global cont02
    if conf_lista['bet365_roulette'] != conf_lista_compara['bet365_roulette']:
        # bet365_premium_roulette(conf_lista['bet365_premium_roulette'])
        print(conf_lista['bet365_roulette'])
        # parimpar(conf_lista['bet365_roulette'])

        # lista02.append(lista_resultado)
        #print(f'Lista02 : {lista02}')
        '''lista02.append(conf_lista['bet365_roulette'])
        print(f'bet365_roulette {lista02}')'''
        #cont02 += 1
        #print(f'Contador: {cont02}')


def Quantum_Roulette_Live():
    global lista03
    global cont03
    if conf_lista['Quantum_Roulette_Live'] != conf_lista_compara['Quantum_Roulette_Live']:
        # bet365_premium_roulette(conf_lista['bet365_premium_roulette'])
        lista03.append(conf_lista['Quantum_Roulette_Live'])
        print(f'Quantum_Roulette_Live {lista03}')
        cont03 += 1
        #print(f'Contador: {cont03}')


def Quantum_Roulette_Italiana():
    global lista04
    global cont04
    if conf_lista['Quantum_Roulette_Italiana'] != conf_lista_compara['Quantum_Roulette_Italiana']:
        # bet365_premium_roulette(conf_lista['bet365_premium_roulette'])
        lista04.append(conf_lista['Quantum_Roulette_Italiana'])
        print(f'Quantum_Roulette_Italiana {lista04}')
        cont04 += 1
        #print(f'Contador: {cont04}')


def Roulette():
    global lista05
    global cont05
    if conf_lista['Roulette'] != conf_lista_compara['Roulette']:
        # bet365_premium_roulette(conf_lista['bet365_premium_roulette'])
        lista05.append(conf_lista['Roulette'])
        print(f'Roulette {lista05}')
        cont05 += 1
        #print(f'Contador: {cont05}')

# <<<<<<<<<<<<<<<<<< INATIVADO!! >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def Age_Of_The_Gods_Bonus_Roulette():
    global lista02
    global cont02
    if conf_lista['bet365_roulette'] != conf_lista_compara['bet365_roulette']:
        # bet365_premium_roulette(conf_lista['bet365_premium_roulette'])
        lista02.append(conf_lista['bet365_roulette'])
        print(f'bet365_roulette {lista02}')
        cont02 += 1
        print(f'Contador: {cont02}')


def Football_Roulette(valor):
    global lista06
    global cont06
    if conf_lista['Football_Roulette'] != conf_lista_compara['Football_Roulette']:
        # bet365_premium_roulette(conf_lista['bet365_premium_roulette'])
        lista06.append(conf_lista['Football_Roulette'])
        print(f'Football_Roulette {lista06}')
        cont06 += 1
        #print(f'Contador: {cont06}')


def Hindi_Roulette(valor):
    global lista07
    global cont07
    if conf_lista['Hindi_Roulette'] != conf_lista_compara['Hindi_Roulette']:
        # bet365_premium_roulette(conf_lista['bet365_premium_roulette'])
        lista07.append(conf_lista['Hindi_Roulette'])
        print(f'Hindi_Roulette {lista07}')
        cont07 += 1
        #print(f'Contador: {cont07}')


def Speed_Roulette(valor):
    global lista08
    global cont08
    if conf_lista['Speed_Roulette'] != conf_lista_compara['Speed_Roulette']:
        # bet365_premium_roulette(conf_lista['bet365_premium_roulette'])
        lista08.append(conf_lista['Speed_Roulette'])
        print(f'Speed_Roulette {lista08}')
        cont08 += 1
        #print(f'Contador: {cont08}')


def Greek_Roulette(valor):  # +1
    global lista09
    global cont09
    if conf_lista['Greek_Roulette'] != conf_lista_compara['Greek_Roulette']:
        # bet365_premium_roulette(conf_lista['bet365_premium_roulette'])
        lista09.append(conf_lista['Greek_Roulette'])
        print(f'Greek_Roulette {lista09}')
        cont09 += 1
        #print(f'Contador: {cont09}')


def Turkish_Roulette(valor):
    global lista10
    global cont10
    if conf_lista['Turkish_Roulette'] != conf_lista_compara['Turkish_Roulette']:
        # bet365_premium_roulette(conf_lista['bet365_premium_roulette'])
        lista10.append(conf_lista['Turkish_Roulette'])
        print(f'Turkish_Roulette {lista10}')
        cont10 += 1
        #print(f'Contador: {cont10}')


def Roleta_Brasileira(valor):
    global lista11
    global cont11
    if conf_lista['Roleta_Brasileira'] != conf_lista_compara['Roleta_Brasileira']:
        # bet365_premium_roulette(conf_lista['bet365_premium_roulette'])
        lista11.append(conf_lista['Roleta_Brasileira'])
        print(f'Roleta_Brasileira {lista11}')
        cont11 += 1
        #print(f'Contador: {cont11}')


def Quantum_Auto_Roulette(valor):
    global lista12
    global cont12
    if conf_lista['Quantum_Auto_Roulette'] != conf_lista_compara['Quantum_Auto_Roulette']:
        # bet365_premium_roulette(conf_lista['bet365_premium_roulette'])
        lista12.append(conf_lista['Quantum_Auto_Roulette'])
        print(f'Quantum_Auto_Roulette {lista12}')
        cont12 += 1
        #print(f'Contador: {cont12}')


def Prestige_Roulette(valor):
    global lista13
    global cont13
    if conf_lista['Prestige_Roulette'] != conf_lista_compara['Prestige_Roulette']:
        # bet365_premium_roulette(conf_lista['bet365_premium_roulette'])
        lista13.append(conf_lista['Prestige_Roulette'])
        print(f'Prestige_Roulette {lista13}')
        cont13 += 1
        #print(f'Contador: {cont13}')


def American_Roulette(valor):
    global lista14
    global cont14
    if conf_lista['American_Roulette'] != conf_lista_compara['American_Roulette']:
        # bet365_premium_roulette(conf_lista['bet365_premium_roulette'])
        lista14.append(conf_lista['American_Roulette'])
        print(f'American_Roulette {lista14}')
        cont14 += 1
        #print(f'Contador: {cont14}')


def Spread_Bet_Roulette(valor):
    global lista15
    global cont15
    if conf_lista['Spread_Bet_Roulette'] != conf_lista_compara['Spread_Bet_Roulette']:
        # bet365_premium_roulette(conf_lista['bet365_premium_roulette'])
        lista15.append(conf_lista['Spread_Bet_Roulette'])
        print(f'Spread_Bet_Roulette {lista15}')
        cont15 += 1
        #print(f'Contador: {cont15}')


def Deutsches_Roulette(valor):
    global lista16
    global cont16
    if conf_lista['Deutsches_Roulette'] != conf_lista_compara['Deutsches_Roulette']:
        # bet365_premium_roulette(conf_lista['bet365_premium_roulette'])
        lista16.append(conf_lista['Deutsches_Roulette'])
        print(f'Deutsches_Roulette {lista16}')
        cont16 += 1
        #print(f'Contador: {cont16}')


def Slingshot(valor):
    global lista17
    global cont17
    if conf_lista['Slingshot'] != conf_lista_compara['Slingshot']:
        # bet365_premium_roulette(conf_lista['bet365_premium_roulette'])
        lista17.append(conf_lista['Slingshot'])
        print(f'Slingshot {lista17}')
        cont17 += 1
        #print(f'Contador: {cont17}')


def UK_Roulette(valor):
    global lista18
    global cont18
    if conf_lista['UK_Roulette'] != conf_lista_compara['UK_Roulette']:
        # bet365_premium_roulette(conf_lista['bet365_premium_roulette'])
        lista18.append(conf_lista['UK_Roulette'])
        print(f'UK_Roulette {lista18}')
        cont18 += 1
        #print(f'Contador: {cont18}')


def Prime_Slingshot(valor):
    global lista19
    global cont19
    if conf_lista['Prime_Slingshot'] != conf_lista_compara['Prime_Slingshot']:
        # bet365_premium_roulette(conf_lista['bet365_premium_roulette'])
        lista19.append(conf_lista['Prime_Slingshot'])
        print(f'Prime_Slingshot {lista19}')
        cont19 += 1
        #print(f'Contador: {cont19}')


def French_Roulette(valor):
    global lista20
    global cont20
    if conf_lista['French_Roulette'] != conf_lista_compara['French_Roulette']:
        # bet365_premium_roulette(conf_lista['bet365_premium_roulette'])
        lista20.append(conf_lista['French_Roulette'])
        print(f'French_Roulette {lista20}')
        cont20 += 1
        #print(f'Contador: {cont20}')


def Triumph_Roulette(valor):  # Talvez é igual
    global lista21
    global cont21
    if conf_lista['Triumph_Roulette'] != conf_lista_compara['Triumph_Roulette']:
        # bet365_premium_roulette(conf_lista['bet365_premium_roulette'])
        lista21.append(conf_lista['Triumph_Roulette'])
        print(f'Triumph_Roulette {lista21}')
        cont21 += 1
        #print(f'Contador: {cont21}')

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< DESATIVADO >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def Triumph_French_Roulette():  # Talvez é igual
    global lista02
    global cont02
    if conf_lista['bet365_roulette'] != conf_lista_compara['bet365_roulette']:
        # bet365_premium_roulette(conf_lista['bet365_premium_roulette'])
        lista02.append(conf_lista['bet365_roulette'])
        print(f'bet365_roulette {lista02}')
        cont02 += 1
        print(f'Contador: {cont02}')


def Roulette_Italiana(valor):
    global lista22
    global cont22
    if conf_lista['Roulette_Italiana'] != conf_lista_compara['Roulette_Italiana']:
        # bet365_premium_roulette(conf_lista['bet365_premium_roulette'])
        lista22.append(conf_lista['Roulette_Italiana'])
        print(f'Roulette_Italiana {lista22}')
        cont22 += 1
        #print(f'Contador: {cont22}')

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< DESATIVADO >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def Football_French_Roulette():
    global lista02
    global cont02
    if conf_lista['bet365_roulette'] != conf_lista_compara['bet365_roulette']:
        # bet365_premium_roulette(conf_lista['bet365_premium_roulette'])
        lista02.append(conf_lista['bet365_roulette'])
        print(f'bet365_roulette {lista02}')
        cont02 += 1
        print(f'Contador: {cont02}')


def parimpar(num):
    global lista_resultado
    global resultado
    resultado = ''
    lista_resultado = []

    if num % 2 == 0 and num > 0:
        # lista_resultado.append('Par')  # Acrescentar 'par' na lista
        # lista_numero.append(num)  # Acrescenta o número em questão
        print('Par')
        resultado = 'Par'
        cont_par.append(0)
        cont_impar.clear()

    else:
        if num % 2 != 0 and num > 0:
            # lista_resultado.append('Impar')  # Acrescenta 'impar' na lista
            # lista_numero.append(num)
            print('Impar')
            resultado = 'Impar'
            cont_impar.append(1)
            cont_par.clear()

    if num == 0:
        cont_impar.clear()
        cont_par.clear()

    conf_lista_compara[i] = conf_lista[i]
    #print(f'bet365_premium_roulette - Par {cont_par}')
    #print(f'bet365_premium_roulette - Impar {cont_impar}')


def pegar_valores_roleta():
    global conf_lista
    global penum_conf_lista
    # bet365_premium_roulette
    ultnum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(12)").text
    penum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(11)").text
    ultimo_numero_int = int(ultnum)
    penum_int = int(penum)
    conf_lista = {'bet365_premium_roulette': ultimo_numero_int}
    penum_conf_lista = {'bet365_premium_roulette': penum_int}

    # bet365_roulette
    ultnum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(12)").text
    penum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(11)").text
    ultimo_numero_int = int(ultnum)  # Inteiro
    penum_int = int(penum)
    conf_lista.update({'bet365_roulette': ultimo_numero_int})
    penum_conf_lista.update({'bet365_roulette': penum_int})

    # Quantum_Roulette_Live
    # ultnum = browser.find_element(By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(12) > div:nth-child(1)").text
    ultnum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(12)")
    numero_certo = ultnum.find_element(
        By.CLASS_NAME, "lobby-table-rol-round-result__item-number").text
    penum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(11)")
    penum_certo = penum.find_element(
        By.CLASS_NAME, "lobby-table-rol-round-result__item-number").text
    ultimo_numero_int = int(numero_certo)
    penum_int = int(penum_certo)
    conf_lista.update({'Quantum_Roulette_Live': ultimo_numero_int})
    penum_conf_lista.update({'Quantum_Roulette_Live': penum_int})

    # Quantum_Roulette_Italiana
    # ultnum = browser.find_element(By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(12) > div:nth-child(1)").text
    ultnum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(12)")
    numero_certo = ultnum.find_element(
        By.CLASS_NAME, "lobby-table-rol-round-result__item-number").text
    penum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(11)")
    penum_certo = penum.find_element(
        By.CLASS_NAME, "lobby-table-rol-round-result__item-number").text
    ultimo_numero_int = int(numero_certo)
    penum_int = int(penum_certo)
    conf_lista.update({'Quantum_Roulette_Italiana': ultimo_numero_int})
    penum_conf_lista.update({'Quantum_Roulette_Italiana': penum_int})

    # Roulette
    ultnum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(12)").text
    penum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(11)").text
    ultimo_numero_int = int(ultnum)
    penum_int = int(penum)
    conf_lista.update({'Roulette': ultimo_numero_int})
    penum_conf_lista.update({'Roulette': penum_int})

    '''# Age_Of_The_Gods_Bonus_Roulette DESATIVADO
    ultnum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-table-history:nth-child(5) > div:nth-child(1) > div:nth-child(12) > div:nth-child(1)").text
    ultimo_numero_int = int(ultnum)
    conf_lista.update({'Age_Of_The_Gods_Bonus_Roulette': ultimo_numero_int})'''

    # Football_Roulette
    # ultnum = browser.find_element( By.CSS_SELECTOR, ".lobby-table_roulette-football-single-zero > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(12) > div:nth-child(1)").text
    ultnum = browser.find_element(
        By.CSS_SELECTOR, ".lobby-table_roulette-football-single-zero > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(12)")
    numero_certo = ultnum.find_element(
        By.CLASS_NAME, "lobby-table-rol-round-result__item-number").text
    penum = browser.find_element(
        By.CSS_SELECTOR, ".lobby-table_roulette-football-single-zero > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(11)")
    penum_certo = penum.find_element(
        By.CLASS_NAME, "lobby-table-rol-round-result__item-number").text
    # .lobby-table_roulette-football-single-zero > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(11) > div:nth-child(11)
    # .lobby-table_roulette-football-single-zero > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(10) > div:nth-child(2)
    # .lobby-table_roulette-football-single-zero > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(9)
    ultimo_numero_int = int(numero_certo)
    penum_int = int(penum_certo)
    conf_lista.update({'Football_Roulette': ultimo_numero_int})
    penum_conf_lista.update({'Football_Roulette': penum_int})

    # Hindi_Roulette
    ultnum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(8) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(12)").text
    penum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(8) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(11)").text
    ultimo_numero_int = int(ultnum)
    penum_int = int(penum)
    conf_lista.update({'Hindi_Roulette': ultimo_numero_int})
    penum_conf_lista.update({'Hindi_Roulette': penum_int})

    # Speed_Roulette
    ultnum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(9) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(12)").text
    penum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(9) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(11)").text
    ultimo_numero_int = int(ultnum)
    penum_int = int(penum)
    conf_lista.update({'Speed_Roulette': ultimo_numero_int})
    penum_conf_lista.update({'Speed_Roulette': penum_int})

    # Greek_Roulette
    ultnum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(10) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(12)").text
    penum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(10) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(11)").text
    ultimo_numero_int = int(ultnum)
    penum_int = int(penum)
    conf_lista.update({'Greek_Roulette': ultimo_numero_int})
    penum_conf_lista.update({'Greek_Roulette': penum_int})

    # Turkish_Roulette
    ultnum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(11) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(12)").text
    penum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(11) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(11)").text
    ultimo_numero_int = int(ultnum)
    penum_int = int(penum)
    conf_lista.update({'Turkish_Roulette': ultimo_numero_int})
    penum_conf_lista.update({'Turkish_Roulette': penum_int})

    # Roleta_Brasileira
    ultnum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(12) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(12)").text
    penum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(12) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(11)").text
    ultimo_numero_int = int(ultnum)
    penum_int = int(penum)
    conf_lista.update({'Roleta_Brasileira': ultimo_numero_int})
    penum_conf_lista.update({'Roleta_Brasileira': penum_int})

    # Quantum_Auto_Roulette
    # ultnum = browser.find_element(By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(13) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(12)").text
    ultnum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(13) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(12)")
    numero_certo = ultnum.find_element(
        By.CLASS_NAME, "lobby-table-rol-round-result__item-number").text
    penum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(13) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(11)")
    # div.lobby-tables__item:nth-child(13) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(11) > div:nth-child(1)
    penum_certo = penum.find_element(
        By.CLASS_NAME, "lobby-table-rol-round-result__item-number").text
    ultimo_numero_int = int(numero_certo)
    penum_int = int(penum_certo)
    conf_lista.update({'Quantum_Auto_Roulette': ultimo_numero_int})
    penum_conf_lista.update({'Quantum_Auto_Roulette': penum_int})

    # Prestige_Roulette
    ultnum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(14) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(12)").text
    penum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(14) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(11)").text
    ultimo_numero_int = int(ultnum)
    penum_int = int(penum)
    conf_lista.update({'Prestige_Roulette': ultimo_numero_int})
    penum_conf_lista.update({'Prestige_Roulette': penum_int})

    # American_Roulette
    ultnum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(15) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(12)").text
    penum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(15) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(11)").text
    ultimo_numero_int = int(ultnum)
    penum_int = int(penum)
    conf_lista.update({'American_Roulette': ultimo_numero_int})
    penum_conf_lista.update({'American_Roulette': penum_int})

    '''# Spread_Bet_Roulette  !!! DESATIVADO !!! 
    ultnum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-table-rol-round-result__item_last:nth-child(1)").text
    # div.lobby-table-sprol-history-item:nth-child(11) > div:nth-child(1) > div:nth-child(1)
    penum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-table-sprol-history-item:nth-child(11) > div:nth-child(1)").text
    # div.lobby-table-sprol-history-item:nth-child(12) > div:nth-child(1) > div:nth-child(1)
    ultimo_numero_int = int(ultnum)
    penum_int = int(penum)
    conf_lista.update({'Spread_Bet_Roulette': ultimo_numero_int})
    penum_conf_lista.update({'Spread_Bet_Roulette': penum_int})'''

    # Deutsches_Roulette
    ultnum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(17) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(12)").text
    penum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(17) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(11)").text
    ultimo_numero_int = int(ultnum)
    penum_int = int(penum)
    conf_lista.update({'Deutsches_Roulette': ultimo_numero_int})
    penum_conf_lista.update({'Deutsches_Roulette': penum_int})

    # Slingshot
    ultnum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(18) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(12)").text
    penum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(18) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(11)").text
    ultimo_numero_int = int(ultnum)
    penum_int = int(penum)
    conf_lista.update({'Slingshot': ultimo_numero_int})
    penum_conf_lista.update({'Slingshot': penum_int})

    # UK_Roulette
    ultnum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(19) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(12)").text
    penum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(19) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(11)").text
    ultimo_numero_int = int(ultnum)
    penum_int = int(penum)
    conf_lista.update({'UK_Roulette': ultimo_numero_int})
    penum_conf_lista.update({'UK_Roulette': penum_int})

    # Prime_Slingshot
    ultnum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(20) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(12)").text
    penum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(20) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(11)").text
    ultimo_numero_int = int(ultnum)
    penum_int = int(penum)
    conf_lista.update({'Prime_Slingshot': ultimo_numero_int})
    penum_conf_lista.update({'Prime_Slingshot': penum_int})

    # French_Roulette
    ultnum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(21) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(12)").text
    penum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(21) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(11)").text
    ultimo_numero_int = int(ultnum)
    penum_int = int(penum)
    conf_lista.update({'French_Roulette': ultimo_numero_int})
    penum_conf_lista.update({'French_Roulette': penum_int})

    # Triumph_Roulette
    ultnum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(22) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(12)").text
    penum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(22) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(11)").text
    # div.lobby-tables__item:nth-child(22) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(11) > div:nth-child(1)
    ultimo_numero_int = int(ultnum)
    penum_int = int(penum)
    conf_lista.update({'Triumph_Roulette': ultimo_numero_int})
    penum_conf_lista.update({'Triumph_Roulette': penum_int})

    # Roulette_Italiana
    ultnum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(24) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(12)").text
    penum = browser.find_element(
        By.CSS_SELECTOR, "div.lobby-tables__item:nth-child(24) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(11)").text
    # div.lobby-tables__item:nth-child(24) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(11) > div:nth-child(1)
    ultimo_numero_int = int(ultnum)
    penum_int = int(penum)
    conf_lista.update({'Roulette_Italiana': ultimo_numero_int})
    penum_conf_lista.update({'Roulette_Italiana': penum_int})


# TOKEN do meu bot telegram
# bot = telepot.Bot('1271928762:AAHOLYb5juaLe5TY9u9uKevnxKfxcYVHQUs') // importar função dele depois
# INICIALIZAÇÃO DO FIREFOX E ENTRANDO NO SITE
options = Options()
options.headless = False  # Coloque True se quiser que não apareça o browser do FireFox
browser = webdriver.Firefox(options=options)
browser.get('https://casino.bet365.com/live-casino/Play/LiveRoulette')
browser.maximize_window()
time.sleep(10)

# DIGITANDO LOGIN E SENHA
# Função. Digite o Login no primeiro campo, e a senha no segundo.
loginsenha('', '')

# Função para clicar na janela de lembrar mais tarde e fecha-la
lembramaistarde()

# Função apenas para clicar na janela de continuar
clickcontinuar()

# Função para aumentar a janela no video ao vivo roleta
aumentajanela()

# Função para clicar na janela mais jogos e entrar na do BlackJack e clicar em mais jogos novamente
clickmaisjogos()

#print('Aqui vamos ver os valores do dicionário')

global conf_lista
global conf_lista_compara
global penum_conf_lista
global lista01
global lista02
global lista03
global lista04
global lista05
global lista06
global lista07
global lista08
global lista09
global lista10
global lista11
global lista12
global lista13
global lista14
global lista15
global lista16
global lista17
global lista18
global lista19
global lista20
global lista21
global lista22
global cont01
global cont02
global cont03
global cont04
global cont05
global cont06
global cont07
global cont08
global cont09
global cont10
global cont11
global cont12
global cont13
global cont14
global cont15
global cont16
global cont17
global cont18
global cont19
global cont20
global cont21
global cont22
cont01 = cont02 = cont03 = cont04 = cont05 = cont06 = cont07 = cont08 = cont09 = cont10 = cont11 = cont12 = cont13 = cont14 = cont15 = cont16 = cont17 = cont18 = cont19 = cont20 = cont21 = cont22 = 0
lista01 = []
lista02 = []
lista03 = []
lista04 = []
lista05 = []
lista06 = []
lista07 = []
lista08 = []
lista09 = []
lista10 = []
lista11 = []
lista12 = []
lista13 = []
lista14 = []
lista15 = []
lista16 = []
lista17 = []
lista18 = []
lista19 = []
lista20 = []
lista21 = []
lista22 = []
conf_lista_compara = {}
penum_conf_lista_compara = {}
tot = 0
cont_par = []
cont_impar = []
n1 = 0
resultado = ''
#lista_resultado = []
#lista_numero = []

while True:
    pegar_valores_roleta()
    print('Todos os Valores pegados das roletas')
    print(conf_lista)
    print('\nTodos os valores Penultimos')
    print(penum_conf_lista)

    if tot == 0:
        conf_lista_compara = conf_lista.copy()
    time.sleep(1)

    # FOR IMPORTANTE, SEMPRE VAI MUDAR O NÚMERO QUANDO FOR DIFERENTE
    for i in conf_lista.keys():

        # -------------------------------------------------------------------------------------------------------------------------
        parimpar(conf_lista['bet365_premium_roulette'])
# -----------------------------------------------------------------------------------------------------------------------------

        '''if conf_lista['bet365_roulette'] != conf_lista_compara['bet365_roulette']:
            parimpar((conf_lista['bet365_roulette']))

            if resultado == 'Par':
                cont_par.append(0)
                cont_impar.clear()
                #print(f'Par {cont_par}')

            else:
                cont_impar.append(1)
                cont_par.clear()
                #print(f'Impar {cont_impar}')

            if conf_lista['bet365_roulette'] == 0:
                cont_impar.clear()
                cont_par.clear()

            conf_lista_compara['bet365_roulette'] = conf_lista['bet365_roulette']
            print(f'bet365_roulette - Par {cont_par}')
            print(f'bet365_roulette - Impar {cont_impar}')

            # test2()'''
        '''bet365_premium_roulette()
            bet365_roulette()
            Quantum_Roulette_Live()
            Quantum_Roulette_Italiana()
            Roulette()
            Football_Roulette(conf_lista['Football_Roulette'])
            Hindi_Roulette(conf_lista['Hindi_Roulette'])
            Speed_Roulette(conf_lista['Speed_Roulette'])
            Greek_Roulette(conf_lista['Greek_Roulette'])
            Turkish_Roulette(conf_lista['Turkish_Roulette'])
            Roleta_Brasileira(conf_lista['Roleta_Brasileira'])
            Quantum_Auto_Roulette(conf_lista['Quantum_Auto_Roulette'])
            Prestige_Roulette(conf_lista['Prestige_Roulette'])
            American_Roulette(conf_lista['American_Roulette'])
            Spread_Bet_Roulette(conf_lista['Spread_Bet_Roulette'])
            Deutsches_Roulette(conf_lista['Deutsches_Roulette'])
            Slingshot(conf_lista['Slingshot'])
            UK_Roulette(conf_lista['UK_Roulette'])
            Prime_Slingshot(conf_lista['Prime_Slingshot'])
            French_Roulette(conf_lista['French_Roulette'])
            Triumph_Roulette(conf_lista['Triumph_Roulette'])
            Roulette_Italiana(conf_lista['Roulette_Italiana'])'''

        # teste()
        conf_lista_compara[i] = conf_lista[i]

        '''else:
            if conf_lista[i] == penum_conf_lista[i]:
                print('Igual')
                print(conf_lista[i])'''

        tot += 1

    # bet365_premium_roulette()'''
    #print(f'quant par {cont_par} e quant impar {cont_impar}')
    #print(f'Valor tot {tot}')

    # print(lista_resultado)
    # print(lista_numero)
    # print('Conf_lista')
    # print(conf_lista)
    # print('conf_lista_compara')
    # print(conf_lista_compara)
    # bet365_premium_roulette()
    # print(bet365_premium_roulette(lista01))
    # bet365_premium_roulette(lista01)
