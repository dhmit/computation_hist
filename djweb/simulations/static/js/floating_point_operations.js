const computer_size = 13;
const num_code_lines = 3;
const highlighted_registers = [12];
const line_descriptions = [
    "<b>CLA 10</b>: Clear the accumulator and add the contents of register 10 to it.",
    "<b>FAD 11</b>: Perform floating point addition with the accumulator and register 11, and store the result in the accumulator.",
    "<b>STO 12</b>: Store the contents of the accumulator into register 12.",
];

/**
 * Initializes floating_point_operations.jinja2.
 */
function start() {
    general_start();
    assemble();
    update();
}
