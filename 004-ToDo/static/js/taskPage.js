document.getElementById("circleButton").addEventListener("click", function() {
    document.getElementById("taskDone").submit();
  });


document.querySelectorAll("#circleButton").forEach(element => {
  if(element.value == "True"){
    element.style.backgroundColor = "#B31312";
  }
});

document.getElementById("dropdown").addEventListener("change", function() {
  
  var selectedOption = this.options[this.selectedIndex];
  if (selectedOption.value !== "") {
    var currentURL = window.location.href;
    currentURL = currentURL.split('?')[0]
    var selectedURL = currentURL + "?sort_by=" + selectedOption.value;
    window.location.href = selectedURL;
  }
});