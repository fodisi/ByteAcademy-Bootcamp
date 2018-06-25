IF object_id('MONDAY.dbo.test') IS NOT NULL
BEGIN
DROP TABLE MONDAY.dbo.test
END

--1,000,000 Random rows of data
SELECT TOP 1000000 IDENTITY(INT,1,1) AS ID, 
RAND(CHECKSUM(NEWID())) * 30000 + CAST('1945' AS DATETIME) AS randomDate,
ABS(CHECKSUM(NEWID())) AS randomBigInt,
(ABS(CHECKSUM(NEWID())) % 100) + 1 AS randomSmallInt,
RAND(CHECKSUM(NEWID())) * 100 AS randomSmallDec,
RAND(CHECKSUM(NEWID())) AS randomTinyDec,
RAND(CHECKSUM(NEWID())) * 100000 AS randomBigDec,
CONVERT(VARCHAR(6),CONVERT(MONEY,RAND(CHECKSUM(NEWID())) * 100),0) AS randomMoney
INTO MONDAY.dbo.test
FROM master.dbo.syscolumns sc1, master.dbo.syscolumns sc2, master.dbo.syscolumns sc3

PRINT '========== BASELINE =========='
SET STATISTICS TIME ON
SELECT COUNT(*) FROM MONDAY.dbo.test
SET STATISTICS TIME OFF
PRINT REPLICATE('=',80)

--SELECT * FROM MONDAY.dbo.test