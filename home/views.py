import pandas as pd
import re
from datetime import datetime
from django.shortcuts import render, redirect
from pathlib import os
from django.http import HttpResponse
from .forms import HomeForm, FilterForm
from django.contrib import messages
from .cart import CARTlgoritm
from .models import Classification
from django.db.models import Q
from django.shortcuts import get_object_or_404
from urllib.parse import urlencode
from django.contrib.auth.decorators import login_required
from django.contrib import messages

""" loginForm(rota para a página de classificalção) """

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado.")
        return redirect('login')
    form = HomeForm()
    filterForm = FilterForm() 
    return render(request,'home/classify.html', {'form': form}) 

""" def index(request):
    form = HomeForm()
    filterForm = FilterForm()
    return render(request,'usuarios/login.html') """

def classifyForm(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado.")
        return redirect('login')
    form = HomeForm()
    #filterForm = FilterForm()
    return render(request,'home/classify.html', {'form': form})


def filterForm(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado.")
        return redirect('login')
    filterForm = FilterForm()
    return render(request,'home/filter.html', {'filterForm': filterForm})

""" def filter(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado.")
        return redirect('login')
    filterForm = FilterForm()
    if request.method == 'GET':
        plantation_name = request.GET.get('plantation_name', None)
        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)

       # Validação dos campos
        errors = []
        if plantation_name and not plantation_name.isalpha():
            errors.append('Nome da planta deve conter apenas letras.')
        try:
            if start_date:
                datetime.strptime(start_date, '%Y-%m-%d')
            if end_date:
                datetime.strptime(end_date, '%Y-%m-%d')
        except ValueError:
            errors.append('Data inválida. O formato correto é YYYY-MM-DD.')

        if errors:
            for error in errors:
                messages.error(request, error)
            return render(request, 'home/filter.html', {'filterForm': filterForm})


        # Crie um objeto de consulta vazia
        queryset = Classification.objects.all()

        # Adicione filtros com base nos parâmetros fornecidos
        filters = Q()  # Crie um objeto Q vazio

        if plantation_name:
            filters &= Q(classification__icontains=plantation_name)

        if start_date and end_date:
            filters &= Q(forecast_date__range=[start_date, end_date])

        # Aplique os filtros à consulta
        queryset = queryset.filter(filters)

        # Renderize o resultado da consulta na template
        return render(request, 'home/filter.html', {'filterForm': filterForm, 'results': queryset})

    return render(request, 'home/filter.html') """

def filter(request):
    filterForm = FilterForm()
    if request.method == 'GET':
        plantation_name = request.GET.get('plantation_name', None)
        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)

        # Validação dos campos
        errors = []
        if plantation_name and not plantation_name.isalpha():
            errors.append('Nome da planta deve conter apenas letras.')

        try:
            if start_date:
                datetime.strptime(start_date, '%Y-%m-%d')
            if end_date:
                datetime.strptime(end_date, '%Y-%m-%d')
        except ValueError:
            errors.append('Data inválida. O formato correto é YYYY-MM-DD.')

        if errors:
            for error in errors:
                messages.error(request, error)
            return render(request, 'home/filter.html', {'filterForm': filterForm})

        # Crie um objeto de consulta vazia
        queryset = Classification.objects.filter(usuario=request.user)  # Filtrar por usuário atual

        # Adicione filtros com base nos parâmetros fornecidos
        filters = Q()  # Crie um objeto Q vazio

        if plantation_name:
            filters &= Q(classification__icontains=plantation_name)

        if start_date and end_date:
            filters &= Q(forecast_date__range=[start_date, end_date])

        # Aplique os filtros à consulta
        queryset = queryset.filter(filters)

        # Renderize o resultado da consulta na template
        return render(request, 'home/filter.html', {'filterForm': filterForm, 'results': queryset})

    return render(request, 'home/filter.html')


def classify(request):
    if not request.user.is_authenticated:
        return redirect('login')
    form = HomeForm()
    filterForm = FilterForm()
    if request.method == 'POST':
        form = HomeForm(request.POST)
        filterForm = FilterForm()

      
        if form.is_valid():
            # Obtenha os valores do formulário
            n_level = form.cleaned_data['N']
            ph_level = form.cleaned_data['P']
            k_level = form.cleaned_data['K']
            temperature = form.cleaned_data['temperature']
            humidity = form.cleaned_data['humidity']
            soil_ph = form.cleaned_data['soil_ph']
            rainfall = form.cleaned_data['rainfall']
            water_per_year = form.cleaned_data['water_per_year']

            if all(isinstance(val, (int, float)) for val in [n_level, ph_level, k_level, temperature, humidity, soil_ph, rainfall, water_per_year]):
            
            # Criar um DataFrame Pandas com as mesmas chaves de coluna que no conjunto de dados original
                new_data = pd.DataFrame({
                    'N': [n_level],
                    'P': [ph_level],
                    'K': [k_level],
                    'temperature(in degree celsius)': [temperature],
                    'humidity(in percentage)': [humidity],
                    'ph of soil': [soil_ph],
                    'rainfall( in mm )': [rainfall],
                    'water-availability(liters per year)': [water_per_year]
                })

                # Remover a coluna de índice numérico
                new_data = new_data.iloc[0]

                # Caminho correto para o modelo
                modelo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'algoritmModel', 'decision_tree_model.pkl'))

                # Criar uma instância da classe AlgoritmoCART com o caminho do modelo treinado
                algoritmo = CARTlgoritm(modelo_path)
                
                # Fazer uma previsão com base nos dados do formulário
                previsao = algoritmo.fazer_previsao(new_data) 
                previsao = previsao[0]
                # Criar uma instância do modelo de dados
                previsao_model = Classification(
                    nitrogen=n_level,
                    potassium=ph_level,
                    calcium=k_level,
                    temperature=temperature,
                    humidity=humidity,
                    soil_ph=soil_ph,
                    ground_precipitation=rainfall,
                    available_water_annual=water_per_year,
                    classification=previsao,  # Coloque o valor de previsão aqui
                    usuario=request.user  # Associe a classificação ao usuário atual
                )

                previsao_model.save()

                # Recupere o objeto Classification recém-criado do banco de dados
                objeto_classificado = Classification.objects.last()

                # Calcula a matriz de confusão
                valores_reais = [previsao_model.classification]  # Obtenha os valores reais do banco de dados
                previsoes = [previsao]  # Valor de previsão do seu modelo

                objeto_classificado_id = previsao_model.id
                return redirect('results', objeto_id=objeto_classificado_id)

        else:          
            messages.error(request, 'Por favor digite apenas valores numéricos')
            return redirect('classifyForm')

    return render(request,'classifyForm', {'form': form})

def removeItem(request, objeto_id):
    if not request.user.is_authenticated:
        return redirect('login')
    objeto_classificado = get_object_or_404(Classification, pk=objeto_id)
    # Obtenha os parâmetros de filtro da consulta atual
    plantation_name = request.GET.get('plantation_name', '')
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')

    # Exclua o objeto
    objeto_classificado.delete()

    # Construa os parâmetros de filtro para incluir na URL
    filters = {
        'plantation_name': plantation_name,
        'start_date': start_date,
        'end_date': end_date
    }

    # Codifique os parâmetros de filtro na URL
    filters_encoded = urlencode(filters)

    # Redirecione para a página de filtro com os parâmetros de filtro incluídos na URL
    return redirect(f'/filter?{filters_encoded}')

def results(request, objeto_id):
    if not request.user.is_authenticated:
        return redirect('login')
    try:
        objeto_classificado = Classification.objects.get(pk=objeto_id)

        contexto = {
                'objeto_classificado': objeto_classificado,
        }
   
    except Classification.DoesNotExist:
        # Trate o caso em que o objeto não existe
        objeto_classificado = None

    return render(request, 'home/results.html', contexto)
