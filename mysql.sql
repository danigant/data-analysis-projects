SELECT TOP 25 b.title, COUNT(bt.goodreads_book_id) AS tag_count
FROM BooksDB.dbo.books AS b
INNER JOIN BooksDB.dbo.book_tags AS bt
ON b.best_book_id = bt.goodreads_book_id
GROUP BY b.title
ORDER BY tag_count DESC;