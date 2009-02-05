  <div class="file">
    <div class="fileHeader">
      <div class="languageBox">
	Language:
	<select name="language-${c.fileId}">
	  <option value="text">plain text</option>
	  <option value="java">java</option>
	</select>
      </div>
      <div class="fileNameBox">
	<input class="fileName" name="fileName-${c.fileId}" type="text" class=""/>
	<a class="fileName" href="#">optional file name</a>
      </div>
    </div>
    <div class="fileContent">
      <textarea name="fileContent-${c.fileId}"></textarea>
    </div>
  </div>
