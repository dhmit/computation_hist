// storage of numbers is currently wrong

const newline_regex = /\r\n|[\n\v\f\r\x85\u2028\u2029]/;

const no_to_operation = {0o601: STO, 0: HTR, 0o500: CLA, 0o400: ADD};
const operation_to_no = {};
for (number in no_to_operation) {
    operation_to_no[(no_to_operation[number]).name] = number;
}

general_memory = Array(32767).fill(0);
accumulator = 0;
mq_register = 0;
storage_register = 0;
instructionregister = 0;
ilc = 0;


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
    return 1;
}

function CLA(address) {
    accumulator = storage_register;
}

function ADD(address) {
    accumulator += storage_register;
}

function assemble() {
    code = document.getElementById("codeBox").value;
    code_lines = code.split(newline_regex);
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


