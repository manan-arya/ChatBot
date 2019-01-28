
# coding: utf-8

# In[7]:


import re
from nltk.corpus import stopwords


# In[8]:


def find_email(string):
    if re.search(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", string):
        email = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", string)
        return email[0]
    else:
        return None


# In[9]:


def find_phone(string):
    for word in string.split():
        if word[0].isdigit():
            if word[0] == '0':
                phone = re.findall(r"([0]\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})",word)
                phone = phone[0][1:]
            else:
                phone = re.findall(r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})",word)
                
            phone = re.sub(r'[-\.\ ]', "", phone)
            return phone
        else:
            return None


# In[10]:


def capture_name(string):
    name = []
    stop_words = stopwords.words('english')
    #print(stop_words)
    ignore_words = ['i','am','my','name','is','people','call','me','.','hey']
    ignore_words = ignore_words + stop_words
    for word in string.split():
        #if word.isalpha():
        if word.lower() not in ignore_words:
            word = word.replace('.','')
            name.append(word)
    if len(name) >=3:
        return name[0],name[1:-1],name[-1]
    elif len(name) == 2:
        return name[0],None,name[-1]
    elif len(name) == 1:
        return name[0],None,None
    else:
        return None,None,None


# In[11]:


#import nltk
#nltk.download()


# In[12]:


#print(find_email('Mail me at mananarya18@gmail.com'))
#print(find_phone('Call me at 08285685590'))
#first_name,middle_name,last_name = capture_name("we")
#if first_name != None
#print(str(first_name)+' '+str(middle_name)+' '+str(last_name))

