// add border-bottom in buying and selling tabs
$(".active-tab").click(function(){
    $('.tab-border-bottom').not(this).removeClass('tab-border-bottom');
    $(this).toggleClass('tab-border-bottom');
 });


//make table sortable

$(document).ready(function () {
    $('#buying-table').DataTable({
        searching: false,
        paging: false,
        info: false,
        "language": {
            "emptyTable": "No Results"
          }
        });
    });


$(document).ready(function () {
    $('#follow-table').DataTable({
        searching: false,
        paging: false,
        info: false,
        "language": {
            "emptyTable": "Your Follow List is empty. We can't even really call it a \"List\" yet because there isn't anything LISTED"
        }
        });
    });


$(document).ready(function () {
    $('#portfolio-table').DataTable({
        searching: false,
        paging: false,
        info: false,
        "language": {
            "emptyTable": " "
        }
        });
    });



new Chart(document.getElementById("pie-chart"), {
    type: 'pie',
    data: {
        datasets: [{
        backgroundColor: ["#gray", "#bababa"],
        data: [90,10]
        }]
    },
    options: {
        title: {
        display: true,
        text: 'ITEM COUNT'
        }
    }
});

new Chart(document.getElementById("pie-chart2"), {
    type: 'pie',
    data: {
        datasets: [{
        backgroundColor: ["#gray", "#bababa"],
        data: [90,10]
        }]
    },
    options: {
        title: {
        display: true,
        text: 'MARKET VALUE'
        }
    }
});