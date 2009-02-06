console.log("loading");

function setupEvents(context) {
    $("a.fileName", context).click(function() {
	    showFileName(this);
	});

    $(".addFileButton a", context).click(function() {
	    addFile();
	});
}

$(document).ready(function() {
	setupEvents($(document));
    });


function showFileName(el) {
    console.log("show file name " + el);

    $(el).css("display", "none");
    $(el).prev().css("display", "block");
    $(el).prev().focus();

    $(".languageBox", $(el).parent().parent()).addClass("named");
}

currentFileId = 2;

function addFile() {
    console.log("adding file");
    $.get("/dashboard/pasteBox/" + currentFileId++, {}, function(data) {
	    $("#files").append(data);
	    setupEvents($("#files .file:last-child"));
	});
}
