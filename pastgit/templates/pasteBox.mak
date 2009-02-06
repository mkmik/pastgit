<%page args="blob='', blobName='', fid=0"/>
  <div class="file">
    <div class="fileHeader">
<% namedClass = "named" %>
%if not blobName or blobName.startswith("pastefile"):
<% namedClass = "" %>
%endif
      <div class="languageBox ${namedClass}">
	<span class="languageSelect">
	Language:
	<select name="language-${fid}">
	  <option value="text">plain text</option>
	  <option value="java">java</option>
	</select>
	</span>
	<span class="languageAuto">language detected from file extension</span>
      </div>
      <div class="fileNameBox">

	<input class="fileName" name="fileName-${fid}" value="${blobName}" type="text"/>
%if not (not blobName or blobName.startswith("pastefile")):
	<a class="fileName" href="#">${blobName}</a>
%else:
	<a class="fileName" href="#">name this file</a>
%endif
      </div>
    </div>
    <div class="fileContent">
      <textarea name="fileContent-${fid}">${blob}</textarea>
    </div>
  </div>
