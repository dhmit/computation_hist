const computer_size = 8;
const num_code_lines = 6;

/**
 * Initializes power_of_2.jinja2, including initializing register 3 of general memory to
 * 12 and register 4 of general memory to 30, and storing the set program into memory.
 */
function start() {
    general_start();
    assemble();
    computer.general_memory[7].fixed_point = 1;
    update();
}

