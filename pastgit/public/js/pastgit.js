console.log("loading");

$(document).ready(function() {
	console.log("ready");

	$("a.fileName").click(function() {
		showFileName(this);
	    });

	$(".addFileButton a").click(function() {
		addFile();
	    });

	console.log("finish");
    });


function showFileName(el) {
    console.log("show file name " + el);

    $(el).css("display", "none");
    $(el).prev().css("display", "block");
    $(el).prev().focus();
}

currentFileId = 1;

function addFile() {
    console.log("adding file");
    var copy = $("#files > .file").html();
    copy = '<div class="file">' + copy + '</div>';
    var newhtml = copy.replace(/-0/g, "-" + currentFileId++);

    $("#files").append(newhtml);
}
