'use strict';

import { GeneralAssemblerRenderer } from './render.js';
import { IBM_704, operation_a_to_no, operation_b_to_no, timer } from './simulator.js';

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
    const assembly_lines = [];
    const code_labels = $(".code_label");
    const code_operations = $(".code_operation");
    const code_numbers =  $(".code_numbers");
    const num_lines = code_labels.length;
    for (let i = 0; i < num_lines; i++) {
        const assembly_line = [
            code_labels[i].value.trim(),
            code_operations[i].value.trim(),
            code_numbers[i].value.trim()
        ];
        assembly_lines.push(assembly_line);
    }
    try {
        computer.assemble(assembly_lines);
    } catch (err) {
        computer.clear();
        throw err;
    }
}


/**
 * Runs scripts to initialize page.
 */
export function start() {
    $("#error_message").modal('hide');
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
    $('#add_line').on('click', () => {
        renderer.add_code_line();
    });
    $('#remove_line').on('click', () => {
        renderer.remove_code_line();
    });

    display_operations();
    renderer.add_code_line();
    renderer.update();
    $('[data-toggle="tooltip"]').tooltip();
    $("#loading").hide();
    const title = document.getElementById("main_header");
    title.setAttribute("data-intro", "Welcome to the IBM 704 simulator!");
    title.setAttribute("data-step", "1");
    title.setAttribute("data-position", "bottom");
    introJs().start();
}
