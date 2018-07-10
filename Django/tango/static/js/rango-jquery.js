$(document).ready(function() {
// JQuery code to be added in here
$("#about-btn").click( function(event) {
msgstr = $("#msg").html()
msgstr = msgstr + "o"
$("#msg").html(msgstr)
});
});