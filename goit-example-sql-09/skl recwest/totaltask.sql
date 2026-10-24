SELECT COUNT (user_id), u.fullname, u.id, t.title 
FROM users AS u
LEFT JOIN tasks AS t ON u.id = t.user_id 
GROUP BY u.fullname, u.id, t.title
