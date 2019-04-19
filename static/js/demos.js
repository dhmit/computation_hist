'use strict';

import { Assembly_Line, IBM_704, timer } from './simulator.js';
import { DemoRenderer } from './render.js';

export const assembly_addition_demo_params = {
    computer_size: 7,
    num_code_lines: 4,
    highlighted_registers: [6],
    initial_memory_values: [[4, 12], [5, 30]],
    instructions: [
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
    ],
};

export const floating_point_operations_demo_params = {
    computer_size: 13,
    num_code_lines: 3,
    highlighted_registers: [12],
    initial_memory_values: [],
    instructions: [
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
    ],
};

export const looping_with_tix_demo_params = {
    computer_size: 8,
    num_code_lines: 5,
    highlighted_registers: [7],
    initial_memory_values: [[7, 1]],
    instructions: [
        new Assembly_Line('LXA 5, 1', "This example is relatively complicated, so you might want to read the long description at the bottom first.<br />" +
        "<code>LXA 5, 1: </code> Load the word at address 5 (which corresponds to PZE 5 as the" +
        " fifth line of code) and store its address into the index register corresponding to 1, which is index register A." +
        "  Basically, index register A now has the value of general memory register 5"),
        new Assembly_Line('CLA 7', "<code>CLA 7: </code> Stores the value at address 7 into the accumulator."),
        new Assembly_Line("ADD 7", "<code>ADD 7: </code> Adds the value at address 7 to the accumulator."),
        new Assembly_Line("STO 7", "<code>STO 7: </code> Stores the value of the accumulator to address 7.  What's the value of address 7 after you" +
        " press step?"),
        new Assembly_Line('TIX 2, 1, 1', "<code>TIX 1, 1, 1: </code> The computer will compare the value of index register A to the decrement, 1.  If the" +
        " index register is greater than the decrement, then we subtract the decrement from the index register and jump\n" +
        "    to the general memory 1, otherwise we continue.  What's the value of index register A after you press Step?"),
        new Assembly_Line("PZE 5"),
    ],
};


function populate_code(instructions) {
    let codeHTML = "";
    for (let i = 0; i < instructions.length; i++) {
        codeHTML += `<p class="symbolic_code" id="symbolic_code${i}">${instructions[i].toString()}</p>\r\n`;
    }
    $('#code')[0].innerHTML = codeHTML;
}

export function start_demo(demo_params) {
    const instructions = demo_params.instructions;
    const initial_memory_values = demo_params.initial_memory_values;
    const computer_size = demo_params.computer_size;
    const num_code_lines = demo_params.num_code_lines;
    const highlighted_registers = demo_params.highlighted_registers;

    const computer = new IBM_704(computer_size);
    const renderer = new DemoRenderer(computer);

    populate_code(instructions);

    $('#reset_button').on('click', () => {
        renderer.reset(instructions, initial_memory_values);
        renderer.update(instructions, num_code_lines, highlighted_registers);
    });

    // jshint... has trouble with async arrow functions...
    $('#run_button').on('click', async () => { // jshint ignore:line
        computer.halt = false; // jshint ignore:line
        while (!computer.halt) {
            computer.step();
            renderer.update(instructions, num_code_lines, highlighted_registers);
            await timer(750); // jshint ignore:line
        }
    }); // jshint ignore:line
    $('#step_button').on('click', () => {
        computer.halt = false;
        computer.step();
        renderer.update(instructions, num_code_lines, highlighted_registers);
    });
    $('#highlight_button').on('click', () => {
        renderer.highlighting = !renderer.highlighting;
        renderer.update(instructions, num_code_lines, highlighted_registers);
    });
    renderer.create_memory_display();
    renderer.reset(instructions, initial_memory_values);
    renderer.update(instructions, num_code_lines);
}
