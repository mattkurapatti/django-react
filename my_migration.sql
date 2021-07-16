--
-- Create model Movie
--
CREATE TABLE `movies_movie` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `movie_id` bigint NOT NULL, `title` varchar(200) NOT NULL, `match_reason` varchar(50) NOT NULL, `tagline` varchar(500) NOT NULL, `overview` varchar(1500) NOT NULL, `vote_average` numeric(3, 1) NOT NULL, `mov_url` varchar(500) NOT NULL);
--
-- Create model Keyword
--
CREATE TABLE `movies_keyword` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `word` varchar(50) NOT NULL);
CREATE TABLE `movies_keyword_movies` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `keyword_id` bigint NOT NULL, `movie_id` bigint NOT NULL);
ALTER TABLE `movies_keyword_movies` ADD CONSTRAINT `movies_keyword_movies_keyword_id_movie_id_7bcc2bb7_uniq` UNIQUE (`keyword_id`, `movie_id`);
ALTER TABLE `movies_keyword_movies` ADD CONSTRAINT `movies_keyword_movies_keyword_id_194486c4_fk_movies_keyword_id` FOREIGN KEY (`keyword_id`) REFERENCES `movies_keyword` (`id`);
ALTER TABLE `movies_keyword_movies` ADD CONSTRAINT `movies_keyword_movies_movie_id_57082a4c_fk_movies_movie_id` FOREIGN KEY (`movie_id`) REFERENCES `movies_movie` (`id`);
