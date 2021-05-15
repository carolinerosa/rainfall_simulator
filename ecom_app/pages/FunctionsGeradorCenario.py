import pandas as pd
from datetime import timedelta
import json
from .config import config
from django.db import connection


class FunctionsGeradorCenario():
    
    @staticmethod
    def get_dist_temporal(dataInicial, dataFinal, yearSelect, cenario):
        table_name_temporal = config['tabelas']['DISTTEMP']['table_name']
        table_name_espacial = config['tabelas']['DISTESP']['table_name']
        print(yearSelect)
        #table_de_para = config['tabelas']['DISTTEMP']['table_depara']
        df_temporal = pd.read_sql_query("select sum(tab.vlrmediachuva) as vlrtemporal, tab.nomsubbacia as Bacia, tab.dtmedicao, to_char(dtmedicao, 'YYYY-MM-01') as dtreferencia from " + table_name_temporal + " as tab  where  tab.dtmedicao between '" + yearSelect + "-"+ dataInicial+"' and '"+yearSelect+"-"+ dataFinal+"' group by tab.nomsubbacia, tab.dtmedicao ",connection)
        df_espacial = pd.read_sql_query("select tab.vlrdistribuicao, tab.nombacia as Bacia from " + table_name_espacial + " as tab  where   upper(cenario) = '"+cenario+"' ",connection)
        df_mlt = pd.read_sql_query("select sum(tab.vlrmediachuva) as mlt, tab.nomsubbacia as Bacia, tab.dtmedicao as dtreferencia from " + table_name_temporal + " as tab  where  tab.dtmedicao between '"+yearSelect+"-"+dataInicial+"' and '"+yearSelect+"-"+dataFinal+"' group by tab.nomsubbacia, tab.dtmedicao ",connection)
        
        df_intermediario = pd.merge(df_espacial, df_mlt, how="left", on=["bacia"])
        df_intermediario['vlrsemana'] = (df_intermediario['mlt']/4) * df_intermediario['vlrdistribuicao']
        print(df_intermediario)
        df = pd.merge(df_temporal, df_intermediario, how="left", on=["bacia","dtreferencia"])
        df['vlrmediachuva'] = (df['vlrtemporal']) * df_intermediario['vlrsemana']
        print(df[["bacia","vlrmediachuva"]])
        result = df.set_index(['bacia','dtmedicao']).rename_axis(['vlr'], axis=1).stack().unstack(['dtmedicao']).reset_index()
        result = result.drop(['vlr'], axis=1)
        json_obj = result.reset_index().to_json(orient ='records')
        resultado = []
        resultado = json.loads(json_obj) 
        df = df.rename({'dtmedicao' : 'dtprevisao'},axis=1)
        return {"df" : df, "psat" : resultado, "columns" : result.columns}
    

    @staticmethod
    def get_resumo_cenario_week(df_psath, df_ecom_hoje,df_mapa,df_temporal):
        df_resumo =pd.concat([df_psath,df_ecom_hoje,df_mapa,df_temporal], ignore_index=True)
        df_resumo['dtprevisao'] = pd.to_datetime(df_resumo['dtprevisao'])
        date_min = min(df_resumo['dtprevisao'])
        weekDay = (date_min + timedelta(days=-1)).strftime('%a')
        df_resumo = df_resumo.groupby(df_resumo['bacia'].str.upper()).resample('W-'+ weekDay, on='dtprevisao').sum().reset_index().sort_values(by='dtprevisao')
        df_resumo['dtprevisao']=pd.to_datetime(df_resumo['dtprevisao']).apply(lambda x: x.date())
        
        result_resumo = df_resumo.set_index(['bacia','dtprevisao']).rename_axis(['vlr'], axis=1).stack().unstack(['dtprevisao']).reset_index()
        result_resumo = result_resumo.drop(['vlr'], axis=1)


        resumo = result_resumo.reset_index().to_json(orient ='records')
        resultado_resumo_week = []
        resultado_resumo_week = json.loads(resumo)
        return  {"resumo":resultado_resumo_week,"columns":result_resumo.columns}
    
    @staticmethod
    def get_resumo_cenario_diario(df_psath, df_ecom_hoje,df_mapa,df_temporal):
        df_resumo =pd.concat([df_psath,df_ecom_hoje,df_mapa,df_temporal], ignore_index=True)        
        
        resumo = df_resumo.reset_index().to_json(orient ='records')
        resultado_resumo_diario = []
        resultado_resumo_diario = json.loads(resumo)
        return  resultado_resumo_diario

    @staticmethod
    def get_psath(dataInicial, dataFinal, dataHoje):
        table_name_psath = config['tabelas']['PSATH']['table_name']
        table_de_para_psath = config['tabelas']['PSATH']['table_depara']
        table_name_psat = config['tabelas']['PSAT']['table_name']
        table_de_para_psat = config['tabelas']['PSAT']['table_depara']
        df_psath = pd.read_sql_query("select sum(tab.vlrmediachuva) as vlrmediachuva, dp.nombacia as Bacia, tab.dtmedicao from "+table_name_psath+" tab join "+table_de_para_psath+" dp on tab.codsubbacia = dp.codsubbacia where tab.dthcargaarquivo='"+dataHoje+"' and tab.dtmedicao between '"+dataInicial+"' and '"+dataFinal+"' group by dp.nombacia, tab.dtmedicao",connection)
        if(df_psath['dtmedicao'].max() != dataFinal):
            df_psath = pd.read_sql_query("select sum(tab.vlrmediachuva) as vlrmediachuva, dp.nombacia as Bacia, tab.dtmedicao from "+table_name_psath+" tab join "+table_de_para_psath+" dp on tab.codsubbacia = dp.codsubbacia where tab.dthcargaarquivo='"+dataFinal+"' and tab.dtmedicao between '"+dataInicial+"' and '"+dataFinal+"' group by dp.nombacia, tab.dtmedicao",connection)
            df_psat_d1 = df_psat = pd.read_sql_query("select sum(tab.vlrmediachuva) as vlrmediachuva, dp.nombacia as Bacia, tab.dtmedicao from "+table_name_psat+" tab join "+table_de_para_psat+" dp on tab.codsubbacia = dp.codsubbacia where tab.dthcargaarquivo='"+dataHoje+"' and tab.dtmedicao ='"+dataFinal+"' group by dp.nombacia, tab.dtmedicao",connection)
            df_psat = pd.concat([df_psath,df_psat_d1], ignore_index=True)
        
        result_psat = df_psat.set_index(['bacia','dtmedicao']).rename_axis(['vlr'], axis=1).stack().unstack(['dtmedicao']).reset_index()
        result_psat = result_psat.drop(['vlr'], axis=1)
        json_obj_psat = result_psat.reset_index().to_json(orient ='records')
        resultado_psat = []
        resultado_psat = json.loads(json_obj_psat) 
        df_psat = df_psat.rename({'dtmedicao' : 'dtprevisao'},axis=1)
        return {"df" : df_psat, "psat" : resultado_psat, "columns" : result_psat.columns}
    
    @staticmethod
    def get_mapa(mapa, dataInicial, dataFinal, dataHoje):
        table_name_mapa = config['mapa'][mapa]['table_name']
        table_depara_mapa = config['mapa'][mapa]['table_depara']
        df_mapa = pd.read_sql_query("select sum(tab.vlrmediachuva)/count(distinct(tab.codsubbacia)) as vlrmediachuva, dp.nombacia as Bacia, tab.dtprevisao from "+table_name_mapa+" tab join "+table_depara_mapa+" dp on tab.codsubbacia = dp.codsubbacia where tab.dthcargaarquivo='"+dataHoje+"' and tab.dtprevisao between '"+dataInicial+"' and '"+dataFinal+"' group by dp.nombacia, tab.dtprevisao",connection)
        result_mapa = df_mapa.set_index(['bacia','dtprevisao']).rename_axis(['vlr'], axis=1).stack().unstack(['dtprevisao']).reset_index()
        result_mapa = result_mapa.drop(['vlr'], axis=1)
        json_obj = result_mapa.reset_index().to_json(orient ='records')
        resultado_mapa = []
        resultado_mapa = json.loads(json_obj) 
        return {"df" : df_mapa, "mapa" : resultado_mapa, "columns" : result_mapa.columns}