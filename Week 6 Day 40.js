let students =[
    {
        name : "Adeel",
        age : 21,
        city : "Vehari"
    },
    {
        name : "Adil",
        age : 21,
        city : "Vehari"
    },
    {
        name : "Ali",
        age : 21,
        city : "Vehari"
    }
];
function show(){
    students.forEach(function(student){
        console.log("Name:", student.name);
        console.log("Age:", student.age);
        console.log("City:", student.city);
            console.log("----------------");

    });

}
show();