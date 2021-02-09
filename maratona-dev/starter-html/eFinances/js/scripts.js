const Modal = {
    open() {
        document
            .querySelector('.modal-overlay')
            .classList
            .add('active')
    },
    closed() {
        document
        .querySelector('.modal-overlay')
        .classList
        .remove('active')
    }
}