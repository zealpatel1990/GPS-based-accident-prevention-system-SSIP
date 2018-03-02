var rslider = document.getElementById("rRange");
var routput = document.getElementById("routvalue");
var gslider = document.getElementById("gRange");var goutput = document.getElementById("goutvalue");
var bslider = document.getElementById("bRange");var boutput = document.getElementById("boutvalue");
var rcolor=0,gcolor=0,bcolor=0;routput.innerHTML = rslider.value;rslider.oninput = function(){	routput.innerHTML = this.value;	rcolor = this.value;	document.getElementById("heading").style.color = "rgb("+rcolor.toString()+","+gcolor.toString()+","+bcolor.toString()+")";}
goutput.innerHTML = gslider.value;gslider.oninput = function(){	goutput.innerHTML = this.value;	gcolor = this.value;	document.getElementById("heading").style.color = "rgb("+rcolor.toString()+","+gcolor.toString()+","+bcolor.toString()+")";
}
boutput.innerHTML = bslider.value;
bslider.oninput = function(){
	boutput.innerHTML = this.value;
	bcolor = this.value;
	document.getElementById("heading").style.color = "rgb("+rcolor.toString()+","+gcolor.toString()+","+bcolor.toString()+")";
}

//---------------do-not-edit-down-below--------------------------------------------------/*var slider = document.getElementById("myRange");var output = document.getElementById("outvalue");output.innerHTML = slider.value;
slider.oninput = function() {  output.innerHTML = this.value;
}
//function mouseUp(){document.getElementById("myRange").value=50; document.getElementById("outvalue").innerHTML = document.getElementById("myRange").value;};
*/