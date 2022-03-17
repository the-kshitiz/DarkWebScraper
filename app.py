from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
from selenium.webdriver.firefox.service import Service
# configure Firefox Driver
import uuid
from Screenshot import Screenshot_Clipping
import os
from bs4 import BeautifulSoup
def configure_firefox_driver():
    # Add additional Options to the webdriver
    firefox_options = FirefoxOptions()
    #firefox_options.binary_location ="C:\\Users\\Admin\\Desktop\\Tor Browser\\Browser\\firefox.exe"
    firefox_options.binary_location ="C:\\Users\\Kshitiz Thakur\\Desktop\\Tor Browser\\Browser\\firefox.exe"
    # add the argument and make the browser Headless.
    # firefox_options.add_argument("--headless")
    # driver = webdriver.Firefox(profile)
    # Instantiate the Webdriver: Mention the executable path of the webdriver you have downloaded
    # if driver is in PATH, no need to provide executable_path
    service = Service(
    # os.path.expandvars(r"%USERPROFILE%\Desktop\Tor Browser\Browser\firefox.exe"),
    # executable_path=GeckoDriverManager().install()
    executable_path="C:\\Users\\Kshitiz Thakur\\Desktop\\Tor Browser\\Browser\\firefox.exe"
    )
    print("work 1")
    firefox_options.set_preference("network.proxy.type", 1)
    firefox_options.set_preference("network.proxy.socks", "127.0.0.1")
    firefox_options.set_preference("network.proxy.socks_port", 9050)
    firefox_options.set_preference("network.proxy.socks_remote_dns", True)
    firefox_options.set_preference("javascript.enabled", False)
    print("work 2")
    driver = webdriver.Firefox(executable_path = "./geckodriver.exe", options = firefox_options)
    print("work 3")
    return driver


print("work 4")
def get_all_links(driver):
    links = []
    for link in driver.find_elements_by_css_selector("a[href]"):
        links.append(link.get_attribute("href"))
    return set(links)
driver = configure_firefox_driver()
links_collection = {}
def scraper(link):
    links_collection[link] = 1
    driver.get(link)
    print(link)
    body = driver.find_element_by_tag_name("body")
    body.screenshot(".//images//"+"screenshot-"+ str(uuid.uuid4())+".png")
    # img_url=ob.full_Screenshot(driver, save_path='.//images', image_name=f'screenshot-{uuid.uuid1()}.png')
    # print(img_url)
    time.sleep(2)
    links = get_all_links(driver)
    for link in links:
        try:
            if ".onion" in link  and links_collection[link] == 1:
                continue
        except KeyError:
            scraper(link)
        
    print(links)

    
scraper("http://exchangehd5455aori4qvrwhyno4ul7xrz4foy6qwga3olnbclp5f4qd.onion/home")