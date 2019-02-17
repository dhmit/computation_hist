const computer = new IBM_704();
code_line = 0;

/**
 * Runs code placed into the textbox of ibm704sim.html with register 10 holding numerical
 * value of 11 and register 11 holding numerical value of 14, and returns value of register 12.
 *
 * @returns {number}    The value of register 12.
 */
function run() {
    code = document.getElementById("codeBox").value;
    code_lines = code.split(newline_regex);
    computer.assemble(0, code_lines);
    computer.general_memory[10].fixed_point = 11; // assign register 10 value of 11
    computer.general_memory[11].fixed_point = 14; // assign register 11 value of 14
    computer.run();
    return computer.general_memory[12].fixed_point; // should be 25
}