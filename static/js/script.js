// JavaScript kodlari (masalan, foydalanuvchi uchun interaktiv elementlar)
document.addEventListener('DOMContentLoaded', function() {
    // Misol uchun, tugma bosilganda xabar ko'rsatish
    const submitButton = document.querySelector('.submit-btn');
    submitButton.addEventListener('click', function(event) {
        alert('Javob yuborildi!');
    });
});
