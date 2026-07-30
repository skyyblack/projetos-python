-- banco_de_dados.profiles definição

CREATE TABLE `profiles` (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
`bio` text,
`description` text,
`user_id` int UNSIGNED DEFAULT NULL,
PRIMARY KEY (`id`),
UNIQUE KEY `profiles_un_user_id` (`user_id`),
CONSTRAINT `profiles_users_FK` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON
DELETE
    CASCADE ON
    UPDATE
        CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 687 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;


-- banco_de_dados.roles definição

CREATE TABLE `roles` (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
`name` varchar(100) NOT NULL,
PRIMARY KEY (`id`)
) ENGINE = InnoDB AUTO_INCREMENT = 7 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;


-- banco_de_dados.users definição

CREATE TABLE `users` (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
`first_name` varchar(150) NOT NULL,
`last_name` varchar(150) DEFAULT NULL,
`email` varchar(255) NOT NULL,
`password_hash` varchar(255) NOT NULL,
`created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
`updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON
UPDATE
    CURRENT_TIMESTAMP,
    `salary` decimal(15, 2) DEFAULT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `users_un_email` (`email`),
    UNIQUE KEY `users_un_password_hash` (`password_hash`)
) ENGINE = InnoDB AUTO_INCREMENT = 213 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

-- banco_de_dados.users_roles definição

CREATE TABLE `users_roles` (
  `user_id` int UNSIGNED NOT NULL,
`role_id` int UNSIGNED NOT NULL,
`created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
`updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON
UPDATE
    CURRENT_TIMESTAMP,
    PRIMARY KEY (`user_id`,
    `role_id`),
    KEY `users_role_roles_FK` (`role_id`),
    CONSTRAINT `users_role_roles_FK` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`) ON
    DELETE
        CASCADE ON
        UPDATE
            CASCADE,
            CONSTRAINT `users_role_users_FK` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON
            DELETE
                CASCADE ON
                UPDATE
                    CASCADE
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;