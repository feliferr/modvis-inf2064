$(function() {
    $('button').click(function() {
        $.ajax({
            url: '/helloTest',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                alert(response)
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});