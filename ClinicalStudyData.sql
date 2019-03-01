
DROP DATABASE ClinicalStudyData;
CREATE DATABASE ClinicalStudyData;
USE ClinicalStudyData;

DROP TABLE PendingResults;
DROP TABLE ProvidedDocuments;
DROP TABLE StudyDocs;
DROP TABLE PatientData;
DROP TABLE BrowseTerms;
DROP TABLE Keywords;
DROP TABLE ResponsibleParty;
DROP TABLE OnlineDates;
DROP TABLE Reference;
DROP TABLE Links;
DROP TABLE RemovedCountries;
DROP TABLE LocationCountries;
DROP TABLE LocationInvestigators;
DROP TABLE LocationContacts;
DROP TABLE Locations;
DROP TABLE Contacts;
DROP TABLE Officials;
DROP TABLE Eligibility;
DROP TABLE Biospecs;
DROP TABLE Interventions;
DROP TABLE ArmGroups;
DROP TABLE Conditions;
DROP TABLE Outcomes;
DROP TABLE StudyDesignInfo;
DROP TABLE ExpandedAccessInfo;
DROP TABLE OversightInfo;
DROP TABLE Sponsors;
DROP TABLE IDInfo;
DROP TABLE ClinicialStudy;


CREATE TABLE ClinicialStudy (
	nct_id VARCHAR(11) PRIMARY KEY,
	download_date DATE,
	url VARCHAR(43)
	brief_title VARCHAR(150),
	acronym VARCHAR(25),
	official_title VARCHAR(250),
	source VARCHAR(30),
	brief_summary VARCHAR(1000),
	detailed_description VARCHAR(3000),
	overall_status VARCHAR(25),
	last_known_status VARCHAR(25),
	why_stopped VARCHAR(??),
	start_date DATE,
	completion_date DATE,
	primary_completion_date DATE,
	phase VARCHAR(15),
	study_type VARCHAR(32),
	has_expanded_access VARCHAR(3), # Yes, No
	target_duration VARCHAR(??),
	number_of_arms INT(3),
	number_of_groups INT(3),
	enrollment INT(4),
	enrollment_type VARCHAR(11), # Actual, Anticipated, Estimate
);

CREATE TABLE IDInfo (
	nct_id VARCHAR(11) PRIMARY KEY,
	FOREIGN KEY (nct_id) REFERENCES ClincialStudy(nct_id),
	org_study_id VARCHAR(20),
	secondary_id VARCHAR(20),
	nct_alias VARCHAR(??)
);

CREATE TABLE Sponsors (
	nct_id VARCHAR(11) PRIMARY KEY,
	FOREIGN KEY (nct_id) REFERENCES ClincialStudy(nct_id),
	sponsor_type VARCHAR(12), # Lead, Collaborator
	agency VARCHAR(30),
	agnecy_class VARCHAR(8) # NIH, US Fed, Industry, Other
);

CREATE TABLE OversightInfo (
	nct_id VARCHAR(11) PRIMARY KEY,
	FOREIGN KEY (nct_id) REFERENCES ClincialStudy(nct_id),
	has_dmc VARCHAR(3), # Yes, No
	is_fda_regulated_drug VARCHAR(3), # Yes, No
	is_fda_regulated_device VARCHAR(3), # Yes, No
	is_uapproved_device VARCHAR(3), # Yes, No
	is_ppsd VARCHAR(3), # Yes, No
	is_us_export VARCHAR(3) # Yes, No
);

CREATE TABLE ExpandedAccessInfo (
	nct_id VARCHAR(11) PRIMARY KEY,
	FOREIGN KEY (nct_id) REFERENCES ClincialStudy(nct_id),
	expanded_access_type_individual VARCHAR(3), # Yes, No
	expanded_access_type_intermediate VARCHAR(3), # Yes, No
	expanded_access_type_treatment VARCHAR(3) # Yes, No
);

CREATE TABLE StudyDesignInfo (
	nct_id VARCHAR(11) PRIMARY KEY,
	FOREIGN KEY (nct_id) REFERENCES ClincialStudy(nct_id),
	allocation VARCHAR(10), # Randomized
	intervention_model VARCHAR(25),
	intervention_model_description VARCHAR(??),
	primary_purpose VARCHAR(15),
	observational_model VARCHAR(??),
	time_perspective VARCHAR(15),
	masking VARCHAR(50),
	masking_description VARCHAR(??)
);

CREATE TABLE Outcomes (
	nct_id VARCHAR(11) PRIMARY KEY,
	FOREIGN KEY (nct_id) REFERENCES ClincialStudy(nct_id),
	outcome_type VARCHAR(9), # Primary, Secondary, Other
	measure VARCHAR(200),
	time_frame VARCHAR(75),
	outcome_description VARCHAR(1000)
);

CREATE TABLE Conditions (
	nct_id VARCHAR(11) PRIMARY KEY,
	FOREIGN KEY (nct_id) REFERENCES ClincialStudy(nct_id),
	condition VARCHAR(50)
);

CREATE TABLE ArmGroups (
	nct_id VARCHAR(11) PRIMARY KEY,
	FOREIGN KEY (nct_id) REFERENCES ClincialStudy(nct_id),
	arm_group_label VARCHAR(35),
	arm_group_type VARCHAR(20), # Experimental, Placebo Comparator
	arm_group_description VARCHAR(1000)
);

CREATE TABLE Interventions (
	nct_id VARCHAR(11) PRIMARY KEY,
	FOREIGN KEY (nct_id) REFERENCES ClincialStudy(nct_id),
	intervention_type VARCHAR(20),
	intervention_name VARCHAR(50),
	intervention_description VARCHAR(200),
	arm_group_label VARCHAR(35),
	other_name VARCHAR(45)
);

CREATE TABLE Biospecs (
	nct_id VARCHAR(11) PRIMARY KEY,
	FOREIGN KEY (nct_id) REFERENCES ClincialStudy(nct_id),
	biospec_retention VARCHAR(20),
	biospec_descr VARCHAR(??)
);

CREATE TABLE Eligibility (
	nct_id VARCHAR(11) PRIMARY KEY,
	FOREIGN KEY (nct_id) REFERENCES ClincialStudy(nct_id),
	study_pop VARCHAR(40),
	sampling_method VARCHAR(22), # Probability Sample, Non-Probability Sample
	criteria VARCHAR(10000),
	gender VARCHAR(6), # Female, Male, All
	gender_based VARCHAR(3), # Yes, No
	gender_description VARCHAR(??),
	minimum_age VARCHAR(8), # XX Years
	maximum_age VARCHAR(8), # XX Years
	healthy_volunteers VARCHAR(3) # Yes, No
);

CREATE TABLE Officials (
	nct_id VARCHAR(11) PRIMARY KEY,
	FOREIGN KEY (nct_id) REFERENCES ClincialStudy(nct_id),
	official_type VARCHAR(12), # Investigator, Overall
	first_name VARCHAR(??),
	middle_name VARCHAR(??),
	last_name VARCHAR(40),
	degree VARCHAR(??),
	role VARCHAR(22), # Principal Investigator, Sub-Investigator, Study, Study Director
	affiliation VARCHAR(50)
);

CREATE TABLE Contacts (
	nct_id VARCHAR(11) PRIMARY KEY,
	FOREIGN KEY (nct_id) REFERENCES ClincialStudy(nct_id),
	contact_type VARCHAR(16), # study_primary, study_backup, facility_primary, facility_backup
	first_name VARCHAR(??),
	middle_name VARCHAR(??),
	last_name VARCHAR(40),
	degrees VARCHAR(??),
	phone VARCHAR(15),
	phone_ext VARCHAR(10),
	email VARCHAR(40)
);

CREATE TABLE Locations (
	nct_id VARCHAR(11) PRIMARY KEY,
	FOREIGN KEY (nct_id) REFERENCES ClincialStudy(nct_id),
	facility_name VARCHAR(60),
	city VARCHAR(40),
	state VARCHAR(40),
	country VARCHAR(20),
	status VARCHAR(23), # "Active, not recruiting", Completed, Enrolling by invitation, Not yet recruiting, Recruiting, Suspended, Terminated, Withdrawn
);

CREATE TABLE LocationContacts (
	nct_id VARCHAR(11) PRIMARY KEY,
	FOREIGN KEY (nct_id) REFERENCES ClincialStudy(nct_id),
	facility_name VARCHAR(60),
	FOREIGN KEY (facility_name) REFERENCES Locations(facility_name),
	contact_type VARCHAR(16), # facility_primary, facility_backup
	FOREIGN KEY (contact_type) REFERENCES Contacts(contact_type)
);

CREATE TABLE LocationInvestigators (
	nct_id VARCHAR(11) PRIMARY KEY,
	FOREIGN KEY (nct_id) REFERENCES ClincialStudy(nct_id),
	facility_name VARCHAR(60),
	FOREIGN KEY (facility_name) REFERENCES Locations(facility_name),
	investigator_last_name VARCHAR(16), # facility_primary, facility_backup
	FOREIGN KEY (investigator_last_name) REFERENCES Officials(last_name)
);

CREATE TABLE LocationCountries (
	nct_id VARCHAR(11) PRIMARY KEY,
	FOREIGN KEY (nct_id) REFERENCES ClincialStudy(nct_id),
	country VARCHAR(20)
);

CREATE TABLE RemovedCountries (
	nct_id VARCHAR(11) PRIMARY KEY,
	FOREIGN KEY (nct_id) REFERENCES ClincialStudy(nct_id),
	country VARCHAR(20)
);

CREATE TABLE Links (
	nct_id VARCHAR(11) PRIMARY KEY,
	FOREIGN KEY (nct_id) REFERENCES ClincialStudy(nct_id),
	url VARCHAR(150),
	link_description VARCHAR(250)
);

CREATE TABLE Reference (
	nct_id VARCHAR(11) PRIMARY KEY,
	FOREIGN KEY (nct_id) REFERENCES ClincialStudy(nct_id),
	citation VARCHAR(300),
	PMID VARCHAR(8)
	reference_type VARCHAR(6) # Result, Origin
);

CREATE TABLE OnlineDates (
	nct_id VARCHAR(11) PRIMARY KEY,
	FOREIGN KEY (nct_id) REFERENCES ClincialStudy(nct_id),
	verficiation_date DATE,
	study_first_submitted DATE,
	study_first_submitted_qc DATE,
	study_first_posted DATE,
	results_first_submitted DATE,
	results_first_submitted_qc DATE,
	results_first_posted DATE,
	disposition_first_submitted DATE,
	disposition_first_submitted_qc DATE,
	disposition_first_posted DATE,
	last_first_submitted DATE,
	last_first_submitted_qc DATE,
	last_first_posted DATE,
);

CREATE TABLE ResponsibleParty (
	nct_id VARCHAR(11) PRIMARY KEY,
	FOREIGN KEY (nct_id) REFERENCES ClincialStudy(nct_id),
	name_title VARCHAR(??),
	organization VARCHAR(??),
	responsibile_party_type VARCHAR(22), # Sponsor, Principal Investigator, Sponsor-Investigator
	investigator_affiliation VARCHAR(40),
	investigator_full_name VARCHAR(40),
	investigator_title VARCHAR(40)
);

CREATE TABLE Keywords (
	nct_id VARCHAR(11) PRIMARY KEY,
	FOREIGN KEY (nct_id) REFERENCES ClincialStudy(nct_id),
	keyword VARCHAR(30)
);

CREATE TABLE BrowseTerms (
	nct_id VARCHAR(11) PRIMARY KEY,
	FOREIGN KEY (nct_id) REFERENCES ClincialStudy(nct_id),
	term VARCHAR(30),
	term_type VARCHAR(12) # Condition, Investigator
);

CREATE TABLE PatientData (
	nct_id VARCHAR(11) PRIMARY KEY,
	FOREIGN KEY (nct_id) REFERENCES ClincialStudy(nct_id),
	sharing_ipd VARCHAR(3), # Yes, No
	ipd_description VARCHAR(??),
	ipd_into_type VARCHAR(??),
	ipd_time_frame VARCHAR(??),
	ipd_access_criteria VARCHAR(??),
	ipd_url VARCHAR(??)
);

CREATE TABLE StudyDocs (
	nct_id VARCHAR(11) PRIMARY KEY,
	FOREIGN KEY (nct_id) REFERENCES ClincialStudy(nct_id),
	doc_id VARCHAR(??),
	doc_type VARCHAR(??),
	doc_url VARCHAR(??),
	doc_comment VARCHAR(??)
);

CREATE TABLE ProvidedDocuments (
	nct_id VARCHAR(11) PRIMARY KEY,
	FOREIGN KEY (nct_id) REFERENCES ClincialStudy(nct_id),
	document_type VARCHAR(??),
	document_has_protocol VARCHAR(??),
	document_has_icf VARCHAR(??),
	document_has_sap VARCHAR(??),
	document_date DATE,
	document_url VARCHAR(??)
);

CREATE TABLE PendingResults (
	nct_id VARCHAR(11) PRIMARY KEY,
	FOREIGN KEY (nct_id) REFERENCES ClincialStudy(nct_id),
	submitted DATE,
	returned DATE,
	submission_canceled DATE
);




