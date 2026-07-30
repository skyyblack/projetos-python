SELECT p.user_id , p.bio, p.description, ur.role_id AS 'permissoes', r.name   FROM profiles AS p
INNER  JOIN users_roles AS ur ON p.user_id = ur.user_id
INNER  JOIN roles AS r ON r.id = ur.role_id;
