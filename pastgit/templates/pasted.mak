<%inherit file="master.mak"/>

<%def name="title()">Pasted</%def>

<p>Copy this link: <a href="${h.url(controller="/dashboard", action="show", id=c.pasteId, rev=None)()}">${c.pasteId}</a></p>