'use strict';

import { timer } from "./simulator.js";

async function flash_text(element) {
    element.classList.add("blink");
    await timer(200);
    element.classList.remove("blink");
}

export class Renderer {
    constructor(computer) {
        this.computer = computer; // an IBM_704 instance
        this.highlighting = true;
    }
    
    /**
     * Produces HTML for all the general memory registers of the computer.
     */
    create_memory_display() {
        const general_memory_display = document.getElementById("general_memory_div");
        for (let i = 0; i < this.computer.size; i++) {
            const para = document.createElement("p");
            const register = document.createTextNode(i.toString()+": ");
            para.appendChild(register);
            const span = document.createElement("span");
            span.setAttribute("class", "general_memory number");
            span.setAttribute("id", "general_memory" + i.toString());
            para.appendChild(span);
            general_memory_display.appendChild(para);
        }
    }

    /**
     * Update the display of the computer's memory.
     */
    update_computer_display(highlighted_registers = []) {
        const general_memory_html = $(".general_memory");
        const next_instruction_address = this.computer.general_memory[this.computer.ilc.valueOf()].instruction.address;
        general_memory_html.removeClass("next_instruction target_register special_highlight changed");
        for (let i = 0; i < this.computer.size; i++) {
            const new_value = this.computer.general_memory[i].toString();
            if (new_value !== general_memory_html[i].innerHTML) {
                if (this.highlighting && general_memory_html[i].innerHTML !== "") {
                    general_memory_html[i].classList.add("changed");
                }

                general_memory_html[i].innerHTML = new_value;
                general_memory_html[i].title = "Instruction: " +
                    this.computer.general_memory[i].instruction.toString();
                general_memory_html[i].title += "\r\nFixed Point: " + this.computer.general_memory[i].fixed_point;
                general_memory_html[i].title += "\r\nFloating Point: " + this.computer.general_memory[i].floating_point;
            }

            if (this.highlighting) {
                if (i === this.computer.ilc.valueOf()) {
                    general_memory_html[i].classList.add("next_instruction");
                } else if (i === next_instruction_address) {
                    general_memory_html[i].classList.add("target_register");
                } else if (highlighted_registers.includes(i)) {
                    general_memory_html[i].classList.add("special_highlight");
                }
            }
        }

        const instruction_location_counter_element = $("#instruction_location_counter")[0];
        instruction_location_counter_element.innerHTML = this.computer.ilc.toString();
        instruction_location_counter_element.title = "Location: " + this.computer.ilc.valueOf();

        $("#instruction_register")[0].innerHTML = this.computer.instruction_register.toString();
        $("#instruction_register")[0].title = "Operation: " + this.computer.instruction_register.get_instruction_str();

        const storage_register_element = $("#storage_register")[0];
        storage_register_element.innerHTML = this.computer.storage_register.toString();
        storage_register_element.title = "Instruction: " + this.computer.storage_register.instruction.toString();
        storage_register_element.title += "\r\nFixed Point: " + this.computer.storage_register.fixed_point;
        storage_register_element.title += "\r\nFloating Point: " + this.computer.storage_register.floating_point;

        const accumulator_element = $("#accumulator")[0];
        accumulator_element.innerHTML = this.computer.accumulator.toString();
        accumulator_element.title = "Fixed Point: " + this.computer.accumulator.fixed_point;
        accumulator_element.title += "\r\nFloating Point: " + this.computer.accumulator.floating_point;

        const mq_register_element = $("#mq_register")[0];
        mq_register_element.innerHTML = this.computer.mq_register.toString();
        mq_register_element.title = "Fixed Point: " + this.computer.mq_register.fixed_point;
        mq_register_element.title += "\r\nFloating Point: " + this.computer.mq_register.floating_point;

        const index_a_element = $("#index_a")[0];
        index_a_element.innerHTML = this.computer.index_a.toString();
        index_a_element.title = "Value: " + this.computer.index_a.valueOf();

        const index_b_element = $("#index_b")[0];
        index_b_element.innerHTML = this.computer.index_b.toString();
        index_b_element.title = "Value: " + this.computer.index_b.valueOf();

        const index_c_element = $("#index_c")[0];
        index_c_element.innerHTML = this.computer.index_c.toString();
        index_c_element.title = "Value: " + this.computer.index_c.valueOf();
    }


    reset(instructions, memory_value_pairs){
        this.computer.clear();
        const instruction_text = [];
        for (let i = 0; i < instructions.length; i++) {
            instruction_text.push(instructions[i].instruction);
        }
        this.computer.assemble(0, instruction_text);

        if (memory_value_pairs !== undefined) {
            for (const [memory_index, value] of memory_value_pairs) {
                this.computer.general_memory[memory_index].fixed_point = value;
            }
        }
    }
}


export class DemoRenderer extends Renderer {
    update(instructions, num_code_lines, highlighted_registers = []) {
        const code_html = $(".symbolic_code");
        code_html.removeClass("next_instruction");
        const code_line = Math.min(this.computer.ilc.valueOf(), num_code_lines-1);
        if (code_html.length !== 0) {
            if (this.highlighting) {
                code_html[code_line].classList.add("next_instruction");
            }
        }

        this.update_computer_display(highlighted_registers);

        // update line descriptions
        let line_desc = "";
        if (typeof instructions[code_line] !== "undefined") {
            line_desc = instructions[code_line].description;
        }
        $('#line_desc')[0].innerHTML = line_desc;
    }
}


export class GeneralAssemblerRenderer extends Renderer {
    update() {
        const computer = this.computer;
        let line_desc = "Next Instruction to be Executed: ";
        line_desc += computer.general_memory[computer.ilc.valueOf()].instruction.toString();
        $('#line_desc')[0].innerHTML = line_desc;
        this.update_computer_display();
    }
}
