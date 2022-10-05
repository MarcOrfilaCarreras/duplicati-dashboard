CREATE DATABASE `dashboard`;

USE `dashboard`;

CREATE TABLE `hosts` (
  `id` varchar(12) NOT NULL,
  `name` varchar(200) NOT NULL,
  `date_created` date NOT NULL DEFAULT current_timestamp(),
  `last_backup` datetime DEFAULT NULL
);

CREATE TABLE `tasks` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `host` varchar(12) DEFAULT NULL,
  `last_backup` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `known_file_size` float NOT NULL,
  `parsed_result` varchar(50) DEFAULT NULL,
  `backup_list_count` int(11) NOT NULL DEFAULT 0
);

ALTER TABLE `hosts`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `tasks`
  ADD PRIMARY KEY (`id`),
  ADD KEY `host` (`host`);

ALTER TABLE `tasks`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `tasks`
  ADD CONSTRAINT `tasks_ibfk_1` FOREIGN KEY (`host`) REFERENCES `hosts` (`id`);

CREATE USER 'dashboard'@'%' IDENTIFIED BY 'dashboard';
GRANT USAGE ON *.* TO 'dashboard'@'%' REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;
GRANT ALL PRIVILEGES ON dashboard.* TO 'dashboard'@'%';
