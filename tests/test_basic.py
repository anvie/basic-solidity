#!/usr/bin/python3

from datetime import datetime, timezone

from consts import *
from helpers import get_mint_sig_with_nonce

import pytest
import brownie

def test_owner_admin(pjf, owner, admin):
    assert pjf.owner() == owner
    assert pjf.admin() == admin

def test_renounce_works(pjf, accounts, owner):
    pjf.renounceOwnership()
    assert pjf.owner() == ZERO_ADDRESS

    # owner no longer has the access
    with brownie.reverts("Ownable: caller is not the owner"):
        pjf.transferOwnership(accounts[3], {"from": owner})

# def test_interface_supports(pjf):
    # assert pjf.supportsInterface("0x780e9d63") == True # ERC-165 - Enumerable
    # assert pjf.supportsInterface("0x5b5e139f") == True # ERC-165 - Metadata
    # assert pjf.supportsInterface("0x80ac58cd") == True # ERC-721
    # assert pjf.supportsInterface("0xffffffff") == False

