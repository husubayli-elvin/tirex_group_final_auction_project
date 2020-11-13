let url = 'http://127.0.0.1:8000/api/v1/search/';

let form = document.querySelector('.search-form');

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
                document.querySelector('.product-listt').innerHTML = ""
                data.forEach(e => {
                    // console.log(e)
                    console.log(e.url)
                document.querySelector('.product-listt').innerHTML += `
                <div class="col-sm-3 col-6 p-3 p-sm-4 p-xl-5">
                     <div class="most-cards pl-1 pr-1 pt-1 pb-2">
                        <a href="${e.url}"><img class="most-images" src="${e.image}" alt=""></a>
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

    console.log(data.category)

    sendRequest(data)

    document.querySelector(".browse-header").innerText = "Sneakers"

    document.querySelector(".sneaker-red").style.color = '#ff5a5f'

    document.querySelector(".streetwear-red").style.color = 'black'
})

document.querySelector('#streetwear-filter').addEventListener('click', () => {
    let wear_category = 'Wear'

    data.category = wear_category

    console.log(data.category)

    sendRequest(data)

    document.querySelector(".browse-header").innerText = "Streetwear"

    document.querySelector(".sneaker-red").style.color = 'black'

    document.querySelector(".streetwear-red").style.color = '#ff5a5f'
})

document.querySelector('#adidas').addEventListener('click', () => {
    let adidas = 'Adidas'

    data.brand = adidas

    console.log(data.brand)

    sendRequest(data)

    document.querySelector(".addi-red").style.color = '#ff5a5f'
    document.querySelector(".jord-red").style.color = 'black'
    document.querySelector(".nike-red").style.color = 'black'
    document.querySelector(".essent-red").style.color = 'black'
})

document.querySelector('#jordan').addEventListener('click', () => {
    let jordan = 'Jordan'

    data.brand = jordan

    console.log(data.brand)

    sendRequest(data)

    document.querySelector(".jord-red").style.color = '#ff5a5f'
    document.querySelector(".addi-red").style.color = 'black'
    document.querySelector(".nike-red").style.color = 'black'
    document.querySelector(".essent-red").style.color = 'black'
})

document.querySelector('#nike').addEventListener('click', () => {
    let nike = 'Nike'

    data.brand = nike

    console.log(data.brand)

    sendRequest(data)

    document.querySelector(".nike-red").style.color = '#ff5a5f'
    document.querySelector(".jord-red").style.color = 'black'
    document.querySelector(".addi-red").style.color = 'black'
    document.querySelector(".essent-red").style.color = 'black'
})

document.querySelector('#essentials').addEventListener('click', () => {
    let essentials = 'Essentials'

    data.brand = essentials

    console.log(data.brand)

    sendRequest(data)

    document.querySelector(".essent-red").style.color = '#ff5a5f'
    document.querySelector(".jord-red").style.color = 'black'
    document.querySelector(".addi-red").style.color = 'black'
    document.querySelector(".nike-red").style.color = 'black'
})



let filterBySizeType = (element, type) => {
    if (element.checked == true) {
    
        data.size_type = type
    
        // console.log(data.size_type)
    
        sendRequest(data)
    }
    else {
    
        console.log(data.size_type)
    
        sendRequest(data)
    }
}

let men_cb = document.querySelector('#men-cb');

let size_types = []

let men = 'Men'

men_cb.addEventListener('click', () => {

    if(size_types.includes(men) == false){
        size_types.push(men)
    }
    else {
        men_index = size_types.indexOf(men)
        size_types.splice(men_index, 1)
        console.log(size_types)
    }
    filterBySizeType(men_cb, size_types)
    console.log(size_types)
})

let women_cb = document.querySelector('#women-cb');
let women = "Women"

women_cb.addEventListener('click', () => {
     if(size_types.includes(women) == false){
        size_types.push(women)
    }
    else {
        women_index = size_types.indexOf(women)
        size_types.splice(women_index, 1)
        console.log(size_types)
    }
    filterBySizeType(women_cb, size_types)
    console.log(size_types)
})

let child_cb = document.querySelector('#child-cb');

let child = 'Child'


child_cb.addEventListener('click', () => {
     if(size_types.includes(child) == false){
        size_types.push(child)
    }
    else {
        child_index = size_types.indexOf(child)
        size_types.splice(child_index, 1)
        console.log(size_types)
    }
    filterBySizeType(child_cb, size_types)
    console.log(size_types)
})


let filterByPrices = (type) => {
        data.price = type
    
        console.log(data.price)
    
        sendRequest(data)
}

let filterByYears = (type) => {
    data.years = type

    console.log(data.years)

    sendRequest(data)
}


let checkThePrice = () => {
let price_list_container = []
document.querySelectorAll('.browse-sidebar-checkbox-prices').forEach((e)=> {
    e.addEventListener('click',function() {
        let price_list = []
        start_price = this.getAttribute('startprice')
        end_price = this.getAttribute('endprice')
        price_list.push(start_price, end_price)

        if (this.checked){
            if (price_list.includes(this)==false){
                price_list_container.push(price_list)
            }
            else {
                console.log(e)
                price_index = price_list.indexOf(e)
                price_list.splice(price_index, 1)
            }
            
        }
        else {
            price_list_index = price_list.indexOf(e)
            price_list_container.splice(price_list_index, 1)
        }
        // price_list = getPriceRange(start_price, end_price)
        filterByPrices( price_list_container)
        // console.log(price_list_container)
   })
})
    
}

checkThePrice()


let checkReleaseYear = () => {
    let years_list = []
    document.querySelectorAll('.browse-sidebar-checkbox-year').forEach((e) => {
        e.addEventListener('click', function() {
        release_year = this.getAttribute('releaseyear')
            if (this.checked) {
                if (years_list.includes(release_year) == false){
                    years_list.push(release_year)
                }
                else {
                    years_index = years_list.indexOf(release_year)
                    years_list.splice(years_index, 1)
                }
            }
            else {
                years_index = years_list.indexOf(release_year)
                    years_list.splice(years_index, 1)
            }
            filterByYears(years_list)
        })
    })
}

checkReleaseYear()
