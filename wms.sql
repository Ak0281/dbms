-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 25, 2024 at 02:39 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `wms`
--

-- --------------------------------------------------------

--
-- Table structure for table `research_scholar`
--

CREATE TABLE `research_scholar` (
  `r_sid` int(11) NOT NULL,
  `email` varchar(50) NOT NULL,
  `fname` varchar(50) NOT NULL,
  `lname` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `dept` varchar(50) NOT NULL,
  `specialization` varchar(50) NOT NULL,
  `rtopic` varchar(50) NOT NULL,
  `elevel` varchar(50) NOT NULL,
  `number` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `scientist`
--

CREATE TABLE `scientist` (
  `sid` int(11) NOT NULL,
  `fname` varchar(50) NOT NULL,
  `lname` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `number` varchar(12) NOT NULL,
  `dept` varchar(50) NOT NULL,
  `specialization` varchar(50) NOT NULL,
  `rtopic` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `scientist`
--

INSERT INTO `scientist` (`sid`, `fname`, `lname`, `email`, `number`, `dept`, `specialization`, `rtopic`) VALUES
(1, 'aditya', 'kartik', 'abc@gmail.com', '759237509', 'mechancial', 'core', 'dbms');

-- --------------------------------------------------------

--
-- Table structure for table `test`
--

CREATE TABLE `test` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(1000) NOT NULL,
  `role` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `email`, `password`, `role`) VALUES
(1, 'abc', 'abc@gmail.com', 'scrypt:32768:8:1$Xai3Ar08IGjiDqfn$b10faa184e86189ebd2335e657e201831d33f6ffb734fe7f6440b5eedf464dc4468b21740aaa210d1d2416657ae4a65445df47c32c317dd9a0539d9f49976d3c', 'scientist');

-- --------------------------------------------------------

--
-- Table structure for table `wheat`
--

CREATE TABLE `wheat` (
  `wid` int(11) NOT NULL,
  `Genotypes` varchar(50) NOT NULL,
  `R1_PH` varchar(12) NOT NULL,
  `R2_PH` varchar(12) NOT NULL,
  `R3_PH` varchar(12) NOT NULL,
  `R1_TPP` varchar(12) NOT NULL,
  `R2_TPP` varchar(12) NOT NULL,
  `R3_TPP` varchar(12) NOT NULL,
  `R1_DFF` varchar(12) NOT NULL,
  `R2_DFF` varchar(12) NOT NULL,
  `R3_DFF` varchar(12) NOT NULL,
  `R1_SPAD` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `research_scholar`
--
ALTER TABLE `research_scholar`
  ADD PRIMARY KEY (`r_sid`);

--
-- Indexes for table `scientist`
--
ALTER TABLE `scientist`
  ADD PRIMARY KEY (`sid`);

--
-- Indexes for table `test`
--
ALTER TABLE `test`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `wheat`
--
ALTER TABLE `wheat`
  ADD PRIMARY KEY (`wid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `research_scholar`
--
ALTER TABLE `research_scholar`
  MODIFY `r_sid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `scientist`
--
ALTER TABLE `scientist`
  MODIFY `sid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `test`
--
ALTER TABLE `test`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `wheat`
--
ALTER TABLE `wheat`
  MODIFY `wid` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
