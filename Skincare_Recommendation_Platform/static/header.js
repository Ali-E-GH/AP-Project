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
    //     const response = await fetch('/product/search/', {
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

    /* ----=== menu ===---- */
    const user_icon = document.getElementById('user_icon');
    const user_menu = document.getElementById('menu_user_content');
    user_icon.addEventListener('click', function() {
        menuClickHandler(user_menu, user_icon);
    });

    // const product_button = document.getElementById('product_button');
    // const product_menu = document.getElementById('menu_products_content');
    // product_button.addEventListener('click', function () {
    //     menuClickHandler(product_menu, product_button);
    // })


    function menuClickHandler(menu, button){
        if(button.classList.contains('clicked')){
            button.classList.remove('clicked');
            menu.style.display = 'none';
        } else {
            button.classList.add('clicked');
            menu.style.display = 'flex';
        }
    }


    document.addEventListener('click', (event) => {
    if (!user_icon.contains(event.target) && !user_menu.contains(event.target)) {
        user_icon.classList.remove('clicked')
        user_menu.style.display = 'none';
    }
    if (!product_button.contains(event.target) && !product_menu.contains(event.target)) {
        product_button.classList.remove('clicked')
        product_menu.style.display = 'none';
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