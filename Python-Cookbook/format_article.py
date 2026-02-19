import json

def format_article_email(article_json):
    articles = article_json.get("results", [])
    email_body = """
    <html>
    <head>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.6;
                color: #333;
            }
            h2 {
                color: #007BFF;
            }
            p {
                margin: 5px 0;
            }
            a {
                color: #007BFF;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
            hr {
                border: 0;
                height: 1px;
                background: #ddd;
                margin: 20px 0;
            }
        </style>
    </head>
    <body>
    """

    for article in articles:
        email_body += f"<h2>{article.get('title', 'No Title')}</h2>"
        email_body += f"<p><strong>Description:</strong> {article.get('description', 'No Description')}</p>"
        email_body += f"<p><strong>Link:</strong> <a href='{article.get('link', '#')}'>Read more</a></p>"
        email_body += f"<p><strong>Source:</strong> {article.get('source_name', 'No Source')}</p>"
        email_body += f"<p><strong>Published Date:</strong> {article.get('pubDate', 'No Date')}</p>"
        email_body += "<hr>"

    email_body += "</body></html>"
    return email_body