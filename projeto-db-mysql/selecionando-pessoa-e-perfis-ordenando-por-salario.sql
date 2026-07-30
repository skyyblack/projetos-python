SELECT p.user_id , p.bio, p.description, r.name, u.salary FROM profiles AS p
INNER  JOIN users_roles AS ur ON p.user_id = ur.user_id
INNER  JOIN roles AS r ON r.id = ur.role_id
INNER JOIN users AS u ON u.id = p.user_id 
ORDER BY salary;
