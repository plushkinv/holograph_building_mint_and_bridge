
#то что ниже обязательно заполнить своими данными
proxy_use = 1 #  0 - не использовать, 1 - прокси без ссылки , 2 - прокси со ссылкой для смены ip
proxy_login = 'pfdsfsdfff5456464'
proxy_password = '9c3dsadssssaa07'
proxy_address = 'node-de-65.astroproxy.com'
proxy_port = '10257'
proxy_changeIPlink = "http://node-de-65.astroproxy.com:10257/api/changeIP?apiToken=b17a9fe5cce3b204"


#то что ниже желательно настроить под себя
NFT_adress = "0x3b2d8bb062d121619acff4e01ece2690789e919f"
min_balance_4_main = 2 # Указывается в $,  минимальный баланс который должен быть на кошельке чтобы начать минтить и брижить. работает только для main.py 
# network4mint = ['avax', 'polygon', 'bsc', 'arbitrum', 'optimism']  # выберите сети, в одной из них будет случайно сминчена НФТ
network4mint = ['bsc', 'optimism']  # выберите сети, в одной из них будет случайно сминчена НФТ
network4bridge = ['avax', 'polygon', 'bsc', 'arbitrum', 'optimism']  # выберите сети, в одну из них будет будет отправлена НФТ через мост


#укажите паузу в работе между кошельками, минимальную и максимальную. 
#При смене каждого кошелька будет выбрано случайное число. Значения указываются в секундах
timeoutMin = 10 #минимальная 
timeoutMax = 30 #максимальная
#задержки между операциями в рамках одного кошелька
timeoutTehMin = 3 #минимальная 
timeoutTehMax = 10 #максимальная



#то что ниже можно менять только если понимаешь что делаешь
proxies = { 'all': f'http://{proxy_login}:{proxy_password}@{proxy_address}:{proxy_port}',}
if proxy_use:
    request_kwargs = {"proxies":proxies, "timeout": 120}
else:
    request_kwargs = {"timeout": 120}
gas_kef=1.5 #коэфициент допустимого расхода газа на подписание транзакций. можно выставлять от 1.3 до 2

rpc_links = {
    'polygon': 'https://polygon-rpc.com/',
    'arbitrum': 'https://arb1.arbitrum.io/rpc',
    'optimism':  'https://rpc.ankr.com/optimism',
    'bsc': 'https://bscrpc.com',
    'fantom': 'https://rpc.ftm.tools/',
    'avax': 'https://api.avax.network/ext/bc/C/rpc',
}

prices = {
    "MATIC": 0.645,
    "AVAX": 11.8,
    "BNB": 246,
    "ETH": 1900,
}

protocol_fee = {
'avax': 0.0081,
'polygon': 0.15,
'bsc': 0.00044,
'arbitrum': 0.000057,
'optimism': 0.000057
}

count_nfts = 1  # количество сколько хотите сминтить  !!!Не менять!