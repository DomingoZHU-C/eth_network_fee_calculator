#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
import requests


def get_latest_gas_price():
    url = 'https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=YourApiKeyToken'
    r = requests.get(url)
    result = r.json()
    try:
        safe_price = result['result']['SafeGasPrice']
        propose_price = result['result']['ProposeGasPrice']
        fast_price = result['result']['FastGasPrice']
    except Exception as e:
        print(e)
    return int(safe_price), int(propose_price), int(fast_price)


def network_fee(price, limit):
    fee = price * limit * 0.000000001
    return fee


eth_gas_limit = 21000
erc20_gas_limit = 200000
print('Check if connected with vpn and wait for a while')
try:
    safe, propose, fast = get_latest_gas_price()
except Exception as e:
    print('API exceed max limit, try again later' + e)

result_erc20_safe = network_fee(safe, erc20_gas_limit)
result_eth_safe = network_fee(safe, eth_gas_limit)
result_erc20_proposed = network_fee(propose, erc20_gas_limit)
result_eth_proposed = network_fee(propose, eth_gas_limit)
result_erc20_fast = network_fee(fast, erc20_gas_limit)
result_eth_fast = network_fee(fast, eth_gas_limit)

print("Current gas price is " + str(safe) + "/" + str(propose) + "/" + str(fast))
print("Current safe ERC-20/ETH network fee is " + '{:.8f}'.format(result_erc20_safe) + '/' + '{:.8f}'.format(result_eth_safe))
print("Current proposed ERC-20/ETH network fee is " + '{:.8f}'.format(result_erc20_proposed) + '/' + '{:.8f}'.format(result_eth_proposed))
print("Current fast ERC-20/ETH network fee is " + '{:.8f}'.format(result_erc20_fast) + '/' + '{:.8f}'.format(result_eth_fast))
