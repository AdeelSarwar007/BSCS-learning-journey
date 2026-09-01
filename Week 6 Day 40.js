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
function add(name, age, city){

    students.push({

        name: name,
        age: age,
        city: city

    });

}

function show(){
    students.forEach(function(student){
        console.log("Name:", student.name);
        console.log("Age:", student.age);
        console.log("City:", student.city);
            console.log("----------------");

    });

}
add("Ahmed", 20, "Karachi");
add("Usman","23","Islamabad");

show();
console.log("Total student : " + students.length);
