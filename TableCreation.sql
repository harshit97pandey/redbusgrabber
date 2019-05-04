--Create Table
IF OBJECT_ID('RedBusTable') IS NOT NULL
    BEGIN
        DROP TABLE RedBusTable;
    END;
GO
CREATE TABLE RedBusTable (
[Name] NVARCHAR(100),	
[Type] NVARCHAR(100),	
DepatureTime NVARCHAR(100),	
DepatureLocation NVARCHAR(100),	
TravelTime	NVARCHAR(100),
ArrivalTime NVARCHAR(100),	
ArrivalLocation NVARCHAR(100),
Rating	NVARCHAR(100),
NoOfRating NVARCHAR(100),	
Amount NVARCHAR(100),	
AvailableSeats	NVARCHAR(100),
AvailableWindowSeats NVARCHAR(100),
CreatedTime NVARCHAR(100)
)
GO

--Configurations
SP_CONFIGURE 'show advanced options', 1; 
GO 
RECONFIGURE; 
go
SP_CONFIGURE 'Ad Hoc Distributed Queries', 1; 
GO 
RECONFIGURE; 
EXEC sp_MSset_oledb_prop N'Microsoft.ACE.OLEDB.12.0', N'AllowInProcess', 1   
EXEC sp_MSset_oledb_prop N'Microsoft.ACE.OLEDB.12.0', N'DynamicParameters', 1

--Insert into table
DECLARE @FilePath NVARCHAR(200) = 'C:\Users\rajesh.khanna\Desktop\AllDataCollected.xlsx'
DECLARE @Sql NVARCHAR(max) = '
INSERT INTO RedBusTable
SELECT *
FROM OPENROWSET(''Microsoft.ACE.OLEDB.12.0'',
''Excel 12.0; Database='+@FilePath+ ';HDR=YES; IMEX=1'',
[Sheet1$]);'
EXEC sp_executesql @Sql 

--select * from RedBusTable

--select name from RedBusTable
--where CreatedTime like '%Apr 24 2019%'
--group by Name	,Type	,DepatureTime,	DepatureLocation,	TravelTime	,ArrivalTime	,ArrivalLocation	,
--Rating,	NoOfRating,	Amount,	CreatedTime