-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : jeu. 19 nov. 2026 à 16:35
-- Version du serveur : 10.4.32-MariaDB
-- Version de PHP : 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `db_employees2`
--

-- --------------------------------------------------------

--
-- Structure de la table `color`
--

CREATE TABLE `color` (
  `id` int(11) NOT NULL,
  `nom` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `dextre`
--

CREATE TABLE `dextre` (
  `id` int(11) NOT NULL,
  `nom` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `employees`
--

CREATE TABLE `employees` (
  `id` int(11) NOT NULL,
  `nom` varchar(255) NOT NULL,
  `prenom` varchar(255) NOT NULL,
  `dextre` varchar(255) NOT NULL,
  `color` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `employees`
--

INSERT INTO `employees` (`id`, `nom`, `prenom`, `dextre`, `color`) VALUES
(1, 'Perrin', 'Jean', 'droitier', 'rouge'),
(2, 'David', 'Claire', 'droitier', 'bleu'),
(3, 'Morin', 'Thomas', 'droitier', 'rouge'),
(4, 'Bernard', 'Jean', 'droitier', 'bleu'),
(5, 'Roux', 'Thomas', 'ambidextre', 'bleu'),
(6, 'Chevalier', 'Claire', 'ambidextre', 'rouge'),
(7, 'Roux', 'Camille', 'ambidextre', 'rouge'),
(8, 'Dupont', 'Claire', 'ambidextre', 'rouge'),
(9, 'Dupuis', 'Lucas', 'droitier', 'bleu'),
(10, 'Gautier', 'Lucas', 'droitier', 'bleu'),
(11, 'Rousseau', 'Jean', 'gaucher', 'rouge'),
(12, 'Gauthier', 'Lucas', 'droitier', 'rouge'),
(13, 'Garnier', 'Jean', 'gaucher', 'bleu'),
(14, 'Chevalier', 'Lucas', 'ambidextre', 'rouge'),
(15, 'Francois', 'Claire', 'ambidextre', 'bleu'),
(16, 'Bernard', 'Claire', 'gaucher', 'bleu'),
(17, 'Roux', 'Jean', 'gaucher', 'rouge'),
(18, 'Andre', 'Lucas', 'droitier', 'rouge'),
(19, 'Lambert', 'Claire', 'ambidextre', 'rouge'),
(20, 'Nicolas', 'Jean', 'ambidextre', 'bleu'),
(21, 'Garnier', 'Claire', 'droitier', 'rouge'),
(22, 'Rousseau', 'Lucas', 'ambidextre', 'bleu'),
(23, 'Morin', 'Lucas', 'droitier', 'bleu'),
(24, 'Bernard', 'Lucas', 'gaucher', 'rouge'),
(25, 'Robert', 'Claire', 'ambidextre', 'rouge'),
(26, 'Leroy', 'Camille', 'gaucher', 'rouge'),
(27, 'Laurent', 'Lucas', 'droitier', 'bleu'),
(28, 'Mathieu', 'Thomas', 'ambidextre', 'rouge'),
(29, 'Mathieu', 'Thomas', 'gaucher', 'rouge'),
(30, 'Fontaine', 'Claire', 'droitier', 'rouge'),
(31, 'Richard', 'Jean', 'droitier', 'bleu'),
(32, 'Perrin', 'Claire', 'ambidextre', 'rouge'),
(33, 'Gauthier', 'Jean', 'gaucher', 'rouge'),
(34, 'Gauthier', 'Camille', 'ambidextre', 'rouge'),
(35, 'Chevalier', 'Jean', 'ambidextre', 'bleu'),
(36, 'Morin', 'Thomas', 'gaucher', 'rouge'),
(37, 'Dubois', 'Lucas', 'gaucher', 'bleu'),
(38, 'Andre', 'Jean', 'ambidextre', 'rouge'),
(39, 'Guerin', 'Claire', 'ambidextre', 'bleu'),
(40, 'Perrin', 'Lucas', 'ambidextre', 'bleu'),
(41, 'Laurent', 'Lucas', 'droitier', 'bleu'),
(42, 'Gauthier', 'Lucas', 'gaucher', 'bleu'),
(43, 'Dubois', 'Lucas', 'gaucher', 'bleu'),
(44, 'Petit', 'Claire', 'ambidextre', 'bleu'),
(45, 'Richard', 'Camille', 'droitier', 'bleu'),
(46, 'Moreau', 'Camille', 'ambidextre', 'bleu'),
(47, 'Bertrand', 'Thomas', 'ambidextre', 'rouge'),
(48, 'Leroy', 'Thomas', 'ambidextre', 'bleu'),
(49, 'Henry', 'Lucas', 'gaucher', 'rouge'),
(50, 'Faure', 'Thomas', 'gaucher', 'bleu');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `color`
--
ALTER TABLE `color`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `dextre`
--
ALTER TABLE `dextre`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `color`
--
ALTER TABLE `color`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `dextre`
--
ALTER TABLE `dextre`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
