/*
Bronson Schultz, 11231230, bcs269
CMPT 350 Assignment 3, javascript
*/

const prompt = require("prompt");
const express = require('express');
const bodyParser = require('body-parser');
var app = express();

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
var port = process.env.PORT || 3000;
const router = express.Router();
router.get('/', function(req, res) {
  res.json({message: 'API in Online!'});
});

console.log("Hello World");

/**
 * chatRoom object allowing users to communicate and save
 * conversation
 */
class ChatRoom {
  constructor() {
      this.numUsers = 0;
      this.logger = null;
  }


/**
 * return current number of users in the chatroom
 * @return {int} numUsers
 */
 getNumUsers() {
    return this.numUsers;
  }


/**
 * set current users in chatroom
 * @param {int} i the new value for numUsers
 */
 setNumUsers(i) {
    this.numUsers = i;
  }


/**
 * prompt the user for new message
 * @throws will throw error if error occurs asking for prompt
 *
 */

  askForMessage() {
    prompt.start();
    prompt.get(['message'], function (err, result){

    if (err) {
        return console.log(err);
    }

    var d = new Date().toString().substring(16,21);

    console.log(d + " > " + result.message);
    return result.message;
    });
  }



}


let c = new ChatRoom();
console.log(c.getNumUsers());


app.use('/', router);
app.listen(port);
console.log('server online at: ' + port);

console.log(c.askForMessage());
