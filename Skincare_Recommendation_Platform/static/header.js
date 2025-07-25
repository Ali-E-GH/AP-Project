document.addEventListener("DOMContentLoaded", function () {
    /* ----=== theme toggle ===---- */

    const themeButton = document.getElementById("theme_toggle");

    if (localStorage.getItem("theme") === "dark") {
        document.body.classList.add("dark-mode");
        themeButton.classList.remove("fa-moon");
        themeButton.classList.add("fa-sun");
    }

    themeButton.addEventListener("click", function () {
        document.body.classList.toggle("dark-mode");

        if (document.body.classList.contains("dark-mode")) {
            localStorage.setItem("theme", "dark");
            themeButton.classList.remove("fa-moon");
            themeButton.classList.add("fa-sun");
        } else {
            localStorage.setItem("theme", "light");
            themeButton.classList.remove("fa-sun");
            themeButton.classList.add("fa-moon");
        }
    });

    /* ----=== search bar ===---- */

    // async function handleSearchClick() {
    //     var search_value = document.getElementById('search_bar').value
    //     // tmp url
    //     const response = await fetch('/', {
    //         method: 'POST',
    //         headers: {
    //             'Content-Type': 'application/json',
    //             'X-CSRFToken': getCookie('csrftoken')
    //         },
    //         body: JSON.stringify({
    //             searched_text: search_value
    //         })
    //     });
    // }
    const search_button = document.getElementById('search_button')
    search_button.addEventListener('click', function () {
        document.getElementById('search_bar_form').submit();
    });

    /* ----=== user menu ===---- */
    const user_icon = document.getElementById('user_icon');
    const user_menu = document.getElementById('menu_content');
    user_icon.addEventListener('click', function(){
        if(user_icon.classList.contains('clicked')){
            user_icon.classList.remove('clicked');
            user_menu.style.display = 'none';
        } else {
            user_icon.classList.add('clicked');
            user_menu.style.display = 'flex';
        }
    });
    document.addEventListener('click', (event) => {
    if (!user_icon.contains(event.target) && !user_menu.contains(event.target)) {
        user_icon.classList.remove('clicked')
        user_menu.style.display = 'none';
    }
    });

});



// window.addEventListener('scroll', function(){
//     const icons = document.getElementsByClassName('icon_container')[0];
    
//     if(window.scrollY > 80){
//         icons.style.display= 'none';
//     }
//     else{
//         icons.style.display= 'flex';
//     }
// });