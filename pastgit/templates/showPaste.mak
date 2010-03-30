<%inherit file="master.mak"/>

<%def name="title()">Show paste</%def>

<style type="text/css">
  ${c.highlighterStyles}
</style>

<div id="sideBox">
  <div id="history">
    <h3>History</h3>
    <ul>
%for short, id, date, revClass in c.history:
      <li class="${revClass}"><a href="${h.url(rev=id)()}">${short}</a> ${date}</li>
%endfor
    </ul>
  </div>
</div>

<div id="files" class="show">
%for b in c.blobs:
  <div class="file">
    <div>
        <div class="fileName">${b.name}</div>
        <span><a href="javascript:window.location=window.location+'/raw/${b.name}'">raw</a></span>
    </div>
    <div class="fileContent">${b.data}</div>
  </div>
%endfor
</div>
<div id="pasteButtons">
%if c.editable:
  <div class="pasteButton">
    <form action="${h.url(action="edit")()}" method="get">
      <input type="submit" value="Edit"/>
    </form>
  </div>
%endif
</div>
