import os
import argparse
import requests as req
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen, urlretrieve

cnt = 0
successful = 0

def download(browser,keyword):
    if not os.path.exists("./img/"+keyword):
        os.mkdir("./img/"+keyword)

    for _ in range(500):
        browser.execute_script("window.scrollBy(0,10000)")

    for x in  browser.find_elements_by_tag_name("img"):
        global cnt
        cnt = cnt + 1
        url = x.get_attribute('src')

        if url != None:
            if url[0] == 'h' :
                print("Image URL : ", url)
                target = urlopen(url).read()
                extension = ("https://google.co.in" + url).replace("/", "")
                img_name =  "img_"+ str(cnt) +".png"

                urlretrieve(url, "./img/"+keyword+"/"+ img_name)
                print("[+] Image Successfully Saved!!!")
                global successful 
                successful = successful + 1
                if successful >200:
                    exit()
                    break
            else:
                pass
        else:
            pass

def main():
    parse = argparse.ArgumentParser(description="Web Image Downloader")
    parse.add_argument("--keyword", "-k", required=True, help='downloader --keyword [url]')

    args = parse.parse_args()

    keyword = args.keyword

    # url = "https://www.google.com/search?q={}&source=lnms&tbm=isch".format(keyword+"solo")
    url = "https://www.google.co.in/search?hl=en&tbm=isch&source=hp&biw=1536&bih=770&q={}".format(keyword+" wallpaper actor")

    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")

    browser = webdriver.Chrome("F:/Downloads2/Compressed/chromedriver_win32/chromedriver.exe",  chrome_options=options)
    browser.get(url)

    download(browser,keyword)

    global successful
    print("[+] Successful Download : ", successful)

    browser.close()

if __name__ == "__main__":
    main()