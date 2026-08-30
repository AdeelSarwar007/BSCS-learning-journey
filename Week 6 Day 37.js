let laptop = {
    add : function(a,b){
        return a+b;
    },
    sub : function (a,b){
        return a-b;
    },
    mul : function(a,b){
        return a*b;
    }
};
console.log(laptop.add(3,7));
console.log(laptop.sub(3,7));
console.log(laptop.mul(3,7));