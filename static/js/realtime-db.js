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

let productId = document.querySelector('.header').dataset.product_id;
var database = firebase.database().ref(`${productId}`)
console.log(database);
let price = document.querySelector('#last_price')
let least_price = document.querySelector('#least_price')

database.on('value', function (callback) {
    let dataa = callback.val();
    if (dataa) {
        if (dataa.sell_price) {
            least_price.innerHTML = `$${dataa.sell_price}`;
        }
        else {
            least_price.innerHTML = document.getElementById('current-price').innerText;
        };

        if (dataa.buy_price) {
            price.innerHTML = `$${dataa.buy_price}`;
        }
        else {
            price.innerHTML = document.getElementById('current-price').innerText;
        };
    };
});
