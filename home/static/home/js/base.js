
$(document).ready(()=>{

    $("#nav_input").focusin(()=>{
        $("#nav_input_div").css("background-color","rgba(255, 255, 255, 0.842)")
        $("#nav_input").css("color","black")

    })

    $("#nav_input").focusout(()=>{
        $("#nav_input_div").css("background-color","rgba(255, 255, 255, 0.404)")
        $("#nav_input").css({"background-color":"rgba(255, 255, 255, 0)","color":"white"})
    })

    

    
})




// SHOW MENU
const showMenu = (toggleId, navbarId, bodyId) => {
    const toggle = document.getElementById(toggleId),
      navbar = document.getElementById(navbarId),
      bodypadding = document.getElementById(bodyId);
  
    if (toggle && navbar) {
      toggle.addEventListener("click", () => {
        // APARECER MENU
        navbar.classList.toggle("show");
        // ROTATE TOGGLE
        toggle.classList.toggle("rotate");
        // PADDING BODY
        bodypadding.classList.toggle("expander");
      });
    }
  };
  showMenu("nav-toggle", "navbar", "body");
  
  // Change active link when clicked

  const linkColor = document.querySelectorAll(".nav-link");
  function colorLink(){
    linkColor.forEach((l) =>{
      l.classList.remove("active")
    });
    this.classList.add("active");
  }
  
  linkColor.forEach((l) => l.addEventListener("click", colorLink));
  