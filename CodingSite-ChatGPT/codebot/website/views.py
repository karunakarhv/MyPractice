from django.shortcuts import render, redirect
from django.contrib import messages
import openai
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from .models import Code

# Create your views here.

def home(request):
    # API Key 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
    lang_list = ['awk', 'bash', 'c', 'clike', 'cpp', 'csharp', 'css', 'gherkin', 'git', 'graphql', 'java', 'javadoc', 'javadoclike', 'javascript', 'json', 'makefile', 'markdown', 'markup', 'powershell', 'python', 'xml-doc', 'yaml']
    if request.method == "POST":
        code = request.POST['code']
        lang = request.POST['lang']
        # Check to make sure they picked a language
        if lang == "Select Programming Language":
            messages.success(request, "Hey! You forgot to pick a programming language")
            return render(request, 'home.html', {'lang_list':lang_list, 'code':code, 'lang':lang})
        else:
            # OPENAI!!!
            openai.api_key = "open_ai_key"
            # Create OpenAI instance
            openai.Model.list()
            # Make an OpenAI Request
            try:
                response = openai.Completion.create(
                    engine = 'text-davinci-003',
                    prompt = f'Respond only with code. Fix this {lang} code: {code}',
                    temperature = 0,
                    max_tokens = 1000,
                    top_p = 1.0,
                    frequency_penalty = 0.0,
                    presence_penalty = 0.0
                )
                response = (response["choices"][0]["text"]).strip()
                record = Code(question=code, code_answer=response, language=lang, user=request.user)
                record.save()
                return render(request, 'home.html', {'lang_list':lang_list, 'response': response, 'lang': lang})
            except Exception as e:
                return render(request, 'home.html', {'lang_list':lang_list, 'response': e, 'lang': lang})
    
    return render(request, 'home.html', {'lang_list':lang_list})

def suggest(request):
    # API Key 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
    lang_list = ['awk', 'bash', 'c', 'clike', 'cpp', 'csharp', 'css', 'gherkin', 'git', 'graphql', 'java', 'javadoc', 'javadoclike', 'javascript', 'json', 'makefile', 'markdown', 'markup', 'powershell', 'python', 'xml-doc', 'yaml']
    if request.method == "POST":
        code = request.POST['code']
        lang = request.POST['lang']
        # Check to make sure they picked a language
        if lang == "Select Programming Language":
            messages.success(request, "Hey! You forgot to pick a programming language")
            return render(request, 'suggest.html', {'lang_list':lang_list, 'code':code, 'lang':lang})
        else:
            # OPENAI!!!
            openai.api_key = "open_ai_key"
            # Create OpenAI instance
            openai.Model.list()
            # Make an OpenAI Request
            try:
                response = openai.Completion.create(
                    engine = 'text-davinci-003',
                    prompt = f'Respond only with code. {code}',
                    temperature = 0,
                    max_tokens = 1000,
                    top_p = 1.0,
                    frequency_penalty = 0.0,
                    presence_penalty = 0.0
                )
                response = (response["choices"][0]["text"]).strip()
                record = Code(question=code, code_answer=response, language=lang, user=request.user)
                record.save()
                return render(request, 'suggest.html', {'lang_list':lang_list, 'response': response, 'lang': lang})
            except Exception as e:
                return render(request, 'suggest.html', {'lang_list':lang_list, 'response': e, 'lang': lang})
    
    return render(request, 'suggest.html', {'lang_list':lang_list})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!! Welcome")
            return redirect('home')
        else:
            messages.success(request, "Error Logging in. Please try again")
            return redirect('home')
    else:
        return render(request, 'home.html', {})

def logout_user(request):
     logout(request)
     messages.success(request, "You have been logged out!!")
     return redirect('home')


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have registered!! Congratulations')
            return redirect('home')
    else:
        form = SignUpForm

    return render(request, 'register.html', {'form': form})

def past(request):
    if request.user.is_authenticated:
        code = Code.objects.filter(user_id=request.user.id)
        return render(request, 'past.html', {"code": code})
    else:
        messages.success(request, 'You have not logged in, Please Login to continue')
        return redirect('home')

def delete_past(request, Past_id):
    code = Code.objects.get(pk=Past_id)
    code.delete()
    messages.success(request, 'Deleted successfully!!')
    return redirect('past')
