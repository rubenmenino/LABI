/*Para deslizar na pagina*/
	
	jQuery(document).ready(function($) {
		$(".scroll").click(function(event){
			event.preventDefault();
			$('html,body').animate({scrollTop:$(this.hash).offset().top}, 1500);
	   });
	});
	

// Fechar a dropdown quando se clica fora da mesma
	window.onclick = function(event) {
	  if (!event.target.matches('.dropbtn')) {

		var dropdowns = document.getElementsByClassName("dropdown-content");
		var i;
		for (i = 0; i < dropdowns.length; i++) {
		  var openDropdown = dropdowns[i];
		  if (openDropdown.classList.contains('show')) {
			openDropdown.classList.remove('show');
		  }
		}
	  }
}

function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}

function like(x){
    $.post("like","id="+x,function(response){
    });
    
    var $voted = $("#voted"+x);
    $voted.attr("style","width: 100%");
}

function dislike(x){
    $.post("dislike","id="+x,function(response){
    });
    
    var $voted = $("#voted"+x);
    $voted.attr("style","width: 100%");
}

function choice1() {
		var audio = document.getElementById('audio1');
		var selectBox = document.getElementById('select1');
		var userChoice = selectBox.options[selectBox.selectedIndex].value;
		
		audio.src = '/samples/'+userChoice;
}

function choice2() {
		var audio = document.getElementById('audio2');
		var selectBox = document.getElementById('select2');
		var userChoice = selectBox.options[selectBox.selectedIndex].value;
		
		audio.src = '/samples/'+userChoice;
}

function choice3() {
		var audio = document.getElementById('audio3');
		var selectBox = document.getElementById('select3');
		var userChoice = selectBox.options[selectBox.selectedIndex].value;
		
		audio.src = '/samples/'+userChoice;
}

function choice4() {
		var audio = document.getElementById('audio4');
		var selectBox = document.getElementById('select4');
		var userChoice = selectBox.options[selectBox.selectedIndex].value;
		
		audio.src = '/samples/'+userChoice;
}

function choice5() {
		var audio = document.getElementById('audio5');
		var selectBox = document.getElementById('select5');
		var userChoice = selectBox.options[selectBox.selectedIndex].value;
		
		audio.src = '/samples/'+userChoice;
}

function choice6() {
		var audio = document.getElementById('audio6');
		var selectBox = document.getElementById('select6');
		var userChoice = selectBox.options[selectBox.selectedIndex].value;
		
		audio.src = '/samples/'+userChoice;
}

function choiseneffect1() {
		var selectBox = document.getElementById('efeito1');
		var userChoice = selectBox.options[selectBox.selectedIndex].value;
		
		/..../
}

function choiseneffect2() {
		var selectBox = document.getElementById('efeito2');
		var userChoice = selectBox.options[selectBox.selectedIndex].value;
		
		/..../
}

function choiseneffect3() {
		var selectBox = document.getElementById('efeito3');
		var userChoice = selectBox.options[selectBox.selectedIndex].value;
		
		/..../
}

function choiseneffect4() {
		var selectBox = document.getElementById('efeito4');
		var userChoice = selectBox.options[selectBox.selectedIndex].value;
		
		/..../
}

function choiseneffect5() {
		var selectBox = document.getElementById('efeito5');
		var userChoice = selectBox.options[selectBox.selectedIndex].value;
		
		/..../
}
function choiseneffect6() {
		var selectBox = document.getElementById('efeito6');
		var userChoice = selectBox.options[selectBox.selectedIndex].value;
		
		/..../
}

 $(() => {
                'use strict';
                $('button').click(function() {
                    $(this).toggleClass('pressed');
                });
            });
