-- phpMyAdmin SQL Dump
-- version 5.3.0-dev+20220527.6201c7f2ba
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 28, 2022 at 12:30 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `face_recognizer`
--

-- --------------------------------------------------------

--
-- Table structure for table `attendance`
--

CREATE TABLE `attendance` (
  `Student_id` varchar(50) NOT NULL,
  `Student_name` varchar(50) NOT NULL,
  `Course` varchar(50) NOT NULL,
  `Branch` varchar(50) NOT NULL,
  `Date` varchar(50) NOT NULL,
  `Time` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `attendance`
--

INSERT INTO `attendance` (`Student_id`, `Student_name`, `Course`, `Branch`, `Date`, `Time`) VALUES
('2014055', 'suryansh', 'MCA', 'ComputerApplication', '13-May-2022', '09:30:56:AM'),
('2014055', 'suryansh', 'MCA', 'ComputerApplication', '13-May-2022', '09:30:56:AM'),
('2014055', 'suryansh', 'MCA', 'ComputerApplication', '13-May-2022', '09:30:56:AM');

-- --------------------------------------------------------

--
-- Table structure for table `registration`
--

CREATE TABLE `registration` (
  `First_name` varchar(45) NOT NULL,
  `Last_name` varchar(45) NOT NULL,
  `Contact` varchar(45) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `Security_Ques` varchar(45) NOT NULL,
  `Security_Answer` varchar(45) NOT NULL,
  `Password` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `registration`
--

INSERT INTO `registration` (`First_name`, `Last_name`, `Contact`, `Email`, `Security_Ques`, `Security_Answer`, `Password`) VALUES
('s', '2', 'qw', 'l', 'your birth place', 'l', '1'),
('sadiq ', 'ali', '7275424276', 'sadiqali302@gmail.com', 'your birth place', 'utraula', '123'),
('Sadiq ali', 'mansoori', '7275424285', 'sadiqali@gmail.com', 'your birth place', 'utraula', 'sadiq');

-- --------------------------------------------------------

--
-- Table structure for table `studentdetails`
--

CREATE TABLE `studentdetails` (
  `Course` varchar(45) NOT NULL,
  `Branch` varchar(45) NOT NULL,
  `Year` varchar(45) NOT NULL,
  `Sem` varchar(45) NOT NULL,
  `Id` varchar(35) NOT NULL,
  `Student_Name` varchar(45) NOT NULL,
  `Father_Name` varchar(45) NOT NULL,
  `Student_Id` varchar(45) NOT NULL,
  `Gender` varchar(45) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `Phone` varchar(45) NOT NULL,
  `Adress` varchar(65) NOT NULL,
  `dob` varchar(45) NOT NULL,
  `PhotoSample` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `studentdetails`
--

INSERT INTO `studentdetails` (`Course`, `Branch`, `Year`, `Sem`, `Id`, `Student_Name`, `Father_Name`, `Student_Id`, `Gender`, `Email`, `Phone`, `Adress`, `dob`, `PhotoSample`) VALUES
('BTECH', 'ComputerApplication', '2022', '1', '1', 'sadiq ali', 'ismile', '2014', 'Male', 'sadiqali32@gmail.com', '7275424276', 'chippiya', '26-05-2022', 'Yes');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `registration`
--
ALTER TABLE `registration`
  ADD PRIMARY KEY (`Email`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;



