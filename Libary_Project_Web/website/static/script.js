

function addbook_visibilty(status){
	document.getElementById("addbook_box").style.display = status;

	if(status === "block"){
		document.getElementById("body").style.overflow = "hidden";

		// Date Picker Max Date
		var date = new Date()
		var date_now = date.getFullYear() + '-' + String(parseInt(date.getMonth()) + 1).padStart(2,'0') + '-' + String(date.getDate()).padStart(2,'0')
		// document.getElementById("release_date").max = date_now
	}
	
	else{
		document.getElementById("body").style.overflow = "auto";
	}


}

function clear_data(){

	document.getElementsByClassName("insert-box").value = ""
}

function form_update(){
	

	var title = document.getElementById("book-title").innerHTML
	var volume = document.getElementById("book-volume").innerHTML
	var author = document.getElementById("book-author").innerHTML 
	var release_date = document.getElementById("book-release").innerHTML
	var placement = document.getElementById("book-placement").innerHTML 

	window.history.replaceState("content", volume,"?edit=True")

	console.log(title)

	document.getElementById("form-title").value = title
	document.getElementById("form-volume").value = parseInt(volume)
	document.getElementById("form-author").value = author
	document.getElementById("form-release").value = release_date
	document.getElementById("form-placement").value = placement

}
