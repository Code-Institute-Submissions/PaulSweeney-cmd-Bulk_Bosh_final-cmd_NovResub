$(document).ready(function(){
    $('.sidenav').sidenav();
    
// cloning the ingredient html fields
    $("body").on("click", "#ing-btn", function() {
      $("#ingredients-form:last").clone().appendTo("#more_ingredients").find("input[type='text']").val("");
    });
});