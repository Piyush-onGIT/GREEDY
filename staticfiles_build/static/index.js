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

function openEnrollForm(course) {
	document.getElementById("myForm1").style.display = "none";
	document.getElementById("myForm2").style.display = "none";

	document.getElementById("courseName").value = course;
	document.getElementById("enroll").style.display = "none";
	document.getElementById("enroll").style.display = "block";
	document.getElementById("mycontainer").style.filter = "blur(5px)";
}

function closeEnrollForm() {
	document.getElementById("enroll").style.display = "none";
  	document.getElementById("mycontainer").style.filter = "blur(0)";
}
const btnE1 = document.querySelector(".mybtn");
const closeIconE1 = document.querySelector(".close-icon");
const trailerContainerE1 = document.querySelector(".trailercontainer");
const ContainerE1 = document.querySelector(".container1");
const ContainerE2 = document.querySelector(".container2");
const ContainerE3 = document.querySelector(".container3");
const ContainerE4 = document.querySelector(".container4");
const ContainerE5 = document.querySelector(".container5");
btnE1.addEventListener("click", () => {
	trailerContainerE1.classList.remove("active");

	ContainerE1.classList.add("active2");
	ContainerE2.classList.add("active2");
	ContainerE3.classList.add("active2");
	ContainerE4.classList.add("active2");
	ContainerE5.classList.add("active2");
});
const videos = document.querySelectorAll('iframe')


closeIconE1.addEventListener('click', () => {
	videos.forEach(i => {
		const source = i.src
		i.src = ''
		i.src = source
	})
});
closeIconE1.addEventListener("click", () => {
	trailerContainerE1.classList.add("active");

	ContainerE1.classList.remove("active2");
	ContainerE2.classList.remove("active2");
	ContainerE3.classList.remove("active2");
	ContainerE4.classList.remove("active2");
	ContainerE5.classList.remove("active2");

});
// slider
		