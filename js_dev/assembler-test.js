const computer = new IBM_704();
const newline_regex = /\r\n|[\n\v\f\r\x85\u2028\u2029]/;

/**
 * Attaches an event listener to a textarea that allows it to dynamically resize as you type in it.
 * From https://stackoverflow.com/questions/37629860/automatically-resizing-textarea-in-bootstrap.
 *
 * @param {string} id   Id of textarea to attach event listener to.
 */
function expand_text_area(id) {
    document.getElementById(id).addEventListener('keyup', function() {
        this.style.overflow = 'hidden';
        this.style.height = 0;
        this.style.height = this.scrollHeight + 'px';
    }, false);
}

/**
 * Assembles code from code box into program which is placed in computer.
 */
function assemble() {
    code = document.getElementById("code_box").value;
    code_lines = code.split(newline_regex);
    computer.assemble(0, code_lines);
    update();
}

/**
 * Cause the computer to advance one step.
 */
function step() {
    computer.step();
    update();
}

/**
 * Runs code placed into the textbox of ibm704sim.html with register 10 holding numerical
 * value of 11 and register 11 holding numerical value of 14, and returns value of register 12.
 *
 * @returns {number}    The value of register 12.
 */
function run() {
    assemble();
    // computer.general_memory[10].fixed_point = 11; // assign register 10 value of 11
    // computer.general_memory[11].fixed_point = 14; // assign register 11 value of 14
    computer.run();
    update();
    return computer.general_memory[12].fixed_point; // should be 25
}

/**
 * Produces HTML for all the general memory registers of the computer.
 */
function create_memory_display() {
    let general_memory_display = document.getElementById("general_memory_div");
    for (let i = 0; i < computer.size; i++) {
        let para = document.createElement("p");
        let register = document.createTextNode(i.toString()+": ");
        para.appendChild(register);
        let span = document.createElement("span");
        span.setAttribute("class", "general_memory");
        span.setAttribute("id", "general_memory" + i.toString());
        para.appendChild(span);
        general_memory_display.appendChild(para);
    }
}

/**
 * Update the display of the computer's memory.
 */
function update() {
    const general_memory_html = $(".general_memory");
    for (let i = 0; i < computer.size; i++) {
        general_memory_html[i].innerHTML = computer.general_memory[i].toString();
        general_memory_html[i].title = "Instruction: " +
            computer.general_memory[i].instruction.toString();
        general_memory_html[i].title += "\r\nFixed Point: " + computer.general_memory[i].fixed_point;
        general_memory_html[i].title += "\r\nFloating Point: " + computer.general_memory[i].floating_point;
    }

    instruction_location_counter_element = $("#instruction_location_counter")[0];
    instruction_location_counter_element.innerHTML = computer.ilc.toString();
    instruction_location_counter_element.title = computer.ilc.valueOf();

    $("#instruction_register").html(computer.instruction_register.toString());

    storage_register_element = $("#storage_register")[0];
    storage_register_element.innerHTML = computer.storage_register.toString();
    storage_register_element.title = "Fixed Point: " + computer.storage_register.fixed_point;
    storage_register_element.title += "\r\nFloating Point: " + computer.storage_register.floating_point;

    accumulator_element = $("#accumulator")[0];
    accumulator_element.innerHTML = computer.accumulator.toString();
    accumulator_element.title = computer.accumulator.fixed_point;
}

/**
 * Clear the computer's memory.
 */
function clear() {
    computer.clear();
    update();
}

/**
 * Sets up page when loaded.
 */
function start() {
    $('#run_button').on('click', run);
    $('#clear_button').on('click', clear);
    $('#assemble_button').on('click', assemble);
    $('#step_button').on('click', step);


    computer.general_memory[4].fixed_point = 12;
    computer.general_memory[5].fixed_point = 30;

    create_memory_display();
    expand_text_area("code_box");
    update();
}

$(document).ready(start);