const computer_size = 13;
const num_code_lines = 3;
const highlighted_registers = [12];
const line_descriptions = [
    "<b>CLA 10</b>: Clear the accumulator and add the contents of register 10 to it.",
    "<b>FAD 11</b>: Perform floating point addition with the accumulator and register 11, and store the result in the accumulator.",
    "<b>STO 12</b>: Store the contents of the accumulator into register 12.",
];
const instructions = [
    new Assembly_Line(
        'CLA 10',"<b>CLA 10</b>: Clear the accumulator and add the contents of register 10 to it."
    ),
    new Assembly_Line(
        'FAD 11', "<b>FAD 11</b>: Perform floating point addition with the accumulator and " +
        "register 11, and store the result in the accumulator."
    ),
    new Assembly_Line(
        'STO 12', "<b>STO 12</b>: Store the contents of the accumulator into register 12."
    ),
    new Assembly_Line(
        'ORG 10', ""
    ),
    new Assembly_Line(
        'DEC -2.54', ""
    ),
    new Assembly_Line(
        'DEC 6.98', ""
    ),
];
/**
 * Initializes floating_point_operations.jinja2.
 */
function start() {
    common_start();
    computer.assemble(0, instructions);
    update();
}
