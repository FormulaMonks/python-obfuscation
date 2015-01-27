$(function () {
    $(document).on('submit', '#mult', function (event) {
	event.preventDefault();

	var $form = $(this);

	$.get('/calc', {
	    m1: $form.find('#m1').val(),
            m2: $form.find('#m2').val()
	}, 'json').done(function (data, response, xhr) {
	    console.log('data: ', data);
	    $form.find('#result').html("<pre>" + data.result + "</pre>");
	});
    });
});
