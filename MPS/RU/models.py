from django.db import models

# Create your models here.

SEXO_CHOICES = [
        ("F", "FEMININO"),
        ("M", "MASCULINO"),
        ("N", "NENHUMA DAS OPCOES")
]


class Cadastro(models.Model):
    STATUS = [('A', 'ATIVO'),
              ('D', 'DESATIVADO'),
              ('P', 'PENDENTE')]

    dataCadastro = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS, blank=False, null=False)


class CorpoAcad(models.Model):
    matricula = models.CharField(max_length=10, blank=False, null=False, unique=True)
    nome = models.CharField(max_length=100, default='Sem Nome', blank=False, null=False)
    dtNascimento = models.DateField(auto_now=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=False)
    cadastro = models.ForeignKey(Cadastro, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Admin(models.Model):
    nome = models.CharField(max_length=100, default='Sem Nome', blank=False, null=False)
    dtNascimento = models.DateField(auto_now=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=False)

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    DINHEIRO = 'DN'
    DEBITO = 'DB'
    CREDITO = 'CR'
    FORMA_PAG = [(DINHEIRO, 'DINHEIRO'),
                 (DEBITO, 'DEBITO'),
                 (CREDITO, 'CREDITO')]

    horario = models.DateTimeField(auto_now=True)
    formaPag = models.CharField(max_length=2, choices=FORMA_PAG, default=DINHEIRO)
    corpoAcad = models.ForeignKey(CorpoAcad, on_delete=models.CASCADE)

    def __str__(self):
        return 'pedido: ' + str(self.pk)


class Prato(models.Model):
    nome = models.CharField(max_length=100, default='Sem Nome', blank=False, null=False)
    valor = models.CharField(max_length=4, default='0.00', blank=False, null=False)
    desc = models.CharField(max_length=1000, default='Sem desc.', blank=False, null=False)

    def __str__(self):
        return self.nome


class Cardapio(models.Model):
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

    tipoRefeicao = models.CharField(max_length=2, choices=REFEICOES, default='NAO SELECIONADO')
    horarioRefeicao = models.DateTimeField(auto_now=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    prato = models.ManyToManyField(Prato)

    def __str__(self):
        return 'cardapio: ' + str(self.pk)

