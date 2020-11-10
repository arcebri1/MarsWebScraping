#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
from bs4 import BeautifulSoup
import requests
import pymongo
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[2]:


#Open web browser/Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


### NASA Mars News##


# In[4]:


# Open URL of page to be scraped
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

# Create BeautifulSoup object; parse with 'html.parser'
html = browser.html
soup = BeautifulSoup(html, 'html.parser')

# Retrieve the title
news_title=soup.find_all('div', class_='content_title')[1].text

# Retrieve the title paragraph
news_p=soup.find_all('div', class_='article_teaser_body')[0].text

print(f'Title: {news_title}')
print(f'Summary: {news_p}')


# In[5]:


### JPL Mars Space Images - Featured Image


# In[6]:


# Open URL of page to be scraped
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)

#Press on the button Full Image
browser.click_link_by_id('full_image')

#Press on the button More Info
browser.click_link_by_partial_text('more info')

# Create BeautifulSoup object; parse with 'html.parser'
html = browser.html
soup = BeautifulSoup(html, 'html.parser') 

#Scrape the page to get the image url
main=soup.find('figure', class_='lede')
img=main.find('a')
href=img['href']
nasa_url='https://www.jpl.nasa.gov'
featured_image_url=nasa_url+href
print(f'The url for NASA featured image of the day is:      {featured_image_url}')


# In[7]:


### Mars Facts


# In[8]:


# Open URL of page to be scraped
url = 'https://space-facts.com/mars/'
browser.visit(url)

#Read the url in html
tables = pd.read_html(url)
tables


# In[9]:


#Create a Dataframe
df=tables[0]
df


# In[10]:


#Rename the key values
df.columns=["Description", "Mars Values"]
df


# In[11]:


index_df=df.set_index('Description')
index_df


# In[12]:


#Create dataframe to html table
html_table = index_df.to_html()
html_table


# In[13]:


#Clean up the html table
html_tb=html_table.replace('\n', '')
html_tb


# In[14]:


### Mars Hemispheres


# In[15]:


# Open URL of page to be scraped
url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

# Create BeautifulSoup object; parse with 'html.parser'
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[16]:


# Retrieve the parent div for all components
articles = soup.find_all('div', class_='description')

#Main url
nasa_url='https://astrogeology.usgs.gov/'

#Create a list to append the title and image
title_and_url=[]

# Iterate through each product
for article in articles:
    # Use Beautiful Soup's find() method to navigate and retrieve attributes
    link = article.find('a')
    href = link['href']
    title = link.find('h3').text
    browser.visit(nasa_url+href)
    
    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    #Scrape to find the image url
    down=soup.find('div', class_='downloads')
    image_url=down.find('a')['href']
    
    #Append the results to the list
    title_and_url.append({"title":title, "img_url":image_url})
    
    #Print the results
    print('-----------')
    print(title)
    print(image_url)



# In[17]:


#Show dictionary
title_and_url


# In[18]:


browser.quit()


# In[ ]:




