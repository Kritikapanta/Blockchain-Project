pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/AccessControl.sol";

contract Evidence{

    //define struct for evidence
    struct EvidenceDetails{
        bytes32 evidenceHash;
        address uploadedBy;
        uint256 timestamp;
    }


}