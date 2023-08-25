from django.db import models

# Create your models here.

SEXO_CHOICES = [
    ('F', 'FEMININO'),
    ('M', 'MASCULINO'),
    ('N', 'NENHUMA DAS OPCOES')
]

STATUS = [
    ('A', 'ATIVO'),
    ('D', 'DESATIVADO'),
    ('P', 'PENDENTE'),
]

DINHEIRO = 'DN'
DEBITO = 'DB'
CREDITO = 'CR'
FORMA_PAG = [
    (DINHEIRO, 'DINHEIRO'),
    (DEBITO, 'DEBITO'),
    (CREDITO, 'CREDITO')
]

VERDURA = 'V'
FRUTA = 'F'
CARNE = 'C'
FRUTO_DO_MAR = 'M'
BEBIDA = 'B'
NENHUM = 'N'
TIPO_MATERIAL = [
    (VERDURA, 'VERDURA'),
    (FRUTA, 'FRUTA'),
    (CARNE, 'CARNE'),
    (FRUTO_DO_MAR, 'FRUTO_DO_MAR'),
    (BEBIDA, 'BEBIDA'),
    (NENHUM, 'NENHUM')
]

CAFE_MANHA = 'CM'
ALMOCO = 'AL'
MERENDA = 'MR'
JANTA = 'JT'

REFEICOES = [
    (CAFE_MANHA, 'CAFE_DA_MANHA'),
    (ALMOCO, 'ALMOCO'),
    (MERENDA, 'MERENDA'),
    (JANTA, 'JANTA')
]

class Cadastro(models.Model):

    dataCadastro = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS, blank=False, null=False)


class CorpoAcad(models.Model):
    matricula = models.CharField(max_length=10, blank=False, null=False, unique=True)
    nome = models.CharField(max_length=100, default='Sem Nome', blank=False, null=False)
    dtNascimento = models.DateField(auto_now=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, default='N', blank=False, null=False)
    cadastro = models.ForeignKey(Cadastro, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Admin(models.Model):
    nome = models.CharField(max_length=100, default='Sem Nome', blank=False, null=False)
    dtNascimento = models.DateField(auto_now=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=False)

    def __str__(self):
        return self.nome


class Feedback(models.Model):
    respondido = models.BooleanField()
    mensagem = models.TextField()
    resposta = models.TextField()

    def __str__(self):
        return 'feedback: ' + str(self.pk)

class Pedido(models.Model):
    diaCompra = models.DateField(auto_now=True)
    formaPag = models.CharField(max_length=2, choices=FORMA_PAG, default=DINHEIRO, blank=False, null=False)
    corpoAcad = models.ForeignKey(CorpoAcad, on_delete=models.CASCADE)
    prato = models.ManyToManyField('Prato')
    feedback = models.OneToOneField(Feedback, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return 'pedido: ' + str(self.pk)




class Prato(models.Model):
    nome = models.CharField(max_length=100, default='Sem Nome', blank=False, null=False)
    valor = models.CharField(max_length=4, default='0.00', blank=False, null=False)
    desc = models.TextField()

    def __str__(self):
        return self.nome

class Cardapio(models.Model):
    tipoRefeicao = models.CharField(max_length=2, choices=REFEICOES, default='NAO SELECIONADO', blank=False, null=False)
    diaRefeicao = models.DateField()
    prato = models.ManyToManyField(Prato)

    def __str__(self):
        return 'cardapio: ' + str(self.pk)

