USE [master]
GO
/****** Object:  Database [covid-19control]    Script Date: 2023/6/26 15:43:19 ******/
CREATE DATABASE [covid-19control]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'covid-19control', FILENAME = N'D:\SQL_Server\Instance\MSSQL16.MYSQLSERVER\MSSQL\DATA\covid-19control.mdf' , SIZE = 2891776KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'covid-19control_log', FILENAME = N'D:\SQL_Server\Instance\MSSQL16.MYSQLSERVER\MSSQL\DATA\covid-19control_log.ldf' , SIZE = 11935744KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT, LEDGER = OFF
GO
ALTER DATABASE [covid-19control] SET COMPATIBILITY_LEVEL = 160
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [covid-19control].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [covid-19control] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [covid-19control] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [covid-19control] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [covid-19control] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [covid-19control] SET ARITHABORT OFF 
GO
ALTER DATABASE [covid-19control] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [covid-19control] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [covid-19control] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [covid-19control] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [covid-19control] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [covid-19control] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [covid-19control] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [covid-19control] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [covid-19control] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [covid-19control] SET  DISABLE_BROKER 
GO
ALTER DATABASE [covid-19control] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [covid-19control] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [covid-19control] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [covid-19control] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [covid-19control] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [covid-19control] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [covid-19control] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [covid-19control] SET RECOVERY SIMPLE 
GO
ALTER DATABASE [covid-19control] SET  MULTI_USER 
GO
ALTER DATABASE [covid-19control] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [covid-19control] SET DB_CHAINING OFF 
GO
ALTER DATABASE [covid-19control] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [covid-19control] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [covid-19control] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [covid-19control] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
ALTER DATABASE [covid-19control] SET QUERY_STORE = ON
GO
ALTER DATABASE [covid-19control] SET QUERY_STORE (OPERATION_MODE = READ_WRITE, CLEANUP_POLICY = (STALE_QUERY_THRESHOLD_DAYS = 30), DATA_FLUSH_INTERVAL_SECONDS = 900, INTERVAL_LENGTH_MINUTES = 60, MAX_STORAGE_SIZE_MB = 1000, QUERY_CAPTURE_MODE = AUTO, SIZE_BASED_CLEANUP_MODE = AUTO, MAX_PLANS_PER_QUERY = 200, WAIT_STATS_CAPTURE_MODE = ON)
GO
USE [covid-19control]
GO
/****** Object:  Table [dbo].[20221001]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221001](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221002]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221002](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221003]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221003](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221004]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221004](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221005]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221005](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221006]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221006](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221007]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221007](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221008]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221008](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221009]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221009](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221010]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221010](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221011]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221011](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221012]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221012](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221013]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221013](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221014]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221014](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221015]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221015](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221016]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221016](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221017]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221017](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221018]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221018](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221019]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221019](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221020]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221020](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221021]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221021](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221022]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221022](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221023]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221023](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221024]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221024](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221025]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221025](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221026]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221026](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221027]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221027](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221028]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221028](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221029]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221029](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221030]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221030](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221031]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221031](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221101]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221101](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221102]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221102](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221103]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221103](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221104]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221104](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221105]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221105](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221106]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221106](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221107]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221107](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221108]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221108](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221109]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221109](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221110]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221110](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221111]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221111](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221112]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221112](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221113]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221113](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221114]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221114](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221115]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221115](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221116]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221116](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221117]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221117](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221118]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221118](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221119]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221119](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221120]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221120](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221121]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221121](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221122]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221122](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221123]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221123](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221124]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221124](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221125]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221125](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221126]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221126](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221127]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221127](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221128]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221128](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221129]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221129](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[20221130]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[20221130](
	[sno] [bigint] NULL,
	[grid_point_id] [float] NULL,
	[user_id] [bigint] NULL,
	[temperature] [float] NULL,
	[create_time] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[场所码扫码信息表]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[场所码扫码信息表](
	[sno] [int] NULL,
	[grid_point_id] [int] NULL,
	[user_id] [int] NULL,
	[temperature] [decimal](18, 2) NULL,
	[create_time] [datetime] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[场所信息表]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[场所信息表](
	[grid_point_id] [int] NOT NULL,
	[name] [nvarchar](255) NULL,
	[point_type] [nvarchar](50) NOT NULL,
	[x_coordinate] [decimal](12, 2) NULL,
	[y_coordinate] [decimal](12, 2) NULL,
	[create_time] [datetime] NULL,
 CONSTRAINT [PK_场所信息表] PRIMARY KEY CLUSTERED 
(
	[grid_point_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[个人自查上报信息表]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[个人自查上报信息表](
	[sno] [int] NOT NULL,
	[user_id] [int] NOT NULL,
	[x_coordinate] [decimal](12, 2) NULL,
	[y_coordinate] [decimal](12, 2) NULL,
	[symptom] [int] NULL,
	[nucleic_acid_result] [int] NULL,
	[resident_flag] [int] NULL,
	[dump_time] [datetime] NULL,
 CONSTRAINT [PK_个人自查上报信息表_1] PRIMARY KEY CLUSTERED 
(
	[sno] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[核酸采样检测信息表]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[核酸采样检测信息表](
	[sno] [int] NULL,
	[user_id] [int] NULL,
	[cysj] [datetime] NULL,
	[jcsj] [datetime] NULL,
	[jg] [varchar](20) NULL,
	[grid_point_id] [int] NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[人员信息表]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[人员信息表](
	[user_id] [int] NOT NULL,
	[openid] [nvarchar](255) NULL,
	[gender] [nvarchar](2) NULL,
	[nation] [nvarchar](50) NULL,
	[age] [int] NULL,
	[birthdate] [datetime] NULL,
	[create_time] [datetime] NULL,
 CONSTRAINT [PK_人员信息表] PRIMARY KEY CLUSTERED 
(
	[user_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[阳性人员]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[阳性人员](
	[user_id] [int] NOT NULL,
	[positive_time] [datetime] NULL,
 CONSTRAINT [PK_阳性人员] PRIMARY KEY CLUSTERED 
(
	[user_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[疫苗接种信息表]    Script Date: 2023/6/26 15:43:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[疫苗接种信息表](
	[sno] [int] NOT NULL,
	[inject_sn] [varchar](50) NOT NULL,
	[user_id] [int] NOT NULL,
	[age] [int] NULL,
	[gender] [varchar](10) NULL,
	[birthdate] [datetime] NULL,
	[inject_date] [datetime] NULL,
	[inject_times] [varchar](20) NULL,
	[vaccine_type] [varchar](20) NULL,
 CONSTRAINT [PK_疫苗接种信息表_1] PRIMARY KEY CLUSTERED 
(
	[sno] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
USE [master]
GO
ALTER DATABASE [covid-19control] SET  READ_WRITE 
GO
