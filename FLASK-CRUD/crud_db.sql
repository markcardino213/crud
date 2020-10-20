-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 20, 2020 at 08:30 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `crud_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `crud_data`
--

CREATE TABLE `crud_data` (
  `id_data` int(11) NOT NULL,
  `idno` varchar(225) NOT NULL,
  `name` varchar(255) NOT NULL,
  `course` varchar(255) NOT NULL,
  `yrlvl` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `crud_data`
--

INSERT INTO `crud_data` (`id_data`, `idno`, `name`, `course`, `yrlvl`, `email`) VALUES
(1, '2018-1197', 'Mark Jason Torres Cardino', 'BSCS', '3', 'markjason.cardino0401@g.msuiit.edu.ph'),
(39, '2019-0660', 'Jason Cardino', 'BSCS', '3', 'jasoncardino151@gmail.com'),
(66, '0000-0001', 'Mark Jason Torres Cardino', 'BSCS', '4', 'markjason.cardino0401@g.msuiit.edu.ph');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `crud_data`
--
ALTER TABLE `crud_data`
  ADD PRIMARY KEY (`id_data`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `crud_data`
--
ALTER TABLE `crud_data`
  MODIFY `id_data` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=67;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
