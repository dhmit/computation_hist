const computer_size = 7;
const num_code_lines = 4;
const highlighted_registers = [6];
const program = [
    new Assembly_Line(
        0, "CLA 4", "<b>CLA 4: </b> Clears the accumulator and stores the value at address 4 (which" +
        " you'll see if you mouseover is 12) into the accumulator.", ["ac"],
        )
];

/**
 * Initializes assembly_addition.jinja2, including initializing register 3 of general memory to
 * 12 and register 4 of general memory to 30, and storing the set program into memory.
 */
function start() {
    general_start();
    assemble();
    computer.general_memory[4].fixed_point = 12;
    computer.general_memory[5].fixed_point = 30;
    update();
}

