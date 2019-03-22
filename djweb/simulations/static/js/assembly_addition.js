const computer_size = 7;
const num_code_lines = 4;
const highlighted_registers = [6];
const line_descriptions = [
    "<b>CLA 4: </b> Clears the accumulator and stores the value at address 4 (which you'll see if you mouseover is 12) into the accumulator.<br />",
    "<b>ADD 5: </b> Adds the value at address 5 (30) to the accumulator.<br />",
    "<b>STO 6: </b> Stores the value of the accumulator into the register at address 6.<br />",
    "<b>HTR: </b> Tells the computer to stop.<br />",
];

const instructions = [
    'CLA 4',
    'ADD 5',
    'STO 6',
    'HTR',
];
/**
 * Initializes assembly_addition.jinja2, including initializing register 3 of general memory to
 * 12 and register 4 of general memory to 30, and storing the set program into memory.
 */
function start() {
    $('#reset_button').on('click', () => {
        reset(instructions, [[4, 12], [5, 30]]);
        update();
    });
    common_start();
    reset(instructions, [[4, 12], [5, 30]]);
    update();
}
