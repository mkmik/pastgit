<%inherit file="master.mak"/>

<%def name="title()">New paste</%def>

${h.start_form(h.url())}
<div id="files">
<%include file="pasteBox.mak" args="fid=c.fileId"/>
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
