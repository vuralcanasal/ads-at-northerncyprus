function goHome(){
	window.location.replace("/ads-at-northerncyprus/index.py");
}

function goRegistration(){
	window.location.replace("/ads-at-northerncyprus/pages/registration.py");
}

function goLogin(){
	window.location.replace("/ads-at-northerncyprus/pages/login.html");
}

function goLogoutControl(){
	window.location.replace("/ads-at-northerncyprus/control/logoutControl.py");
}

function goOperationPage(){
	window.location.replace("/ads-at-northerncyprus/pages/operation.py");
}

function createAdv(){
	window.location.replace("/ads-at-northerncyprus/pages/createAdv.py");
}

function listAdv(){
	window.location.replace("/ads-at-northerncyprus/pages/listAdv.py");
}

function checkusername(str)
{
	if(str.length == 0){
		document.getElementById("checker").innerHTML = ""
	}
	else{
		var xmlhttp = new XMLHttpRequest();
		xmlhttp.onreadystatechange = function(){
			if (this.readyState == 4  && this.status == 200){
				document.getElementById("checker").innerHTML = this.responseText;
			}
			
		}
		
		xmlhttp.open("GET", "/ads-at-northerncyprus/control/checkusername.py?q=" + str, true);
		xmlhttp.send();
	}
}