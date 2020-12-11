let url = 'http://127.0.0.1:8000/api/v1/search/';

let form = document.querySelector('.sell-this-form');

let data = {
}

let sendRequest = (data) => {
    let csrf = document.querySelector('[name=csrfmiddlewaretoken]').value;
    fetch(url, {
        method: "POST",
        headers: {
            "Content-type": "application/json",
            'X-CSRFToken': csrf,
        },
        body: JSON.stringify(data)
    }).then(response => response.json())
    .then(data => {
        
        
            if (data.length == 0) {
                document.querySelector('.product-listt').innerHTML = `
                    <h1 class="ml-5">Nothing Found</h1>
                `
            }
            else{
                document.querySelector('#choose-here').innerHTML = ""
                data.forEach(e => {
                    // console.log(e)
                    console.log(e.url)
                document.querySelector('#choose-here').innerHTML += `
                <a href="/sell_it/${e.slug}" style="color: black;"><div class="mt-3 pb-3" style="border-bottom: 2px solid #e5e7ea; width: 500px; margin: 0 auto;">
                <div style="display: flex;">
                <img style="width: 100px;" src="${e.image}" alt="">  
                <p class="pl-3">${e.title}</p>
                </div>
                <p style="margin-top: -45px; margin-left: -230px; color: #999;">${e.made_for}</p>
            </div></a>
                `
                });
            }
            
          
    })
}

form.addEventListener('keyup', function(e){
    // e.preventDefault();
    let title = document.querySelector('#site-search').value;
    
    data.title = title
    
    console.log(data.title)
    
    sendRequest(data)
})