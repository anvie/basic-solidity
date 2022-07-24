#!/usr/bin/python3

from datetime import datetime, timezone

from consts import *
from helpers import get_mint_sig_with_nonce

import pytest
import brownie

def test_owner_admin($name_snake_case$, owner, admin):
    assert $name_snake_case$.owner() == owner
    assert $name_snake_case$.admin() == admin

def test_renounce_works($name_snake_case$, accounts, owner):
    $name_snake_case$.renounceOwnership()
    assert $name_snake_case$.owner() == ZERO_ADDRESS

    # owner no longer has the access
    with brownie.reverts("Ownable: caller is not the owner"):
        $name_snake_case$.transferOwnership(accounts[3], {"from": owner})

# def test_interface_supports($name_snake_case$):
    # assert $name_snake_case$.supportsInterface("0x780e9d63") == True # ERC-165 - Enumerable
    # assert $name_snake_case$.supportsInterface("0x5b5e139f") == True # ERC-165 - Metadata
    # assert $name_snake_case$.supportsInterface("0x80ac58cd") == True # ERC-721
    # assert $name_snake_case$.supportsInterface("0xffffffff") == False

