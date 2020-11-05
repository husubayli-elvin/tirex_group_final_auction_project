
let size = document.querySelectorAll('.dropdown-item')

size.forEach((i) => {
    
    i.addEventListener('click', (e)=>{
        let value = e.target.innerText;
        console.log(value);
        document.querySelector('.dropdown-toggle').innerText = value;
    });

});


