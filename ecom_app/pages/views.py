from django.views.generic import TemplateView, ListView
from .models import TbDistribuicaoEspacialBacias,TbChuvaprevistaEcmwf,TbDeparaEcmwfEns,Tbbase,TbProdutibilidade
from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize
from sqlalchemy import create_engine
from django.conf import settings
from datetime import timedelta
import json
from django.db import connection
from .config import config
from django_pandas.managers import DataFrameManager
from django_pandas.io import read_frame
import pandas as pd
from selenium import webdriver
from django.views.decorators.csrf import csrf_exempt
from .FunctionsGeradorCenario import FunctionsGeradorCenario
from datetime import datetime


user = settings.DATABASES['default']['USER']
password = settings.DATABASES['default']['PASSWORD']
database_name = settings.DATABASES['default']['NAME']
database_url = 'postgresql://{user}:{password}@localhost:5432/{database_name}'.format(
    user=user,
    password=password,
    database_name=database_name,
)

engine = create_engine(database_url, echo=False)

def serialize_bootstraptable(queryset):
    json_data = serialize('json', queryset, use_natural_foreign_keys=True)
    
    json_final = {"total": queryset.count(), "rows": []}
    data = json.loads(json_data)
    for item in data:
        del item["model"]
        item["fields"].update({"id": item["pk"]})
        item = item["fields"]
        json_final['rows'].append(item)
    return json_final



# Create your views here.
class IndexView(TemplateView):
    template_name = 'pages/formulario.html'

class DistribEspacialView(TemplateView):
    template_name = 'pages/distribespacial.html'
    
    def get_context_data(self, **kwargs):
        context = super(DistribEspacialView, self).get_context_data(**kwargs)
        table_dist_esp_name = config['tabelas']['DISTESP']['table_name']
        
        df = pd.read_sql_query("select nombacia as Bacia, cenario as Cenario, vlrdistribuicao from "+table_dist_esp_name,connection)
        result_mapa = df.set_index(['bacia','cenario']).rename_axis(['vlr'], axis=1).stack().unstack(['cenario']).reset_index()
        result_mapa = result_mapa.drop(['vlr'], axis=1)
        print(result_mapa)
        json_obj = result_mapa.reset_index().to_json(orient ='records')#.rename({result_mapa.columns[0]:"0",result_mapa.columns[1]:"1",result_mapa.columns[2]:"2"},axis=1).reset_index().to_json(orient ='records')
        #print(json_obj)
        resultado = []
        resultado = json.loads(json_obj) 
        print(resultado)
        context['distribespacial'] = resultado
        context['columns'] = result_mapa.columns
        return context

class ProdutibilidadeView(TemplateView):
    template_name = 'pages/produtibilidade.html'
    
    def get_context_data(self, **kwargs):
        context = super(ProdutibilidadeView, self).get_context_data(**kwargs)
        table_produtibilidade = config['tabelas']['PRODUTIBILIDADE']['table_name']
        
        df = pd.read_sql_query("select codposto , nomeposto , vlrvazao as Vazao from "+table_produtibilidade,connection)
        #result_mapa = df.set_index(['bacia','cenario']).rename_axis(['vlr'], axis=1).stack().unstack(['cenario']).reset_index()
        #result_mapa = result_mapa.drop(['vlr'], axis=1)
        print(df)
        json_obj = df.reset_index().to_json(orient ='records')#.rename({result_mapa.columns[0]:"0",result_mapa.columns[1]:"1",result_mapa.columns[2]:"2"},axis=1).reset_index().to_json(orient ='records')
        #print(json_obj)
        resultado = []
        resultado = json.loads(json_obj)
        print(resultado)
        context['produtibilidade'] = resultado
        context['columns'] = df.columns
        return context


@csrf_exempt
def sendTable(request, *args, **kwargs):
    tabela = request.POST.get('table')
    
    df = pd.read_html(tabela)
    
    if('Unnamed' in df[0].columns[len(df[0].columns)-1]):
        df[0] = df[0].drop(df[0].columns[len(df[0].columns)-1],axis=1)

    distrib_esp_tab = pd.melt(df[0],id_vars=["Bacia"], var_name="cenario", value_name="vlrdistribuicao")
    distrib_esp_tab = distrib_esp_tab.rename({distrib_esp_tab.columns[0]:"nombacia"},axis=1)

    distrib_esp_tab.index += 1 
    distrib_esp_tab.to_sql(TbDistribuicaoEspacialBacias._meta.db_table, con=engine, if_exists = 'replace')

    return JsonResponse({'Tbbase':'OK'})

@csrf_exempt
def sendTableProdutibilidade(request, *args, **kwargs):
    tabela = request.POST.get('table')
    dtreferencia = request.POST.get('dtreferencia')
    
    df = pd.read_html(tabela)
    
    #distrib_esp_tab = pd.melt(df[0],id_vars=["Bacia"], var_name="cenario", value_name="vlrdistribuicao")
    distrib_esp_tab = df[0].rename({df[0].columns[0]:"codposto",df[0].columns[1]:"nomeposto",df[0].columns[2]:"vlrvazao"},axis=1)
    df_produtibilidade = distrib_esp_tab
    df_produtibilidade["dtreferencia"] = dtreferencia
    df_produtibilidade.index += 1 
    print(df_produtibilidade)
    df_produtibilidade.to_sql(TbProdutibilidade._meta.db_table, con=engine, if_exists = 'replace')

    return JsonResponse({'Tbbase':'OK'})
def tablesJoin(request):
    mapa = request.GET.get('mapa')
    datainicial = request.GET.get('datainicial')
    
    datafinal = request.GET.get('datafinal')
    mapeamentoinicial = request.GET.get('mapeamentoinicial')
    mapeamentofinal = request.GET.get('mapeamentofinal')
    data_dist_temp = request.GET.get('datatemporal')
    cenario = request.GET.get('cenario')
    anodistribtemp = request.GET.get('anodistribtemp')
    yearSelect = anodistribtemp.split("-")[0]
    print(yearSelect)
    dateinicial_mapa = (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d')
    date_hoje = (datetime.today()).strftime('%Y-%m-%d')
    datafinal_psat = (datetime.today() + timedelta(days=-1)).strftime('%Y-%m-%d')
    ##apagar as linhas seguintes
    dateinicial_mapa = (datetime.today() + timedelta(days=-23)).strftime('%Y-%m-%d')
    date_hoje = (datetime.today() + timedelta(days=-21)).strftime('%Y-%m-%d')
    dateinicial_mapa = "2021-04-01"
    date_hoje = "2021-04-03"
    
    
    result_mapa = FunctionsGeradorCenario.get_mapa(mapa,dateinicial_mapa,mapeamentofinal,date_hoje)
    datainicial = "2021-01-02"
    datafinal_psat = "2021-01-02"
    date_hoje = "2021-04-12"
    result_psath = FunctionsGeradorCenario.get_psath(datainicial,datafinal_psat,date_hoje)##date_hoje) provisorio
    datainicial_temporal = (max(result_mapa['df']['dtprevisao']) + timedelta(days=1)).strftime('%m-%d')
    mapeamentofinal_temporal = datetime.strptime(mapeamentofinal,'%Y-%m-%d').strftime('%m-%d')
    print(datainicial_temporal)
    #result_temporal = FunctionsGeradorCenario.get_dist_temporal(datainicial_temporal,mapeamentofinal_temporal,yearSelect,cenario)
    print("PSAT")
    print(result_psath['df'])
    result_resumo = FunctionsGeradorCenario.get_resumo_cenario_week(result_psath['df'],result_mapa["df"],result_mapa["df"],result_mapa["df"])

    #cursor = connection.cursor()
    #cursor.execute("select sum(tab.vlrmediachuva) as vlrmediachuva, dp.nombacia, tab.dtprevisao, tab.dthcargaarquivo from "+table_name+" tab join "+table_depara+" dp on tab.codsubbacia = dp.codsubbacia where tab.dthcargaarquivo='2021-04-07' group by dp.nombacia, tab.dtprevisao, tab.dthcargaarquivo")
    #results_mapa = cursor.fetchall()

    table_dist_esp_name = config['tabelas']['DISTESP']['table_name']
    table_mlt =  config['tabelas']['MLT']['table_name']
    
   
    context = {'mapa': result_mapa["mapa"],'columns' : result_mapa["columns"],'psat': result_psath['psat'],'psat_columns' : result_psath['columns'],'resumo': result_resumo['resumo'] , 'resumo_columns' : result_resumo['columns']} 
    #data = {'rendered_table': render_to_string('tablemodel.html', context={'Tbbase':results})}
    #return JsonResponse(data)
    #return render(request,'pages/tablemodel.html',{'Tbbase':result_mapa.to_html()})
    return render(request,'pages/tablemodel.html',context)
    #return JsonResponse({'Tbbase':results},safe=False)

def hometeste(request):
    base = TbChuvaprevistaEcmwf.objects.all()
    base = TbChuvaprevistaEcmwf.objects.values('codsubbacia','codsubbacia__nombacia')
    
    print(base.query)
          
    return JsonResponse({'Tbbase':json.loads(json.dumps(list(base)))})

class modelView(TemplateView):
    template_name = 'pages/formulario.html'
    
    

class VOListView(ListView):
    model = TbDistribuicaoEspacialBacias
    template_name = 'pages/index.html'