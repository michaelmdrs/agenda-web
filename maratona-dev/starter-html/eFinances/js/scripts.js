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

const transactions = []

const Transaction = {
    incomes() {
        // soma a entrada
    },
    expenses() {
        // soma as saídas
    },
    total() {
        // entradas - saídas
    }
}