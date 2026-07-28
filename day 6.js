function changeText(){
    document.getElementById("title").innerHTML = "Welcome Adeel";
    document.getElementById("title").style.color = "red";
}
console.log("program start")
setTimeout(function() {
    console.log("2 second baad ye print ho");
}, 2000);
console.log("Ye turant print hoga");
async function getData(){
    let result = await fetch("https://jsonplaceholder.typicode.com/users");
    let data= await result.json();
    console.log(data);
}

getData();