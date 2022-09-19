import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACcea7a416af347dff0dbd03edd435c366"
# Your Auth Token from twilio.com/console
auth_token  = "d6e593edec80658fc5353b148dbfaa7c"
client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas =  tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes} o/a vendedor {vendedor} bateu a meta com {vendas} reais em vendas')
        message = client.messages.create(
            to="+5517981021804",
            from_="+19897350352",
            body=f'No mês de {mes} o/a vendedor {vendedor} bateu a meta com {vendas} reais em vendas')
        print(message.sid)


