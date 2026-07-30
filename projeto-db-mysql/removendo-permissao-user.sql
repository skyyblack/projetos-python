
SELECT user_id, role_id FROM users_roles AS ur
right JOIN users as u
ON ur.user_id  = u.id
WHERE u.id = 212;

DELETE ur FROM users_roles AS ur 
WHERE user_id = 212;