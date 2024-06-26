document.addEventListener('DOMContentLoaded', function() {
    const innerDiv = document.querySelector('.container');
    if (innerDiv.querySelector('.form')) {
        innerDiv.classList.add('centered');
    }
});