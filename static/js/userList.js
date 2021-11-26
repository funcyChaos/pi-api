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

function addUser(e){
	e.preventDefault();
	const username = document.getElementById('username-box').value;
	const password = document.getElementById('password-box').value;

	let data = {'username':username,'password':password};

	console.log(username, password);

	fetch('/users/newuser', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(data)
	})
	.then(()=>{
		fetch('/db')
		.then(res=>res.json())
		.then(data=>{
			const element = document.createElement('li');
			element.innerText = data.username[data.username.length - 1];
			userList.appendChild(element);
		});
	});

}