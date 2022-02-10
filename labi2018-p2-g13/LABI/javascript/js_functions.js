//function to tell the server to do a upvote
function upVote(x){
    $.post("/like","id="+x,function(response){
    });
    
}

//function to tell the server to do a downvote
function downVote(x){
    $.post("/dislike","id="+x,function(response){
    });
    
}


// sends file to server
function sendFile(file) {
	var data =new FormData();
	data.append("myFile", file);
	var xhr = new XMLHttpRequest();
	xhr.open("POST", "upload");
	xhr.send(data);
}	


// reads music file from html form submit button
document.getElementById('upMusic').onchange = function(){

	var file = this.files[0];

	var reader = new FileReader();

	reader.readAsDataURL(file);
	sendFile(file);
	
};



