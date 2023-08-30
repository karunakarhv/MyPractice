from django.shortcuts import render
from django.contrib import messages

# Create your views here.

def home(request):
    lang_list = ['awk', 'bash', 'c', 'clike', 'cpp', 'csharp', 'css', 'gherkin', 'git', 'graphql', 'java', 'javadoc', 'javadoclike', 'javascript', 'json', 'makefile', 'markdown', 'markup', 'powershell', 'python', 'xml-doc', 'yaml']
    if request.method == "POST":
        code = request.POST['code']
        if "lang" in request.POST:
            lang = request.POST['lang']
        # Check to make sure they picked a language
        if lang == "Select Programming Language":
            messages.success(request, "Hey! You forgot to pick a programming language")
            return render(request, 'home.html', {'lang_list':lang_list, 'code':code, 'lang':lang})
        
        return render(request, 'home.html', {'lang_list':lang_list, 'code':code, 'lang':lang})
    
    return render(request, 'home.html', {'lang_list':lang_list})