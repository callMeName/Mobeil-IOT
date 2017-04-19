var http = require('http');

// Object accessing python subprocess of buzzler.
var python = null;
function stopPlay(){
    if(python != null) {
        python.kill();
        python = null;
    }
}

function startPlay(mode){
    python = require('child_process').spawn(
        'python',
        ["./passive_buzzer.py", mode]);
}

var express = require('express'); 
var app = express();
app.get('/play/:mode', function(req, res){
    var mode = req.params.mode;
    if(mode == null || (mode != "1" && mode!= "2" )) {
        res.end(404, "Bad Request!");
        return;
    }
    console.log(mode);
    stopPlay(); // stop playing first
    startPlay(mode);

    res.send(200, 'Start playing!');
});

app.get('/stop', function(req, res) {
    stopPlay();
    res.send(200, "Stop Playing");
});

require('http').createServer(app).listen(9999, function(){
  console.log('Listening on 9999');
});
