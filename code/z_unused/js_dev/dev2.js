class BinaryDisplay {
    constructor($where, num_digits=10) {
        this.num_digits = num_digits;
        this.$where = $where || $('body');
        this.digits = [];
    }

    /**
     * Initializes the digits and display.
     */
    init() {
        this.get_digits();
        this.create_display();
    }

    /**
     * gets a stream of random digits, stores in this.digits and returns it
     *
     * @return Array<Int>
     */
    get_digits() {
        this.digits = []; // make sure to clear
        for (let i = 0; i < this.num_digits; i++) {
            let digit = 0;
            if (Math.random() < 0.5) {
                digit = 1;
            }
            this.digits.push(digit);
        }
    }

    /**
     * Creates a display of digits at this.$where.  Returns $container.
     *
     * @return JQueryObject
     */
    create_display() {
        const $container = $('<div class="binary"></div>');
        for (const digit of this.digits) {
            const $digit_holder = $('<div class="binary_digit">' + digit.toString() + '</div>');
            $digit_holder.addClass('binary_digit_' + digit.toString());
            $container.append($digit_holder);
        }
        this.$where.append($container);
    }
}

$(document).ready(() => {
    const binary_display = new BinaryDisplay($('#put_binary_here'));
    binary_display.init();
});
