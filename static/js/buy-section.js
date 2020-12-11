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
let slug_title = document.querySelector("#title-with-slug");
let slug = slug_title.getAttribute("ss")

change_color.forEach( i => {
    i.addEventListener('click', function(){
        this.classList.add('sell-back')
        change_color.forEach( i => {
            if( this != i){
                i.classList.remove('sell-back');
            }
        });
        if(this.classList.contains('sell')){
            document.querySelector('.changable').disabled=true;
            // document.querySelector('.button-inner').innerHTML = `
            // <button>Next</button>`
            document.querySelector('#right-button').innerHTML = `
            <a href="/for-buy/${slug}"><button style="min-width: 100px; padding: 12px 18px; background-color: rgb(8, 160, 92); color: rgb(255, 255, 255); border: 1px solid rgb(8, 160, 92);">Next</button></a>`
        }else{
            document.querySelector('.changable').disabled=false;
            document.querySelector('#right-button').innerHTML = `
            <input class="right-button" value="Next" type="submit" style="min-width: 100px; padding: 12px 18px; background-color: rgb(8, 160, 92); color: rgb(255, 255, 255); border: 1px solid rgb(8, 160, 92);">`
        }
    });

});
