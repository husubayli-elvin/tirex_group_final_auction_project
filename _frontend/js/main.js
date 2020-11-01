// add border-bottom in buying and selling tabs
$(".active-tab").click(function(){
    $('.tab-border-bottom').not(this).removeClass('tab-border-bottom');
    $(this).toggleClass('tab-border-bottom');
 })