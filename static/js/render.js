'use strict';

import { timer } from "./simulator.js";

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
            span.setAttribute("data-toggle", "tooltip");
            para.appendChild(span);
            general_memory_display.appendChild(para);
        }
    }

    /**
     * Update the display of the computer's memory.
     */
    async update_computer_display(highlighted_registers = []) { // jshint ignore:line
        const general_memory_html = $(".general_memory");
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
        }

        const instruction_location_counter_element = $("#instruction_location_counter")[0];
        if (parseInt(instruction_location_counter_element.innerHTML, 2) !== this.computer.ilc.valueOf() - 1 && instruction_location_counter_element.innerHTML !== "" && this.highlighting) {
            instruction_location_counter_element.classList.add("changed");
        } else {
            instruction_location_counter_element.classList.remove("changed");
        }
        instruction_location_counter_element.innerHTML = this.computer.ilc.toString();
        instruction_location_counter_element.title = "Location: " + this.computer.ilc.valueOf();
        
        const instruction_register_element = $("#instruction_register")[0];
        if (instruction_register_element.innerHTML !== this.computer.instruction_register.toString()) {
            instruction_register_element.innerHTML = this.computer.instruction_register.toString();
            instruction_register_element.title = "Operation: " + this.computer.instruction_register.get_instruction_str();
        }

        const storage_register_element = $("#storage_register")[0];
        if (storage_register_element.innerHTML !== this.computer.storage_register.toString()) {
            storage_register_element.innerHTML = this.computer.storage_register.toString();
            storage_register_element.title = "Instruction: " + this.computer.storage_register.instruction.toString();
            storage_register_element.title += "\r\nFixed Point: " + this.computer.storage_register.fixed_point;
            storage_register_element.title += "\r\nFloating Point: " + this.computer.storage_register.floating_point;
        }

        const accumulator_element = $("#accumulator")[0];
        if (accumulator_element.innerHTML !== this.computer.accumulator.toString()) {
            if (this.highlighting && accumulator_element.innerHTML !== "") {
                accumulator_element.classList.add("changed");
            } else {
                accumulator_element.classList.remove("changed");
            }
            accumulator_element.innerHTML = this.computer.accumulator.toString();
            accumulator_element.title = "Fixed Point: " + this.computer.accumulator.fixed_point;
            accumulator_element.title += "\r\nFloating Point: " + this.computer.accumulator.floating_point;
        } else {
            accumulator_element.classList.remove("changed");
        }

        const mq_register_element = $("#mq_register")[0];
        if (mq_register_element.innerHTML !== this.computer.mq_register.toString()) {
            if (this.highlighting && mq_register_element.innerHTML !== "") {
                mq_register_element.classList.add("changed");
            } else {
                mq_register_element.classList.remove("changed");
            }
            mq_register_element.innerHTML = this.computer.mq_register.toString();
            mq_register_element.title = "Fixed Point: " + this.computer.mq_register.fixed_point;
            mq_register_element.title += "\r\nFloating Point: " + this.computer.mq_register.floating_point;
        } else {
            mq_register_element.classList.remove("changed");
        }

        const index_a_element = $("#index_a")[0];
        if (index_a_element.innerHTML !== this.computer.index_a.toString()) {
            if (this.highlighting && index_a_element.innerHTML !== "") {
                index_a_element.classList.add("changed");
            } else {
                index_a_element.classList.remove("changed");
            }
            index_a_element.innerHTML = this.computer.index_a.toString();
            index_a_element.title = "Value: " + this.computer.index_a.valueOf();
        } else {
            index_a_element.classList.remove("changed");
        }

        const index_b_element = $("#index_b")[0];
        if (index_b_element.innerHTML !== this.computer.index_b.toString()) {
            if (this.highlighting && index_b_element.innerHTML !== "") {
                index_b_element.classList.add("changed");
            } else {
                index_b_element.classList.remove("changed");
            }
            index_b_element.innerHTML = this.computer.index_b.toString();
            index_b_element.title = "Value: " + this.computer.index_b.valueOf();
        } else {
            index_b_element.classList.remove("changed");
        }

        const index_c_element = $("#index_c")[0];
        if (index_c_element.innerHTML !== this.computer.index_c.toString()) {
            if (this.highlighting && index_c_element.innerHTML !== "") {
                index_c_element.classList.add("changed");
            } else {
                index_c_element.classList.remove("changed");
            }
            index_c_element.innerHTML = this.computer.index_c.toString();
            index_c_element.title = "Value: " + this.computer.index_c.valueOf();
        } else {
            index_c_element.classList.remove("changed");
        }

        const changed_registers = $(".changed");
        changed_registers.addClass("blink");
        await timer(500); // jshint ignore:line
        changed_registers.removeClass("blink");

        general_memory_html.removeClass("next_instruction target_register special_highlight changed");
        const next_instruction_target = this.computer.general_memory[this.computer.ilc.valueOf()].instruction.address;
        if (this.highlighting) {
            for (let i = 0; i < this.computer.size; i++) {
                if (i === this.computer.ilc.valueOf()) {
                    general_memory_html[i].classList.add("next_instruction");
                } else if (i === next_instruction_target) {
                    general_memory_html[i].classList.add("target_register");
                } else if (highlighted_registers.includes(i)) {
                    general_memory_html[i].classList.add("special_highlight");
                }
            }
        }
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
    async update(instructions, num_code_lines, highlighted_registers = []) {

        await this.update_computer_display(highlighted_registers);

        const code_html = $(".symbolic_code");
        code_html.removeClass("next_instruction");
        const code_line = Math.min(this.computer.ilc.valueOf(), num_code_lines-1);
        if (code_html.length !== 0) {
            if (this.highlighting) {
                code_html[code_line].classList.add("next_instruction");
            }
        }

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
