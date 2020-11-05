let input = document.querySelector(".form-control")

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
