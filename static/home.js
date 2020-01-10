var changeHeading = function(e) {
  var h = document.getElementById("h");
  h.innerHTML = this.innerHTML;
  //console.log(h.innerHTML);
};

var removeItem = function(e) {
  this.remove();
}

var lis = document.getElementsByTagName("li");

for (var i = 0; i < lis.length; i++) {
  //console.log(lis[i]);
  //console.log("Length: " + lis.length);
  lis[i].addEventListener('mouseover', changeHeading);
  lis[i].addEventListener('mouseout', function(e) {document.getElementById("h").innerHTML = "Hello World!";});
  lis[i].addEventListener('click', removeItem);
}

var addItem = function(e) {
  var list = document.getElementById("thelist");
  var item = document.createElement("li");
  item.innerHTML = "WORD";
  item.addEventListener('mouseover', changeHeading);
  item.addEventListener('mouseout', function(e) {document.getElementById("h").innerHTML = "Hello World!";});
  item.addEventListener('click', removeItem);
  list.append(item);
}

var button = document.getElementById("b");
button.addEventListener('click', addItem);
