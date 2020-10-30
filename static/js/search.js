let url = 'http://127.0.0.1:8000/api/v1/search/';

let form = document.querySelector('.search-form');

form.addEventListener('submit', function(e){
    e.preventDefault();
    let title = document.querySelector('.single-input').value;
    let csrf = document.querySelector('[name=csrfmiddlewaretoken]').value;
    let data = {
        'title': title,
    }
    console.log(data.title)

    fetch(url, {
        method: "POST",
        headers: {
            "Content-type": "application/json",
            'X-CSRFToken': csrf,
        },
        body: JSON.stringify(data)
    }).then(response => response.json())
    .then(data => {
        console.log(data)
        for(var i=0; i<=data.length; i++) {
            console.log(data[i])
            document.querySelector('.product-listt').innerHTML = `
            <div class="col-sm-3 col-6 p-3 p-sm-4 p-xl-5">
                 <div class="most-cards pl-1 pr-1 pt-1 pb-2">
                    <img class="most-images" src="${data[i].image}" alt="">
                     <p class="mt-2">${data[i].title}</p>
                    <h5>${data[i].current_price}</h5>
                    <small>1918 Sold</small>
                </div>
            
            </div>
            `
        }
    })
})