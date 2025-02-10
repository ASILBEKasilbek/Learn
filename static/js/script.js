$(document).ready(function() {
    let items = $('.category-item');
    let totalItems = items.length;

    if (totalItems > 1) {
        $('.nav-button').show(); // Tugmalarni ko'rsatish
    } else {
        $('.nav-button').hide(); // Agar bitta kategoriya bo'lsa, tugmalarni yashirish
    }

    let currentIndex = 0;

    function showItem(index) {
        $('.category-slider').animate({
            scrollLeft: items.eq(index).position().left
        }, 500);
    }

    $('#nextButton').click(function() {
        currentIndex = (currentIndex + 1) % totalItems;
        showItem(currentIndex);
    });

    $('#prevButton').click(function() {
        currentIndex = (currentIndex - 1 + totalItems) % totalItems;
        showItem(currentIndex);
    });
});
document.querySelectorAll(".nav-link").forEach(link => {
    link.addEventListener("click", function(e) {
        e.preventDefault();
        let target = document.querySelector(this.getAttribute("href"));
        if (target) {
            window.scrollTo({
                top: target.offsetTop - 70, // Navbarni hisobga olish
                behavior: "smooth"
            });
        }
    });
});