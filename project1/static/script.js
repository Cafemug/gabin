$("#addNote").click(function(e) {
    e.preventDefault();

    $.ajax({
        type: "POST",
        url: $( "#addNoteForm" ).attr("action"),
        data: $( "#addNoteForm" ).serialize(),
        success: function(data){
            $("#notesContainer").prepend(data.renderedNote);
            $('#addNoteForm')[0].reset();
        },
        error:function (xhr, ajaxOptions, thrownError){
            responseCode = xhr.status;
            if(responseCode == "400" || responseCode == "403")
                alert("ERROR")
        }
    });
});