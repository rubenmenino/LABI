/*Para mudar a cor da opção selecionada na Navbar*/
function navbar() {
	$('li').click(function () {
		$('li.active').removeClass('active');
		$(this).closest('li').addClass('active');
	});
};