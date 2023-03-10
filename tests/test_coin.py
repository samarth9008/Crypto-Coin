import pytest
from brownie import Coin, accounts, reverts


@pytest.fixture
def contract(scope="module"):
    return Coin.deploy({
        "from": accounts[0],
        "gas_price": "60 gwei"
    })


def test_minter_getter(contract):
    assert contract.minter() == accounts[0]

def test_balance_getter(contract):
    assert contract.balance(accounts[0]) == 0

def test_mint_set_balance(contract):
    contract.mint(accounts[0], 10000, {"from": accounts[0],  "gas_price": "60 gwei"})
    contract.mint(accounts[1], 5000, {"from": accounts[0],  "gas_price": "60 gwei"})
    assert contract.balance(accounts[0]) == 10000
    assert contract.balance(accounts[1]) == 5000

def test_send_set_balance(contract):
    contract.mint(accounts[0], 10000, {"from": accounts[0],  "gas_price": "60 gwei"})
    contract.send(accounts[1], 1000, {"from": accounts[0],  "gas_price": "60 gwei"})
    assert contract.balance(accounts[0]) == 9000
    assert contract.balance(accounts[1]) == 1000

def test_send_fail_revert(contract):
    with reverts():
        contract.send(accounts[1], 1000, {"from": accounts[0],  "gas_price": "60 gwei"})

    contract.mint(accounts[0], 10000, {"from": accounts[0],  "gas_price": "60 gwei"})

    with reverts():
        contract.send(accounts[1], 11000, {"from": accounts[0],  "gas_price": "60 gwei"})


def test_sent_event_emitted(contract):
    contract.mint(accounts[0], 10000, {"from": accounts[0],  "gas_price": "60 gwei"})
    tx = contract.send(accounts[1], 1000, {"from": accounts[0],  "gas_price": "60 gwei"})

    assert "Sent" in tx.events
    assert tx.events.count("Sent") == 1

def test_mint_will_fail(contract):
    with reverts():
        contract.mint(accounts[0], 10000, {"from": accounts[6],  "gas_price": "60 gwei"})

