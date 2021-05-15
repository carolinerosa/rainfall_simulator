from django.db import models
from django_pandas.managers import DataFrameManager

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class Tbbase(models.Model):
    vlrmediachuva = models.FloatField(blank=True, null=True)
    nombacia = models.CharField(max_length=50, blank=True, null=True)
    dtprevisao = models.DateField(blank=True, null=True)
    #dthcargaarquivo = models.DateField(blank=True, null=True)

class TbAcompanhamentoPh(models.Model):
    idacompph = models.BigIntegerField()
    dtreferencia = models.DateField(blank=True, null=True)
    dtmedicao = models.DateField(blank=True, null=True)
    codposto = models.CharField(max_length=50, blank=True, null=True)
    vlrnivelreslido = models.FloatField(blank=True, null=True)
    vlrnivelresconsol = models.FloatField(blank=True, null=True)
    vlrvazaodefluentelido = models.FloatField(blank=True, null=True)
    vlrvazaodefluenteconsol = models.FloatField(blank=True, null=True)
    vlrvazaoafluentelido = models.FloatField(blank=True, null=True)
    vlrvazaoafluenteconsol = models.FloatField(blank=True, null=True)
    vlrvazaoincremconsol = models.FloatField(blank=True, null=True)
    vlrvazaonaturalconsol = models.FloatField(blank=True, null=True)
    dtcarga = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_acompanhamento_ph'


class TbChuvaobservadaPdpSmap(models.Model):
    idchobpdpsmap = models.BigIntegerField()
    codsubbacia = models.CharField(max_length=50, blank=True, null=True)
    dtgeracao = models.DateField(blank=True, null=True)
    hrgeracao = models.CharField(max_length=10, blank=True, null=True)
    vlrmediachuva = models.FloatField(blank=True, null=True)
    dthcargaarquivo = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_chuvaobservada_pdp_smap'


class TbChuvaobservadaPsat(models.Model):
    idchobpsat = models.BigIntegerField()
    dthcargaarquivo = models.DateField(blank=True, null=True)
    codsubbacia = models.CharField(max_length=50, blank=True, null=True)
    numlatitude = models.FloatField(blank=True, null=True)
    numlong = models.FloatField(blank=True, null=True)
    vlrmediachuva = models.FloatField(blank=True, null=True)
    
    objects = DataFrameManager()
    class Meta:
        managed = False
        db_table = 'tb_chuvaobservada_psat'


class TbChuvaobservadaPsath(models.Model):
    idchobpsath = models.BigIntegerField()
    dthcargaarquivo = models.DateField(blank=True, null=True)
    codsubbacia = models.CharField(max_length=50, blank=True, null=True)
    numlatitude = models.FloatField(blank=True, null=True)
    numlong = models.FloatField(blank=True, null=True)
    vlrmediachuva = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_chuvaobservada_psath'




class TbChuvaprevistaEcmwfEns(models.Model):
    idchprvecmwfens = models.BigIntegerField(primary_key=True)
    codsubbacia = models.CharField(max_length=50, blank=True, null=True)
    numlatitude = models.FloatField(blank=True, null=True)
    numlong = models.FloatField(blank=True, null=True)
    dtarquivo = models.DateField(blank=True, null=True)
    dtprevisao = models.DateField(blank=True, null=True)
    vlrmediachuva = models.FloatField(blank=True, null=True)
    dthcargaarquivo = models.DateField(blank=True, null=True)
    membro = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_chuvaprevista_ecmwf_ens'


class TbChuvaprevistaEta40(models.Model):
    idchprveta40 = models.BigIntegerField()
    codsubbacia = models.CharField(max_length=50, blank=True, null=True)
    numlatitude = models.FloatField(blank=True, null=True)
    numlong = models.FloatField(blank=True, null=True)
    dtarquivo = models.DateField(blank=True, null=True)
    dtprevisao = models.DateField(blank=True, null=True)
    vlrmediachuva = models.FloatField(blank=True, null=True)
    dthcargaarquivo = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_chuvaprevista_eta40'


class TbChuvaprevistaGefs(models.Model):
    idchprvgefs = models.BigIntegerField()
    codsubbacia = models.CharField(max_length=50, blank=True, null=True)
    numlatitude = models.FloatField(blank=True, null=True)
    numlong = models.FloatField(blank=True, null=True)
    dtarquivo = models.DateField(blank=True, null=True)
    dtprevisao = models.DateField(blank=True, null=True)
    vlrmediachuva = models.FloatField(blank=True, null=True)
    dthcargaarquivo = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_chuvaprevista_gefs'


class TbChuvaprevistaPmedia(models.Model):
    idchprvpmedia = models.BigIntegerField()
    codsubbacia = models.CharField(max_length=50, blank=True, null=True)
    numlatitude = models.FloatField(blank=True, null=True)
    numlong = models.FloatField(blank=True, null=True)
    dtarquivo = models.DateField(blank=True, null=True)
    dtprevisao = models.DateField(blank=True, null=True)
    vlrmediachuva = models.FloatField(blank=True, null=True)
    dthcargaarquivo = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_chuvaprevista_pmedia'


class TbDadosfluviometricosvazaoobservadaSin(models.Model):
    iddpluvazobssin = models.BigIntegerField()
    dtreferencia = models.DateField(blank=True, null=True)
    dtmedicao = models.DateField(blank=True, null=True)
    codposto = models.CharField(max_length=50, blank=True, null=True)
    nomreservatorioassoc = models.CharField(max_length=50, blank=True, null=True)
    vlrvmd = models.FloatField(blank=True, null=True)
    vlrvms = models.FloatField(blank=True, null=True)
    dtcarga = models.DateField(db_column='DtCarga', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_dadosfluviometricosvazaoobservada_sin'


class TbDeparaEcmwf(models.Model):
    idcodsubbacia = models.BigIntegerField()
    codsubbacia = models.CharField(primary_key=True,max_length=50, blank=True)
    nombacia = models.CharField(max_length=50, blank=True, null=True)
    nomsubbacia = models.CharField(max_length=50, blank=True, null=True)
    numlatitude = models.FloatField(blank=True, null=True)
    numlongitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_depara_ecmwf'


class TbDeparaEcmwfEns(models.Model):
    idcodsubbacia = models.BigIntegerField()
    codsubbacia = models.CharField(primary_key=True,db_column='codsubbacia',max_length=50, blank=True)
    nombacia = models.CharField(max_length=50, blank=True, null=True)
    nomsubbacia = models.CharField(max_length=50, blank=True, null=True)
    numlatitude = models.FloatField(blank=True, null=True)
    numlongitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_depara_ecmwf_ens'


class TbDeparaEta40(models.Model):
    idcodsubbacia = models.BigIntegerField()
    codsubbacia = models.CharField(max_length=50, blank=True, null=True)
    nombacia = models.CharField(max_length=50, blank=True, null=True)
    nomsubbacia = models.CharField(max_length=50, blank=True, null=True)
    numlatitude = models.FloatField(blank=True, null=True)
    numlongitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_depara_eta40'


class TbDeparaGefs(models.Model):
    idcodsubbacia = models.BigIntegerField()
    codsubbacia = models.CharField(max_length=50, blank=True, null=True)
    nombacia = models.CharField(max_length=50, blank=True, null=True)
    nomsubbacia = models.CharField(max_length=50, blank=True, null=True)
    numlatitude = models.FloatField(blank=True, null=True)
    numlongitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_depara_gefs'


class TbDeparaImerge(models.Model):
    iddeparaimerge = models.BigIntegerField()
    codsubbacia = models.CharField(max_length=50, blank=True, null=True)
    nombacia = models.CharField(max_length=50, blank=True, null=True)
    nomsubbacia = models.CharField(max_length=50, blank=True, null=True)
    numlatitude = models.FloatField(blank=True, null=True)
    numlongitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_depara_imerge'


class TbDeparaPmedia(models.Model):
    idcodsubbacia = models.BigIntegerField()
    codsubbacia = models.CharField(max_length=50, blank=True, null=True)
    nombacia = models.CharField(max_length=50, blank=True, null=True)
    nomsubbacia = models.CharField(max_length=50, blank=True, null=True)
    numlatitude = models.FloatField(blank=True, null=True)
    numlongitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_depara_pmedia'


class TbDeparaPsat(models.Model):
    idcodpsat = models.BigIntegerField()
    codsubbacia = models.CharField(max_length=50, blank=True, null=True)
    nombacia = models.CharField(max_length=50, blank=True, null=True)
    nomsubbacia = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_depara_psat'


class TbHidraulicohidrologicaRdh(models.Model):
    idhidrdh = models.BigIntegerField()
    dtreferencia = models.DateField(blank=True, null=True)
    codposto = models.CharField(max_length=50, blank=True, null=True)
    vlrvazao = models.FloatField(blank=True, null=True)
    vlrnivelres_m = models.FloatField(blank=True, null=True)
    vlrvolumearm = models.FloatField(blank=True, null=True)
    vlrvolumeesp = models.FloatField(blank=True, null=True)
    vlrvazaotur = models.FloatField(blank=True, null=True)
    vlrvazaover = models.FloatField(blank=True, null=True)
    vlrvazaootr = models.FloatField(blank=True, null=True)
    vlrvazaodfl = models.FloatField(blank=True, null=True)
    vlrvazaotra = models.FloatField(blank=True, null=True)
    vlrvazaoafl = models.FloatField(blank=True, null=True)
    vlrvazaoinc = models.FloatField(blank=True, null=True)
    vlrvazaousoscon = models.FloatField(blank=True, null=True)
    vlrvazaoevp = models.FloatField(blank=True, null=True)
    vlrvazaoart = models.FloatField(blank=True, null=True)
    dtcarga = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_hidraulicohidrologica_rdh'


class TbVazaoobservadaMlt(models.Model):
    idvazobsmlt = models.BigIntegerField()
    codposto = models.CharField(max_length=50, blank=True, null=True)
    dtreferencia = models.DateField(blank=True, null=True)
    vlrvazao = models.FloatField(blank=True, null=True)
    dtcarga = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_vazaoobservada_mlt'


class TbVazaoobservadaPdp(models.Model):
    idvazobspdp = models.BigIntegerField()
    dtmedicao = models.DateField(blank=True, null=True)
    codposto = models.CharField(max_length=50, blank=True, null=True)
    cod1 = models.CharField(max_length=50, blank=True, null=True)
    cod2 = models.CharField(max_length=50, blank=True, null=True)
    tipovazao = models.CharField(max_length=50, blank=True, null=True)
    vlrvazao = models.FloatField(blank=True, null=True)
    dtcarga = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_vazaoobservada_pdp'


class TbVazaoobservadaSemanal(models.Model):
    idvazobssem = models.BigIntegerField()
    codposto = models.CharField(max_length=50, blank=True, null=True)
    ano = models.IntegerField(blank=True, null=True)
    semana = models.IntegerField(blank=True, null=True)
    vlrvazao = models.FloatField(blank=True, null=True)
    cenario = models.IntegerField(blank=True, null=True)
    dtcenario = models.DateField(blank=True, null=True)
    dtcarga = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_vazaoobservada_semanal'


class TbVazaoobservadaSin(models.Model):
    idvazobssin = models.BigIntegerField()
    dtreferencia = models.DateField(blank=True, null=True)
    dtmedicao = models.DateField(blank=True, null=True)
    vlrvnm = models.FloatField(blank=True, null=True)
    vlrvia = models.FloatField(blank=True, null=True)
    vlrvns = models.FloatField(blank=True, null=True)
    vlrvip = models.FloatField(blank=True, null=True)
    vlrvna = models.FloatField(blank=True, null=True)
    vlrvar = models.FloatField(blank=True, null=True)
    dtcarga = models.DateField(db_column='DtCarga', blank=True, null=True)  # Field name made lowercase.
    codposto = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_vazaoobservada_sin'


class TbVazaoobservadaSinTeste(models.Model):
    idvazobssin = models.BigIntegerField()
    dtreferencia = models.DateField(blank=True, null=True)
    dtmedicao = models.DateField(blank=True, null=True)
    nomsubbacia = models.CharField(max_length=50, blank=True, null=True)
    vlrvnm = models.FloatField(blank=True, null=True)
    vlrvia = models.FloatField(blank=True, null=True)
    vlrvns = models.FloatField(blank=True, null=True)
    vlrvip = models.FloatField(blank=True, null=True)
    vlrvna = models.FloatField(blank=True, null=True)
    vlrvar = models.FloatField(blank=True, null=True)
    vlrvmd = models.FloatField(blank=True, null=True)
    vlrvms = models.FloatField(blank=True, null=True)
    dtcarga = models.DateField(db_column='DtCarga', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_vazaoobservada_sin_teste'


class TbVazaoobservadaVazoes(models.Model):
    idvazobsvazoes = models.BigIntegerField()
    codposto = models.CharField(max_length=50, blank=True, null=True)
    dtreferencia = models.DateField(blank=True, null=True)
    dtcenario = models.DateField(blank=True, null=True)
    codcenario = models.IntegerField(blank=True, null=True)
    vlrvazao = models.FloatField(blank=True, null=True)
    dtcarga = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_vazaoobservada_vazoes'

class TbDistribuicaoEspacialBacias(models.Model):
    iddistresp = models.BigIntegerField(primary_key=True)
    cenario = models.CharField(max_length=50, blank=True, null=True)
    nombacia = models.CharField(max_length=50, blank=True, null=True)
    vlrdistribuicao = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_distribuicao_espacial_bacias'
    def __str__(self):
        """String for representing the Model object."""
        return '{self.cenario} ({self.nombacia})'
        
class TbVazaoobservadaVazpast(models.Model):
    idvazobsvazpast = models.BigIntegerField(primary_key=True)
    dtmedicao = models.DateField(blank=True, null=True)
    dtreferencia = models.DateField(blank=True, null=True)
    codposto = models.CharField(max_length=50, blank=True, null=True)
    vlrvazao = models.FloatField(blank=True, null=True)
    dtcarga = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_vazaoobservada_vazpast'


    def __str__(self):
        """String for representing the Model object."""
        return '{self.codposto} ({self.vlrvazao})'


class TbChuvaprevistaEcmwf(models.Model):
    idchprvecmwf = models.BigIntegerField(primary_key=True)
    codsubbacia = models.ForeignKey(TbDeparaEcmwfEns,db_column='codsubbacia',on_delete=models.CASCADE)
    numlatitude = models.FloatField(blank=True, null=True)
    numlong = models.FloatField(blank=True, null=True)
    dtarquivo = models.DateField(blank=True, null=True)
    dtprevisao = models.DateField(blank=True, null=True)
    vlrmediachuva = models.FloatField(blank=True, null=True)
    dthcargaarquivo = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_chuvaprevista_ecmwf'


class Teste(models.Model):
    teste = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teste'
class TbProdutibilidade(models.Model):
    
    idprodutibilidade = models.BigIntegerField()
    codposto = models.BigIntegerField()
    nomeposto = models.CharField(max_length=50, blank=True, null=True)
    vlrvazao = models.CharField(max_length=50, blank=True, null=True)
    dtreferencia =  models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_ena_produtibilidade'

class TbEnaRegra(models.Model):
    
    idregra = models.BigIntegerField()
    codposto = models.BigIntegerField()
    mes = models.BigIntegerField()
    formula = models.CharField(max_length=300, blank=True, null=True)
    dtreferencia =  models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_ena_regra'
