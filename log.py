from flask import Flask, request, url_for
from logdb import get_popular_article, get_popular_authors, find_anomaly

app = Flask(__name__)

HTML_WRAP = '''
<!DOCTYPE html>
<html>
<head>
    <title>Database Log Analysis</title>
</head>
<body>
    <h1>DB Log Analysis</h1>
    %s
</body>
</html>
'''

POST = '''
    <br>
    <h2>%s</h2>
    <hr>
    <div><li>%s</li><br></div>
    <hr>
'''

LIST = '''
    <ul>%s</ul>
'''

@app.route('/', methods=['GET'])
def main():
    """Main Page of the Log Analysis"""
    post_list = []
    top_articles = "".join(LIST % (article) for article in get_popular_article())
    top_articles_text = "Top Articles"
    top_article_post = POST % (top_articles_text, top_articles)
    post_list.append(top_article_post)

    top_authors = "".join(LIST % (author) for author in get_popular_authors)
    top_authors_text = "Top Authors"
    top_authors_post = POST % (top_authors_text, top_authors)
    post_list.append(top_authors_post)

    top_anomalies = "".join(LIST % (anomaly) for anomaly in find_anomaly())
    top_anomalies_text = "Top Anomalies"
    top_anomalies_post = POST % (top_anomalies_text, top_anomalies)
    post_list.append(top_anomalies_post)

    posts = "".join(post_list)
    html = HTML_WRAP % posts
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
