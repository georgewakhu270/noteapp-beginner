
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

function delete_confirm(form){
    if (form){
        form.addEventListener('submit', (event)=>{
            const confirmed = confirm('Are you absolutely sure you want to delete this note? This action cannot be undone')

            if (!confirmed) {
                event.preventDefault()
            }
        })
    }
}


    const deleteForm = document.querySelector('.delete-page #deleteform')
    delete_confirm(deleteForm)



setTimeout(() => {
    const alerts = document.querySelectorAll('#flash-messages .alert');
    alerts.forEach(alert => {
        alert.style.transition = 'opacity 0.5s ease';
        alert.style.opacity = '0';
        setTimeout(() => {
            alert.remove();
            // Clean up container if empty
            const container = document.querySelector('#flash-messages');
            if (container && container.children.length === 0) {
                container.remove();
            }
        }, 500);
    });
}, 3000);

