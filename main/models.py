from django.db import models

TYP_ACCOUNT = (('c','Carteira'),('cc','Conta Corrente'),('p','Poupança'))
TYP_RECEITA = (('s','salário'),('p', 'prêmio,'),('o','outros') )
TYP_DESPESA = (('a','alimentação'),('e', 'educação'),('l', 'lazer'), ('m','moradia'),('r', 'roupa'),
                ('s', 'saúde'),('t', 'transporte'),('o', 'outros'))

class Conta(models.Model):
    titular = models.CharField(max_length=50, blank=True)
    saldo = models.DecimalField(max_digits = 18, decimal_places = 2,default= 0.00)
    typ_account = models.CharField(max_length = 2, choices = TYP_ACCOUNT,)
    inst_finaceira = models.CharField(max_length = 30)

    def __str__(self):
        return (self.titular) +' '+ (self.inst_finaceira)

class Receitas(models.Model):
    valor = models.DecimalField(max_digits = 18, decimal_places = 2)
    dRecebimento = models.DateField()
    dRe_Esperado = models.DateField()
    desc = models.TextField()
    conta = models.ForeignKey(Conta, on_delete = models.CASCADE, related_name = 'R_conta')
    typ_receita = models.CharField(max_length = 1, choices = TYP_RECEITA,default='s')

    
class Despesas(models.Model):
     valor = models.DecimalField(max_digits = 18, decimal_places = 2)
     dPagamento = models.DateField()
     dPa_Esperado = models.DateField()
     desc = models.TextField()
     conta = models.ForeignKey(Conta, on_delete = models.CASCADE, related_name = 'D_conta')
     typ_despesa = models.CharField(max_length = 2, choices = TYP_DESPESA)