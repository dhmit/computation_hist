const computer_size = 8;
const num_code_lines = 5;
const highlighted_registers = [7];
const line_descriptions = [
    "<b>LXA 5, 1: </b> This means load the word at address 5 (which corresponds to PZE 5 as the fifth\n" +
    "    line of code) and store its address into the index register corresponding to 1, which is index register A.",
    "<b>CLA 7: </b> Just stores the value at address 7 into the accumulator.",
    "<b>ADD 7: </b> And then add the value at address 7 to the accumulator.",
    "<b>STO 7: </b> And then store the value of the accumulator to address 7.  Nothing too fancy here.  But then...",
    "<b>TIX 2, 1, 1: </b> This instruction has four parts, the operation, the address, a tag corresponding to the index register 1 (A), and the last number, the decrement.  What will happen is that\n" +
    "    the computer will compare the value of index register A to the decrement.  If the index register is greater than the decrement, then we subtract the decrement from the index register and jump\n" +
    "    to the specified address, otherwise we continue.  Do you see how this works?  The first time we reach this instruction, the index register is 5, so we subtract 1 to get 4 and jump back to the\n" +
    "    instruction at address 2, which is ADD 7.  Then the next time the index register will be 4... then 3... then 2... then 1... and then the program will be done running.  You can see this if you\n" +
    "    step through the program.  At the end, register 7 should have a value of 2^5, 32, from repeated adding.  ",
];

const instructions = [
    'LXA 5, 1',
    'CLA 7',
    'ADD 7',
    'STO 7',
    'TIX 2, 1, 1',
    'PZE 5',
];
/**
 * Initializes looping_with_tix.jinja2, including initializing register 3 of general memory to
 * 12 and register 4 of general memory to 30, and storing the set program into memory.
 */
function start() {
    $('#reset_button').on('click', () => {
        reset(instructions, [[7, 1]]);
        update();
    });
    common_start();
    reset(instructions, [[7, 1]]);
    update();
}
