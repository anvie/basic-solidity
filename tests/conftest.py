#!/usr/bin/python3

from brownie import config
import pytest


@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass

@pytest.fixture(scope="module")
def owner(accounts):
    # acc = accounts.add(config['wallets']['owner_key'])
    return accounts[0]

@pytest.fixture(scope="module")
def admin(accounts):
    # acc = accounts.add(config['wallets']['admin_key'])
    acc = accounts.add()
    accounts[1].transfer(acc.address, '30 ethers')
    return acc

@pytest.fixture(scope="module")
def pjf($name_pascal_case$, owner, admin):
    _pjf_contract = $name_pascal_case$.deploy(admin, {'from': owner})
    return _pjf_contract

