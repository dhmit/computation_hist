// storage of numbers is currently only fixed point and doesn't have negative numbers
// also there are no index registers or Type A functions.  Or most of the Type B functions
// basically most of the computer is missing
// TODO: figure out how to use modules or sharing scripts or something like that in Javascript?

const newline_regex = /\r\n|[\n\v\f\r\x85\u2028\u2029]/;

const no_to_operation = {0o601: STO, 0: HTR, 0o500: CLA, 0o400: ADD};
const operation_to_no = {};
for (number in no_to_operation) {
    operation_to_no[(no_to_operation[number]).name] = number;
}

general_memory = Array(8192).fill(0);
accumulator = 0;
mq_register = 0;
storage_register = 0;
instructionregister = 0;
ilc = 0;

const num_code_lines = 3;
const general_memory_display = 7;
code_line = 0;
permanent_halt = false;


function get_address(word) {
    binary_rep = word.toString(2);
    str_address = binary_rep.substr(-15);
    return parseInt(str_address, 2);
}

function get_operation(word) { //TODO: handle Type A instructions
    binary_rep = word.toString(2);
    str_operation = binary_rep.substring(0, binary_rep.length-24);
    operation_number = parseInt(str_operation, 2)
    return no_to_operation[operation_number];
}

function STO(address) {
    general_memory[address] = accumulator;
}

function HTR(address) {
    permanent_halt = true;
    return 1;
}

function CLA(address) {
    accumulator = storage_register;
}

function ADD(address) {
    accumulator += storage_register;
}

function assemble(code_lines) {
    register = 0;
    for (line_no in code_lines) {
        line = code_lines[line_no];
        console.log(line);
        operation = line.substring(0,3);
        address = parseInt(line.substring(3, 6));
        assemble_line(operation, address, register);
        register++;
    }
}

function assemble_line(operation, address, register) {
    general_memory[register] = Math.pow(2,24)*operation_to_no[operation] + address;
}

function run() {
    code = document.getElementById("codeBox").value;
    code_lines = code.split(newline_regex);
    assemble(code_lines);
    general_memory[10] = 11; // assign register 10 value of 11
    general_memory[11] = 14; // assign register 11 value of 14
    // general_memory[0] = Math.pow(2,24)*0o500 + 10; // CLA 10
    // general_memory[1] = Math.pow(2,24)*0o400 + 11; // ADD 11
    // general_memory[2] = Math.pow(2,24)*0o601 + 12; // STO 12

    // Why does javascript have only 32-bit numbers, but can do computation to 2^64?
    // Why does the IBM 704 have 36-bit words? Why does this have to make my life harder?
    // general_memory[0] = (0o500 << 24) | 10; // CLA 10
    // general_memory[1] = (0o400 << 24) | 11; // ADD 11
    // general_memory[2] = (0o601 << 24) | 12; // STO 12

    for (ilc = 0; ilc < 8192; ilc++) {
        instructionregister = general_memory[ilc];
        if (instructionregister == 0) {
            break;
        }
        address = get_address(instructionregister);
        storage_register = general_memory[address];
        operation = get_operation(instructionregister);
        if (operation(address) == 1) {
            break;
        }
    }
    return general_memory[12]; // should be 25
}

function convert_to_binary(number, digits) {
    result = number.toString(2);
    length = result.length;
    for (let i = 0; i < digits - length; i++) {
        result = "0" + result;
    }
    return result.toString();
}

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
        return "Operation not found"
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
    result = parseInt(binary_rep, 2).toString();
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
    fraction = parseInt(fraction_bits, 2)/Math.pow(2, 27);
    characteristic_bits = binary_rep.substring(1, 9);
    characteristic = parseInt(characteristic_bits, 2);
    exponent = characteristic - 128;
    result = fraction*Math.pow(2,exponent);
    if (binary_rep[0] == 1) {
        result = -result;
    }
    return result.toString();
}

function update() {
    const code_html = $(".symbolic_code");
    code_html.removeClass("highlighted");
    code_html[code_line].className += " highlighted";

    const general_memory_html = $(".general_memory");
    for (let i = 0; i < general_memory_display; i++) {
        general_memory_html[i].innerHTML = convert_to_binary(general_memory[i], 36);
    }
    // const general_memory_0 = $('#general_memory0');
    // general_memory_0.tooltip({title: binary_to_instruction_a(general_memory_0.html())});
    // const general_memory_1 = $('#general_memory1');
    // general_memory_1.tooltip({title: binary_to_instruction_a(general_memory_1.html())});
    // const general_memory_2 = $('#general_memory2');
    // general_memory_2.tooltip({title: binary_to_instruction_a(general_memory_2.html())});
    // const general_memory_3 = $('#general_memory3');
    // general_memory_3.tooltip({title: binary_to_fixed_point(general_memory_3.html())});
    // const general_memory_4 = $('#general_memory4');
    // general_memory_4.tooltip({title: binary_to_fixed_point(general_memory_4.html())});
    // const general_memory_5 = $('#general_memory5');
    // general_memory_5.tooltip({title: binary_to_fixed_point(general_memory_5.html())});

    general_memory_0 = $('#general_memory0')[0];
    general_memory_0.title = binary_to_instruction_b(general_memory_0.innerHTML);
    general_memory_1 = $('#general_memory1')[0];
    general_memory_1.title = binary_to_instruction_b(general_memory_1.innerHTML);
    general_memory_2 = $('#general_memory2')[0];
    general_memory_2.title = binary_to_instruction_b(general_memory_2.innerHTML);
    general_memory_3 = $('#general_memory3')[0];
    general_memory_3.title = binary_to_fixed_point(general_memory_3.innerHTML);
    general_memory_4 = $('#general_memory4')[0];
    general_memory_4.title = binary_to_fixed_point(general_memory_4.innerHTML);
    general_memory_5 = $('#general_memory5')[0];
    general_memory_5.title = binary_to_fixed_point(general_memory_5.innerHTML);

    $("#instruction_location_counter").html(convert_to_binary(ilc, 13));
    $("#instruction_register").html(convert_to_binary(instructionregister, 18));
    $("#storage_register").html(convert_to_binary(storage_register, 36));
    $("#accumulator").html(convert_to_binary(accumulator, 38));
}

function store_instruction_register(instruction) {
    result = "";
    instruction = convert_to_binary(instruction, 36);
    result += instruction[0];
    result += instruction.substring(3, 12);
    length = result.length;
    for (let i = 0; i <= 18 - length; i++) {
        result += "1";
    }
    instructionregister = parseInt(result, 2);
}

function step() {
    instruction = general_memory[ilc];
    if (instruction == 0) {
        return;
    }
    store_instruction_register(instruction);
    address = get_address(instruction);
    storage_register = general_memory[address];
    operation = get_operation(instruction);
    operation(address);
    code_line++;
    update();
    ilc++;
}

function start() {
    $('#step_button').on('click', step);

    general_memory[3] = 12;
    general_memory[4] = 30;

    const code = $(".symbolic_code");
    const code_innerHTML = Array(code.length);
    for (let i = 0; i < num_code_lines; i++) {
        code_innerHTML[i] = code[i].innerHTML;
    }
    assemble(code_innerHTML);
    update();
}

$(document).ready(start);


