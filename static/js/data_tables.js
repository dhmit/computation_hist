"use strict";


// Defines the columns for each datatable view
const column_defs = {
    'people': [
        {data: 'name'},
        {data: 'docs_authored'},
        {data: 'docs_received'}
    ],
    'organizations': [
        {data: 'name'},
        {data: 'docs_authored'},
        {data: 'docs_received'}
    ],
    'folders': [
        {data: 'folder_number'},
        {data: 'folder_name'}
    ],
    'person_or_org': [
        {data: 'document_date'},
        {data: 'document_title'},
    ],
    'folder': [
        {data: 'doc_id'},
        {data: 'document_date'},
        {data: 'document_title'},
    ]
};

// which column (from column_defs) to sort by default and in what direction
const order_defs = {
    'people': [[1, 'desc']],
    'organizations': [[1, 'desc']],
    'folders': [[0, 'asc']],
    'person_or_org': [[0, 'asc']],
    'folder': [[0, 'asc']],
};


export function create_datatable(datatable_id, list_type, obj_list) {
    // uses datatables.js to display an interactive tables of people, organizations, folders, etc.

    $(`#${datatable_id}`).DataTable({
        data: obj_list,
        destroy: true,
        order: order_defs[list_type],
        "pageLength": 25,
        "bLengthChange": false,
        columns: column_defs[list_type],
    });
}
