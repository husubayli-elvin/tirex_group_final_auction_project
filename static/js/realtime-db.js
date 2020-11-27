var firebaseConfig = {
    apiKey: "AIzaSyDGwmtmwlblsjqE5MWlMsvl0TZv2RXftgc",
    authDomain: "compass-b142f.firebaseapp.com",
    databaseURL: "https://compass-b142f.firebaseio.com",
    projectId: "compass-b142f",
    storageBucket: "compass-b142f.appspot.com",
    messagingSenderId: "735801639390",
    appId: "1:735801639390:web:2acf6d85adb29ac1e95d4f",
    measurementId: "G-9KPL66G3XK"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
firebase.analytics();

var database = firebase.database().ref()
let price = document.querySelector('#last_price')
let least_price = document.querySelector('#least_price')

let url = 'http://127.0.0.1:8000/api/v1/search/';

send_data = {}

let csrf = document.querySelector('[name=csrfmiddlewaretoken]').value;
fetch(url, {
    method: "POST",
    headers: {
        "Content-type": "application/json",
        'X-CSRFToken': csrf,
    },
    body: JSON.stringify(send_data)
}).then(response => response.json())
    .then(data => {
        console.log(data);
        data.forEach(e => {

            database.on('value', function (callback) {
                let dataa = callback.val()
                console.log(dataa.sell);
                for (let [k, v] of Object.entries(dataa.buy)) {
                    // console.log(k, v.id);
                    if (v.id == e.id) {
                        price.innerHTML = ` $${v.price}`
                    }

                }
                for (let [k, v] of Object.entries(dataa.sell)) {
                    console.log(k, v.id);
                    if (v.id == e.id) {
                        least_price.innerHTML = ` $${v.price}`
                    }

                }


            })

        })


    })







