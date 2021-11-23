const userList = document.getElementById('userList');

fetch('/db')
.then(res=>res.json())
.then(data=>{
	for (const key in data.username){
		const element = document.createElement('li');
		element.innerText = data.username[key];
		userList.appendChild(element);
	}
});