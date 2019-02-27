
/* DROP DATABASE ClinicalStudyData;
CREATE DATABASE ClinicalStudyData;
USE ClinicalStudyData; */

CREATE TABLE ClincialStudy (
	nct_id VARCHAR(11) PRIMARY KEY,
	brief_title VARCHAR(150),
	acronym VARCHAR(25),
	official_title VARCHAR(250),
	brief_summary VARCHAR(1000)
)