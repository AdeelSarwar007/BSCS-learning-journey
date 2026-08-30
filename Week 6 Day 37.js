let student = {

    name: "Adeel",
    age: 21,
    degree: "BSCS",

    showProfile: function(){

        console.log("Name:", this.name);
        console.log("Age:", this.age);
        console.log("Degree:", this.degree);

    }

};

student.showProfile();