

from bs4 import BeautifulSoup

html = """
<html>
<head><title>黑马程序员</title></head>
<body>
<p id="test01">软件测试</p>
<p id="test02">2020年</p>
<a href="/api.html">接口测试</a>
<a href="/web.html">Web自动化测试</a>
<a href="/app.html">APP自动化测试</a>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
for s in soup.find_all("a"):
     print("herf={} text={}".format(s["href"], s.string))





# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.p)
# print(soup.find_all("p"))
# print(soup.p["id"])
# print(soup.p.name)
# print(soup.p.string)

