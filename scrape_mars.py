from distutils.log import info
from matplotlib.pyplot import table
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time


def scrape_data():

    mars_data = {}
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'http://redplanetscience.com/'
    browser.visit(url)

    time.sleep(3)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    news = soup.find_all('div', class_='content_title')
    body = soup.find_all('div', class_='article_teaser_body')

    # title7 = soup.find_all('div', class_='content_title')[0].text
    # paragraph = soup.find_all ('div', class_= 'article_teaser_body')[0].text

    title8 = news[0].text
    paragraph = body[0].text

    print(title8)

    print(news)
    url = "https://spaceimages-mars.com/"
    browser.visit(url)

        # Scrape page into Soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    image = soup.find_all('img', class_='headerimage')

    relative_image_path = soup.find_all('img')[1]["src"]

    image_url = url + relative_image_path

    print(relative_image_path)

    print(image_url)

    url = 'https://galaxyfacts-mars.com'

    # tables = pd.read_html(url)
    # tables[1]

    df = pd.read_html('https://galaxyfacts-mars.com')[0]
    df.columns = ['description', 'Mars', 'Earth']
  
    df.set_index('description', inplace=True)
    
    #mars_facts= df.to_html(index=False) 

    #df.to_html('web-scraping-challenge-/data.html',
     #    classes=['table', 'table-striped', 'table-hover'])
    mars_facts = df.to_html(classes=['table', 'table-striped', 'table-hover'])

    print(mars_facts)



    url = 'https://marshemispheres.com/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find_all('div', class_='description')
    Hemisphere_img_urls = []
    # Loop through returned results
    for result in results:
        # Error handling
        try:
            # Identify and return title of listing
            title1 = result.find('h3').text
            # get the image link
            img_link = result.a['href']
            url = f"https://marshemispheres.com/" + img_link
            browser.visit(url)
            html = browser.html
            soup = BeautifulSoup(html, 'html.parser')
            output = soup.find('img', class_= "wide-image")
            download_link = output['src']
            img_url = f"https://marshemispheres.com/" + download_link
                # Print results only if title, price, and link are available
            if (title1 and download_link):
                print(title1)
                print(f"https://marshemispheres.com/" + download_link)
                print('-'*107)
                
                hemis_dictionary = { 
                    'Title' :title1, 
                    'img_url': img_url}
                
                Hemisphere_img_urls.append(hemis_dictionary)
                
        except Exception as error:
            print(error)
    mars_data = {"title":title8, "news":paragraph, "image_url":image_url,"facts":mars_facts, "hemis":Hemisphere_img_urls}
    print(mars_data)
    browser.quit()

    return mars_data 

if __name__ == "__main__":
    print(scrape_data())
