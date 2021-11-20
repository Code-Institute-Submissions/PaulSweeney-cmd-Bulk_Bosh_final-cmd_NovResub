const nav = document.getElementsByName(".sidenav");

const button = document.querySelector("#ing-btn");
const form = document.getElementsById("#ingredients-form:last");


$(document).ready(function(){
  nav.sidenav();
    
// cloning the ingredient html fields
    button.addEventListener("click", function() {
      form.clone().appendTo("#more_ingredients").find("input[type='text']").val("");
    });
});

