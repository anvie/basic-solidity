// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

/**
 *
 *
 * $name$ by $param.author_name$
 *
 * $param.description$
 *
 */
import "@openzeppelin/contracts/access/Ownable.sol";
import "./HasAdmin.sol";
import "./SigVerifier.sol";

contract $name_pascal_case$ is Ownable, HasAdmin, SigVerifier {

    constructor(address admin){
        _setAdmin(admin);
    }

    function changeAdmin(address newAdmin) external onlyOwner {
        _setAdmin(newAdmin);
    }
}
