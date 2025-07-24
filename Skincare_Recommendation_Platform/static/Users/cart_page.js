document.addEventListener('DOMContentLoaded', function(){
    const cost = parseFloat(document.getElementById('total_cost').innerText) + 10;
    document.getElementById('total_cost').innerText = '$' + cost.toString();


    const product_containers = document.querySelectorAll('.product_container');
    product_containers.forEach(container => {
        const item_id = container.getAttribute('data-item-id');

        const increase_button = document.getElementById(`increase_button_${item_id}`);
        increase_button.addEventListener('click', increaseQuantity);

        async function increaseQuantity(){
            const response = await fetch('/user/item_quantity/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({
                    action: 'add',
                    id: item_id
                })
            });
            data = await response.json();
            document.getElementById(`total_price_${item_id}`).innerText=`$${data.total_cost}`;
            document.getElementById(`quantity_${item_id}`).innerHTML = parseInt(document.getElementById(`quantity_${item_id}`).innerHTML) + 1;
            document.getElementById('total_quantities').innerHTML = data.total_cart_quantity;
            document.getElementById('total_cost').innerHTML = '$' + data.total_cart_cost.toString();
        }

        const decrease_button = document.getElementById(`decrease_button_${item_id}`);
        decrease_button.addEventListener('click', decreaseQuantity);

        async function decreaseQuantity() {
            const response = await fetch('/user/item_quantity/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({
                    action: 'remove',
                    id: item_id
                })
            });

            const data = await response.json();
            if(data.status != 'deleted'){
                document.getElementById(`total_price_${item_id}`).innerText=`$${data.total_cost}`;
            } else {
                window.location.replace(window.location.href);
            }
            document.getElementById(`quantity_${item_id}`).innerHTML = parseInt(document.getElementById(`quantity_${item_id}`).innerHTML) - 1;
            document.getElementById('total_quantities').innerHTML = data.total_cart_quantity;
            document.getElementById('total_cost').innerHTML = '$' + data.total_cart_cost.toString();
        }
    });

    const purchase_button = document.getElementById('complete_purchase');
    purchase_button.addEventListener('click', purchase);

    async function purchase(){
        const response = await fetch('/user/purchase/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({
            })
        });

        window.location.replace(window.location.href);
    }


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