/*
Bronson Schultz, 11231230, bcs269
CMPT 350 Assignment 3, javascript
*/

const prompt = require("prompt");
console.log("Hello World");

class ChatRoom {
  constructor() {
      this.numUsers = 0;
      this.logger = null;
  }

  getNumUsers() {
    return this.numUsers;
  }

  setNumUsers(i) {
    this.numUsers = i;
  }

}

let c = new ChatRoom();
console.log(c.getNumUsers());

prompt.start();
prompt.get(['users'], function (err, result){
  if (err) {return console.log(err); }
  console.log('Users' + result.users);
})
