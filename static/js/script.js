const nav = document.querySelector(".sidenav");
const doc = document;

const hi = document.querySelector("body");
const button = document.getElementById("#ing-btn");
const form = document.querySelector("#ingredients-form:last");
const more = document.getElementById("#more_ingredients");

doc.ready(function() {
    nav.sidenav();
    
// cloning the ingredient html fields
    hi.on("click", button, function() {
      form.clone().appendTo(more).find("input[type='text']").val("");
    });
});