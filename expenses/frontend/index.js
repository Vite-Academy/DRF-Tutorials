let root = document.querySelector("#root");

fetch("http://127.0.0.1:8000/")
      .then(response => response.json())
      .then(json => root.innerHTML = `Expenses name: ${json[0].name}, Expenses price: ${json[0].price}`)