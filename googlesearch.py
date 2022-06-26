#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import pandas
import requests 
import urllib.request
import time
import regex
import urllib.parse, lxml
from serpapi import GoogleSearch
import os
from gnewsclient import gnewsclient


# In[2]:


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from stop_words import get_stop_words


# In[3]:


def scrape_website_li(page_number, message):
    page_num = str(page_number)
    URL = 'https://thelogicalindian.com/fact-check/' + page_num
    webpage = requests.get(URL)
    soup = BeautifulSoup(webpage.text, 'html.parser')
    statement_footer = soup.find_all('div', {'class':'single-article'})
    
    '''
    for i in statement_footer:
        print(i)
        print("\n\n******************************************************************\n\n")
    '''
    
    msg = message.split()
    msg_words = [word for word in msg if word not in get_stop_words('english')]

    words = ['No,', 'False', 'false', 'no,' 'rumour', 'fake news', 'falsely']
    check = 0
    match = 0
    matched = 0
    article = ""

    for i in statement_footer:
        i = str(i)
        rgx = regex.compile(r'(?si)(?|{0}(.*?){1}|{1}(.*?){0})'.format('title="', '"/></a>'))
        m = rgx.findall(i)
        '''
        link1 = i.find('a', {'class':'general-anchor'}).find('img').get('alt')
        for j in words:
            if j in link1:
                match = match + 1
                articles.append(link1)
        '''
        
        
        try:
            j = ((m[0])[0]).split()
            for i in j:
                for m in msg_words:
                    if i == m:
                        match = match + 1
            if match >= len(j) - 1:
                matched = 1
                article = m[0]
        except:
            print("Searched a page")

    if matched == 1:
        print("Matching news found")
        
        for i in article:
            for j in words:
                if j in i:
                    check = 1
        if check == 1:
            print("It is a true rumour")
            return 1
        else:
            print("It is a fake rumour")
            return 0
    else:
        print("No matching news found")
        return 2
        
    check = 0
    match = 0
    matched = 0
    article = ""
    
    


# In[4]:


def scrape_website_pf(page_number, message):
    page_num = str(page_number)
    URL = 'https://www.politifact.com/factchecks/list/?page=' + page_num
    webpage = requests.get(URL)
    soup = BeautifulSoup(webpage.text, 'html.parser')
    statement_footer = soup.find_all('div', {'class':'m-statement__body'})
    
    '''
    for i in statement_footer:
        print(i)
        print("\n\n******************************************************************\n\n")
    '''

    
    msg = message.split()
    msg_words = [word for word in msg if word not in get_stop_words('english')]

    #words = ['No,', 'False', 'false', 'no,' 'rumour', 'fake news', 'falsely']
    check = 0
    match = 0
    matched = 0
    article = ""
    data = ""

    for i in statement_footer:
        i = str(i)
        d = str(i)
        rgx = regex.compile(r'(?si)(?|{0}(.*?){1}|{1}(.*?){0})'.format('/">', '</a>'))
        m = rgx.findall(i)
        
        #print(i)
        #print("****************")
        msplit = (m[0])[0].split()
        #print("-----------------------------------msplit-------------------------------")
        #print(msplit)
        
        try:
            for i in msplit:
                for j in msg_words:
                    if j == i:
                        match = match + 1
            #print(match)
            #print("---------------------------------match-------------------------------")
            if match >= (len(msplit) - 1)/2:
                matched = 1
                article = m[0]
                data = d
                #print(data)
                #print("---------------------------------data-----------------------------------")
                break
        except:
            print("Searched a page")

    if matched == 1:
        print("Matching news found")
        
        rgx = regex.compile(r'(?si)(?|{0}(.*?){1}|{1}(.*?){0})'.format('alt="', '" class='))
        m = rgx.findall(data)
        
        try:
            k = (m[0])[0]
            if k == "false":
                return 1
            elif k == "true":
                return 0
            else:
                return 2
        except:
            print("")
        
        '''
        try:
            print((m[0])[0])
        except:
            print("-----------------------------here--------------------------------")
        '''
        
    else:
        print("No matching news found")
        return 2
        
    check = 0
    match = 0
    matched = 0
    article = ""
    


# In[5]:


def scrape_website_gn(message):
    print("*_*_*_*_*_*_*_*_*_*_*_*_*_*")
    URL = 'https://news.google.com/search?q=' + message + '&hl=en-IN&gl=IN&ceid=IN%3Aen'
    webpage = requests.get(URL)
    soup = BeautifulSoup(webpage.text, 'html.parser')
    statement_footer = soup.find_all('h3', {'class':'ipQwMb ekueJc RD0gLb'})
    
    '''
    for i in statement_footer:
        print(i)
        print("\n\n******************************************************************\n\n")
    '''
    
    msg = message.split()
    msg_words = [word for word in msg if word not in get_stop_words('english')]
    for mw in range(len(msg_words)):
        msg_words[mw] = msg_words[mw].lower()

    #words = ['No,', 'False', 'false', 'no,' 'rumour', 'fake news', 'falsely']
    check = 0
    match = 0
    matched = 0
    article = ""

    print("-----------------------------------------------------")
    print(msg_words)
    print("-----------------------------------------------------")

    for i in statement_footer:
        i = str(i)
        #print(i)
        rgx = regex.compile(r'(?si)(?|{0}(.*?){1}|{1}(.*?){0})'.format('">', '</h3>'))
        m = rgx.findall(i)
        '''
        link1 = i.find('a', {'class':'general-anchor'}).find('img').get('alt')
        for j in words:
            if j in link1:
                match = match + 1
                articles.append(link1)
        '''
        
        j = str((m[0])[0])
        
        #print(j)
        rgx = regex.compile(r'(?si)(?|{0}(.*?){1}|{1}(.*?){0})'.format('">', '</a>'))
        m = rgx.findall(j)
        
        #print("----------------------------")
        
        #print(m)
        j = str((m[0])[0])
        j = j.split()
        
        print(j)

        for k in range(len(j)):
            j[k] = j[k].lower()
        
        try:
            for i in j:
                for m in msg_words:
                    if m == i:
                        match = match + 1

            print("________________________result from gn____________________________________")
            print("Match = " + str(match))
            print("____________________________________________________________")
            
            if match >= ((len(m[0]) - 1) / 2) + 4 :
                matched = 1
                article = m[0]
                break
        except:
            print("Searched a page")

        match = 0

    print("_______________________matched from gn_____________________________________")
    print("matched = " + str(matched) + "\n")
    print("____________________________________________________________")

    if matched == 1:
        return 1
    else:
        print("No matching news found")
        return 0
        
    check = 0
    match = 0
    matched = 0
    article = ""


# In[6]:


def googlesearch(message):
    for i in range(1, 3):
        result = scrape_website_li(i, message)
        if result != 2:
            break
        else:
            continue
    if result == 2:
        print("pf")
        for i in range(1, 3):
            result = scrape_website_pf(i, message)
            if result != 2:
                break
            else:
                continue
                
    if result == 2:
        print("gn")
        result = scrape_website_gn(message) 
    return result
            
            


# In[7]:


#Viral Video Shows Last Moments Of Chinese Boeing 737 Crash 
#false = 0
#true = 1
#pants-fire = 3
#barely-true = 3
#b1a9dd860e598900dd5292d49fcd676b52c21d437cd9968479ef935acb52cd97


# In[8]:


#googlesearch('Some gta online players are getting banned mistakely')
