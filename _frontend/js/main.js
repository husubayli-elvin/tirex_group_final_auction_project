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
