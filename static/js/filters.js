let url = 'http://127.0.0.1:8000/api/v1/search/';

let form = document.querySelector('.search-form');

let data = {
    'title': '',
    'category': ''
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
        console.log(data)
            if (data.length == 0) {
                document.querySelector('.product-listt').innerHTML = `
                    <h1 class="ml-5">Nothing Found</h1>
                `
            }
            else{
                document.querySelector('.product-listt').innerHTML = ""
                data.forEach(e => {
                    console.log(e)
                document.querySelector('.product-listt').innerHTML += `
                <div class="col-sm-3 col-6 p-3 p-sm-4 p-xl-5">
                     <div class="most-cards pl-1 pr-1 pt-1 pb-2">
                        <img class="most-images" src="${e.image}" alt="">
                         <p class="mt-2">${e.title}</p>
                        <h5>$${e.current_price}</h5>
                        <small>1918 Sold</small>
                    </div>
                
                </div>
                `
                });
            }
            
          
    })
}

form.addEventListener('submit', function(e){
    e.preventDefault();
    let title = document.querySelector('.single-input').value;
    
    data.title = title
    
    
    console.log(data.title)

    sendRequest(data)
})




document.querySelector("#sneakers-filter").addEventListener('click', () => {
    let sneaker_category = 'Sneakers'

    data.category = sneaker_category
    
    // data.title = ''

    data.category = sneaker_category

    console.log(data.category)

    sendRequest(data)

    document.querySelector(".browse-header").innerText = "Sneakers"

    document.querySelector(".sneaker-red").style.color = '#ff5a5f'

    document.querySelector(".streetwear-red").style.color = 'black'
})

document.querySelector('#streetwear-filter').addEventListener('click', () => {
    let wear_category = 'Wear'

    data.category = wear_category

    // data.title = ''

    console.log(data.category)

    sendRequest(data)

    document.querySelector(".browse-header").innerText = "Streetwear"

    document.querySelector(".sneaker-red").style.color = 'black'

    document.querySelector(".streetwear-red").style.color = '#ff5a5f'
})