document.addEventListener('DOMContentLoaded', function(){
    function menuClickHandler(menu, button){
        if(button.classList.contains('clicked')){
            button.classList.remove('clicked');
            button.classList.remove('fa-angle-up');
            button.classList.add('fa-angle-down');
            menu.style.display = 'none';
        } else {
            button.classList.add('clicked');
            button.classList.remove('fa-angle-down');
            button.classList.add('fa-angle-up');
            menu.style.display = 'flex';
        }
    }
    const question_ids = JSON.parse(document.getElementById('quiz_container').dataset.question_ids);
    question_ids.forEach(id => {
        const options = document.querySelectorAll(`.question_${id}`);
        if (options[0].dataset.q_type == 'single_choice') {
            options.forEach(option => {
                option.addEventListener('change', function() {
                    const checked_count = document.querySelectorAll(`.question_${id}:checked`).length;
                    if(checked_count >= 1){
                        const checked = document.querySelectorAll(`.question_${id}:checked`);
                        checked.forEach(checkbox => {
                            checkbox.checked = false;
                        });
                        option.checked = true;
                    }
                });
            });
        }
        document.getElementById(`question_${id}_arrow`).addEventListener('click', function() {
            const menu = document.getElementById(`question_${id}_options`);
            const arrow = document.getElementById(`question_${id}_arrow`);
            menuClickHandler(menu, arrow);
        });
    });




    
});