from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker('pt_BR')  # Gera dados realistas br

# Gerar dados para a tabela 'gastos'
def gerar_gastos(n=20) -> int:
    categorias = ['Alimentação', 'Transporte', 'Educação', 'Lazer', 'Saúde', 'Moradia']
    formas_pagamento = ['Dinheiro', 'Cartão de Crédito', 'Cartão de Débito', 'Pix', 'Boleto']
    for _ in range(n):
        data = fake.date_between(start_date='-1y', end_date='today')
        categoria = random.choice(categorias)
        valor = round(random.uniform(10, 2000), 2)
        forma_pagamento = random.choice(formas_pagamento)
        print(f"INSERT INTO gastos (data, categoria, descricao, valor, forma_pagamento) VALUES ('{data}', '{categoria}', {valor}, '{forma_pagamento}');")

# Gerar dados para a tabela 'investimentos'
def gerar_investimentos(n=20) -> int:
    tipos = ['CDB', 'Tesouro Direto', 'Ações', 'Fundo Imobiliário', 'Criptomoeda']
    instituicoes = ['Nubank', 'XP Investimentos', 'Rico', 'Banco Inter', 'BTG Pactual']
    for _ in range(n):
        data = fake.date_between(start_date='-2y', end_date='today')
        tipo = random.choice(tipos)
        instituicao = random.choice(instituicoes)
        valor_aplicado = round(random.uniform(1000, 50000), 2)
        valor_atual = round(valor_aplicado * random.uniform(0.8, 1.5), 2)
        rentabilidade = round(((valor_atual - valor_aplicado) / valor_aplicado) * 100, 2)
        print(f"INSERT INTO investimentos (data, tipo, instituicao, valor_aplicado, valor_atual, rentabilidade_percentual) VALUES ('{data}', '{tipo}', '{instituicao}', {valor_aplicado}, {valor_atual}, {rentabilidade});")

# Gerar dados para a tabela 'metas'
def gerar_metas(n=20) -> int:
    nomes = ['Viagem', 'Compra de Carro', 'Reserva de Emergência', 'Curso', 'Reforma da Casa']
    for _ in range(n):
        nome = random.choice(nomes)
        valor_necessario = round(random.uniform(5000, 100000), 2)
        valor_atual = round(random.uniform(0, valor_necessario), 2)
        data_limite = fake.date_between(start_date='today', end_date='+2y')
        print(f"INSERT INTO metas (nome_meta, descricao, valor_necessario, valor_atual, data_limite) VALUES ('{nome}', {valor_necessario}, {valor_atual}, '{data_limite}');")

#padraox: n= 20
x = gerar_gastos()
y = gerar_investimentos()
z = gerar_metas()
