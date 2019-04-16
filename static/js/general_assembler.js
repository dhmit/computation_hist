'use strict';

import { Renderer } from './render.js';
import { IBM_704 } from './simulator.js';

/**
 * Attaches an event listener to a textarea that allows it to dynamically resize as you type in it.
 * From https://stackoverflow.com/questions/37629860/automatically-resizing-textarea-in-bootstrap.
 *
 * @param {string} id   Id of textarea to attach event listener to.
 */
function expand_text_area(id) {
    document.getElementById(id).addEventListener('keyup', function() {
        this.style.overflow = 'hidden';
        this.style.height = this.scrollHeight + 'px';
    }, false);
}


function display_operations() {
    const operations = new Set();

    for (const operation in operation_b_to_no) {
        operations.add(operation);
    }

    for (const operation in operation_a_to_no) {
        operations.add(operation);
    }
    const operations_str = Array.from(operations).join(", ");
    const place = document.getElementById("available_operations");
    place.innerText = operations_str;
}

function assemble_from_code_box(computer) {
    try {
        const code = document.getElementById("code_box").value;
        const newline_regex = /\r\n|[\n\v\f\r\x85\u2028\u2029]/;
        const code_lines = code.split(newline_regex);
        computer.assemble(0, code_lines);
    } catch (err) {
        computer.clear();
    }
}

function update(renderer) {
    const computer = renderer.computer;
    let line_desc = "Next Instruction to be Executed: ";
    line_desc += computer.general_memory[computer.ilc.valueOf()].instruction.toString();
    $('#line_desc')[0].innerHTML = line_desc;
    renderer.update_computer_display();
}

/**
 * Runs scripts to initialize page.
 */
export function start() {
    const computer = new IBM_704();
    const renderer = new Renderer(computer);

    renderer.create_memory_display();

    $('#assemble_button').on('click', () => {
        assemble_from_code_box(computer);
        update(renderer);
    });
    $('#clear_button').on('click', () => {
        computer.clear();
        update(renderer);
    });
    $('#run_button').on('click', () => {
        computer.halt = false;
        computer.run();
        update(renderer);

    });
    $('#step_button').on('click', () => {
        computer.halt = false;
        computer.step();
        update(renderer);
    });
    $('#highlight_button').on('click', () => {
        renderer.highlighting = !renderer.highlighting;
        update(renderer);
    });
    expand_text_area("code_box");
    display_operations();
    update(renderer);
}
