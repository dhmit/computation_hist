// this is a sample javascript file for JS development


/**
 * not_all: nots every binary digit on the page.
 */
function not_all() {
    console.log('Hello!');
    const $ones = $('.binary_digit_1');
    const $zeros = $('.binary_digit_0');
    $ones.html('0');
    $zeros.html('1');
}

function start() {
    $('#not_operation').on('click', not_all);
}

$(document).ready(start);
