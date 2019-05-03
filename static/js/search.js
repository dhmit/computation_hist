'use strict';

export function start() {
    const advanced_search = $('#advanced_search');
    const adv_search_link = $('#show_advanced_search');

    // Only show advanced search fields if one of them has been filled in
    let advanced_search_fields_all_empty = true;
    for (const field of ['#title', '#text', '#author', '#recipient', '#cced',
                         '#min_year', '#max_year', '#doc_type_selector']) {

        if (field === '#doc_type_selector') {
            if (($(field).val()).length) {
                advanced_search_fields_all_empty = false;
            }
        } else if ($(field).val()) {
            advanced_search_fields_all_empty = false;
        }
    }

    if (advanced_search_fields_all_empty) {
        advanced_search.hide();
    } else {
        adv_search_link.remove();
    }

    adv_search_link.click(() => {
        advanced_search.show();
        adv_search_link.remove();
    });

    setup_refine_search();
}

export function setup_refine_search() {

    const refine_author = $("a[id^='refine_author:']"); // elements whose id starts with 'refine_author'
    for (const el of refine_author) {
        $(el).click(() => {
            const author = el.id.split(":")[1];
            $('#author').val(author);
            $('#search').submit();
        });
    }

    const refine_recipient = $("a[id^='refine_recipient:']"); // elements whose id starts with 'refine_recipient'
    for (const el of refine_recipient) {
        $(el).click(() => {
            const recipient = el.id.split(":")[1];
            $('#recipient').val(recipient);
            $('#search').submit();
        });
    }

    const refine_cced = $("a[id^='refine_cced:']"); // elements whose id starts with 'refine_cced'
    for (const el of refine_cced) {
        $(el).click(() => {
            const cced = el.id.split(":")[1];
            $('#cced').val(cced);
            $('#search').submit();
        });
    }

    const refine_year = $("a[id^='refine_year:']"); // elements whose id starts with 'refine_year'
    for (const el of refine_year) {
        $(el).click(() => {
            const year = parseInt(el.id.split(":")[1]);
            $('#min_year').val(year);
            $('#max_year').val(year);
            $('#search').submit();
        });
    }

}
