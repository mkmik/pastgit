<%inherit file="master.mak"/>

<%def name="title()">New paste</%def>

${h.start_form(h.url())}
<div id="files">
  <div class="file">
    <div class="fileHeader">
      <div class="languageBox">
	Language:
	<select name="language-0">
	  <option value="text">plain text</option>
	  <option value="java">java</option>
	</select>
      </div>
      <div class="fileNameBox">
	<input class="fileName" name="fileName-0" type="text" class=""/>
	<a class="fileName" href="#">optional file name</a>
      </div>
    </div>
    <div class="fileContent">
      <textarea name="fileContent-0"></textarea>
    </div>
  </div>
</div>
<div id="pasteButtons">
  <div class="addFileButton">
    <a href="#">Add file</a>
  </div>
  <div class="pasteButton">
    <input type="submit" value="Paste"/>
  </div>
</div>
${h.end_form}
