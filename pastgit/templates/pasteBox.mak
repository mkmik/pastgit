<%page args="b='', fid=0"/>
  <div class="file">
    <div class="fileHeader">
      <div class="languageBox">
	Language:
	<select name="language-${fid or c.fileId}">
	  <option value="text">plain text</option>
	  <option value="java">java</option>
	</select>
      </div>
      <div class="fileNameBox">
%if b:
	<input class="fileName" style="display: block" value="${b.name}" name="fileName-${fid}" type="text"/>
%else:
	<input class="fileName" name="fileName-${c.fileId}" type="text"/>
	<a class="fileName" href="#">optional file name</a>
%endif
      </div>
    </div>
    <div class="fileContent">
      <textarea name="fileContent-${fid or c.fileId}">${b and b.data}</textarea>
    </div>
  </div>
