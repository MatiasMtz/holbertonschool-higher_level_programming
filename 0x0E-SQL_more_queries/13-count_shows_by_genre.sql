-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_genres.name AS "genre", COUNT(*) AS showsCount FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres."genre_id"
GROUP BY tv_genres.name ORDER BY showsCount DESC;
