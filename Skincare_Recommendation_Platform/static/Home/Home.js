document.addEventListener('DOMContentLoaded', function(){
    const rec_button = document.getElementById("for_you_replacement");
    rec_button.addEventListener('click', function(){
        document.getElementById('for_you_form').submit();
    });
});