const computer_size = 7;
const num_code_lines = 4;
const highlighted_registers = [6];


const instructions = [
    new Assembly_Line(
        "CLA 4", "<b>CLA 4: </b> Clears the accumulator and stores the value at address 4 (which" +
        " you'll see if you mouseover is 12) into accumulator."
    ),
    new Assembly_Line(
        "ADD 5", "<b>ADD 5: </b> Adds the value at address 5 (30) to the accumulator."
    ),
    new Assembly_Line(
        "STO 6", "<b>STO 6: </b> Stores the value of the accumulator into the register at address 6."
    ),
    new Assembly_Line(
        "HTR", "<b>HTR: </b> Tells the computer to stop."
    ),
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
