var addFav = function(e) {
  //console.log(e);
  var n = document.getElementById("favorites");
  var fav = document.createElement("li");
  fav.innerHTML = e;
  fav.addEventListener('click', removeItem);
  n.append(fav);
}

var removeItem = function(e) {
  //console.log(this);
  addFav(this.innerHTML);
  this.remove();
}

var lis = document.getElementsByTagName("li");

for (var i = 0; i < lis.length; i++) {
  lis[i].addEventListener('click', removeItem);
}

var addItem = function(e) {
  var list = document.getElementById("thelist");
  var item = document.createElement("li");
  item.innerHTML = "WORD";
  item.addEventListener('click', removeItem);
  list.append(item);
}

var button = document.getElementById("b");
button.addEventListener('click', addItem);
