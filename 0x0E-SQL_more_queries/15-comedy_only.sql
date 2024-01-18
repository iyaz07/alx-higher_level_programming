-- List all Comedy shows in 'hbtn_0d_tvshows'
SELECT tv_shows.title FROM tv_shows
INNER JOIN tv_show_genres m ON tv_shows.id = m.show_id
INNER JOIN tv_genres o ON m.genre_id = o.id
WHERE o.name = 'Comedy'
ORDER BY tv_shows.title ASC;
