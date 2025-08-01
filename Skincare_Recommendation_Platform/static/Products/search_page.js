document.addEventListener('DOMContentLoaded', function(){
    const priceSlider = document.getElementById('price-slider');

    if (!priceSlider) return; // Prevent error if slider is missing

    noUiSlider.create(priceSlider, {
        start: [0, 2500],
        connect: true,
        range: {
        min: 0,
        max: 2500
        },
        step: 10,
        format: {
        to: value => Math.round(value),
        from: value => parseInt(value)
        }
    });

    const minOutput = document.getElementById('minPrice');
    const maxOutput = document.getElementById('maxPrice');
    const minInput = document.getElementById('min_price_input');
    const maxInput = document.getElementById('max_price_input');

    priceSlider.noUiSlider.on('update', function (values) {
        const minVal = values[0];
        const maxVal = values[1];
        minOutput.textContent = minVal;
        maxOutput.textContent = maxVal;
        minInput.value = minVal;
        maxInput.value = maxVal;
    });

    const ratingSlider = document.getElementById('rating-slider');

    if (ratingSlider) {
    noUiSlider.create(ratingSlider, {
        start: [0, 5],
        connect: true,
        range: {
        min: 0,
        max: 5
        },
        step: 0.1,
        format: {
        to: value => parseFloat(value).toFixed(1),
        from: value => parseFloat(value)
        }
    });

    const minRatingOutput = document.getElementById('minrating');
    const maxRatingOutput = document.getElementById('maxrating');
    const minRatingInput = document.getElementById('min_rating_input');
    const maxRatingInput = document.getElementById('max_rating_input');

    ratingSlider.noUiSlider.on('update', function (values) {
        const minVal = values[0];
        const maxVal = values[1];
        minRatingOutput.textContent = minVal;
        maxRatingOutput.textContent = maxVal;
        minRatingInput.value = minVal;
        maxRatingInput.value = maxVal;
    });
    }


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

    const skin_type_arrow = document.getElementById('skin_type_arrow');
    const skin_type_menu = document.getElementById('hidden_skin_type_list');
    skin_type_arrow.addEventListener('click', function(){
        menuClickHandler(skin_type_menu, skin_type_arrow);
    })

    const concerns_arrow = document.getElementById('targeted_concerns_arrow');
    const concerns_menu = document.getElementById('hidden_targeted_concerns_list');
    concerns_arrow.addEventListener('click', function(){
        menuClickHandler(concerns_menu, concerns_arrow);
    })

    const ingredients_arrow = document.getElementById('ingredients_arrow');
    const ingredient_menu = document.getElementById('hidden_ingredients_list')
    ingredients_arrow.addEventListener('click', function(){
        menuClickHandler(ingredient_menu, ingredients_arrow);
    })

    function submitValues() {
        var searched_phrase = document.getElementById('search_bar').value;
        const filter_form = document.getElementById('filter_form');
        document.getElementById('search_input').value = searched_phrase;
        filter_form.submit();
    }

    const filter_button = document.getElementById('filter_button');
    const search_button = document.getElementById('search_button');
    filter_button.addEventListener('click', submitValues);
    search_button.addEventListener('click', submitValues);

    const nav_arrow = document.getElementById('nav_arrow');
    const nav_arrow_closed = document.getElementById('nav_arrow_closed');
    nav_arrow.addEventListener('click', function(){
        document.getElementsByTagName('body')[0].classList.add('nav_closed');
        document.getElementById('filter_form').style.display = 'none';
        document.getElementsByTagName('nav')[0].classList.add('closed');
        nav_arrow_closed.style.display = 'block';
    });

    nav_arrow_closed.addEventListener('click', function(){
        document.getElementsByTagName('body')[0].classList.remove('nav_closed');
        document.getElementById('filter_form').style.display = 'block';
        document.getElementsByTagName('nav')[0].classList.remove('closed');
        nav_arrow_closed.style.display = 'none';
    })

})