from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth import get_user_model # importando o modelo user customizado
from django.contrib import messages
from django.contrib import auth


# Create your views here.S

def logout(request):
    auth.logout(request)
    messages.success(request,"Logout efetuado com sucesso")
    return redirect('login')

def login(request):
    form = LoginForms
    formCadastro = CadastroForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            email = form['email_login'].value()
            senha = form['senha'].value()

        usuario = auth.authenticate(
            request,
            email=email,
            password=senha
        )

        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f"{email} logado com sucesso!")
            return redirect('classifyForm')
        else:
            messages.error(request, "Erro ao efetuar login! :(")
            return redirect('login')    

    return render(request, "usuarios/login.html", {"form": form})

def cadastro(request):
    CustomUser = get_user_model()
    formCadastro = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)
        
        if form.is_valid():
            if form["senha_1"].value() != form["senha_2"].value():
                messages.error(request, "Senhas não são iguais.")
                return redirect('cadastro')

            first_name = form["first_name"].value()
            last_name = form["last_name"].value()
            email = form["email"].value()
            senha = form['senha_1'].value()

            if CustomUser.objects.filter(email=email).exists():
                messages.error(request, "Este email já foi cadastrado, por favor digite outro.")
                return redirect('cadastro')

            usuario = CustomUser.objects.create_user(
                first_name =  first_name,
                last_name = last_name,
                email = email,
                password = senha
            )

            usuario.save()
            messages.success(request, "Cadastro efetuado com sucesso! :D")
            return redirect('login')


    return render(request, 'usuarios/cadastro.html',{"form": formCadastro})
