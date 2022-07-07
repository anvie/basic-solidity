#!/usr/bin/python3

from brownie import $name_pascal_case$, accounts, config, web3
import json

def main():
    print("config['wallets']['owner_key']", config['wallets']['owner_key'])
    owner = accounts.add(config['wallets']['owner_key'])
    admin = accounts.add(config['wallets']['admin_key'])

    print("Deploying $name$ contract...")
    print("using owner key:", owner.address)
    print("using admin key:", admin.address)
    print("current gas price:", web3.eth.gas_price, "wei")
    print("Are you sure? (y/n)")
    if input() != 'y':
        print("Aborted.")
        return

    contract = $name_pascal_case$.deploy(admin, {'from': owner})
    print("contract address:", contract.address)

    standard_json_input = $name_pascal_case$.get_verification_info()['standard_json_input']
    with open('$name_pascal_case$Flattened.json', 'w') as f:
      f.write(json.dumps(standard_json_input))
    print("$name_pascal_case$Flattened.json saved.")

