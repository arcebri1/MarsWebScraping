#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
import pandas as pd
from bs4 import BeautifulSoup
import requests
import pymongo
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:

def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)


# In[ ]:


# NASA Mars News


# In[3]:

def scrape_info():
    browser = init_browser


    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)


# In[4]:


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


# In[25]:


# soup.find_all('div', class_='content_title')[1].text


# In[19]:


    news_title = soup.find_all('div', class_='content_title')[1].text


# In[26]:


# soup.find_all('div', class_='article_teaser_body')[0].text


# In[27]:


    news_p = soup.find_all('div', class_='article_teaser_body')[0].text


# In[33]:


    print(f'Title: {news_title}')
    print(f'Summary: {news_p}')


# In[34]:


# browser.quit()


# In[ ]:


# JPL Mars Space Images - Featured Image


# In[35]:


# executable_path = {'executable_path': ChromeDriverManager().install()}
# browser = Browser('chrome', **executable_path, headless=False)


# In[113]:


url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[114]:


# html = browser.html
# soup = BeautifulSoup(html, 'html.parser')


# In[115]:


# soup.find('figure', class_='lede')


# In[116]:


browser.click_link_by_id('full_image')


# In[117]:


# browser.links.find_by_partial_text('full_image').click()


# In[118]:


# browser.links.find_by_partial_text('more info').click()


# In[119]:


browser.click_link_by_partial_text('more info')


# In[63]:


# soup.find('a', class_='src')


# In[127]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[140]:


main = soup.find('figure', class_='lede')
img = main.find('a')
href = img['href']
nasa_url = 'https://www.jpl.nasa.gov'
featured_image_url = nasa_url+href
print(
    f'The url for NASA featured image of the day is:      {featured_image_url}')


# In[143]:


# href


# In[142]:


# img


# In[141]:


# main


# In[ ]:


# Mars Facts


# In[144]:


url = 'https://space-facts.com/mars/'
browser.visit(url)


# In[146]:


# In[147]:


tables = pd.read_html(url)
tables


# In[150]:


df = tables[0]
df


# In[152]:


df.columns = ["Description", "Mars Values"]
df


# In[153]:


html_table = df.to_html()
html_table


# In[156]:


html_tb = html_table.replace('\n', '')


# In[162]:


html_tb


# In[ ]:


# Mars Hemispheres


# In[197]:


url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[198]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[199]:


# soup.find_all('div', class_='item')


# In[169]:


# soup.find_all('div', class_='description')


# In[200]:


articles = soup.find_all('div', class_='description')
nasa_url = 'https://astrogeology.usgs.gov/'

title_and_url = []

# Iterate through each product
for article in articles:
    # Use Beautiful Soup's find() method to navigate and retrieve attributes
    link = article.find('a')
    href = link['href']
    title = link.find('h3').text
    browser.visit(nasa_url+href)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    down = soup.find('div', class_='downloads')
    image_url = down.find('a')['href']

    title_and_url.append({"title": title, "img_url": image_url})

    print('-----------')
    print(title)
    print(image_url)


# In[195]:


# html = browser.html
# soup = BeautifulSoup(html, 'html.parser')


# In[194]:


# down=soup.find('div', class_='downloads')
# image_url=down.find('a')['href']


# In[201]:


title_and_url


# In[202]:


browser.quit()


# In[ ]:
