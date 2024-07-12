import random
from django.shortcuts import render
import markdown2

from . import util

def convertMarkdownToHtml(title):
    content = util.get_entry(title)
    if content == None:
        return None
    else:
       return markdown2.markdown(content)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request , title):
    html_content = convertMarkdownToHtml(title)
    if html_content == None:
        return render(request , "encyclopedia/error.html" , {
            "message": "This entry does not exist!"
        })
    return render(request , "encyclopedia/entry.html" , {
        "content": html_content, "title":title
    })

def search(request):
    if request.method == "POST":
        entry_search = request.POST['q']
        html_content = convertMarkdownToHtml(entry_search)
        if html_content is not None:
            return render(request , "encyclopedia/entry.html" , {
                "title": entry_search , "content": html_content
            }) 
        else:
            allEntries = util.list_entries()
            foundEntry=[]
            for entry in allEntries:
                if entry_search.lower() in entry.lower():
                    foundEntry.append(entry)
            return render(request , "encyclopedia/search.html" , {
                "foundEntries": foundEntry
            })
        
def newPage(request):
    if request.method == "GET":
        return render(request , "encyclopedia/new.html")
    else:
        title = request.POST['title']
        content = request.POST['content']
        titleExist = util.get_entry(title)
        if titleExist is not None:
            return render(request , "encyclopedia/error.html" , {
                "message": "This page already exists!"
            })
        else:
            util.save_entry(title, content)
            html_content = convertMarkdownToHtml(title)
            print(title , html_content)   
            return render(request, "encyclopedia/entry.html", {
                "title": title, 
                "content": html_content 
            })
        
def edit(request):
    if request.method == "POST":
        title = request.POST['title']
        content = util.get_entry(title)
        return render(request , "encyclopedia/edit.html" , {
            "title": title , "content": content
        }) 
    
def saveEdit(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        html_content = convertMarkdownToHtml(title)
        return render(request , "encyclopedia/entry.html" , { 
            "title": title , "content": html_content
        })
    
def randomPage(request):
    allEntries = util.list_entries()
    randEntry = random.choice(allEntries)
    html_content = convertMarkdownToHtml(randEntry)
    return render(request , "encyclopedia/entry.html" , {
        "title": randEntry , "content": html_content
    })