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
    $ones.addClass('binary_digit_0').removeClass('binary_digit_1');
    $zeros.addClass('binary_digit_1').removeClass('binary_digit_0');
}

/**
 * move_digits:
 */
function move_digits() {
    const $digits = $('.binary_digit');
    $digits.css('position', 'relative');
    $digits.animate(
        { top: '200px', fontSize: '300%' },
        { duration: 2000, complete: function() { alert('hello!'); } }
    );
}

function load_number() {
    var num = $('#inputNum').val();
    $('.loadedNumber').html(num);


    //Finding the significand as follows:

    // This will take the Number and make it an Exponential with 2 decimal places, ie of the form
    // d.ddeSn, where N is the power it is raised to, S is the sign (+ or -) of the exponent, and
    // d are digits. Since this is a string and not a number, we can use it as a means of
    // representing numbers easily. Note that for future versions if we want to change the
    // precision p, we could have that be an input and make the function .toExponential(p-1) (as
    // the first digit before the decimal counts). The base operation is less obvious.
    var exponentialString = Number(num).toExponential(2).toString();

    // This removes the decimal place. We only want to show the digits. (This is mathematically
    // equivalent to multiplying the number by 100; we can't do that to display it, however, as
    // that will break the exponential representation of the number.
    var significand = Number(exponentialString.substring(0,1) + exponentialString.substring(2,4));

    // Since the are displaying the significand*100, the exponent we should display can't
    // actually be the exponent from exponentialString, but that exponent -2 (ie, *10^-2)
    var exponent = Number(exponentialString.substring(5))-2;

    $('.significand').html(significand);

    $('.exponent').html(exponent);

    // Recreates the number from its significand and exponent
    var recNumber = significand*(10**exponent);

    $('.reconstructedNumber').html(recNumber);

    // Calculates the error as the difference between the actual number and the reconstructed number
    $('#error').html(num-recNumber);
}


function start() {
    $('#load_number_operation').on('click', load_number);
    $('#move_operation').on('click', move_digits);
}

$(document).ready(start);
