#!/usr/bin/env python
# coding: utf-8

# In[43]:


from git import repo
import git
import os


# In[49]:


repo = git.Repo( '/home/manan/anaconda3/ChatBot/' )
#print(repo.git.status())
# checkout and track a remote branch
#print(repo.git.checkout( 'origin', b='master' ))
# add a file
repo.git.add(".")
# commit
repo.git.commit( "--allow-empty",m='Just another commit' )
# now we are one commit ahead
#print(repo.git.status())

os.environ['GIT_USERNAME'] = "manan-arya"
os.environ['GIT_PASSWORD'] = "Delhicb10c!"

repo.git.push("origin")

