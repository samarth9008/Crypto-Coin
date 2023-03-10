// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract Coin {
    address public minter;
    mapping(address=>uint) public balance;
    event Sent(address from, address to, uint256 amount);


    constructor() {
        minter = msg.sender;
    }

    function mint(address _reciever, uint _amount) public {
        require(msg.sender == minter);
        balance[_reciever] += _amount;
    }

    function send(address _reciever, uint _amount) public {

         require(balance[msg.sender] >= _amount);
         balance[msg.sender] -= _amount;
         balance[_reciever] += _amount;
         emit Sent(msg.sender, _reciever, _amount);
    }
}