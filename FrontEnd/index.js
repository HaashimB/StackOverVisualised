
let url = 'http://127.0.0.1:8000/stack/post/';
let xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState === 4 && this.status === 200) {
       // Typical action to be performed when the document is ready:
       document.getElementById("root").innerHTML = xhttp.responseText;
    }
};
xhttp.open("GET", url, true ,'headers: no-cors');
xhttp.send();
