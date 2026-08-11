document.addEventListener('mouseenter', (event) => {
    // Check if the hovered element matches our target inputs
    if (event.target.matches('.signin #id_username')) {
        const div = document.querySelector('.signin #id_username_helptext');
        if (div) div.style.display = 'block';
    }
    if (event.target.matches('.signin #id_password1')) {
        const div = document.querySelector('.signin #id_password1_helptext');
        if (div) div.style.display = 'block';
    }
    if (event.target.matches('.signin #id_password2')) {
        const div = document.querySelector('.signin #id_password2_helptext');
        if (div) div.style.display = 'block';
    }
}, true); 

document.addEventListener('mouseleave', (event) => {
    if (event.target.matches('.signin #id_username')) {
        const div = document.querySelector('.signin #id_username_helptext');
        if (div) div.style.display = 'none';
    }
    if (event.target.matches('.signin #id_password1')) {
        const div = document.querySelector('.signin #id_password1_helptext');
        if (div) div.style.display = 'none';
    }
    if (event.target.matches('.signin #id_password2')) {
        const div = document.querySelector('.signin #id_password2_helptext');
        if (div) div.style.display = 'none';
    }
}, true);