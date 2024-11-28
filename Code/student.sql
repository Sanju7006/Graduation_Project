-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 24, 2024 at 11:41 AM
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
-- Database: `student`
--

-- --------------------------------------------------------

--
-- Table structure for table `tbl_form`
--

CREATE TABLE `tbl_form` (
  `id` int(111) NOT NULL,
  `fullname` varchar(11) NOT NULL,
  `email` varchar(20) NOT NULL,
  `username` varchar(111) NOT NULL,
  `password` varchar(111) NOT NULL,
  `cpassword` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_form`
--

INSERT INTO `tbl_form` (`id`, `fullname`, `email`, `username`, `password`, `cpassword`) VALUES
(1, '', '', 'aishwarya', 'zz', ''),
(2, '', '', 'aishwarya', 'llll', ''),
(3, '', '', '', '', ''),
(4, '', '', 'aishwarya', 'qq', ''),
(5, '', '', 'dfd', 'fd', ''),
(6, 'aa', 'chavanpriti@gmail.co', 'aishwaryakadam2303@gmail.cpm', 'aaa', ''),
(7, 'rgf', '9860471272x@ff', 'aishwarya', 'hhh', 'hhh'),
(8, '', '', '', '', ''),
(9, 's', 'chavanpriti@gmail.co', 's', 'ss', 'ss'),
(10, 'aa', 'chavanpriti@gmail.co', 'aishwarya', 'www', 'www'),
(11, 'aa', 'pp@ww', 'aishwarya', 'wwww', 'wwww'),
(12, 'aa', 'pp@ww', 'aishwarya', 'wwww', 'wwww'),
(13, '', '', 'aishwaryaaaaaaaaaaaaa', 'wwwaa', ''),
(14, 'aaaaa', 'chavanpriti@gmail.co', 'zzz', 'zzz', 'zzz'),
(15, '', '', 'zzzz', 'zzz', ''),
(16, '', '', 'aishwarya2', 's', ''),
(17, '', '', 'aa', 'a', ''),
(18, 'ewesf', 'pp@111', 'aishwarya', '<!DOCTYPE html> <html> <head> <style> body {   font-family: Arial, sans-serif;   background-color: #f2f2f2;   m', '<!DOCTYPE h'),
(19, 'ewesf', 'pp@qqqq', 'aishwarya', 'aishwarya', 'aishwarya'),
(20, '', '', 'aishwarya11111111111111111', 'aaaa', ''),
(21, '', '', 'aishwaryammnb', 'fff', ''),
(22, 'aa', 'chavanpriti@gmail.co', 'aishwarya', 'Registration ', 'Registratio'),
(23, 'aa', 'chavanpriti@gmail.co', 'aishwarya', 'Registration ', 'Registratio'),
(24, 'aa', 'chavanpriti@gmail.co', 'aishwarya', 'Registration ', 'Registratio'),
(25, 'ewesf', 'pp@223242', 'aishwaryakadam2303@gmail.cpm', 'Registration ', 'Registratio'),
(26, 'ewesf', 'pp@223242', 'aishwaryakadam2303@gmail.cpm', 'Registration ', 'Registratio'),
(27, 'ewesfwdesf', 'pp@223242', 'aishwaryakadam2303@gmail.cpm', 'Registration ', 'Registratio'),
(28, 'aa', 'chavanpriti@gmail.co', 'aishwarya', 'Registration ', 'Registratio'),
(29, 'aa', 'chavanpriti@gmail.co', 'aishwarya', 'Registration ', 'Registratio'),
(30, 'aa', 'chavanpriti@gmail.co', 'aishwarya', 'Registration ', 'Registratio'),
(31, 'aa', 'pp@223242', 'aishwarya', 'Registration ', 'Registratio'),
(32, 'aa', 'pp@223242', 'aishwarya', 'Registration ', 'Registratio'),
(33, 'aa', 'pp@223242', 'aishwarya', 'Registration ', 'Registratio'),
(34, 'aa', 'pp@223242', 'aishwarya', 'Registration ', 'Registratio'),
(35, 'aa', 'chavanpriti@gmail.co', 'aishwarya', 'Registration ', 'Registratio'),
(36, 'ewesf', 'chavanpriti@gmail.co', 'pattern=\".{6}\"', '12345678', '12345678'),
(37, 'rgf', 'chavanpriti@gmail.co', 'aishwarya', 'abcd', 'abcd'),
(38, 'ewesf', 'chavanpriti@gmail.co', 'aishwarya', 'aaaa', 'aaaa'),
(39, 'aa', 'pp@223242', 'aishwarya', 'Registration ', 'Registratio'),
(40, 'ewesf', 'pp@223242', 'aishwarya', 'aaaaaaaaa', 'aaaaaaaaa'),
(41, 'komal', 'k@123', 'komal', 'komal1234', 'komal1234'),
(42, 'aa', 'chavanpriti@gmail.co', 'aishwarya', 'Registration ', 'Registratio');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tbl_form`
--
ALTER TABLE `tbl_form`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tbl_form`
--
ALTER TABLE `tbl_form`
  MODIFY `id` int(111) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
