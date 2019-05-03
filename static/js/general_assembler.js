'use strict';

import { GeneralAssemblerRenderer } from './render.js';
import { IBM_704, operation_a_to_no, operation_b_to_no, timer } from './simulator.js';

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
        if (!Object.prototype.hasOwnProperty.call(operation_b_to_no, operation)) { continue; }
        operations.add(operation);
    }

    for (const operation in operation_a_to_no) {
        if (!Object.prototype.hasOwnProperty.call(operation_a_to_no, operation)) { continue; }
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


/**
 * Runs scripts to initialize page.
 */
export function start() {
    const computer = new IBM_704();
    const renderer = new GeneralAssemblerRenderer(computer);

    renderer.create_memory_display();

    $('#assemble_button').on('click', () => {
        assemble_from_code_box(computer);
        renderer.update();
    });
    $('#clear_button').on('click', () => {
        computer.clear();
        renderer.update();
    });
    $('#run_button').on('click', async () => {
        computer.halt = false; // jshint ignore:line
        while (!computer.halt) {
            computer.step();
            renderer.update();
            await timer(300); // jshint ignore:line
        }
    }); // jshint ignore:line
    $('#step_button').on('click', () => {
        computer.halt = false;
        computer.step();
        renderer.update();
    });
    $('#highlight_button').on('click', () => {
        renderer.highlighting = !renderer.highlighting;
        renderer.update();
    });
    // expand_text_area("code_box");
    display_operations();
    renderer.add_code_line();
    renderer.update();
    $('[data-toggle="tooltip"]').tooltip();
    $("#loading").hide();
}
