<%page args="blob='', blobName='', fid=0"/>
  <div class="file">
    <div class="fileHeader">
<% languageDisplay = "none" %>
%if blobName.startswith("pastefile"):
<% languageDisplay = "block" %>
%endif
      <div class="languageBox">
	<span style="display: ${languageDisplay}">
	Language:
	<select name="language-${fid}">
	  <option value="text">plain text</option>
	  <option value="java">java</option>
	</select>
	</span>
	%if not blobName.startswith("pastefile"):
	<span>language detected from file extension</span>
	%endif
      </div>
      <div class="fileNameBox">

	<input class="fileName" name="fileName-${fid}" value="${blobName}" type="text"/>
%if not blobName.startswith("pastefile"):
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
