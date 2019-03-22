const computer_size = 8;
const num_code_lines = 5;
const highlighted_registers = [7];
const line_descriptions = [
    "This example is relatively complicated, so you might want to read the long description at the bottom first.<br />" +
    "<code>LXA 5, 1: </code> Load the word at address 5 (which corresponds to PZE 5 as the" +
    " fifth line of code) and store its address into the index register corresponding to 1, which is index register A." +
    "  Basically, index register A now has the value of general memory register 5",
    "<code>CLA 7: </code> Stores the value at address 7 into the accumulator.",
    "<code>ADD 7: </code> Adds the value at address 7 to the accumulator.",
    "<code>STO 7: </code> Stores the value of the accumulator to address 7.  What's the value of address 7 after you" +
    " press step?",
    "<code>TIX 1, 1, 1: </code> The computer will compare the value of index register A to the decrement, 1.  If the" +
    " index register is greater than the decrement, then we subtract the decrement from the index register and jump\n" +
    "    to the general memory 1, otherwise we continue.  What's the value of index register A after you press Step?",
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
