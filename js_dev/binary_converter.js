const no_to_operation_str = {0o601: "STO", 0: "HTR", 0o500: "CLA", 0o400: "ADD", 0b110: "TNX"};

function binary_to_instruction_a(binary_rep) {
    for (let i = 0; i < 36 - binary_rep.length; i++) {
        binary_rep = "0" + binary_rep;
    }
    prefix_bits = binary_rep.substring(0,3);
    prefix = no_to_operation_str[parseInt(prefix_bits, 2)];
    if(prefix == undefined || prefix == "HTR") {
        return "Operation not found"
    }
    result = prefix;
    address_bits = binary_rep.substr(-15);
    result += " " + parseInt(address_bits, 2).toString();
    tag_bits = binary_rep.substring(18,21);
    result += ", " + parseInt(tag_bits, 2).toString();
    decrement_bits = binary_rep.substring(3, 18);
    decrement = parseInt(decrement_bits, 2);
    result += decrement.toString();
    result += ", " + decrement.toString();
    return result;
}

function binary_to_instruction_b(binary_rep) {
    for (let i = 0; i < 36 - binary_rep.length; i++) {
        binary_rep = "0" + binary_rep;
    }
    operation_bits = binary_rep.substring(0, 12);
    operation_number = parseInt(operation_bits, 2);
    var operation;
    operation = no_to_operation_str[operation_number];
    if (operation == undefined) {
        return "Operation not found";
    }
    result = operation;
    address_bits = binary_rep.substr(-15);
    result += " " + parseInt(address_bits, 2).toString();
    tag_bits = binary_rep.substring(18,21);
    if (tag_bits != "000") {
        result += ", " + parseInt(tag_bits, 2).toString();
    }
    return result;
}

function binary_to_fixed_point(binary_rep) {
    var positive;
    if (binary_rep.length == 36) {
        positive = binary_rep[0] == "0";
        binary_rep = binary_rep.substring(1);
    } else {
        positive = true;
    }
    result = parseInt(binary_rep, 2);
    if (!positive) {
        result = -result;
    }
    return result.toString();
}

function binary_to_floating_point(binary_rep) {
    for (let i = 0; i < 36 - binary_rep.length; i++) {
        binary_rep = "0" + binary_rep;
    }
    fraction_bits = binary_rep.substring(9,36);
    fraction = parseInt(fraction_bits, 2) / Math.pow(2, 27);
    characteristic_bits = binary_rep.substring(1, 9);
    characteristic = parseInt(characteristic_bits, 2);
    exponent = characteristic - 128;
    result = fraction*Math.pow(2,exponent);
    if (binary_rep[0] == 1) {
        result = -result;
    }
    return result.toString();
}

function convert() {
    binary_rep = document.getElementById("textBox").value;
    document.getElementById('typeA').innerHTML = "Type A: " + binary_to_instruction_a(binary_rep);
    document.getElementById('typeB').innerHTML = "Type B: " + binary_to_instruction_b(binary_rep);
    document.getElementById('floating').innerHTML =  "Floating" +
        " point: " + binary_to_fixed_point(binary_rep);
    document.getElementById('fixed').innerHTML = "Fixed point: " + binary_to_floating_point(binary_rep);
}

function start() {
    $('#convert').on('click', convert);
}

$(document).ready(start);