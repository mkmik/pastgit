<%page args="blob='', blobName='', fid=0"/>
  <div class="file">
    <div class="fileHeader">
      <div class="languageBox">
	Language:
	<select name="language-${fid}">
	  <option value="text">plain text</option>
	  <option value="java">java</option>
	</select>
      </div>
      <div class="fileNameBox">
%if blobName:
	<input class="fileName" style="display: block" value="${blobName}" name="fileName-${fid}" type="text"/>
%else:
	<input class="fileName" name="fileName-${fid}" type="text"/>
	<a class="fileName" href="#">optional file name</a>
%endif
      </div>
    </div>
    <div class="fileContent">
      <textarea name="fileContent-${fid}">${blob}</textarea>
    </div>
  </div>
