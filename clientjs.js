// var exampleSocket = new WebSocket("ws://0a22ec06.ngrok.io");
var exampleSocket = new WebSocket("ws://localhost:4040");

exampleSocket.onopen = function (event) {
    // exampleSocket.send("titid"); 
    console.log("Connection Established Pepeg", event)
};

exampleSocket.onclose = function (event) {
    console.log("Connection Closed", event)
};

function close_conn(){
    exampleSocket.close(1000,'closing')
}

function sendText(msg) {
    exampleSocket.send(msg);
}

exampleSocket.onmessage = function (event) {
    console.log("GOT DATA")
    console.log(event.data);
}