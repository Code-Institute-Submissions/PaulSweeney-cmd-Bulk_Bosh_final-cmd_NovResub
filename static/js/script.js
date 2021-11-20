// $(document).ready(function(){
//     $('.sidenav').sidenav();
    
// // cloning the ingredient html fields
//     $("body").on("click", "#ing-btn", function() {
//       $("#ingredients-form:last").clone().appendTo("#more_ingredients").find("input[type='text']").val("");
//     });
// });

const siteBody = document.querySelector("body");
const button = document.querySelector("#ing-btn");
const form = document.querySelector("#ingredients-form:last");
const more = document.querySelector("#more_ingredients");
const doc = document.querySelector(document);
const side = document.querySelector(".sidenav");

doc.ready(function(){
  side.sidenav();

  siteBody.addEventListener("click", button, function(event) {
    form.clone().appendTo(more).find("input[type='text']").val("");
    });
});