var currentAddNewNoteFormVisibility = false;

function toggleAddNewNoteFormVisibility() {
    currentAddNewNoteFormVisibility = !currentAddNewNoteFormVisibility;
    if (currentAddNewNoteFormVisibility) {
        showAddNewNoteForm();
    } else {
        hideAddNewNoteForm();
    }
}

function showAddNewNoteForm() {
    $("#add_notes_div").show();
}

function hideAddNewNoteForm() {
    $("#add_notes_div").hide()
}

$(document).ready( function () {
        hideAddNewNoteForm();
});

