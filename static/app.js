solve_it = function(a, b, c) {
    $.ajax({
        url: '/solve',
        contentType: 'application/json',
        method: 'POST',
        data: JSON.stringify({'a': a, 'b': b, 'c': c}),
        success: function(resp) {
            $('#solutions').show();
            $('span#root_1').html(resp.root_1)
            $('span#root_2').html(resp.root_2)
        }
    })
}

$(document).ready(function() {
    $('input#c').on('keypress', function(e){
        if(e.which == 13) {
            solve_it(parseInt($('input#a').val()),
                     parseInt($('input#b').val()),
                     parseInt($('input#c').val())
            )
        }
    })
})
