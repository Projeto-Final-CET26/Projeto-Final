-- --------------------------------------------------------
-- Anfitrião:                    127.0.0.1
-- Versão do servidor:           8.4.3 - MySQL Community Server - GPL
-- SO do servidor:               Win64
-- HeidiSQL Versão:              12.17.0.7270
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- A despejar estrutura da base de dados para projeto_final
CREATE DATABASE IF NOT EXISTS `projeto_final` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `projeto_final`;

-- A despejar estrutura para tabela projeto_final.campo
DROP TABLE IF EXISTS `campo`;
CREATE TABLE IF NOT EXISTS `campo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `morada` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `cidade` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `capacidade` int NOT NULL DEFAULT (0),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- A despejar dados para tabela projeto_final.campo: ~0 rows (aproximadamente)
INSERT INTO `campo` (`id`, `nome`, `morada`, `cidade`, `capacidade`) VALUES
	(1, 'Lusitano da Luz', '', '', 0);

-- A despejar estrutura para tabela projeto_final.categoria_metricas
DROP TABLE IF EXISTS `categoria_metricas`;
CREATE TABLE IF NOT EXISTS `categoria_metricas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `desc` varchar(50) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '0',
  `desporto_id` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `FK_categoria_metricas_desportos` (`desporto_id`),
  CONSTRAINT `FK_categoria_metricas_desportos` FOREIGN KEY (`desporto_id`) REFERENCES `desportos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- A despejar dados para tabela projeto_final.categoria_metricas: ~0 rows (aproximadamente)
INSERT INTO `categoria_metricas` (`id`, `desc`, `desporto_id`) VALUES
	(35, 'Ataque', 1),
	(36, 'Defesa', 1),
	(37, 'Posses e Transição', 1),
	(38, 'Disciplina e Faltas', 1),
	(39, 'Ataque', 2),
	(40, 'Defesa', 2),
	(41, 'Construção e Passe', 2),
	(42, 'Bolas Paradas', 2),
	(43, 'Disciplina e Faltas', 2),
	(44, 'Ataque', 3),
	(45, 'Defesa e Bloco', 3),
	(46, 'Serviço e Receção', 3),
	(47, 'Ocorrências e Faltas', 3),
	(48, 'Ataque', 4),
	(49, 'Defesa e Guarda-Redes', 4),
	(50, 'Transição', 4),
	(51, 'Disciplina e Sanções', 4);

-- A despejar estrutura para tabela projeto_final.competicao
DROP TABLE IF EXISTS `competicao`;
CREATE TABLE IF NOT EXISTS `competicao` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '0',
  `tipo_competicao` int NOT NULL DEFAULT (0),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- A despejar dados para tabela projeto_final.competicao: ~0 rows (aproximadamente)

-- A despejar estrutura para tabela projeto_final.coordenadas_metrica
DROP TABLE IF EXISTS `coordenadas_metrica`;
CREATE TABLE IF NOT EXISTS `coordenadas_metrica` (
  `id` int NOT NULL AUTO_INCREMENT,
  `registo_metrica_id` int NOT NULL DEFAULT '0',
  `posicao_X` decimal(20,6) NOT NULL,
  `posicao_Y` decimal(20,6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK__metricas_id` (`registo_metrica_id`) USING BTREE,
  CONSTRAINT `FK_coordenadas_metrica_registo_metrica` FOREIGN KEY (`registo_metrica_id`) REFERENCES `registo_metrica` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- A despejar dados para tabela projeto_final.coordenadas_metrica: ~0 rows (aproximadamente)

-- A despejar estrutura para tabela projeto_final.desportos
DROP TABLE IF EXISTS `desportos`;
CREATE TABLE IF NOT EXISTS `desportos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '0',
  `icone_url` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- A despejar dados para tabela projeto_final.desportos: ~4 rows (aproximadamente)
INSERT INTO `desportos` (`id`, `nome`, `icone_url`) VALUES
	(1, 'Basquetebol', NULL),
	(2, 'Futebol', NULL),
	(3, 'Voleibol', NULL),
	(4, 'Andebol', NULL);

-- A despejar estrutura para tabela projeto_final.epoca
DROP TABLE IF EXISTS `epoca`;
CREATE TABLE IF NOT EXISTS `epoca` (
  `id` int NOT NULL AUTO_INCREMENT,
  `epoca` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- A despejar dados para tabela projeto_final.epoca: ~27 rows (aproximadamente)
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

-- A despejar estrutura para tabela projeto_final.equipa
DROP TABLE IF EXISTS `equipa`;
CREATE TABLE IF NOT EXISTS `equipa` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '0',
  `campo_id` int NOT NULL,
  `desporto_id` int NOT NULL,
  `escalao` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `cidade` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `pais` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `ano_fundacao` year DEFAULT NULL,
  `logo_url` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_equipa_campo` (`campo_id`),
  KEY `FK_equipa_desportos` (`desporto_id`),
  CONSTRAINT `FK_equipa_campo` FOREIGN KEY (`campo_id`) REFERENCES `campo` (`id`),
  CONSTRAINT `FK_equipa_desportos` FOREIGN KEY (`desporto_id`) REFERENCES `desportos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- A despejar dados para tabela projeto_final.equipa: ~0 rows (aproximadamente)
INSERT INTO `equipa` (`id`, `nome`, `campo_id`, `desporto_id`, `escalao`, `cidade`, `pais`, `ano_fundacao`, `logo_url`) VALUES
	(1, 'Lusitano FC', 1, 2, '3', 'Évora', 'Portugal', '2026', 'klknlmk'),
	(2, 'Atlético Lusitano FC', 1, 2, 'Séniores', 'Évora', 'Portugal', '1954', ''),
	(3, 'Sporting Clube Alentejano', 1, 2, 'Séniores', 'Beja', 'Portugal', '1962', ''),
	(4, 'Atlético Lusitano FC', 1, 2, 'Séniores', 'Évora', 'Portugal', '1954', ''),
	(5, 'Sporting Clube Alentejano', 1, 2, 'Séniores', 'Beja', 'Portugal', '1962', '');

-- A despejar estrutura para tabela projeto_final.gestor
DROP TABLE IF EXISTS `gestor`;
CREATE TABLE IF NOT EXISTS `gestor` (
  `id` int NOT NULL AUTO_INCREMENT,
  `primeiro_nome` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `apelido` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `equipa_id` int DEFAULT NULL,
  `utilizador_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_gestor_equipa` (`equipa_id`),
  KEY `FK_gestor_utilizadores` (`utilizador_id`),
  CONSTRAINT `FK_gestor_equipa` FOREIGN KEY (`equipa_id`) REFERENCES `equipa` (`id`),
  CONSTRAINT `FK_gestor_utilizadores` FOREIGN KEY (`utilizador_id`) REFERENCES `utilizadores` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- A despejar dados para tabela projeto_final.gestor: ~0 rows (aproximadamente)

-- A despejar estrutura para tabela projeto_final.jogador
DROP TABLE IF EXISTS `jogador`;
CREATE TABLE IF NOT EXISTS `jogador` (
  `id` int NOT NULL AUTO_INCREMENT,
  `primeiro_nome` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '0',
  `apelido` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `nacionalidade` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `data_nascimento` date NOT NULL,
  `altura_cm` float NOT NULL,
  `peso_kg` float NOT NULL,
  `foto_url` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `numero_camisola` int NOT NULL,
  `equipa_id` int NOT NULL,
  `desporto_id` int NOT NULL,
  `posicao` int NOT NULL,
  `utilizador_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_jogador_desportos` (`desporto_id`),
  KEY `FK_jogador_posicoes` (`posicao`),
  KEY `FK_jogador_utilizadores` (`utilizador_id`),
  KEY `FK_jogador_equipa` (`equipa_id`),
  CONSTRAINT `FK_jogador_desportos` FOREIGN KEY (`desporto_id`) REFERENCES `desportos` (`id`),
  CONSTRAINT `FK_jogador_equipa` FOREIGN KEY (`equipa_id`) REFERENCES `equipa` (`id`),
  CONSTRAINT `FK_jogador_posicoes` FOREIGN KEY (`posicao`) REFERENCES `posicoes` (`id`),
  CONSTRAINT `FK_jogador_utilizadores` FOREIGN KEY (`utilizador_id`) REFERENCES `utilizadores` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- A despejar dados para tabela projeto_final.jogador: ~51 rows (aproximadamente)
INSERT INTO `jogador` (`id`, `primeiro_nome`, `apelido`, `nacionalidade`, `data_nascimento`, `altura_cm`, `peso_kg`, `foto_url`, `numero_camisola`, `equipa_id`, `desporto_id`, `posicao`, `utilizador_id`) VALUES
	(2, 'Cristiano', 'Ronaldo', 'Português', '2026-11-03', 180, 75, NULL, 7, 1, 2, 15, NULL),
	(3, 'Tiago', 'Ferreira', 'Portuguesa', '1998-03-14', 189, 82, NULL, 1, 2, 2, 6, NULL),
	(4, 'Rafael', 'Mendes', 'Portuguesa', '2001-07-22', 187, 80.5, NULL, 12, 2, 2, 6, NULL),
	(5, 'Lucas', 'Oliveira', 'Brasileira', '2003-11-05', 191, 84, NULL, 24, 2, 2, 6, NULL),
	(6, 'Diogo', 'Almeida', 'Portuguesa', '1997-02-19', 186, 79, NULL, 4, 2, 2, 7, NULL),
	(7, 'Henrique', 'Silva', 'Portuguesa', '1999-09-10', 188, 81.5, NULL, 5, 2, 2, 7, NULL),
	(8, 'Mateus', 'Rocha', 'Brasileira', '2000-04-28', 185, 78, NULL, 15, 2, 2, 7, NULL),
	(9, 'André', 'Carvalho', 'Portuguesa', '2004-01-17', 184, 76.5, NULL, 22, 2, 2, 7, NULL),
	(10, 'Gonçalo', 'Costa', 'Portuguesa', '1998-06-03', 178, 73, NULL, 2, 2, 2, 8, NULL),
	(11, 'Vasco', 'Pinto', 'Portuguesa', '2002-10-12', 179, 74, NULL, 13, 2, 2, 8, NULL),
	(12, 'Pedro', 'Marques', 'Portuguesa', '1997-12-08', 177, 72.5, NULL, 3, 2, 2, 9, NULL),
	(13, 'Fábio', 'Sousa', 'Portuguesa', '2003-05-25', 176, 71, NULL, 14, 2, 2, 9, NULL),
	(14, 'Rúben', 'Lopes', 'Portuguesa', '1996-08-15', 182, 76, NULL, 6, 2, 2, 10, NULL),
	(15, 'Tomás', 'Nunes', 'Portuguesa', '2001-01-30', 180, 74.5, NULL, 16, 2, 2, 10, NULL),
	(16, 'Bruno', 'Gomes', 'Portuguesa', '1998-11-21', 179, 73.5, NULL, 8, 2, 2, 11, NULL),
	(17, 'Daniel', 'Ribeiro', 'Portuguesa', '2002-04-11', 181, 75, NULL, 18, 2, 2, 11, NULL),
	(18, 'Miguel', 'Teixeira', 'Portuguesa', '1999-03-07', 178, 72, NULL, 10, 2, 2, 12, NULL),
	(19, 'Artur', 'Cardoso', 'Brasileira', '2002-09-19', 177, 71.5, NULL, 20, 2, 2, 12, NULL),
	(20, 'Francisco', 'Martins', 'Portuguesa', '2000-02-14', 176, 70.5, NULL, 7, 2, 2, 13, NULL),
	(21, 'Rodrigo', 'Pereira', 'Portuguesa', '2003-08-29', 175, 69.5, NULL, 17, 2, 2, 13, NULL),
	(22, 'João', 'Antunes', 'Portuguesa', '1998-05-02', 177, 71, NULL, 11, 2, 2, 14, NULL),
	(23, 'Samuel', 'Araújo', 'Angolana', '2001-12-16', 179, 73, NULL, 21, 2, 2, 14, NULL),
	(24, 'Guilherme', 'Moreira', 'Portuguesa', '1997-07-04', 186, 81, NULL, 9, 2, 2, 15, NULL),
	(25, 'Gabriel', 'Santos', 'Brasileira', '2000-10-23', 185, 80, NULL, 19, 2, 2, 15, NULL),
	(26, 'David', 'Correia', 'Portuguesa', '2002-06-18', 183, 78.5, NULL, 23, 2, 2, 15, NULL),
	(27, 'Bernardo', 'Fonseca', 'Portuguesa', '2004-03-11', 184, 77.5, NULL, 25, 2, 2, 15, NULL),
	(28, 'Tiago', 'Ferreira', 'Portuguesa', '1998-03-14', 189, 82, NULL, 1, 4, 2, 6, NULL),
	(29, 'Rafael', 'Mendes', 'Portuguesa', '2001-07-22', 187, 80.5, NULL, 12, 4, 2, 6, NULL),
	(30, 'Lucas', 'Oliveira', 'Brasileira', '2003-11-05', 191, 84, NULL, 24, 4, 2, 6, NULL),
	(31, 'Diogo', 'Almeida', 'Portuguesa', '1997-02-19', 186, 79, NULL, 4, 4, 2, 7, NULL),
	(32, 'Henrique', 'Silva', 'Portuguesa', '1999-09-10', 188, 81.5, NULL, 5, 4, 2, 7, NULL),
	(33, 'Mateus', 'Rocha', 'Brasileira', '2000-04-28', 185, 78, NULL, 15, 4, 2, 7, NULL),
	(34, 'André', 'Carvalho', 'Portuguesa', '2004-01-17', 184, 76.5, NULL, 22, 4, 2, 7, NULL),
	(35, 'Gonçalo', 'Costa', 'Portuguesa', '1998-06-03', 178, 73, NULL, 2, 4, 2, 8, NULL),
	(36, 'Vasco', 'Pinto', 'Portuguesa', '2002-10-12', 179, 74, NULL, 13, 4, 2, 8, NULL),
	(37, 'Pedro', 'Marques', 'Portuguesa', '1997-12-08', 177, 72.5, NULL, 3, 4, 2, 9, NULL),
	(38, 'Fábio', 'Sousa', 'Portuguesa', '2003-05-25', 176, 71, NULL, 14, 4, 2, 9, NULL),
	(39, 'Rúben', 'Lopes', 'Portuguesa', '1996-08-15', 182, 76, NULL, 6, 4, 2, 10, NULL),
	(40, 'Tomás', 'Nunes', 'Portuguesa', '2001-01-30', 180, 74.5, NULL, 16, 4, 2, 10, NULL),
	(41, 'Bruno', 'Gomes', 'Portuguesa', '1998-11-21', 179, 73.5, NULL, 8, 4, 2, 11, NULL),
	(42, 'Daniel', 'Ribeiro', 'Portuguesa', '2002-04-11', 181, 75, NULL, 18, 4, 2, 11, NULL),
	(43, 'Miguel', 'Teixeira', 'Portuguesa', '1999-03-07', 178, 72, NULL, 10, 4, 2, 12, NULL),
	(44, 'Artur', 'Cardoso', 'Brasileira', '2002-09-19', 177, 71.5, NULL, 20, 4, 2, 12, NULL),
	(45, 'Francisco', 'Martins', 'Portuguesa', '2000-02-14', 176, 70.5, NULL, 7, 4, 2, 13, NULL),
	(46, 'Rodrigo', 'Pereira', 'Portuguesa', '2003-08-29', 175, 69.5, NULL, 17, 4, 2, 13, NULL),
	(47, 'João', 'Antunes', 'Portuguesa', '1998-05-02', 177, 71, NULL, 11, 4, 2, 14, NULL),
	(48, 'Samuel', 'Araújo', 'Angolana', '2001-12-16', 179, 73, NULL, 21, 4, 2, 14, NULL),
	(49, 'Guilherme', 'Moreira', 'Portuguesa', '1997-07-04', 186, 81, NULL, 9, 4, 2, 15, NULL),
	(50, 'Gabriel', 'Santos', 'Brasileira', '2000-10-23', 185, 80, NULL, 19, 4, 2, 15, NULL),
	(51, 'David', 'Correia', 'Portuguesa', '2002-06-18', 183, 78.5, NULL, 23, 4, 2, 15, NULL),
	(52, 'Bernardo', 'Fonseca', 'Portuguesa', '2004-03-11', 184, 77.5, NULL, 25, 4, 2, 15, NULL);

-- A despejar estrutura para tabela projeto_final.jogador_equipas
DROP TABLE IF EXISTS `jogador_equipas`;
CREATE TABLE IF NOT EXISTS `jogador_equipas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `jogador_id` int DEFAULT NULL,
  `equipa_id` int DEFAULT NULL,
  `epoca_id` int DEFAULT NULL,
  `data_inicio` int DEFAULT NULL,
  `data_fim` int DEFAULT NULL,
  `posicao_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK__jogador__` (`jogador_id`),
  KEY `FK__equipa` (`equipa_id`),
  KEY `FK__epoca` (`epoca_id`),
  KEY `FK__posicoes_` (`posicao_id`),
  CONSTRAINT `FK__epoca` FOREIGN KEY (`epoca_id`) REFERENCES `epoca` (`id`),
  CONSTRAINT `FK__equipa` FOREIGN KEY (`equipa_id`) REFERENCES `equipa` (`id`),
  CONSTRAINT `FK__jogador__` FOREIGN KEY (`jogador_id`) REFERENCES `jogador` (`id`),
  CONSTRAINT `FK__posicoes_` FOREIGN KEY (`posicao_id`) REFERENCES `posicoes` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- A despejar dados para tabela projeto_final.jogador_equipas: ~0 rows (aproximadamente)

-- A despejar estrutura para tabela projeto_final.jogo
DROP TABLE IF EXISTS `jogo`;
CREATE TABLE IF NOT EXISTS `jogo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `epoca_id` int NOT NULL,
  `campo_id` int NOT NULL,
  `equipa_casa` int NOT NULL,
  `equipa_fora` int NOT NULL,
  `pontos_casa` int NOT NULL,
  `pontos_fora` int NOT NULL,
  `data_hora` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_epoca_id` (`epoca_id`),
  KEY `FK_jogo_campo` (`campo_id`),
  KEY `FK_jogo_equipa_casa` (`equipa_casa`),
  KEY `FK_jogo_equipa_fora` (`equipa_fora`),
  CONSTRAINT `fk_epoca_id` FOREIGN KEY (`epoca_id`) REFERENCES `epoca` (`id`),
  CONSTRAINT `FK_jogo_campo` FOREIGN KEY (`campo_id`) REFERENCES `campo` (`id`),
  CONSTRAINT `FK_jogo_equipa_casa` FOREIGN KEY (`equipa_casa`) REFERENCES `equipa` (`id`),
  CONSTRAINT `FK_jogo_equipa_fora` FOREIGN KEY (`equipa_fora`) REFERENCES `equipa` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- A despejar dados para tabela projeto_final.jogo: ~2 rows (aproximadamente)
INSERT INTO `jogo` (`id`, `epoca_id`, `campo_id`, `equipa_casa`, `equipa_fora`, `pontos_casa`, `pontos_fora`, `data_hora`) VALUES
	(2, 28, 1, 1, 1, 1, 1, '2026-11-03 09:18:50'),
	(4, 2, 1, 4, 5, 0, 0, '2026-11-29 15:00:00');

-- A despejar estrutura para tabela projeto_final.jogo_jogadores
DROP TABLE IF EXISTS `jogo_jogadores`;
CREATE TABLE IF NOT EXISTS `jogo_jogadores` (
  `id` int NOT NULL AUTO_INCREMENT,
  `jogo_id` int NOT NULL,
  `equipa_id` int NOT NULL,
  `jogador_id` int NOT NULL,
  `estatuto` enum('Titular','Suplente') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `numero_camisola` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `KF_jogo_jogo` (`jogo_id`),
  KEY `FK__equipa_jogo` (`equipa_id`),
  KEY `FK__jogador_jogo` (`jogador_id`),
  CONSTRAINT `FK__equipa_jogo` FOREIGN KEY (`equipa_id`) REFERENCES `equipa` (`id`),
  CONSTRAINT `FK__jogador_jogo` FOREIGN KEY (`jogador_id`) REFERENCES `jogador` (`id`),
  CONSTRAINT `KF_jogo_jogo` FOREIGN KEY (`jogo_id`) REFERENCES `jogo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- A despejar dados para tabela projeto_final.jogo_jogadores: ~25 rows (aproximadamente)
INSERT INTO `jogo_jogadores` (`id`, `jogo_id`, `equipa_id`, `jogador_id`, `estatuto`, `numero_camisola`) VALUES
	(1, 4, 4, 28, 'Titular', 1),
	(2, 4, 4, 35, 'Titular', 2),
	(3, 4, 4, 31, 'Titular', 4),
	(4, 4, 4, 32, 'Titular', 5),
	(5, 4, 4, 37, 'Titular', 3),
	(6, 4, 4, 39, 'Titular', 6),
	(7, 4, 4, 41, 'Titular', 8),
	(8, 4, 4, 43, 'Titular', 10),
	(9, 4, 4, 45, 'Titular', 7),
	(10, 4, 4, 47, 'Titular', 11),
	(11, 4, 4, 49, 'Titular', 9),
	(12, 4, 4, 29, 'Suplente', 12),
	(13, 4, 4, 30, 'Suplente', 24),
	(14, 4, 4, 33, 'Suplente', 15),
	(15, 4, 4, 34, 'Suplente', 22),
	(16, 4, 4, 36, 'Suplente', 13),
	(17, 4, 4, 38, 'Suplente', 14),
	(18, 4, 4, 40, 'Suplente', 16),
	(19, 4, 4, 42, 'Suplente', 18),
	(20, 4, 4, 44, 'Suplente', 20),
	(21, 4, 4, 46, 'Suplente', 17),
	(22, 4, 4, 48, 'Suplente', 21),
	(23, 4, 4, 50, 'Suplente', 19),
	(24, 4, 4, 51, 'Suplente', 23),
	(25, 4, 4, 52, 'Suplente', 25);

-- A despejar estrutura para tabela projeto_final.jogo_substituicoes
DROP TABLE IF EXISTS `jogo_substituicoes`;
CREATE TABLE IF NOT EXISTS `jogo_substituicoes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `jogo_id` int NOT NULL,
  `equipa_id` int NOT NULL,
  `jogador_sai_id` int NOT NULL,
  `jogador_entra_id` int NOT NULL,
  `periodo` int NOT NULL,
  `tempo_segundos` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_jogo_substituicoes_jogo` (`jogo_id`),
  KEY `FK_jogo_substituicoes_equipa` (`equipa_id`),
  KEY `FK_jogo_substituicoes_jogador_sai` (`jogador_sai_id`),
  KEY `FK_jogo_substituicoes_jogador_entra` (`jogador_entra_id`),
  CONSTRAINT `FK_jogo_substituicoes_equipa` FOREIGN KEY (`equipa_id`) REFERENCES `equipa` (`id`),
  CONSTRAINT `FK_jogo_substituicoes_jogador_entra` FOREIGN KEY (`jogador_entra_id`) REFERENCES `jogador` (`id`),
  CONSTRAINT `FK_jogo_substituicoes_jogador_sai` FOREIGN KEY (`jogador_sai_id`) REFERENCES `jogador` (`id`),
  CONSTRAINT `FK_jogo_substituicoes_jogo` FOREIGN KEY (`jogo_id`) REFERENCES `jogo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- A despejar dados para tabela projeto_final.jogo_substituicoes: ~0 rows (aproximadamente)

-- A despejar estrutura para tabela projeto_final.lesao
DROP TABLE IF EXISTS `lesao`;
CREATE TABLE IF NOT EXISTS `lesao` (
  `id` int NOT NULL AUTO_INCREMENT,
  `estado` enum('Átiva','Recuperada') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT 'Átiva',
  `descricao` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `jogador_id` int NOT NULL,
  `epoca_id` int NOT NULL,
  `zona` int NOT NULL,
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- A despejar dados para tabela projeto_final.lesao: ~0 rows (aproximadamente)

-- A despejar estrutura para tabela projeto_final.metricas
DROP TABLE IF EXISTS `metricas`;
CREATE TABLE IF NOT EXISTS `metricas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `descricao` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `unidade` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `desporto_id` int NOT NULL,
  `categoria` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_metricas_desportos` (`desporto_id`),
  KEY `FK_metricas_categoria_metricas` (`categoria`),
  CONSTRAINT `FK_metricas_categoria_metricas` FOREIGN KEY (`categoria`) REFERENCES `categoria_metricas` (`id`),
  CONSTRAINT `FK_metricas_desportos` FOREIGN KEY (`desporto_id`) REFERENCES `desportos` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- A despejar dados para tabela projeto_final.metricas: ~0 rows (aproximadamente)
INSERT INTO `metricas` (`id`, `descricao`, `unidade`, `desporto_id`, `categoria`) VALUES
	(3, 'Remate', 'qtd', 2, 35);

-- A despejar estrutura para tabela projeto_final.metricas_jogo
DROP TABLE IF EXISTS `metricas_jogo`;
CREATE TABLE IF NOT EXISTS `metricas_jogo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `gestor_id` int NOT NULL,
  `jogador_id` int NOT NULL,
  `jogo_id` int NOT NULL,
  `equipa_id` int NOT NULL,
  `metrica_id` int NOT NULL,
  `valor` decimal(20,6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_mjogo` (`jogo_id`,`jogador_id`,`metrica_id`),
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- A despejar dados para tabela projeto_final.metricas_jogo: ~0 rows (aproximadamente)

-- A despejar estrutura para tabela projeto_final.posicao_metricas
DROP TABLE IF EXISTS `posicao_metricas`;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- A despejar dados para tabela projeto_final.posicao_metricas: ~0 rows (aproximadamente)

-- A despejar estrutura para tabela projeto_final.posicoes
DROP TABLE IF EXISTS `posicoes`;
CREATE TABLE IF NOT EXISTS `posicoes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `desporto_id` int NOT NULL,
  `nome` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `sigla` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_posicoes_desportos` (`desporto_id`),
  CONSTRAINT `FK_posicoes_desportos` FOREIGN KEY (`desporto_id`) REFERENCES `desportos` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- A despejar dados para tabela projeto_final.posicoes: ~29 rows (aproximadamente)
INSERT INTO `posicoes` (`id`, `desporto_id`, `nome`, `sigla`) VALUES
	(1, 1, 'Base', 'PG'),
	(2, 1, 'Escolta', 'SG'),
	(3, 1, 'Extremo', 'SF'),
	(4, 1, 'Extremo-Poste', 'PF'),
	(5, 1, 'Poste', 'C'),
	(6, 2, 'Guarda-Redes', 'GR'),
	(7, 2, 'Defesa Central', 'DC'),
	(8, 2, 'Lateral Direito', 'LD'),
	(9, 2, 'Lateral Esquerdo', 'LE'),
	(10, 2, 'Médio Defensivo', 'MDF'),
	(11, 2, 'Médio Centro', 'MC'),
	(12, 2, 'Médio Ofensivo', 'MO'),
	(13, 2, 'Extremo Direito', 'ED'),
	(14, 2, 'Extremo Esquerdo', 'EE'),
	(15, 2, 'Ponta de Lança', 'PL'),
	(16, 3, 'Distribuidor', 'DIS'),
	(17, 3, 'Oposto', 'OP'),
	(18, 3, 'Rececionista-Atacante (Zona 4)', 'RA'),
	(19, 3, 'Central', 'CEN'),
	(20, 3, 'Líbero', 'LIB'),
	(21, 4, 'Guarda-Redes', 'GR'),
	(22, 4, 'Ponta Esquerdo', 'PE'),
	(23, 4, 'Lateral Esquerdo', 'LE'),
	(24, 4, 'Central', 'CENT'),
	(25, 4, 'Pivô', 'PIV'),
	(26, 4, 'Lateral Direito', 'LD'),
	(27, 4, 'Ponta Direito', 'PD'),
	(28, 2, 'Médio Esquerdo', 'ME'),
	(29, 2, 'Médio Direito', 'MD');

-- A despejar estrutura para tabela projeto_final.posicoes_secundarias
DROP TABLE IF EXISTS `posicoes_secundarias`;
CREATE TABLE IF NOT EXISTS `posicoes_secundarias` (
  `id` int NOT NULL AUTO_INCREMENT,
  `posicao_id` int NOT NULL,
  `jogador_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK__posicoes` (`posicao_id`),
  KEY `FK__jogador_` (`jogador_id`),
  CONSTRAINT `FK__jogador_` FOREIGN KEY (`jogador_id`) REFERENCES `jogador` (`id`),
  CONSTRAINT `FK__posicoes` FOREIGN KEY (`posicao_id`) REFERENCES `posicoes` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- A despejar dados para tabela projeto_final.posicoes_secundarias: ~0 rows (aproximadamente)

-- A despejar estrutura para tabela projeto_final.registo_metrica
DROP TABLE IF EXISTS `registo_metrica`;
CREATE TABLE IF NOT EXISTS `registo_metrica` (
  `id` int NOT NULL AUTO_INCREMENT,
  `jogador_id` int NOT NULL,
  `equipa_id` int NOT NULL,
  `jogo_id` int NOT NULL,
  `metrica_id` int NOT NULL,
  `periodo` int NOT NULL DEFAULT '0',
  `tempo_segundos` float NOT NULL DEFAULT (0),
  `sucesso` enum('S','N','N/A') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `tem_posicao` enum('S','N') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `obs` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_registo_metrica_jogador` (`jogador_id`),
  KEY `FK_registo_metrica_jogo` (`jogo_id`),
  KEY `FK_registo_metrica_metricas` (`metrica_id`),
  KEY `FK_registo_metrica_equipa` (`equipa_id`),
  CONSTRAINT `FK_registo_metrica_equipa` FOREIGN KEY (`equipa_id`) REFERENCES `equipa` (`id`),
  CONSTRAINT `FK_registo_metrica_jogador` FOREIGN KEY (`jogador_id`) REFERENCES `jogador` (`id`),
  CONSTRAINT `FK_registo_metrica_jogo` FOREIGN KEY (`jogo_id`) REFERENCES `jogo` (`id`),
  CONSTRAINT `FK_registo_metrica_metricas` FOREIGN KEY (`metrica_id`) REFERENCES `metricas` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- A despejar dados para tabela projeto_final.registo_metrica: ~0 rows (aproximadamente)

-- A despejar estrutura para tabela projeto_final.registo_submetricas
DROP TABLE IF EXISTS `registo_submetricas`;
CREATE TABLE IF NOT EXISTS `registo_submetricas` (
  `registo_metrica_id` int NOT NULL,
  `submetrica_id` int NOT NULL,
  PRIMARY KEY (`registo_metrica_id`,`submetrica_id`),
  KEY `fk_rms_registo` (`registo_metrica_id`),
  KEY `fk_rms_submetrica` (`submetrica_id`),
  CONSTRAINT `fk_rms_registo` FOREIGN KEY (`registo_metrica_id`) REFERENCES `registo_metrica` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_rms_submetrica` FOREIGN KEY (`submetrica_id`) REFERENCES `submetricas` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- A despejar dados para tabela projeto_final.registo_submetricas: ~0 rows (aproximadamente)

-- A despejar estrutura para tabela projeto_final.submetricas
DROP TABLE IF EXISTS `submetricas`;
CREATE TABLE IF NOT EXISTS `submetricas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `metrica_id` int NOT NULL,
  `descricao` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `equipa_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK__metricas__` (`metrica_id`),
  KEY `FK_submetricas_equipa` (`equipa_id`),
  CONSTRAINT `FK__metricas__` FOREIGN KEY (`metrica_id`) REFERENCES `metricas` (`id`) ON DELETE CASCADE,
  CONSTRAINT `FK_submetricas_equipa` FOREIGN KEY (`equipa_id`) REFERENCES `equipa` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- A despejar dados para tabela projeto_final.submetricas: ~0 rows (aproximadamente)
INSERT INTO `submetricas` (`id`, `metrica_id`, `descricao`, `equipa_id`) VALUES
	(5, 3, 'Pontapé de Bicicleta', NULL),
	(6, 3, 'Cabeçeamento', NULL);

-- A despejar estrutura para tabela projeto_final.submetricas_jogo
DROP TABLE IF EXISTS `submetricas_jogo`;
CREATE TABLE IF NOT EXISTS `submetricas_jogo` (
  `jogo_id` int NOT NULL,
  `jogador_id` int NOT NULL,
  `submetrica_id` int NOT NULL,
  `valor` decimal(20,6) NOT NULL,
  PRIMARY KEY (`jogo_id`,`jogador_id`,`submetrica_id`),
  KEY `jogador_id` (`jogador_id`),
  KEY `submetrica_id` (`submetrica_id`),
  CONSTRAINT `submetricas_jogo_ibfk_1` FOREIGN KEY (`jogo_id`) REFERENCES `jogo` (`id`),
  CONSTRAINT `submetricas_jogo_ibfk_2` FOREIGN KEY (`jogador_id`) REFERENCES `jogador` (`id`),
  CONSTRAINT `submetricas_jogo_ibfk_3` FOREIGN KEY (`submetrica_id`) REFERENCES `submetricas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- A despejar dados para tabela projeto_final.submetricas_jogo: ~0 rows (aproximadamente)

-- A despejar estrutura para tabela projeto_final.tipo_competicao
DROP TABLE IF EXISTS `tipo_competicao`;
CREATE TABLE IF NOT EXISTS `tipo_competicao` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tipo` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- A despejar dados para tabela projeto_final.tipo_competicao: ~0 rows (aproximadamente)

-- A despejar estrutura para tabela projeto_final.tipo_utilizador
DROP TABLE IF EXISTS `tipo_utilizador`;
CREATE TABLE IF NOT EXISTS `tipo_utilizador` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tipo` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- A despejar dados para tabela projeto_final.tipo_utilizador: ~3 rows (aproximadamente)
INSERT INTO `tipo_utilizador` (`id`, `tipo`) VALUES
	(1, 'Admin'),
	(2, 'Gestor'),
	(3, 'Jogador');

-- A despejar estrutura para tabela projeto_final.utilizadores
DROP TABLE IF EXISTS `utilizadores`;
CREATE TABLE IF NOT EXISTS `utilizadores` (
  `id` int NOT NULL AUTO_INCREMENT,
  `primeiro_nome` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '0',
  `apelido` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `tipo` int NOT NULL DEFAULT '0',
  `password` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `foto_url` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `data_registo` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_utilizadores_tipo_utilizador` (`tipo`) USING BTREE,
  CONSTRAINT `FK_utilizadores_tipo_utilizador` FOREIGN KEY (`tipo`) REFERENCES `tipo_utilizador` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- A despejar dados para tabela projeto_final.utilizadores: ~0 rows (aproximadamente)

-- A despejar estrutura para vista projeto_final.vw_estatisticas_jogador_epoca
DROP VIEW IF EXISTS `vw_estatisticas_jogador_epoca`;
-- A criar tabela temporária para vencer erros de dependências VIEW
CREATE TABLE `vw_estatisticas_jogador_epoca` (
	`jogador_id` INT NOT NULL,
	`nome_jogador` VARCHAR(1) NULL COLLATE 'utf8mb4_general_ci',
	`epoca_id` INT NOT NULL,
	`metrica_id` INT NOT NULL,
	`metrica` VARCHAR(1) NOT NULL COLLATE 'utf8mb4_general_ci',
	`total_epoca` DECIMAL(32,2) NULL,
	`media_por_jogo` DECIMAL(14,6) NULL,
	`jogos` BIGINT NOT NULL
);

-- A despejar estrutura para vista projeto_final.vw_estatisticas_submetricas_jogador_epoca
DROP VIEW IF EXISTS `vw_estatisticas_submetricas_jogador_epoca`;
-- A criar tabela temporária para vencer erros de dependências VIEW
CREATE TABLE `vw_estatisticas_submetricas_jogador_epoca` (
	`jogador_id` INT NOT NULL,
	`nome_jogador` VARCHAR(1) NULL COLLATE 'utf8mb4_general_ci',
	`epoca_id` INT NOT NULL,
	`metrica_id` INT NOT NULL,
	`metrica` VARCHAR(1) NOT NULL COLLATE 'utf8mb4_general_ci',
	`submetrica_id` INT NOT NULL,
	`submetrica` VARCHAR(1) NOT NULL COLLATE 'utf8mb4_general_ci',
	`total_epoca` DECIMAL(42,6) NULL,
	`jogos` BIGINT NOT NULL,
	`percentagem_da_metrica` DECIMAL(43,1) NULL
);

-- A despejar estrutura para tabela projeto_final.zona_lesao
DROP TABLE IF EXISTS `zona_lesao`;
CREATE TABLE IF NOT EXISTS `zona_lesao` (
  `id` int NOT NULL AUTO_INCREMENT,
  `descricao` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `segmento` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- A despejar dados para tabela projeto_final.zona_lesao: ~0 rows (aproximadamente)
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

-- A despejar estrutura para disparador projeto_final.trg_inserir_gestor_automatico
DROP TRIGGER IF EXISTS `trg_inserir_gestor_automatico`;
SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
DELIMITER //
CREATE TRIGGER `trg_inserir_gestor_automatico` AFTER INSERT ON `utilizadores` FOR EACH ROW BEGIN
	if NEW.tipo = 2 then
		INSERT INTO gestor(primeiro_nome, apelido, equipa_id, utilizador_id) VALUES(NEW.primeiro_nome, NEW.apelido, NULL, NEW.id);
	END if;
END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

-- A remover tabela temporária e a criar estrutura VIEW final
DROP TABLE IF EXISTS `vw_estatisticas_jogador_epoca`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `vw_estatisticas_jogador_epoca` AS select `j`.`id` AS `jogador_id`,trim(concat_ws(' ',`j`.`primeiro_nome`,`j`.`apelido`)) AS `nome_jogador`,`g`.`epoca_id` AS `epoca_id`,`m`.`id` AS `metrica_id`,`m`.`descricao` AS `metrica`,sum(cast(`mj`.`valor` as decimal(10,2))) AS `total_epoca`,avg(cast(`mj`.`valor` as decimal(10,2))) AS `media_por_jogo`,count(distinct `mj`.`jogo_id`) AS `jogos` from (((`metricas_jogo` `mj` join `jogador` `j` on((`j`.`id` = `mj`.`jogador_id`))) join `jogo` `g` on((`g`.`id` = `mj`.`jogo_id`))) join `metricas` `m` on((`m`.`id` = `mj`.`metrica_id`))) group by `j`.`id`,`j`.`primeiro_nome`,`j`.`apelido`,`g`.`epoca_id`,`m`.`id`,`m`.`descricao`
;

-- A remover tabela temporária e a criar estrutura VIEW final
DROP TABLE IF EXISTS `vw_estatisticas_submetricas_jogador_epoca`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `vw_estatisticas_submetricas_jogador_epoca` AS select `t`.`jogador_id` AS `jogador_id`,`t`.`nome_jogador` AS `nome_jogador`,`t`.`epoca_id` AS `epoca_id`,`t`.`metrica_id` AS `metrica_id`,`t`.`metrica` AS `metrica`,`t`.`submetrica_id` AS `submetrica_id`,`t`.`submetrica` AS `submetrica`,`t`.`total_epoca` AS `total_epoca`,`t`.`jogos` AS `jogos`,round(((100 * `t`.`total_epoca`) / nullif(`e`.`total_epoca`,0)),1) AS `percentagem_da_metrica` from ((select `j`.`id` AS `jogador_id`,trim(concat_ws(' ',`j`.`primeiro_nome`,`j`.`apelido`)) AS `nome_jogador`,`g`.`epoca_id` AS `epoca_id`,`m`.`id` AS `metrica_id`,`m`.`descricao` AS `metrica`,`s`.`id` AS `submetrica_id`,`s`.`descricao` AS `submetrica`,sum(`sj`.`valor`) AS `total_epoca`,count(distinct `sj`.`jogo_id`) AS `jogos` from ((((`submetricas_jogo` `sj` join `submetricas` `s` on((`s`.`id` = `sj`.`submetrica_id`))) join `metricas` `m` on((`m`.`id` = `s`.`metrica_id`))) join `jogador` `j` on((`j`.`id` = `sj`.`jogador_id`))) join `jogo` `g` on((`g`.`id` = `sj`.`jogo_id`))) group by `j`.`id`,`j`.`primeiro_nome`,`j`.`apelido`,`g`.`epoca_id`,`m`.`id`,`m`.`descricao`,`s`.`id`,`s`.`descricao`) `t` left join `vw_estatisticas_jogador_epoca` `e` on(((`e`.`jogador_id` = `t`.`jogador_id`) and (`e`.`epoca_id` = `t`.`epoca_id`) and (`e`.`metrica_id` = `t`.`metrica_id`))))
;

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
