const btnDelete = document.querySelectorAll('.btn-delete')


if (btnDelete) {

    const btArray = Array.from(btnDelete);
    btArray.forEach((btn) => {
        btn.addEventListener('click', (e) => {
            if (!confirm('Estas seguro de Eliminar este registro...? ')) {
                e.preventDefault();
            }

        });

    });
}