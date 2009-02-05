<%inherit file="master.mak"/>

<%def name="title()">Pasted</%def>

<p>Copy this link: <a href="${h.url(action="show",id=c.pasteId)()}">${c.pasteId}</a></p>