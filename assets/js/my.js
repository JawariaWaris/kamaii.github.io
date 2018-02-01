

$(document).ready(function() {

    $('#register-form').submit(function(){

    var formData = new FormData($(this)[0]);

    $.ajax({
        url: '',
        type: 'POST',
        data: formData,
        async: false,
        success: function (data) {
            if (data.message=="Added"){
                document.location.href ="profile";
            }
            else{
                document.getElementById('error-register').innerHTML = data.message+'<br>';
            }

        },
        cache: false,
        contentType: false,
        processData: false
    });

    return false;
});


    $('#login-form').submit(function(){

    var formData = new FormData($(this)[0]);

    $.ajax({
        url: '',
        type: 'POST',
        data: formData,
        async: false,
        success: function (data) {
            if (data.message=="exists"){
                document.location.href ="profile";
            }
            else{
                document.getElementById('error-login').innerHTML = data.message+'<br>';
            }

        },
        cache: false,
        contentType: false,
        processData: false
    });

    return false;
});

    $('#login-form1').submit(function(){

    var formData = new FormData($(this)[0]);

    $.ajax({
        url: '',
        type: 'POST',
        data: formData,
        async: false,
        success: function (data) {
            if (data.message=="exists"){
                document.location.href ="profile";
            }
            else{
                document.getElementById('error-login1').innerHTML = data.message+'<br>';
            }

        },
        cache: false,
        contentType: false,
        processData: false
    });

    return false;
});

    $('#forget-form').submit(function(){

    var formData = new FormData($(this)[0]);

    $.ajax({
        url: '',
        type: 'POST',
        data: formData,
        async: false,
        success: function (data) {
            if (data.message=="Check your email for password!"){
                document.getElementById('error-forget').innerHTML = data.message+'<br>';
                document.getElementById('forget-form').reset();
                //$('#pop-forget').toggle();

            }
            else{
                document.getElementById('error-forget').innerHTML = data.message+'<br>';
            }

        },
        cache: false,
        contentType: false,
        processData: false
    });

    return false;
});



});