const computer = new IBM_704(computer_size);


/**
 * Assembles code from code box into program which is placed in computer.
 */
function assemble() {
    if (typeof(GENERAL_ASSEMBLER) !== "undefined") {
        code = document.getElementById("code_box").value;
        code_lines = code.split(newline_regex);
        computer.assemble(0, code_lines);
    } else {
        const code = $(".symbolic_code");
        const code_innerHTML = Array(code.length);
        for (let i = 0; i < num_code_lines; i++) {
            code_innerHTML[i] = code[i].innerHTML;
        }
        computer.assemble(0, code_innerHTML);
    }
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
    // return computer.general_memory[12].fixed_point; // should be 25
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
    const code_html = $(".symbolic_code");
    if (code_html.length !== 0) {
        code_line = Math.min(computer.ilc.valueOf(), num_code_lines-1);
        for (let line = 0; line < num_code_lines; line++) {
            code_html[line].style.backgroundColor = "white";
        }
        code_html[code_line].style.backgroundColor = "deepskyblue";
    }

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
    instruction_location_counter_element.title = "Location: " + computer.ilc.valueOf();

    $("#instruction_register").html(computer.instruction_register.toString());

    storage_register_element = $("#storage_register")[0];
    storage_register_element.innerHTML = computer.storage_register.toString();
    storage_register_element.title = "Instruction: " + computer.storage_register.instruction.toString();
    storage_register_element.title += "\r\nFixed Point: " + computer.storage_register.fixed_point;
    storage_register_element.title += "\r\nFloating Point: " + computer.storage_register.floating_point;

    accumulator_element = $("#accumulator")[0];
    accumulator_element.innerHTML = computer.accumulator.toString();
    accumulator_element.title = "Fixed Point: " + computer.accumulator.fixed_point;
    accumulator_element.title += "\r\nFloating Point: " + computer.accumulator.floating_point;
    
    mq_register_element = $("#mq_register")[0];
    mq_register_element.innerHTML = computer.mq_register.toString();
    mq_register_element.title = "Fixed Point: " + computer.mq_register.fixed_point;
    mq_register_element.title += "\r\nFloating Point: " + computer.mq_register.floating_point;
    
    index_a_element = $("#index_a")[0];
    index_a_element.innerHTML = computer.index_a.toString();
    index_a_element.title = "Value: " + computer.index_a.valueOf();
    
    index_b_element = $("#index_b")[0];
    index_b_element.innerHTML = computer.index_b.toString();
    index_b_element.title = "Value: " + computer.index_b.valueOf();
    
    index_c_element = $("#index_c")[0];
    index_c_element.innerHTML = computer.index_c.toString();
    index_c_element.title = "Value: " + computer.index_c.valueOf();
}

/**
 * Clear the computer's memory.
 */
function clear() {
    computer.clear();
    update();
}

/**
 * Sets up general elements of page when loaded.
 */
function general_start() {
    $('#run_button').on('click', run);
    $('#clear_button').on('click', clear);
    $('#assemble_button').on('click', assemble);
    $('#step_button').on('click', step);
    create_memory_display();
}

$(document).ready(start);