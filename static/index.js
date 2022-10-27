function openForm1() {
    document.getElementById("myForm1").style.display = "block";
    document.getElementById("myForm2").style.display = "none";
    document.getElementById("mycontainer").style.filter = "blur(5px)";
  }
  
  function closeForm1() {
    document.getElementById("myForm1").style.display = "none";
    document.getElementById("mycontainer").style.filter = "blur(0)";
  }
  function openForm2() {
      document.getElementById("myForm1").style.display = "none";
    document.getElementById("myForm2").style.display = "block";
    document.getElementById("mycontainer").style.filter = "blur(5px)";
  }
  
  function closeForm2() {
    document.getElementById("myForm2").style.display = "none";
    document.getElementById("mycontainer").style.filter = "blur(0)";
  }