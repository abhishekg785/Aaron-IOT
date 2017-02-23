// sending the file using node request module
// cool stuff :)

var util = require('util');
var exec = require('child_process').exec;
var command = 'curl -XPOST "https://api.wit.ai/speech" -i -L -H "Authorization: Bearer ' + 'GVMQQM3B7DO2GLZDBUKEJ2A2XF4TP2IU' + '" -H "Content-Type: audio/wav" --data-binary "@output.wav"';

child = exec(command, function(error, stdout, stderr){

console.log('stdout: ' + stdout);
console.log('stderr: ' + stderr);

if(error !== null)
{
    console.log('exec error: ' + error);
}
});
