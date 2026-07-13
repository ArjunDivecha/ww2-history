import os
import ssl
import urllib.request
import urllib.error
from html.parser import HTMLParser

class LinkExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == 'a' and 'href' in attrs_dict:
            self.links.append(('a', attrs_dict['href']))
        elif tag == 'img' and 'src' in attrs_dict:
            self.links.append(('img', attrs_dict['src']))
        elif tag == 'link' and 'href' in attrs_dict:
            rel = attrs_dict.get('rel', '')
            if rel == 'stylesheet':
                self.links.append(('stylesheet', attrs_dict['href']))

def check_local_file(html_file, path):
    # Resolve relative path
    dir_path = os.path.dirname(html_file)
    target_path = os.path.normpath(os.path.join(dir_path, path))
    
    # Strip query parameters or hashes if present
    target_path = target_path.split('#')[0].split('?')[0]
    
    return os.path.exists(target_path)

def check_external_url(url, ssl_context):
    print(f"  Checking external URL: {url}")
    try:
        # Mimic a modern browser user agent
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
        )
        with urllib.request.urlopen(req, timeout=10, context=ssl_context) as response:
            return response.status in [200, 301, 302]
    except urllib.error.HTTPError as e:
        # Treat 403 Forbidden or 401 Unauthorized as warning, since they indicate the link resolves but blocks bots
        if e.code in [403, 401]:
            print(f"    Warning: URL returned HTTP status {e.code} (potentially anti-bot). Link is likely OK.")
            return True
        print(f"    ERROR: HTTP status {e.code} for URL: {url}")
        return False
    except urllib.error.URLError as e:
        print(f"    ERROR: URL Error: {e.reason} for URL: {url}")
        return False
    except Exception as e:
        print(f"    ERROR: Unexpected error: {e} for URL: {url}")
        return False

def main():
    battles_dir = "battles"
    errors = 0
    
    # Create unverified SSL context to bypass local issuer certificate chain errors
    ssl_context = ssl._create_unverified_context()
    
    if not os.path.exists(battles_dir):
        print(f"Error: {battles_dir} directory not found.")
        return
        
    html_files = [os.path.join(battles_dir, f) for f in os.listdir(battles_dir) if f.endswith(".html")]
    # Include main index.html
    html_files.append("index.html")
    
    print(f"Found {len(html_files)} HTML files to verify links inside.")
    
    for html_file in html_files:
        print(f"\nScanning: {html_file}")
        with open(html_file, "r", encoding="utf-8") as f:
            content = f.read()
            
        parser = LinkExtractor()
        parser.feed(content)
        
        for link_type, link in parser.links:
            # Skip empty, mailto, javascript, or hash-only links
            if not link or link.startswith('#') or link.startswith('mailto:') or link.startswith('javascript:'):
                continue
                
            # External Links
            if link.startswith('http://') or link.startswith('https://'):
                if not check_external_url(link, ssl_context):
                    errors += 1
                    print(f"  [FAIL] Broken external link in {html_file}: {link}")
                else:
                    print(f"  [PASS] {link}")
            # Local assets or links
            else:
                if not check_local_file(html_file, link):
                    errors += 1
                    print(f"  [FAIL] Broken local reference in {html_file}: {link}")
                else:
                    print(f"  [PASS] Local path: {link}")
                    
    print("\n" + "="*40)
    print(f"Scan complete. Total errors found: {errors}")
    if errors > 0:
        exit(1)
    else:
        print("All internal and external links are functioning perfectly!")
        exit(0)

if __name__ == "__main__":
    main()
