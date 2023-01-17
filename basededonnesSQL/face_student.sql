-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : mar. 17 jan. 2023 à 04:19
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
(142, 'Moustafa', 'Gaye', 'Licence 3', 'Homme', '1/16/23', 'Mbacke', '736352221', 0),
(143, 'Thierno', 'Diallo', 'Licence 3', 'Homme', '1/18/23', 'Dakar', '776556633', 0),
(144, 'Abdou ', 'Diallo', 'Licence 3', 'Homme', '1/18/23', 'Dakar', '776556633', 3);

-- --------------------------------------------------------

--
-- Structure de la table `presence`
--

CREATE TABLE `presence` (
  `id` int(20) NOT NULL,
  `date` varchar(20) NOT NULL,
  `seance` varchar(100) NOT NULL,
  `matiere` varchar(30) NOT NULL,
  `status` varchar(10) NOT NULL,
  `enseignant` varchar(100) NOT NULL,
  `idEtudiant` int(10) NOT NULL,
  `nomPrenomEtudiant` varchar(100) NOT NULL,
  `heureDebut` varchar(20) NOT NULL,
  `heureFin` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `presence`
--

INSERT INTO `presence` (`id`, `date`, `seance`, `matiere`, `status`, `enseignant`, `idEtudiant`, `nomPrenomEtudiant`, `heureDebut`, `heureFin`) VALUES
(105, '2023-01-17', 'TD', 'PYTHON', 'Présent', 'Monsieur Dahirou Gueye', 143, 'Thierno Diallo', '18:00', '01:51:17'),
(106, '2023-01-17', 'TD', 'PYTHON', 'Absent', 'Abdou khadre DIOP', 142, 'Moustafa Gaye', '18:00', '01:52:05');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `etudiant`
--
ALTER TABLE `etudiant`
  ADD PRIMARY KEY (`id_etudiant`);

--
-- Index pour la table `presence`
--
ALTER TABLE `presence`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `etudiant`
--
ALTER TABLE `etudiant`
  MODIFY `id_etudiant` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=145;

--
-- AUTO_INCREMENT pour la table `presence`
--
ALTER TABLE `presence`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=107;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
