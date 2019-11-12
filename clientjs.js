var exampleSocket = new WebSocket("ws://localhost:6969");

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
    console.log(event.data);
}