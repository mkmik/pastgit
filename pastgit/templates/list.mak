<%inherit file="master.mak"/>

<%def name="title()">Recent pastes</%def>

<ul>
%for i in c.ids:
 <li><a href="${h.url(controller="/dashboard",action="show", id=i, rev=None)()}">${i}</a></li>
%endfor
</ul>
