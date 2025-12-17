-- MySQL dump 10.13  Distrib 8.0.43, for macos15 (arm64)
--
-- Host: localhost    Database: university_db
-- ------------------------------------------------------
-- Server version	8.0.43

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `enrollments`
--

DROP TABLE IF EXISTS `enrollments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `enrollments` (
  `enrollment_id` int NOT NULL AUTO_INCREMENT,
  `student_id` int NOT NULL,
  `subject_id` int NOT NULL,
  `academic_year` varchar(9) NOT NULL,
  `semester` int NOT NULL,
  `enrolled_date` date DEFAULT NULL,
  PRIMARY KEY (`enrollment_id`),
  UNIQUE KEY `uk_enrollments` (`student_id`,`subject_id`,`academic_year`,`semester`),
  KEY `idx_enrollments_student` (`student_id`),
  KEY `idx_enrollments_subject` (`subject_id`),
  CONSTRAINT `enrollments_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `students` (`student_id`) ON DELETE CASCADE,
  CONSTRAINT `enrollments_ibfk_2` FOREIGN KEY (`subject_id`) REFERENCES `subjects` (`subject_id`) ON DELETE CASCADE,
  CONSTRAINT `enrollments_chk_1` CHECK ((`semester` in (1,2)))
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `enrollments`
--

LOCK TABLES `enrollments` WRITE;
/*!40000 ALTER TABLE `enrollments` DISABLE KEYS */;
INSERT INTO `enrollments` VALUES (1,1,1,'2024-2025',1,'2025-12-16'),(2,1,3,'2024-2025',1,'2025-12-16'),(3,1,4,'2024-2025',1,'2025-12-16'),(4,2,1,'2024-2025',1,'2025-12-16'),(5,2,2,'2024-2025',2,'2025-12-16'),(6,3,1,'2024-2025',1,'2025-12-16'),(7,3,3,'2024-2025',1,'2025-12-16'),(8,4,1,'2024-2025',1,'2025-12-16'),(9,4,4,'2024-2025',1,'2025-12-16'),(10,5,2,'2024-2025',2,'2025-12-16'),(11,1,6,'2024-2025',1,'2025-12-16'),(12,2,6,'2024-2025',1,'2025-12-16'),(13,3,6,'2024-2025',1,'2025-12-16'),(14,4,6,'2024-2025',1,'2025-12-16'),(15,2,4,'2024-2025',1,'2025-12-16'),(16,1,1,'2023-2024',1,'2023-09-01'),(17,1,2,'2023-2024',2,'2023-09-01'),(18,1,3,'2023-2024',1,'2023-09-01'),(19,1,1,'2025-2026',1,'2025-09-01'),(21,1,4,'2025-2026',1,'2025-09-01');
/*!40000 ALTER TABLE `enrollments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grades`
--

DROP TABLE IF EXISTS `grades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `grades` (
  `grade_id` int NOT NULL AUTO_INCREMENT,
  `student_id` int NOT NULL,
  `subject_id` int NOT NULL,
  `teacher_id` int NOT NULL,
  `grade` int NOT NULL,
  `grade_date` date DEFAULT NULL,
  `academic_year` varchar(9) NOT NULL,
  `semester` int NOT NULL,
  PRIMARY KEY (`grade_id`),
  KEY `idx_grades_student` (`student_id`),
  KEY `idx_grades_subject` (`subject_id`),
  KEY `idx_grades_teacher` (`teacher_id`),
  CONSTRAINT `grades_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `students` (`student_id`) ON DELETE CASCADE,
  CONSTRAINT `grades_ibfk_2` FOREIGN KEY (`subject_id`) REFERENCES `subjects` (`subject_id`) ON DELETE CASCADE,
  CONSTRAINT `grades_ibfk_3` FOREIGN KEY (`teacher_id`) REFERENCES `teachers` (`teacher_id`) ON DELETE CASCADE,
  CONSTRAINT `grades_chk_1` CHECK ((`grade` between 1 and 5)),
  CONSTRAINT `grades_chk_2` CHECK ((`semester` in (1,2)))
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grades`
--

LOCK TABLES `grades` WRITE;
/*!40000 ALTER TABLE `grades` DISABLE KEYS */;
INSERT INTO `grades` VALUES (1,1,1,1,5,'2025-12-16','2024-2025',1),(2,1,3,2,4,'2025-12-16','2024-2025',1),(3,1,4,4,3,'2025-12-16','2024-2025',1),(4,2,1,1,4,'2025-12-16','2024-2025',1),(5,2,2,1,5,'2025-12-16','2024-2025',2),(6,3,1,3,3,'2025-12-16','2024-2025',1),(7,3,3,2,5,'2025-12-16','2024-2025',1),(8,4,1,1,2,'2025-12-16','2024-2025',1),(9,4,4,4,4,'2025-12-16','2024-2025',1),(10,5,2,1,2,'2025-12-16','2024-2025',2),(11,1,6,1,5,'2025-12-16','2024-2025',1),(12,2,6,1,4,'2025-12-16','2024-2025',1),(13,3,6,1,5,'2025-12-16','2024-2025',1),(14,4,6,1,3,'2025-12-16','2024-2025',1),(15,2,3,2,2,'2025-12-16','2024-2025',1),(16,2,3,2,2,'2025-12-16','2024-2025',1),(17,2,4,4,2,'2025-12-16','2024-2025',1),(18,2,3,2,2,'2025-12-16','2024-2025',1),(19,2,4,4,2,'2025-12-16','2024-2025',1),(20,1,1,1,4,'2023-12-15','2023-2024',1),(21,1,2,1,3,'2024-05-20','2023-2024',2),(22,1,3,2,5,'2023-12-10','2023-2024',1),(23,1,1,1,5,'2025-12-15','2025-2026',1),(25,1,4,4,4,'2025-12-10','2025-2026',1),(26,5,2,1,3,'2025-06-15','2024-2025',2);
/*!40000 ALTER TABLE `grades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students` (
  `student_id` int NOT NULL AUTO_INCREMENT,
  `full_name` varchar(255) NOT NULL,
  `birth_date` date NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` varchar(20) NOT NULL,
  `group_number` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`student_id`),
  KEY `idx_students_full_name` (`full_name`),
  KEY `idx_students_email` (`email`),
  CONSTRAINT `students_chk_1` CHECK (((`email` like _utf8mb4'%@%') or (`email` is null)))
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES (1,'Иван Петров','2005-03-15','ivan.petrov@example.com','+79123456789','Б23-01'),(2,'Петр Иванов','2004-05-20','petr.ivanov@example.com','+79987654321','Б23-01'),(3,'Анна Сидорова','2005-08-10','anna.sidorova@example.com','+79654321098','Б23-02'),(4,'Сергей Смирнов','2004-11-25','sergey.smirnov@example.com','+79111222333','Б23-02'),(5,'Мария Волкова','2005-01-30','maria.volkova@example.com','+79444555666','Б23-03'),(8,'Алексей Козлов','2005-07-12','alexey.kozlov@example.com','+79155556666','Б23-04');
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subjects`
--

DROP TABLE IF EXISTS `subjects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `subjects` (
  `subject_id` int NOT NULL AUTO_INCREMENT,
  `subject_name` varchar(255) NOT NULL,
  `category` varchar(50) NOT NULL,
  `description` text,
  `credits` int DEFAULT NULL,
  PRIMARY KEY (`subject_id`),
  CONSTRAINT `subjects_chk_1` CHECK ((`category` in (_utf8mb4'Математические',_utf8mb4'Гуманитарные',_utf8mb4'Естественные',_utf8mb4'Прочие')))
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subjects`
--

LOCK TABLES `subjects` WRITE;
/*!40000 ALTER TABLE `subjects` DISABLE KEYS */;
INSERT INTO `subjects` VALUES (1,'Математика','Математические','Основы математического анализа',4),(2,'Алгебра','Математические','Линейная алгебра и матрицы',3),(3,'История России','Гуманитарные','История России XX века',3),(4,'Английский язык','Гуманитарные','Практический английский язык',4),(6,'Дифференциальные уравнения','Математические','Теория дифференциальных уравнений',4);
/*!40000 ALTER TABLE `subjects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teachers`
--

DROP TABLE IF EXISTS `teachers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teachers` (
  `teacher_id` int NOT NULL AUTO_INCREMENT,
  `full_name` varchar(255) NOT NULL,
  `birth_date` date NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` varchar(20) NOT NULL,
  `department` varchar(100) NOT NULL,
  PRIMARY KEY (`teacher_id`),
  KEY `idx_teachers_full_name` (`full_name`),
  KEY `idx_teachers_email` (`email`),
  CONSTRAINT `teachers_chk_1` CHECK (((`email` like _utf8mb4'%@%') or (`email` is null)))
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teachers`
--

LOCK TABLES `teachers` WRITE;
/*!40000 ALTER TABLE `teachers` DISABLE KEYS */;
INSERT INTO `teachers` VALUES (1,'Дмитрий Калугин','1975-05-20','dmitry.new@example.com','+79159999999','Кафедра математики'),(2,'Елена Петрова','1980-08-15','elena.petrova@example.com','+79123222222','Кафедра истории'),(3,'Владимир Сидоров','1978-03-10','vladimir.sidorov@example.com','+79123333333','Кафедра математики'),(4,'Ольга Смирнова','1982-12-01','olga.smirnova@example.com','+79123444444','Кафедра иностранных языков');
/*!40000 ALTER TABLE `teachers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teaching_assignments`
--

DROP TABLE IF EXISTS `teaching_assignments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teaching_assignments` (
  `assignment_id` int NOT NULL AUTO_INCREMENT,
  `teacher_id` int NOT NULL,
  `subject_id` int NOT NULL,
  `academic_year` varchar(9) NOT NULL,
  `semester` int NOT NULL,
  `assigned_date` date DEFAULT NULL,
  PRIMARY KEY (`assignment_id`),
  UNIQUE KEY `uk_teaching` (`teacher_id`,`subject_id`,`academic_year`,`semester`),
  KEY `idx_teaching_assignments_teacher` (`teacher_id`),
  KEY `idx_teaching_assignments_subject` (`subject_id`),
  CONSTRAINT `teaching_assignments_ibfk_1` FOREIGN KEY (`teacher_id`) REFERENCES `teachers` (`teacher_id`) ON DELETE CASCADE,
  CONSTRAINT `teaching_assignments_ibfk_2` FOREIGN KEY (`subject_id`) REFERENCES `subjects` (`subject_id`) ON DELETE CASCADE,
  CONSTRAINT `teaching_assignments_chk_1` CHECK ((`semester` in (1,2)))
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teaching_assignments`
--

LOCK TABLES `teaching_assignments` WRITE;
/*!40000 ALTER TABLE `teaching_assignments` DISABLE KEYS */;
INSERT INTO `teaching_assignments` VALUES (1,1,1,'2024-2025',1,'2025-12-16'),(2,1,2,'2024-2025',2,'2025-12-16'),(4,3,1,'2024-2025',1,'2025-12-16'),(5,2,3,'2024-2025',1,'2025-12-16'),(6,4,4,'2024-2025',1,'2025-12-16'),(7,1,6,'2024-2025',1,'2025-12-16'),(8,1,1,'2023-2024',1,'2023-09-01'),(9,1,2,'2023-2024',2,'2023-09-01'),(10,2,3,'2023-2024',1,'2023-09-01'),(11,4,4,'2023-2024',1,'2023-09-01'),(12,1,1,'2025-2026',1,'2025-09-01'),(14,4,4,'2025-2026',1,'2025-09-01');
/*!40000 ALTER TABLE `teaching_assignments` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-12-17 22:03:51
