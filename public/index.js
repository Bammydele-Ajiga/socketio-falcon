const sio = io();
sio.on("connect",()=>{
console.log("connecteds")
function pro() {sio.emit("progress",{id :"bams"},(result) =>{
console.log(result)
} )}
});
sio.on("disconnect",()=>{
console.log("disconnected")

});
//sio.on("mult",(data,cb) =>{
//const result = data.numbers[0] * data.numbers[1];
//cb(result);
//});
function pro(){
        var id = document.getElementById('id').value
        sio.emit("progress",{id :id},(result) =>{
        console.log(result)
        } )
        }

//sio.on("sum_result", (data) =>{
//console.log(data)
//})


