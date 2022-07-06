-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_genres.name AS "genre", COUNT(tv_show_genres.show_id) AS "number_of_shows" FROM tv_genres
LEFT OUTER JOIN tv_show_genres
