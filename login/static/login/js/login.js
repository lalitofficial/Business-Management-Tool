let email = document.querySelector("#email");

let password = document.querySelector("#password");

let error = document.getElementById("error");

let button = document.getElementById("submit").addEventListener("click",submit);


function submit() {
 
    emaildata = String(email.value);
  passworddata = String(password.value);
  
  if (emaildata == ""| passworddata == "") {
    error.textContent = "Please Add Login informations";
    
  }

}


