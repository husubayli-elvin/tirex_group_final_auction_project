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
        backgroundColor: ["#bebebe", '#d3d3d3'],
        data: [90,10],
        hoverBackgroundColor :['white', 'white']
        }]
    },
    options: {
        tooltips : {enabled: false},
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
        backgroundColor: ['#bebebe', '#d3d3d3'],
        data: [90,10],
        hoverBackgroundColor :['white', 'white']
        }]
    },
    options: {
        tooltips : {enabled: false},
        title: {
        display: true,
        text: 'MARKET VALUE'
        }
    }
});

new Chart(document.getElementById("bar-chart"), {
    type: 'bar',
    data: {
      datasets: [
        {
          data: [0, 20, 40, 80, 60, 100]
        }
      ]
    },
    options: {
      legend: { display: false },
      title: {
        display: true,
        text: 'RESELL PRICE PREMIUM'
      }
    }
});


new Chart(document.getElementById("bar-chart2"), {
    type: 'bar',
    data: {
      datasets: [
        {
          data: [0, 60, 100]
        }
      ]
    },
    options: {
      legend: { display: false },
      title: {
        display: true,
        text: 'AVERAGE PRICE'
      }
    }
});