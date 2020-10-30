let input = document.querySelector(".form-control").value
// console.log(input);
// console.log(input.length);
// if (input.length > 0) {
//     document.querySelector(".button").style.backgroundColor="black";
// }
// else{
//     document.querySelector(".button").style.backgroundColor="#c7c7c7";
// }

function check_input(input){
    console.log(input);
    console.log(input.length);
    if (input.length > 0) {
        document.querySelector(".button").style.backgroundColor="black";
    }
    else{
        document.querySelector(".button").style.backgroundColor="#c7c7c7";
    }
}

check_input(input);