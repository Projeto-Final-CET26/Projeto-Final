-- --------------------------------------------------------
-- Anfitrião:                    127.0.0.1
-- Versão do servidor:           8.4.3 - MySQL Community Server - GPL
-- SO do servidor:               Win64
-- HeidiSQL Versão:              12.8.0.6908
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- A despejar estrutura da base de dados para teste
CREATE DATABASE IF NOT EXISTS `teste` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `teste`;

-- A despejar estrutura para tabela teste.campo
DROP TABLE IF EXISTS `campo`;
CREATE TABLE IF NOT EXISTS `campo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Exportação de dados não seleccionada.

-- A despejar estrutura para tabela teste.competicao
DROP TABLE IF EXISTS `competicao`;
CREATE TABLE IF NOT EXISTS `competicao` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL DEFAULT '0',
  `tipo_competicao` int NOT NULL DEFAULT (0),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Exportação de dados não seleccionada.

-- A despejar estrutura para tabela teste.desportos
DROP TABLE IF EXISTS `desportos`;
CREATE TABLE IF NOT EXISTS `desportos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Exportação de dados não seleccionada.

-- A despejar estrutura para tabela teste.epoca
DROP TABLE IF EXISTS `epoca`;
CREATE TABLE IF NOT EXISTS `epoca` (
  `id` int NOT NULL AUTO_INCREMENT,
  `epoca` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Exportação de dados não seleccionada.

-- A despejar estrutura para tabela teste.equipa
DROP TABLE IF EXISTS `equipa`;
CREATE TABLE IF NOT EXISTS `equipa` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL DEFAULT '0',
  `campo_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_equipa_campo` (`campo_id`),
  CONSTRAINT `FK_equipa_campo` FOREIGN KEY (`campo_id`) REFERENCES `campo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Exportação de dados não seleccionada.

-- A despejar estrutura para tabela teste.gestor
DROP TABLE IF EXISTS `gestor`;
CREATE TABLE IF NOT EXISTS `gestor` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL DEFAULT '0',
  `equipa_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_gestor_equipa` (`equipa_id`),
  CONSTRAINT `FK_gestor_equipa` FOREIGN KEY (`equipa_id`) REFERENCES `equipa` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Exportação de dados não seleccionada.

-- A despejar estrutura para tabela teste.jogador
DROP TABLE IF EXISTS `jogador`;
CREATE TABLE IF NOT EXISTS `jogador` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Exportação de dados não seleccionada.

-- A despejar estrutura para tabela teste.jogo
DROP TABLE IF EXISTS `jogo`;
CREATE TABLE IF NOT EXISTS `jogo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `jogo` varchar(50) NOT NULL DEFAULT '0',
  `epoca_id` int NOT NULL,
  `campo_id` int NOT NULL,
  `competicao_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_epoca_id` (`epoca_id`),
  KEY `FK_jogo_campo` (`campo_id`),
  KEY `FK_jogo_competicao` (`competicao_id`),
  CONSTRAINT `fk_epoca_id` FOREIGN KEY (`epoca_id`) REFERENCES `epoca` (`id`),
  CONSTRAINT `FK_jogo_campo` FOREIGN KEY (`campo_id`) REFERENCES `campo` (`id`),
  CONSTRAINT `FK_jogo_competicao` FOREIGN KEY (`competicao_id`) REFERENCES `competicao` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Exportação de dados não seleccionada.

-- A despejar estrutura para tabela teste.metricas
DROP TABLE IF EXISTS `metricas`;
CREATE TABLE IF NOT EXISTS `metricas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `metrica` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Exportação de dados não seleccionada.

-- A despejar estrutura para tabela teste.metricas_jogo
DROP TABLE IF EXISTS `metricas_jogo`;
CREATE TABLE IF NOT EXISTS `metricas_jogo` (
  `desporto_id` int NOT NULL,
  `gestor_id` int NOT NULL,
  `jogador_id` int NOT NULL,
  `jogo_id` int NOT NULL,
  `metrica_id` int NOT NULL,
  `valor` varchar(50) DEFAULT NULL,
  KEY `FK__desportos` (`desporto_id`),
  KEY `FK__gestor` (`gestor_id`),
  KEY `FK__jogador` (`jogador_id`),
  KEY `FK__jogo` (`jogo_id`),
  KEY `FK__metricas` (`metrica_id`),
  CONSTRAINT `FK__desportos` FOREIGN KEY (`desporto_id`) REFERENCES `desportos` (`id`),
  CONSTRAINT `FK__gestor` FOREIGN KEY (`gestor_id`) REFERENCES `gestor` (`id`),
  CONSTRAINT `FK__jogador` FOREIGN KEY (`jogador_id`) REFERENCES `jogador` (`id`),
  CONSTRAINT `FK__jogo` FOREIGN KEY (`jogo_id`) REFERENCES `jogo` (`id`),
  CONSTRAINT `FK__metricas` FOREIGN KEY (`metrica_id`) REFERENCES `metricas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Exportação de dados não seleccionada.

-- A despejar estrutura para tabela teste.tipo_competicao
DROP TABLE IF EXISTS `tipo_competicao`;
CREATE TABLE IF NOT EXISTS `tipo_competicao` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tipo` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Exportação de dados não seleccionada.

-- A despejar estrutura para tabela teste.tipo_utilizador
DROP TABLE IF EXISTS `tipo_utilizador`;
CREATE TABLE IF NOT EXISTS `tipo_utilizador` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tipo` varchar(50) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Exportação de dados não seleccionada.

-- A despejar estrutura para tabela teste.utilizadores
DROP TABLE IF EXISTS `utilizadores`;
CREATE TABLE IF NOT EXISTS `utilizadores` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL DEFAULT '0',
  `tipo` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `FK_utilizadores_tipo_utilizador` (`tipo`),
  CONSTRAINT `FK_utilizadores_tipo_utilizador` FOREIGN KEY (`tipo`) REFERENCES `tipo_utilizador` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Exportação de dados não seleccionada.

-- A despejar estrutura para vista teste.vw_estatisticas_jogador_epoca
DROP VIEW IF EXISTS `vw_estatisticas_jogador_epoca`;
-- A criar tabela temporária para vencer erros de dependências VIEW
CREATE TABLE `vw_estatisticas_jogador_epoca` (
	`jogador_id` INT NOT NULL,
	`nome_jogador` VARCHAR(1) NOT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`epoca_id` INT NOT NULL,
	`metrica` VARCHAR(1) NULL COLLATE 'utf8mb4_0900_ai_ci',
	`total_epoca` DOUBLE NULL,
	`media_por_jogo` DOUBLE NULL
) ENGINE=MyISAM;

-- A remover tabela temporária e a criar estrutura VIEW final
DROP TABLE IF EXISTS `vw_estatisticas_jogador_epoca`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `vw_estatisticas_jogador_epoca` AS select `j`.`id` AS `jogador_id`,`j`.`nome` AS `nome_jogador`,`jog`.`epoca_id` AS `epoca_id`,`m`.`metrica` AS `metrica`,sum(`me`.`valor`) AS `total_epoca`,avg(`me`.`valor`) AS `media_por_jogo` from (((`metricas_jogo` `me` join `jogador` `j` on((`me`.`jogador_id` = `j`.`id`))) join `jogo` `jog` on((`me`.`jogo_id` = `jog`.`id`))) join `metricas` `m` on((`me`.`metrica_id` = `m`.`id`))) group by `j`.`id`,`jog`.`epoca_id`,`me`.`metrica_id`;

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
