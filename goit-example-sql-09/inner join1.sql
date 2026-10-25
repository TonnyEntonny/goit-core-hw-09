SELECT u.fullname, u.id, t.id, t.title AS task
FROM users AS u
INNER JOIN tasks AS t ON u.id = t.user_id
INNER JOIN status AS s ON s.id = t.status_id  WHERE s.name = 'in progress'