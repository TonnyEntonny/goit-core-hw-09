SELECT fullname, email
FROM users
WHERE email LIKE '%@example.net%'
ORDER BY email;