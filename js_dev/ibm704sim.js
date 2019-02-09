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
const no_to_operation_a_str = {0b110: "TNX"};
const no_to_operation_b_str = {0o601: "STO", 0o000: "HTR", 0o500: "CLA", 0o400: "ADD"};

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

/**
 * A class representing a fixed-width word in the IBM 704.
 */
class Word {
    /**
     * Constructor that sets the length and contents of the word.
     *
     * @param           contents    The contents of the word.
     * @param {number}  length      The length of the word in bits.
     */
    constructor(contents, length) {
        this.length = length;
        this.update_contents(contents);
    }

    /**
     * Adds zeroes to the beginning of a string until it reaches the length of this word's instance.
     *
     * @param   {string}  binary_rep   String of 1's and 0's.
     * @returns {string}               String binary_rep with leading zeroes to be of length
     * this.length.
     */
    pad_zeroes(binary_rep) {
        for (let i = 0; i < this.length - binary_rep.length; i++) {
            binary_rep = "0" + binary_rep;
        }
        return binary_rep;
    }

    /**
     * Function that sets the contents of the word.
     *
     * @param           contents    The contents that the word should be set to.
     */
    update_contents(contents) {
        if (typeof contents === "number") {
            contents = convert_to_binary(contents, length);
        }
        if (typeof contents === "string") {
            if (contents.length > length) {
                throw "Word has more than " + length + " bits!";
            }
            if (isNaN(parseInt(contents, 2))) {
                throw "String contains characters aside from 1 and 0!";
            }
            this.contents = this.pad_zeroes(contents);
        } else {
            throw "Contents must be of type number or string!";
        }
    }

    /**
     * Returns string representation of word.
     *
     * @returns {string}   String representing contents of word.
     */
    toString() {
        return this.contents.slice(0);
    }

    /**
     * Returns numerical value corresponding to the contents of the word interpreted as a
     * literal binary number.
     *
     * @returns {number}   Literal numerical value of contents of word.
     */
    valueOf() {
        return parseInt(this.contents, 2);
    }
}

/**
 * Returns the address that an instruction is directed at.
 *
 * @param   {number}    word    Numerical value of instruction to extract address from.
 * @returns {number} Address that instruction is directed at.
 */
function get_address(word) {
    binary_rep = word.toString(2);
    str_address = binary_rep.substr(-15);
    return parseInt(str_address, 2);
}

/**
 * Returns the operation of a Type B instruction.
 *
 * @param   {number}    word    Numerical value of instruction to extract operation from.
 * @returns {function} Function corresponding to the operation contained in instruction.
 */
function get_operation(word) { //TODO: handle Type A instructions
    binary_rep = word.toString(2);
    str_operation = binary_rep.substring(0, binary_rep.length-24);
    operation_number = parseInt(str_operation, 2)
    return no_to_operation[operation_number];
}

/**
 * Emulates the IBM 704 STO operation.
 *
 * Stores the value of the accumulator into the register with specified address.
 *
 * @param {number}  address     Address to store value to.
 */
function STO(address) {
    general_memory[address] = accumulator;
}

/**
 * Emulates the IBM 704 HTR operation.
 *
 * Indicates the computer to halt.
 *
 * @param {number} address      Required for Type B instruction.
 * @returns {number} Returns 1 to indicate halt.
 */
function HTR(address) {
    permanent_halt = true;
    return 1;
}

/**
 * Emulates the IBM 704 CLA operation.
 *
 * Replaces the value of the accumulator with the value of the storage register (which should be
 * the value of the register with the indicated address).
 *
 * @param {number}  address     The address of the value to put into the accumulator (not
 * actually used).
 */
function CLA(address) {
    accumulator = storage_register;
}

/**
 * Emulates the IBM 704 ADD operation.
 *
 * Adds the value of the storage register (which should be the value at address) to the
 * accumulator as if it were a fixed point number.  Note: does not handle negative numbers properly
 * right now.
 *
 * @param {number} address      The address of the value to add to the accumulator.
 */
function ADD(address) {
    accumulator += storage_register;
}

/**
 * Converts an array of strings that contain lines of SHARE assembly into numerical code that is
 * placed in general memory.
 *
 * Currently missing most operations and all pseudo-operations, and doesn't handle tags.
 *
 * @param {Array} code_lines    Array of lines of code.
 */
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

/**
 * Stores an instruction into general memory as a number.
 *
 * @param {string} operation    String name of operation.
 * @param {number} address      Address that instruction is directed at.
 * @param {number} register     Address that instruction should be stored in.
 */
function assemble_line(operation, address, register) {
    general_memory[register] = Math.pow(2,24)*operation_to_no[operation] + address;
}

/**
 * Runs code placed into the textbox of ibm704sim.html with register 10 holding numerical
 * value of 11 and register 11 holding numerical value of 14, and returns value of register 12.
 *
 * @returns {number}    The value of register 12.
 */
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

/**
 * Returns a string binary representation of a number with leading zeros to achieve a certain
 * number of digits.
 *
 * @param {number} number   The number to be converted.
 * @param {number} digits   Number of digits that resulting binary representation should have.
 * @returns {string}    Binary representation with specified number of digits.
 */
function convert_to_binary(number, digits) {
    result = number.toString(2);
    length = result.length;
    for (let i = 0; i < digits - length; i++) {
        result = "0" + result;
    }
    return result.toString();
}

/**
 * Returns a string that holds the SHARE assembly notation for a Type A instruction of a binary
 * representation of a number.
 *
 * If it fails returns "Operation not found".
 *
 * @param {string} binary_rep   The binary representation of a Type A instruction.
 * @returns {string}    SHARE assembly notation for the Type A instruction.
 */
function binary_to_instruction_a(binary_rep) {
    for (let i = 0; i < 36 - binary_rep.length; i++) {
        binary_rep = "0" + binary_rep;
    }
    prefix_bits = binary_rep.substring(0,3);
    prefix = no_to_operation_a_str[parseInt(prefix_bits, 2)];
    if(prefix == undefined || prefix == "HTR") {
        return "Operation not found";
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

/**
 * Returns a string that holds the SHARE assembly notation for a Type B instruction of a binary
 * representation of a number.
 *
 * If it fails returns "Operation not found".
 *
 * @param {string} binary_rep   The binary representation of a Type B instruction.
 * @returns {string}    SHARE assembly notation for the Type B instruction.
 */
function binary_to_instruction_b(binary_rep) {
    for (let i = 0; i < 36 - binary_rep.length; i++) {
        binary_rep = "0" + binary_rep;
    }
    operation_bits = binary_rep.substring(0, 12);
    operation_number = parseInt(operation_bits, 2);
    var operation;
    operation = no_to_operation_b_str[operation_number];
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

/**
 * Converts a string binary representation of an IBM 704 word to a string decimal representation
 * of that word interpreted as a fixed point number.
 *
 *
 * @param {string} binary_rep   The binary representation of an IBM 704 word.
 * @returns {string}    Decimal representation of that word interpreted as a fixed-point number.
 */
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

/**
 * Converts a string binary representation of an IBM 704 word to a string decimal representation
 * of that word interpreted as a floating point number.
 *
 *
 * @param {string} binary_rep   The binary representation of an IBM 704 word.
 * @returns {string}    Decimal representation of that word interpreted as a floating-point
 * number.
 */
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

/**
 * Updates page to highlight correct line of code and display correct memory values.
 */
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


    instruction_location_counter_element = $("#instruction_location_counter")[0];
    instruction_location_counter_element.innerHTML = convert_to_binary(ilc, 38);
    instruction_location_counter_element.title = binary_to_fixed_point(instruction_location_counter_element.innerHTML);

    $("#instruction_register").html(convert_to_binary(instructionregister, 18));

    storage_register_element = $("#storage_register")[0];
    storage_register_element.innerHTML = convert_to_binary(storage_register, 38);
    storage_register_element.title = binary_to_fixed_point(storage_register_element.innerHTML);

    accumulator_element = $("#accumulator")[0];
    accumulator_element.innerHTML = convert_to_binary(accumulator, 38);
    accumulator_element.title = binary_to_fixed_point(accumulator_element.innerHTML);
}

/**
 * Stores Type B instruction into the instruction register in the way the IBM 704 does it.
 *
 * Does not handle Type A, input-output, shifting, or sense instructions.
 *
 * @param {number}  instruction     Instruction to be stored in instruction register.
 */
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

/**
 * Stores a fixed point number into the indicated address in general memory.
 *
 * @param {number} number       Number to be stored.
 * @param {number} register     Address where number is to be stored.
 */
function store_fixed_point_number(number, register) {
    if (number < 0) {
        sign_bit = "1";
    } else {
        sign_bit = "0";
    }
    unsigned_binary_rep = convert_to_binary(Math.abs(number), 35);
    binary_rep = sign_bit + unsigned_binary_rep;
    general_memory[register] = parseInt(binary_rep, 2);
}

/**
 * Returns the proper interpretation of a fixed point number from the indicated address.
 *
 * @param {number} register     Address where number is stored.
 * @returns {number}    Value of word at the address, interpreted as fixed point.
 */
function get_fixed_point_number(register) {
    binary_rep = convert_to_binary(general_memory[register], 36);
    return parseInt(binary_to_fixed_point(binary_rep));
}

/**
 * Stores a number in floating-point format into the indicated address in general memory.
 *
 * @param {number}  number      Number to be stored.
 * @param {number}  register    Address where number is to be stored.
 */
function store_floating_point_number(number, register) {
    if (number < 0) {
        sign_bit = "1";
    } else {
        sign_bit = "0";
    }
    binary_rep = sign_bit;
    number = Math.abs(number);
    exponent = Math.floor(Math.log2(number)) + 1;
    characteristic = exponent + 128;
    binary_rep += convert_to_binary(characteristic, 8);
    magnitude = number / Math.pow(2, exponent);
    magnitude_binary = (magnitude.toString(2)).substring(2,29);
    length = magnitude_binary.length
    for (let i = 0; i < 27 - length; i++) {
        magnitude_binary = magnitude_binary + "0";
    }
    binary_rep += magnitude_binary;
    general_memory[register] = parseInt(binary_rep, 2);
}

/**
 * Returns the proper interpretation of a floating-point number from the indicated address.
 *
 * @param {number} register     Address where number is stored.
 * @returns {number}    Value of word at the address, interpreted as floating point.
 */
function get_floating_point_number(register) {
    binary_rep = convert_to_binary(general_memory[register], 36);
    return parseFloat(binary_to_floating_point(binary_rep));
}

/**
 * Steps through a single line of code indicated by the instruction location counter.
 */
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
    ilc++;
    update();
}

/**
 * Initializes ibm704_assembly_addition.html, including initializing register 3 of general memory to
 * 12 and register 4 of general memory to 30, and storing the set program into memory.
 */
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


