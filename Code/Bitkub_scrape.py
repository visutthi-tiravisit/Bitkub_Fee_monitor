from importlib.resources import path
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd



#driver chrome def
website = 'https://www.bitkub.com/fee/cryptocurrency'
options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(website)

#giving variable
#coin name
coin_name = [my_elem.text for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//tbody//tr//td[2]//span")))]
#print(coin_name)
coin_name_res = [coin_name[i] for i in range(len(coin_name)) if i % 2 == 0]
#print (coin_name_res)

#chain name
chain_name = [my_elem.text for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//tbody//tr//td[3]//div")))]

#fee
coin_icon_list = [my_elem.text for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//tbody//tr//td[2]//span//span")))]
#print(coin_icon_list)
coin_icon = ''.join(coin_icon_list)
#print(coin_icon)
withdrawal_fees = [my_elem.text for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//tbody//tr//td[4]//div")))]
fee_res = ([s.strip(coin_icon) for s in withdrawal_fees])
#print(fee_res)



def make_df(file_path):
#for loop make list
    
    for coin, chains, wdf in zip(coin_name_res, chain_name, fee_res):
    #print("Coin name: {} Chain: {} Fee: {}".format(coin, chains, wdf))

    #create dataframe
        df=(pd.DataFrame({'coin_name': coin_name_res[0:100], 'chain_name': chain_name, 'withdrawal_fees':fee_res}))
    #print(df)  
    #csv
        df.to_csv(file_path, index=False)
        df_saved_file = pd.read_csv(file_path)
        df_saved_file
    driver.quit()
#make_df()