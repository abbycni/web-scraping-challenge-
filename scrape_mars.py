from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scraper():
    

    mars_data={}
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'http://redplanetscience.com/'
    browser.visit(url)


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
        
    News = soup.find_all('div', class_='content_title')
    body=soup.find_all('div', class_='article_teaser_body')

    title3=News[0].text
    paragraph=body[0].text

    print(title3)
    print (News)
    url = "https://spaceimages-mars.com/"
    browser.visit(url)

        # Scrape page into Soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

        
    image = soup.find_all('img', class_='headerimage')

    relative_image_path = soup.find_all('img')[1]["src"]

    image_url= url + relative_image_path

    print(relative_image_path)

    print(image_url)

    url = 'https://galaxyfacts-mars.com'

    tables = pd.read_html(url)
    tables[1]

    tables[1].to_html('data.html',classes=['table', 'table-striped', 'table-hover'])
    table=tables[1].to_html(classes=['table', 'table-striped', 'table-hover'])

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

            mars_data = {"title":title3, "news":paragraph, "image_url":image_url,"table":table, "hemis":Hemisphere_img_urls}
             
    return mars_data 

if __name__ == "__main__":
    print(scraper())