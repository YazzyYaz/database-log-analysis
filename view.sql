CREATE VIEW popular_posts
AS SELECT art.title, COUNT(*) AS views
    FROM articles as art, log as l
    WHERE l.path LIKE CONCAT('/article/', art.slug)
    GROUP BY art.title
    ORDER BY views DESC;

CREATE VIEW popular_authors
AS SELECT auth.name as author, COUNT(*) AS views
    FROM articles AS art, authors AS auth, log as l
    WHERE art.author = auth.id
    AND l.path LIKE CONCAT('/article/', art.slug)
    GROUP BY auth.name
    ORDER BY views DESC;

CREATE VIEW error_log
AS SELECT time::date as day,
    ROUND(
        COUNT(status)
        FILTER (WHERE status LIKE '404 NOT FOUND') * 100::numeric) / COUNT(STATUS)::numeric, 2)
    AS error_percent
    FROM log
    GROUP BY time::date;
