from brownie import SimpleStorage, Coin, accounts, config
from brownie.network import gas_price
from brownie.network.gas.strategies import LinearScalingStrategy

gas_strategy = LinearScalingStrategy("60 gwei", "70 gwei", 1.1)

gas_price(gas_strategy)

def main():
    admin = accounts[0]
    ss = SimpleStorage.deploy({
        "from": admin,
        "gas_price": gas_strategy
    })

    admin = accounts[0]
    c = Coin.deploy({
        "from": admin,
        "gas_price": gas_strategy
    })

    ss.set(7,{
        "from": admin,
        "gas_price": gas_strategy
    } )

    ss.get()

