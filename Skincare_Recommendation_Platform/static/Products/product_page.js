document.addEventListener("DOMContentLoaded", function () {
   /* ----=== rating of the product ===---- */
  const rating_text = document.querySelector(".product_rating");
  const star_container = document.getElementById("star_slider");
  if (!rating_text || !star_container) return;

  const stars = star_container.querySelectorAll(".star");
  const rating = parseFloat(rating_text.textContent.trim());

  if (isNaN(rating)) return;

  stars.forEach(star => {
    const star_value = parseInt(star.getAttribute("data-value"));

    if (rating >= star_value) {
      star.style.setProperty('--clip-bottom', '0%');
    } else if (rating > star_value - 1) {
      const fraction = rating - (star_value - 1);
      const clip_bottom_percent = 100 - fraction * 100;
      star.style.setProperty('--clip-bottom', `${clip_bottom_percent}%`);
    } else {
      star.style.setProperty('--clip-bottom', '100%');
    }
  });

  /* ----=== rating given by user ===---- */

    const user_input = document.getElementById("user_input");
    const user_star_container = document.getElementById("user_star_slider");

    if (!user_input || !user_star_container) return;

    const user_stars = user_star_container.querySelectorAll(".user_star");

    user_input.addEventListener("input", () => {
        const user_rating = parseFloat(user_input.value);

        user_stars.forEach(star => {
        const star_value = parseInt(star.getAttribute("data-value"));

        if (isNaN(user_rating)) {
            star.style.setProperty('--clip-right', '100%');
        } else if (user_rating >= star_value) {
            star.style.setProperty('--clip-right', '0%');
        } else if (user_rating > star_value - 1) {
            const fraction = user_rating - (star_value - 1);
            const clip_right = 100 - (fraction * 100);
            star.style.setProperty('--clip-right', `${clip_right}%`);
        } else {
            star.style.setProperty('--clip-right', '100%');
        }
        });
    });

  /* ----=== like handling ===---- */

    async function handleLikeClick() {
        const like_button = document.getElementById('like_button')
        try {
            const response = await fetch('/history/like/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({
                product_id: document.getElementById('section').getAttribute('data-product_id')
            })
        });
        if(like_button.classList.contains('liked')){
            like_button.classList.remove('liked');
        } else {
            like_button.classList.add('liked');
        }
        } catch (error) {
            console.error('Fetch failed:', error);
        }
    }

    const like_button = document.getElementById('like_button')
    like_button.addEventListener('click', handleLikeClick); 

    if(like_button.getAttribute('data-liked').toLowerCase() === "true"){
        if(!like_button.classList.contains('liked')){
            like_button.classList.add('liked');
        }
    } else {
        if(like_button.classList.contains('liked')){
            like_button.classList.remove('liked');
        }
    }

    /* ----=== adding view ===---- */

    async function addView() {
        try {
            const response = await fetch('/history/view/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({
                    product_id: document.getElementById('section').getAttribute('data-product_id')
                })
            });
        } catch (error) {
            console.error('Fetch failed:', error);
        }
    }
    window.addEventListener('load', addView);



    /* ----=== csrf handling ===---- */
    function getCookie(name) {
        let cookie_value = null;
        if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
            cookie_value = decodeURIComponent(cookie.substring(name.length + 1));
            break;
            }
        }
        }
        return cookie_value;
    }
});
