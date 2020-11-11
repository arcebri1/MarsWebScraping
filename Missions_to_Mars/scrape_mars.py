from bs4 import BeautifulSoup
import requests
import pymongo
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)


def scrape():
    browser = init_browser()

    mars_data={}

### NASA Mars News
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    news_title=soup.find_all('div', class_='content_title')[1].text

    news_p=soup.find_all('div', class_='article_teaser_body')[0].text

### JPL Mars Space Images - Featured Image

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    browser.click_link_by_id('full_image')

    browser.click_link_by_partial_text('more info')

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser') 

    main=soup.find('figure', class_='lede')
    img=main.find('a')
    href=img['href']
    nasa_url='https://www.jpl.nasa.gov'
    featured_image_url=nasa_url+href

### Mars Facts

    url = 'https://space-facts.com/mars/'
    browser.visit(url)

    tables = pd.read_html(url)

    df=tables[0]
    
    df.columns=["Description", "Mars Values"]

    index_df=df.set_index('Description')

    html_table = index_df.to_html()
   
    html_tb=html_table.replace('\n', '')
    

### Mars Hemispheres

    url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    articles = soup.find_all('div', class_='description')

    nasa_url='https://astrogeology.usgs.gov/'

    title_and_url=[]

    for article in articles:
    
        link = article.find('a')
        href = link['href']
        title = link.find('h3').text
        browser.visit(nasa_url+href)
    
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
    
        down=soup.find('div', class_='downloads')
        image_url=down.find('a')['href']
    
        title_and_url.append({"title":title, "img_url":image_url})
    
 
    mars_data={
        "news_title":news_title,
        "news_p": news_p,
        "featured_image_url":featured_image_url,
        "facts_table":html_tb,
        "hemisphere_images":title_and_url
    }

    # browser.quit()

    return mars_data





