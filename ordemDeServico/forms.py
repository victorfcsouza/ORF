from django.forms import Form, ModelForm, CheckboxSelectMultiple, ChoiceField
from .models import OrdemDeServico, Sistema, Subsistemas, TIPO_CHOICES, CLASSE_CHOICES

class Tipo(Form):
    tipo = ChoiceField(label='Tipo', choices=TIPO_CHOICES)

    def __init__(self,*args,**kwargs):
        classe = kwargs.pop('classe')
        super(Tipo,self).__init__(*args,**kwargs)
        new_list = []
        if classe:
            for entry in classe:
                new_list.append(CLASSE_CHOICES[entry['classe']])
            self.fields['classe'] = ChoiceField(label='Classe', choices=new_list)

class OrdemServicoDireto(ModelForm):
    class Meta:
        model = OrdemDeServico

        #Direto
        fields = ['realizacao_date',
        'tempo',
        'pit',
        'motivo',
        'desc_material',
        'quantidade',
        'serv_realizado',
        'suprimento_aplicado',
        'custo_total',
        'om_requerente',
        'quant_homens',
        'sistema',
        'subsistemas_manutenidos']

        labels = {
            'tempo':'Tempo (em horas)',
            'custo_total':'Custo Total (em R$)'
        }

        widgets = {
            'subsistemas_manutenidos': CheckboxSelectMultiple(),
        }


    def __init__(self,*args,**kwargs):
        classe = kwargs.pop('classe')
        super(OrdemServicoDireto,self).__init__(*args,**kwargs)
        if classe != 0:
            self.fields['sistema'].queryset = Sistema.objects.filter(classe=classe)
            self.fields['subsistemas_manutenidos'].queryset = Subsistemas.objects.filter(classe=classe)

class OrdemServicoSuprimento(ModelForm):
    class Meta:
        model = OrdemDeServico

        #Direto
        fields = ['realizacao_date',
        'pit',
        'motivo',
        'desc_material',
        'quantidade',
        'suprimento_aplicado',
        'custo_total',
        'om_requerente',
        'sistema']

        labels = {
            'tempo':'Tempo (em horas)',
            'custo_total':'Custo Total (em R$)'
        }

    def __init__(self,*args,**kwargs):
        classe = kwargs.pop('classe')
        super(OrdemServicoSuprimento,self).__init__(*args,**kwargs)
        if classe != 0:
            self.fields['sistema'].queryset = Sistema.objects.filter(classe=classe)
    
class OrdemServicoConjunto(ModelForm):
    class Meta:
        model = OrdemDeServico

        #Direto
        fields = ['om_requerente',
        'ordem_recolhimento',
        'guia_recolhimento',
        'num_diex',
        'pit',
        'nd',
        'motivo',
        'desc_material']

class ConsultaOrdemServico(ModelForm):
    class Meta:
        model = OrdemDeServico

        #Direto
        fields = ['id',
        'classe',
        'status',
        'om_requerente']

#class ConsultaOrdemServico(ModelForm):
#    class Meta:
#        model = OrdemDeServico
#
#        fields = ['falha']
