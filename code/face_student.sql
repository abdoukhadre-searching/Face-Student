-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : jeu. 29 déc. 2022 à 01:32
-- Version du serveur : 10.4.24-MariaDB
-- Version de PHP : 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `face_student`
--

-- --------------------------------------------------------

--
-- Structure de la table `etudiant`
--

CREATE TABLE `etudiant` (
  `id_etudiant` int(20) NOT NULL,
  `prenom` varchar(50) NOT NULL,
  `nom` varchar(45) DEFAULT NULL,
  `niveau` varchar(45) DEFAULT NULL,
  `sexe` varchar(45) DEFAULT NULL,
  `dateNaissance` varchar(45) DEFAULT NULL,
  `lieuNaissance` varchar(50) NOT NULL,
  `telephone` varchar(20) DEFAULT NULL,
  `absence_semestre` int(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `etudiant`
--

INSERT INTO `etudiant` (`id_etudiant`, `prenom`, `nom`, `niveau`, `sexe`, `dateNaissance`, `lieuNaissance`, `telephone`, `absence_semestre`) VALUES
(1, 'baye serigne', 'mbacke', 'Licence 2', 'Homme', '12/29/22', 'bamako', '776543456', 0),
(2, 'moustapha', 'gaye', 'Licence 3', 'Homme', '12/29/22', 'mbacke', '776543456', 0),
(3, 'thierno', 'diallo', 'Licence 3', 'Homme', '12/29/22', 'dakar', '776543456', 0),
(4, 'Modou Nar', 'ndongo', 'Licence 1', 'Homme', '12/29/22', 'Ndia', '7765432312', 0),
(5, 'abdou', 'ndiaye', 'Licence 2', 'Homme', '12/29/22', 'Dakar', '767564512', 0);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `etudiant`
--
ALTER TABLE `etudiant`
  ADD PRIMARY KEY (`id_etudiant`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `etudiant`
--
ALTER TABLE `etudiant`
  MODIFY `id_etudiant` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
