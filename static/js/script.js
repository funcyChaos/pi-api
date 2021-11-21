function ledActuate(state){
	fetch(`/led/${state}`);
}

fetch('/db')
.then(res=>res.json())
.then(data=>document.getElementById('username').innerHTML = data.username[0]);