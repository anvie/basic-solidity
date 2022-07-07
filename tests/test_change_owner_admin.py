#!/usr/bin/python3

import pytest
import brownie


def test_change_owner(pjf, accounts, owner):
    pjf.transferOwnership(accounts[1], {"from": owner})
    assert pjf.owner() == accounts[1]

def test_change_admin(pjf, accounts, owner):
    pjf.changeAdmin(accounts[1], {"from": owner})
    assert pjf.admin() == accounts[1]

def test_only_owner_can_change_admin(pjf, accounts, owner):
    with brownie.reverts():
        pjf.changeAdmin(accounts[1], {"from": accounts[1]})
    
    pjf.changeAdmin(accounts[1], {"from": owner})

    # admin cannot change admin
    with brownie.reverts():
        pjf.changeAdmin(accounts[1], {"from": accounts[1]})

    pjf.transferOwnership(accounts[1], {"from": owner})
    pjf.changeAdmin(accounts[1], {"from": accounts[1]})

