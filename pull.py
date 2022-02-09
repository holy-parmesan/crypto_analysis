from selenium import webdriver
PATH = "C:\Program Files (x86)\chromedriver.exe"

browser = webdriver.Chrome(PATH)
browser.get('https://www.flightradar24.com/56.16,-49.51/3')

soup = BeautifulSoup(browser.page_source, "html.parser")
result = soup.find_all("span", {"id": "menuPlanesValue"})

for item in result:
    print(item.text)

browser.quit()
