<%inherit file="master.mak"/>
<%!
    from itertools import count
%>

<%def name="title()">Edit Paste</%def>

${h.start_form(h.url())}
<div id="files" class="edit">
% for fid, b in zip(count(), c.blobs):
<%include file="pasteBox.mak" args="blob=b.data, blobName=b.name, fid=fid"/>
%endfor
</div>
<div id="pasteButtons">
  <div class="addFileButton">
    <a href="#">Add file</a>
  </div>
  <div class="pasteButton">
    <input type="submit" value="Save"/>
  </div>
</div>
${h.end_form}
