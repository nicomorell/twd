$(document).ready(function() {

	$("#about-btn").click( function(event) {
		alert("You clicked the button using JQuery!");
	});

$("#about-btn").click( function(event) {
msgstr = $("#msg").html()
        msgstr = msgstr + " is gay" 
        $("#msg").html(msgstr)
 });

$("p").hover( function() {
            $(this).css('color', 'red');
    },
    function() {
            $(this).css('color', 'blue');
    });
});
