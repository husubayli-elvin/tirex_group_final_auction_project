let input = document.querySelector(".form-control")
// console.log(input);
// console.log(input.length);
// if (input.length > 0) {
//     document.querySelector(".button").style.backgroundColor="black";
// }
// else{
//     document.querySelector(".button").style.backgroundColor="#c7c7c7";
// }
let form = document.querySelector(".form-login")
function check_input(input){
    console.log(input.value);
    console.log(input.length);
    
    if (input.value == "") {
        console.log(input.value)
        document.querySelector(".button").style.backgroundColor="green";
    }
    else{
        document.querySelector(".button").style.backgroundColor="gray";

    }
}



// form.addEventListener("submit", function(e){
//     e.preventDefault();
//     check_input(input);

// });


let change_color = document.querySelectorAll(".selection");




change_color.forEach( i => {
    i.addEventListener('click', function(){
        this.classList.add('back')
        change_color.forEach( i => {
            if( this != i){
                i.classList.remove('back');
            }
        });
        if(this.classList.contains('sell')){
            document.querySelector('.changable').disabled=true;
        }else{
            document.querySelector('.changable').disabled=false;
        }
    });

});
