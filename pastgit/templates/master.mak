<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" http://www.w3.org/TR/html4/loose.dtd>
<html>
  
  <%def name="title()">default title</%def>
  <%def name="subtitle()"></%def>

  <head>
    <meta http-equiv=content-type content="text/html; charset=UTF-8">
    <title>${self.title()}</title>
    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.2.6/jquery.min.js"></script>

    <script type="text/javascript" src="/js/pastgit.js"></script>

    ${h.stylesheet_link_tag("/css/common.css")}
    ${h.stylesheet_link_tag("/css/pastgit.css")}
  </head>
  <body>
    <div id="nav">
      <div align="right">
	<a href="${h.url(controller="dashboard", action="index", id=None)()}">New </a>
      </div>
    </div>

    <div id="messageBox">
      % if session.get('message'):
      <div class="message ${session['message'].type}">
        ${session['message'].message}
<%
session['message'] = None
session.save()
%>
      </div>
      % endif
    </div>
    <h1 id="header"><span>Pastgit - Paste with the power of git</span></h1>
    <h2><span>${self.subtitle()}</span></h2>
    <div id="content">
      ${next.body()}
    </div>
  </body>
</html>
