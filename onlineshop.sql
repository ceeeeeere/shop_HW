-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2022-11-08 21:07:40
-- 伺服器版本： 10.4.19-MariaDB
-- PHP 版本： 8.0.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `onlineshop`
--

-- --------------------------------------------------------

--
-- 資料表結構 `onlineshop`
--

CREATE TABLE `onlineshop` (
  `id` int(11) NOT NULL,
  `name` text DEFAULT NULL,
  `intro` text DEFAULT NULL,
  `seller` text DEFAULT NULL,
  `invenNum` int(11) DEFAULT NULL,
  `price` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `onlineshop`
--

INSERT INTO `onlineshop` (`id`, `name`, `intro`, `seller`, `invenNum`, `price`) VALUES
(1, '橄欖油', '很好喝的橄欖油', '奧立佛', 100, 100),
(2, '沙拉油', '好喝沙拉油，滋味樂無窮', '薩勒', 200, 70),
(3, '芝麻油', '閑賢知音，米偶有空', 'SENSEI', 870000, 50),
(13, '該刪除的商品', '這是一個一個一個商品啊啊啊啊啊', '先輩', 86415411, 400);

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `onlineshop`
--
ALTER TABLE `onlineshop`
  ADD PRIMARY KEY (`id`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `onlineshop`
--
ALTER TABLE `onlineshop`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
