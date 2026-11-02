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
CREATE TABLE IF NOT EXISTS `campo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) DEFAULT NULL,
  `morada` varchar(50) DEFAULT NULL,
  `cidade` varchar(50) DEFAULT NULL,
  `capacidade` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- A despejar dados para tabela teste.campo: ~0 rows (aproximadamente)
INSERT INTO `campo` (`id`, `nome`, `morada`, `cidade`, `capacidade`) VALUES
	(1, 'Lusitano da Luz', NULL, NULL, NULL);

-- A despejar estrutura para tabela teste.competicao
CREATE TABLE IF NOT EXISTS `competicao` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL DEFAULT '0',
  `tipo_competicao` int NOT NULL DEFAULT (0),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- A despejar dados para tabela teste.competicao: ~0 rows (aproximadamente)

-- A despejar estrutura para tabela teste.desportos
CREATE TABLE IF NOT EXISTS `desportos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL DEFAULT '0',
  `icone_url` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- A despejar dados para tabela teste.desportos: ~4 rows (aproximadamente)

-- A despejar estrutura para tabela teste.epoca
CREATE TABLE IF NOT EXISTS `epoca` (
  `id` int NOT NULL AUTO_INCREMENT,
  `epoca` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- A despejar dados para tabela teste.epoca: ~17 rows (aproximadamente)
INSERT INTO `epoca` (`id`, `epoca`) VALUES
	(2, '2000/2001'),
	(3, '2001/2002'),
	(4, '2002/2003'),
	(5, '2003/2004'),
	(6, '2004/2005'),
	(7, '2005/2006'),
	(8, '2006/2007'),
	(9, '2007/2008'),
	(10, '2008/2009'),
	(11, '2009/2010'),
	(12, '2010/2011'),
	(13, '2011/2012'),
	(14, '2012/2013'),
	(15, '2013/2014'),
	(16, '2014/2015'),
	(17, '2015/2016'),
	(18, '2016/2017'),
	(19, '2017/2018'),
	(20, '2018/2019'),
	(21, '2019/2020'),
	(22, '2020/2021'),
	(23, '2021/2022'),
	(24, '2022/2023'),
	(25, '2023/2024'),
	(26, '2024/2025'),
	(27, '2025/2026'),
	(28, '2026/2027');

-- A despejar estrutura para tabela teste.equipa
CREATE TABLE IF NOT EXISTS `equipa` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL DEFAULT '0',
  `campo_id` int NOT NULL,
  `desporto_id` int DEFAULT NULL,
  `escalao` varchar(50) DEFAULT NULL,
  `cidade` varchar(50) DEFAULT NULL,
  `pais` varchar(50) DEFAULT NULL,
  `ano_fundacao` year DEFAULT NULL,
  `logo_url` text,
  PRIMARY KEY (`id`),
  KEY `FK_equipa_campo` (`campo_id`),
  KEY `FK_equipa_desportos` (`desporto_id`),
  CONSTRAINT `FK_equipa_campo` FOREIGN KEY (`campo_id`) REFERENCES `campo` (`id`),
  CONSTRAINT `FK_equipa_desportos` FOREIGN KEY (`desporto_id`) REFERENCES `desportos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- A despejar dados para tabela teste.equipa: ~0 rows (aproximadamente)
INSERT INTO `equipa` (`id`, `nome`, `campo_id`, `desporto_id`, `escalao`, `cidade`, `pais`, `ano_fundacao`, `logo_url`) VALUES
	(1, 'Lusitano FC', 1, NULL, NULL, NULL, NULL, NULL, NULL);

-- A despejar estrutura para tabela teste.gestor
CREATE TABLE IF NOT EXISTS `gestor` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) DEFAULT NULL,
  `equipa_id` int NOT NULL,
  `utilizador_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_gestor_equipa` (`equipa_id`),
  KEY `FK_gestor_utilizadores` (`utilizador_id`),
  CONSTRAINT `FK_gestor_equipa` FOREIGN KEY (`equipa_id`) REFERENCES `equipa` (`id`),
  CONSTRAINT `FK_gestor_utilizadores` FOREIGN KEY (`utilizador_id`) REFERENCES `utilizadores` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- A despejar dados para tabela teste.gestor: ~0 rows (aproximadamente)

-- A despejar estrutura para tabela teste.jogador
CREATE TABLE IF NOT EXISTS `jogador` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL DEFAULT '0',
  `nacionalidade` varchar(50) NOT NULL,
  `data_nascimento` date NOT NULL,
  `altura_cm` float NOT NULL,
  `peso_kg` float NOT NULL,
  `foto_url` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `numero_camisola` int NOT NULL,
  `desporto_id` int NOT NULL DEFAULT '0',
  `posicao` int NOT NULL,
  `utilizador_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_jogador_desportos` (`desporto_id`),
  KEY `FK_jogador_posicoes` (`posicao`),
  KEY `FK_jogador_utilizadores` (`utilizador_id`),
  CONSTRAINT `FK_jogador_desportos` FOREIGN KEY (`desporto_id`) REFERENCES `desportos` (`id`),
  CONSTRAINT `FK_jogador_posicoes` FOREIGN KEY (`posicao`) REFERENCES `posicoes` (`id`),
  CONSTRAINT `FK_jogador_utilizadores` FOREIGN KEY (`utilizador_id`) REFERENCES `utilizadores` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- A despejar dados para tabela teste.jogador: ~0 rows (aproximadamente)

-- A despejar estrutura para tabela teste.jogador_equipas
CREATE TABLE IF NOT EXISTS `jogador_equipas` (
  `jogador_id` int DEFAULT NULL,
  `equipa_id` int DEFAULT NULL,
  `epoca_id` int DEFAULT NULL,
  `data_inicio` int DEFAULT NULL,
  `data_fim` int DEFAULT NULL,
  `posicao_id` int DEFAULT NULL,
  KEY `FK__jogador__` (`jogador_id`),
  KEY `FK__equipa` (`equipa_id`),
  KEY `FK__epoca` (`epoca_id`),
  KEY `FK__posicoes_` (`posicao_id`),
  CONSTRAINT `FK__epoca` FOREIGN KEY (`epoca_id`) REFERENCES `epoca` (`id`),
  CONSTRAINT `FK__equipa` FOREIGN KEY (`equipa_id`) REFERENCES `equipa` (`id`),
  CONSTRAINT `FK__jogador__` FOREIGN KEY (`jogador_id`) REFERENCES `jogador` (`id`),
  CONSTRAINT `FK__posicoes_` FOREIGN KEY (`posicao_id`) REFERENCES `posicoes` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- A despejar dados para tabela teste.jogador_equipas: ~0 rows (aproximadamente)

-- A despejar estrutura para tabela teste.jogo
CREATE TABLE IF NOT EXISTS `jogo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `jogo` varchar(50) NOT NULL DEFAULT '0',
  `epoca_id` int NOT NULL,
  `campo_id` int NOT NULL,
  `competicao_id` int DEFAULT NULL,
  `equipa_casa` int DEFAULT NULL,
  `equipa_fora` int DEFAULT NULL,
  `pontos_casa` int DEFAULT NULL,
  `pontos_fora` int DEFAULT NULL,
  `data_hora` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_epoca_id` (`epoca_id`),
  KEY `FK_jogo_campo` (`campo_id`),
  KEY `FK_jogo_competicao` (`competicao_id`),
  KEY `FK_jogo_equipa_casa` (`equipa_casa`),
  KEY `FK_jogo_equipa_fora` (`equipa_fora`),
  CONSTRAINT `fk_epoca_id` FOREIGN KEY (`epoca_id`) REFERENCES `epoca` (`id`),
  CONSTRAINT `FK_jogo_campo` FOREIGN KEY (`campo_id`) REFERENCES `campo` (`id`),
  CONSTRAINT `FK_jogo_competicao` FOREIGN KEY (`competicao_id`) REFERENCES `competicao` (`id`),
  CONSTRAINT `FK_jogo_equipa_casa` FOREIGN KEY (`equipa_casa`) REFERENCES `equipa` (`id`),
  CONSTRAINT `FK_jogo_equipa_fora` FOREIGN KEY (`equipa_fora`) REFERENCES `equipa` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- A despejar dados para tabela teste.jogo: ~0 rows (aproximadamente)

-- A despejar estrutura para tabela teste.lesao
CREATE TABLE IF NOT EXISTS `lesao` (
  `id` int NOT NULL AUTO_INCREMENT,
  `estado` enum('Átiva','Recuperada') NOT NULL DEFAULT 'Átiva',
  `descricao` varchar(50) NOT NULL,
  `jogador_id` int NOT NULL DEFAULT (0),
  `epoca_id` int NOT NULL DEFAULT (0),
  `zona` int NOT NULL DEFAULT (0),
  `data_inicio` date NOT NULL,
  `data_prevista_fim` date DEFAULT NULL,
  `data_fim` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK__jogador___` (`jogador_id`),
  KEY `FK__epoca_` (`epoca_id`),
  KEY `FK_lesao_zona_lesao` (`zona`),
  CONSTRAINT `FK__epoca_` FOREIGN KEY (`epoca_id`) REFERENCES `epoca` (`id`),
  CONSTRAINT `FK__jogador___` FOREIGN KEY (`jogador_id`) REFERENCES `jogador` (`id`),
  CONSTRAINT `FK_lesao_zona_lesao` FOREIGN KEY (`zona`) REFERENCES `zona_lesao` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- A despejar dados para tabela teste.lesao: ~0 rows (aproximadamente)

-- A despejar estrutura para tabela teste.metricas
CREATE TABLE IF NOT EXISTS `metricas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `descricao` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `unidade` varchar(50) DEFAULT NULL,
  `desporto_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_metricas_desportos` (`desporto_id`),
  CONSTRAINT `FK_metricas_desportos` FOREIGN KEY (`desporto_id`) REFERENCES `desportos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- A despejar dados para tabela teste.metricas: ~0 rows (aproximadamente)

-- A despejar estrutura para tabela teste.metricas_jogo
CREATE TABLE IF NOT EXISTS `metricas_jogo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `gestor_id` int NOT NULL,
  `jogador_id` int NOT NULL,
  `jogo_id` int NOT NULL,
  `equipa_id` int NOT NULL,
  `metrica_id` int NOT NULL,
  `valor` decimal(20,6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK__gestor` (`gestor_id`),
  KEY `FK__jogador` (`jogador_id`),
  KEY `FK__jogo` (`jogo_id`),
  KEY `FK__metricas` (`metrica_id`),
  KEY `FK_metricas_jogo_equipa` (`equipa_id`),
  CONSTRAINT `FK__gestor` FOREIGN KEY (`gestor_id`) REFERENCES `gestor` (`id`),
  CONSTRAINT `FK__jogador` FOREIGN KEY (`jogador_id`) REFERENCES `jogador` (`id`),
  CONSTRAINT `FK__jogo` FOREIGN KEY (`jogo_id`) REFERENCES `jogo` (`id`),
  CONSTRAINT `FK__metricas` FOREIGN KEY (`metrica_id`) REFERENCES `metricas` (`id`),
  CONSTRAINT `FK_metricas_jogo_equipa` FOREIGN KEY (`equipa_id`) REFERENCES `equipa` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- A despejar dados para tabela teste.metricas_jogo: ~0 rows (aproximadamente)

-- A despejar estrutura para tabela teste.posicao_metricas
CREATE TABLE IF NOT EXISTS `posicao_metricas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `posicao_id` int NOT NULL,
  `metrica_id` int NOT NULL,
  `equipa_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_pm_posicao` (`posicao_id`),
  KEY `fk_pm_metrica` (`metrica_id`),
  KEY `fk_pm_equipa` (`equipa_id`),
  CONSTRAINT `fk_pm_equipa` FOREIGN KEY (`equipa_id`) REFERENCES `equipa` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_pm_metrica` FOREIGN KEY (`metrica_id`) REFERENCES `metricas` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_pm_posicao` FOREIGN KEY (`posicao_id`) REFERENCES `posicoes` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- A despejar dados para tabela teste.posicao_metricas: ~0 rows (aproximadamente)

-- A despejar estrutura para tabela teste.posicoes
CREATE TABLE IF NOT EXISTS `posicoes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `desporto_id` int NOT NULL,
  `nome` varchar(50) NOT NULL,
  `sigla` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_posicoes_desportos` (`desporto_id`),
  CONSTRAINT `FK_posicoes_desportos` FOREIGN KEY (`desporto_id`) REFERENCES `desportos` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- A despejar dados para tabela teste.posicoes: ~27 rows (aproximadamente)

-- A despejar estrutura para tabela teste.posicoes_secundarias
CREATE TABLE IF NOT EXISTS `posicoes_secundarias` (
  `posicao_id` int DEFAULT NULL,
  `jogador_id` int DEFAULT NULL,
  KEY `FK__posicoes` (`posicao_id`),
  KEY `FK__jogador_` (`jogador_id`),
  CONSTRAINT `FK__jogador_` FOREIGN KEY (`jogador_id`) REFERENCES `jogador` (`id`),
  CONSTRAINT `FK__posicoes` FOREIGN KEY (`posicao_id`) REFERENCES `posicoes` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- A despejar dados para tabela teste.posicoes_secundarias: ~0 rows (aproximadamente)

-- A despejar estrutura para tabela teste.registo_metrica
CREATE TABLE IF NOT EXISTS `registo_metrica` (
  `id` int NOT NULL AUTO_INCREMENT,
  `jogador_id` int NOT NULL DEFAULT '0',
  `jogo_id` int NOT NULL DEFAULT (0),
  `metrica_id` int NOT NULL DEFAULT '0',
  `periodo` int NOT NULL DEFAULT '0',
  `tempo_segundos` int NOT NULL DEFAULT '0',
  `sucesso` enum('1','0') NOT NULL,
  `obs` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `FK_registo_metrica_jogador` (`jogador_id`),
  KEY `FK_registo_metrica_jogo` (`jogo_id`),
  KEY `FK_registo_metrica_metricas` (`metrica_id`),
  CONSTRAINT `FK_registo_metrica_jogador` FOREIGN KEY (`jogador_id`) REFERENCES `jogador` (`id`),
  CONSTRAINT `FK_registo_metrica_jogo` FOREIGN KEY (`jogo_id`) REFERENCES `jogo` (`id`),
  CONSTRAINT `FK_registo_metrica_metricas` FOREIGN KEY (`metrica_id`) REFERENCES `metricas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- A despejar dados para tabela teste.registo_metrica: ~0 rows (aproximadamente)

-- A despejar estrutura para tabela teste.tipo_competicao
CREATE TABLE IF NOT EXISTS `tipo_competicao` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tipo` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- A despejar dados para tabela teste.tipo_competicao: ~0 rows (aproximadamente)

-- A despejar estrutura para tabela teste.tipo_utilizador
CREATE TABLE IF NOT EXISTS `tipo_utilizador` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tipo` varchar(50) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- A despejar dados para tabela teste.tipo_utilizador: ~0 rows (aproximadamente)
INSERT INTO `tipo_utilizador` (`id`, `tipo`) VALUES
	(4, 'Admin'),
	(5, 'Gestor'),
	(6, 'Jogador');

-- A despejar estrutura para tabela teste.utilizadores
CREATE TABLE IF NOT EXISTS `utilizadores` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL DEFAULT '0',
  `tipo` int NOT NULL DEFAULT '0',
  `password` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `email` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `foto_url` text,
  `data_registo` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_utilizadores_tipo_utilizador` (`tipo`) USING BTREE,
  CONSTRAINT `FK_utilizadores_tipo_utilizador` FOREIGN KEY (`tipo`) REFERENCES `tipo_utilizador` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- A despejar dados para tabela teste.utilizadores: ~0 rows (aproximadamente)

-- A despejar estrutura para vista teste.vw_estatisticas_jogador_epoca
-- A criar tabela temporária para vencer erros de dependências VIEW
CREATE TABLE `vw_estatisticas_jogador_epoca` (
	`jogador_id` INT NOT NULL,
	`nome_jogador` VARCHAR(1) NOT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`epoca_id` INT NOT NULL,
	`metrica_id` INT NOT NULL,
	`metrica` VARCHAR(1) NULL COLLATE 'utf8mb4_0900_ai_ci',
	`total_epoca` DECIMAL(32,2) NULL,
	`media_por_jogo` DECIMAL(14,6) NULL,
	`jogos` BIGINT NOT NULL
) ENGINE=MyISAM;

-- A despejar estrutura para tabela teste.zona_lesao
CREATE TABLE IF NOT EXISTS `zona_lesao` (
  `id` int NOT NULL AUTO_INCREMENT,
  `descricao` varchar(50) DEFAULT NULL,
  `segmento` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- A despejar dados para tabela teste.zona_lesao: ~0 rows (aproximadamente)
INSERT INTO `zona_lesao` (`id`, `descricao`, `segmento`) VALUES
	(1, 'Cabeça / Crânio', 'Cabeça e Pescoço'),
	(2, 'Rosto / Face', 'Cabeça e Pescoço'),
	(3, 'Coluna Cervical / Pescoço', 'Cabeça e Pescoço'),
	(4, 'Ombro', 'Membros Superiores'),
	(5, 'Clavícula', 'Membros Superiores'),
	(6, 'Braço / Bíceps / Tríceps', 'Membros Superiores'),
	(7, 'Cotovelo', 'Membros Superiores'),
	(8, 'Antebraço', 'Membros Superiores'),
	(9, 'Punho / Pulso', 'Membros Superiores'),
	(10, 'Mão / Dedos', 'Membros Superiores'),
	(11, 'Peito / Tórax / Costelas', 'Tronco'),
	(12, 'Abdómen', 'Tronco'),
	(13, 'Coluna Lombar / Costas', 'Tronco'),
	(14, 'Anca / Pélvis', 'Anca e Virilha'),
	(15, 'Virilha / Adutores', 'Anca e Virilha'),
	(16, 'Glúteo', 'Anca e Virilha'),
	(17, 'Coxa Anterior (Quadríceps)', 'Membros Inferiores'),
	(18, 'Coxa Posterior (Isquiotibiais)', 'Membros Inferiores'),
	(19, 'Joelho (Ligamentos / Menisco)', 'Membros Inferiores'),
	(20, 'Rótula / Tendão Rotuliano', 'Membros Inferiores'),
	(21, 'Perna / Tíbia / Perónio', 'Membros Inferiores'),
	(22, 'Gémeos / Panturrilha', 'Membros Inferiores'),
	(23, 'Tendão de Aquiles', 'Membros Inferiores'),
	(24, 'Tornozelo', 'Membros Inferiores'),
	(25, 'Pé / Dedos do Pé', 'Membros Inferiores'),
	(26, 'Planta do Pé / Fascia Plantar', 'Membros Inferiores');

-- A despejar estrutura para disparador teste.trg_inserir_gestor_automatico
SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
DELIMITER //
CREATE TRIGGER `trg_inserir_gestor_automatico` AFTER INSERT ON `utilizadores` FOR EACH ROW BEGIN
    -- Verifica se o tipo de utilizador inserido é o 5
    IF NEW.tipo = 5 THEN
        INSERT INTO `gestor` (`nome`, `equipa_id`, `utilizador_id`) 
        VALUES (NEW.nome, NULL, NEW.id);
    END IF;
END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

-- A remover tabela temporária e a criar estrutura VIEW final
DROP TABLE IF EXISTS `vw_estatisticas_jogador_epoca`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `vw_estatisticas_jogador_epoca` AS select `j`.`id` AS `jogador_id`,`j`.`nome` AS `nome_jogador`,`g`.`epoca_id` AS `epoca_id`,`m`.`id` AS `metrica_id`,`m`.`descricao` AS `metrica`,sum(cast(`mj`.`valor` as decimal(10,2))) AS `total_epoca`,avg(cast(`mj`.`valor` as decimal(10,2))) AS `media_por_jogo`,count(distinct `mj`.`jogo_id`) AS `jogos` from (((`metricas_jogo` `mj` join `jogador` `j` on((`j`.`id` = `mj`.`jogador_id`))) join `jogo` `g` on((`g`.`id` = `mj`.`jogo_id`))) join `metricas` `m` on((`m`.`id` = `mj`.`metrica_id`))) group by `j`.`id`,`j`.`nome`,`g`.`epoca_id`,`m`.`id`,`m`.`descricao`;

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
