"use strict";

export function create_datatable(list_type, obj_list) {
    // uses datatables.js to display an interactive table
    // of people, organizations, or folders.

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
        ]
    };

    const order_defs = {
        'people': [[1, 'desc']],
        'organizations': [[1, 'desc']],
        'folders': [[0, 'asc']]
    };

    $('#data_table').DataTable({
        data: obj_list,
        destroy: true,
        order: order_defs[list_type],
        "pageLength": 25,
        "bLengthChange": false,
        columns: column_defs[list_type]
    });
}
