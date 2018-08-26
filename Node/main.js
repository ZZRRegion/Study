var dgram = require("dgram");
var server = dgram.createSocket("udp4");
var hmis = new Set();
server.on("close", ()=>{
    console.log("已关闭");
});
server.on("error", (err)=>{
    console.log(err);
});
server.on("listening", ()=>{
    console.log("正在监听中...");
    server.setBroadcast(true);
    server.setTTL(128);
});
server.on("message", (msg, rinfo)=>{
    var content = msg.toString();
    if(!hmis.has(content)){
        hmis.add(content);
    }
    console.log(hmis.size);
});
server.bind("8060", "192.168.200.221");
function mySend(){
    server.send("haiwell scada", "3366", "255.255.255.255");
}
setInterval(mySend, 1000);