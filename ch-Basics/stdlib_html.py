import html

print(html.escape("This HTML fragment contains a <script>script</script>"))


#Escape removes the grt and lt sign to &lt; and &gt;

print(html.unescape("I &hearts; Python &lt;standard library&gt;.")) 
