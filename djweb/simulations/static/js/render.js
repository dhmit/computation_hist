var highlighting = true;


/**
 * Produces HTML for all the general memory registers of the computer.
 */
function create_memory_display(computer) {
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
function update(computer, instructions, num_code_lines) {
    const code_html = $(".symbolic_code");
    if (code_html.length !== 0) {
        code_line = Math.min(computer.ilc.valueOf(), num_code_lines-1);
        for (let line = 0; line < num_code_lines; line++) {
            code_html[line].style.backgroundColor = "white";
        }
        if (highlighting) {
            code_html[code_line].style.backgroundColor = "deepskyblue";
        }
    }

    const general_memory_html = $(".general_memory");
    let next_instruction_address = computer.general_memory[computer.ilc.valueOf()].instruction.address;
    for (let i = 0; i < computer.size; i++) {
        general_memory_html[i].innerHTML = computer.general_memory[i].toString();
        general_memory_html[i].title = "Instruction: " +
            computer.general_memory[i].instruction.toString();
        general_memory_html[i].title += "\r\nFixed Point: " + computer.general_memory[i].fixed_point;
        general_memory_html[i].title += "\r\nFloating Point: " + computer.general_memory[i].floating_point;
        if (highlighting) {
            if (i === computer.ilc.valueOf() && !computer.halt) {
                general_memory_html[i].style.backgroundColor = "deepskyblue";
            } else if (i === next_instruction_address && !computer.halt) {
                general_memory_html[i].style.backgroundColor = "#ff0066";
            } else if (typeof highlighted_registers !== "undefined" && highlighted_registers.includes(i)) {
                general_memory_html[i].style.backgroundColor = "mediumseagreen";
            } else {
                general_memory_html[i].style.backgroundColor = "transparent";
            }
        } else {
            general_memory_html[i].style.backgroundColor = "transparent";
        }
    }

    instruction_location_counter_element = $("#instruction_location_counter")[0];
    instruction_location_counter_element.innerHTML = computer.ilc.toString();
    instruction_location_counter_element.title = "Location: " + computer.ilc.valueOf();

    $("#instruction_register")[0].innerHTML = computer.instruction_register.toString();
    $("#instruction_register")[0].title = "Operation: " + computer.instruction_register.get_instruction_str();

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

    // Finally, update line descriptions
    let line_desc;
    if (typeof GENERAL_ASSEMBLER !== "undefined") {
        line_desc = "Next Instruction to be Executed: ";
        line_desc += computer.general_memory[computer.ilc.valueOf()].instruction.toString();
    } else {
        let code_line = Math.min(computer.ilc.valueOf(), num_code_lines-1);
        if (typeof instructions[code_line] !== "undefined") {
            line_desc = instructions[code_line].description;
        }
    }
    $('#line_desc')[0].innerHTML = line_desc;
}


/**
 * Sets up general elements of page when loaded.
 */
function common_start(computer, instructions, num_code_lines) {
    $('#run_button').on('click', () => {
        computer.run();
        update(computer, instructions, num_code_lines);

    });
    $('#clear_button').on('click', () => {
        computer.clear();
        update(computer, instructions, num_code_lines);
    });
    $('#step_button').on('click', () => {
        computer.step();
        update(computer, instructions, num_code_lines);
    });
    $('#highlight_button').on('click', function() { highlighting = !highlighting; update(); });

    create_memory_display(computer);
}

function reset(computer, instructions, memory_value_pairs){
    computer.clear();
    let instruction_text = [];
    for (let i in instructions) {
        instruction_text.push(instructions[i].instruction);
    }
    computer.assemble(0, instruction_text);

    if (memory_value_pairs !== undefined) {
            for (const [memory_index, value] of memory_value_pairs) {
            computer.general_memory[memory_index].fixed_point = value;
        }
    }
}

