"""Check the six published bilingual pages: python .github/scripts/check_bilingual.py [base_url]."""
from html.parser import HTMLParser
import sys
from urllib.parse import urljoin
from urllib.request import urlopen


class Page(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.lang = None
        self.switches = []
        self.links = []
        self.frames = []
        self.alternates = {}
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html":
            self.lang = attrs.get("lang")
        if tag == "a":
            self.links.append(attrs.get("href", ""))
            if "language-switch" in attrs.get("class", "").split():
                self.switches.append(attrs.get("href", ""))
        if tag == "iframe":
            self.frames.append(attrs.get("src", ""))
        if tag == "link" and attrs.get("rel") == "alternate":
            self.alternates[attrs.get("hreflang")] = attrs.get("href")


def check(base):
    for english, chinese in [("/", "/zh/"), ("/publications/", "/zh/publications/"), ("/cv/", "/zh/cv/")]:
        for route, counterpart, lang in [(english, chinese, "en-US"), (chinese, english, "zh-CN")]:
            with urlopen(urljoin(base, route), timeout=30) as response:
                html = response.read().decode("utf-8")
            page = Page(html)
            assert page.lang == lang, (route, "document language", page.lang)
            assert [urljoin(base, link) for link in page.switches] == [urljoin(base, counterpart)], (route, "language switch", page.switches)
            assert page.alternates.get("en") == urljoin(base, english), (route, "English alternate")
            assert page.alternates.get("zh-CN") == urljoin(base, chinese), (route, "Chinese alternate")
            assert "mailto:zhichenghe@u.nus.edu" in page.links, (route, "contact email")
            assert "{{" not in html and "{%" not in html, (route, "unrendered Liquid")
            if route == "/zh/":
                assert "/zh/cv/" in page.links and "/zh/publications/" in page.links
                assert "MEng by Research" in html and "共同第一作者" in html
            if route == "/zh/cv/":
                assert page.frames == ["https://drive.google.com/file/d/12sFLRFlFvZ4XTMVpTSutYwzUZKcdKYi0/preview"]
            if route == "/cv/":
                assert page.frames == ["https://drive.google.com/file/d/1LIRfYnPNvxU5Ip5ix8xk4xGYo1cuYB49/preview"]
            print(f"PASS {route}")


if __name__ == "__main__":
    check(sys.argv[1] if len(sys.argv) > 1 else "https://hezhicheng2002.github.io/")
