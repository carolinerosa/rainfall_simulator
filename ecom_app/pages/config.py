config = {
    'tabelas':{
        'DISTESP' : {
            'table_name': 'tb_distribuicao_espacial_bacias'
        },
        'PRODUTIBILIDADE' : {
            'table_name': 'tb_ena_produtibilidade'
        },
        'MLT' : {
            'table_name': 'tb_cargahistorica_ecom'
        },
        'DISTTEMP' : {
            'table_name': 'tb_cargahistorica_ecom'
        },
        'PSATH': {
            'table_name' : 'tb_chuvaobservada_psat',
            'table_depara' : 'tb_depara_psat'
        },
        'PSAT': {
            'table_name' : 'tb_chuvaobservada_psat',
            'table_depara' : 'tb_depara_psat'
        }
        

    },
    'mapa': {
        'EC': {
            'table_name': 'tb_chuvaprevista_ecmwf_controle',
            'table_depara': 'tb_depara_ecmwf_controle'
        },
        'ECENS': {
            'table_name': 'tb_chuvaprevista_ecmwf_ens',
            'table_depara': 'tb_depara_ecmwf_ens'
        },
        'GEFS': {
            'table_name': 'tb_chuvaprevista_gefs',
            'table_depara': 'tb_depara_gefs'
        },
        'REMOVIES': {
            'table_name': 'tb_chuvaprevista_pmedia',
            'table_depara': 'tb_depara_pmedia'
        }
        
    }
}
