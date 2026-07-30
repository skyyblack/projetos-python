INSERT INTO profiles 
(bio, description, user_id)
SELECT CONCAT('bio de ', first_name), CONCAT('Description de ',first_name), id 
FROM users u; 


DELETE FROM profiles; 