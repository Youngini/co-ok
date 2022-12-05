let id = $('#id');
let pw = $('#pw');
let btn = $('#btn');

$(btn).on('click', function() { 
    if($(id).val() == ""){
        $(id).next('label').addClass('warning');
    }
    else if($(pw).val() == ""){
        $(pw).next('label').addClass('warning');
    }
});