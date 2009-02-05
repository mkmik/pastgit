<%inherit file="master.mak"/>

<%def name="title()">Show paste</%def>

<div id="files" class="show">
% for b in c.blobs:
  <div class="file">
    <div class="fileName">
      ${b.name}
    </div>
    <div class="fileContent">${b.data}</div>
  </div>
%endfor
</div>
<div id="pasteButtons">
  <div class="pasteButton">
    <form action="${h.url(action="edit")()}" method="get">
      <input type="submit" value="Edit"/>
    </form>
  </div>
</div>
