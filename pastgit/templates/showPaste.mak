<%inherit file="master.mak"/>

<%def name="title()">Paste</%def>

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
