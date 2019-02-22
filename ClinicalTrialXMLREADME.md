# Clinical Trial Data from ClinicalTrials.gov
-
## Quick explanatory guide of the possible fields in one XML file 
### XML Conforms to this [Schema](https://clinicaltrials.gov/ct2/html/images/info/public.xsd)
### Further explanation of important terms can be found [here](https://clinicaltrials.gov/ct2/about-studies/glossary)
-
* **clinical_study** - all data about the clinical trial stored under this field (all fields until clinical_results are nested under here)
* **required_header** - header that provides general info about the download
	* **download_date** - date the data was downloaded
	* **link_text** - the text that would display instead of the url if opened in a webpage
		* Says the same thing for each file
	* **url** - where to find the data for the file online
* **id_info** - different ways to classify the study id
	* **org\_study\_id** - full id of the study
	* **secondary_id** - shortened or different id to use to find the study
	* **nct_id** - ClinicalTrials.gov identifier for the study (unique)
	* **nct_alias**
* **brief_title** - title of the clinical trial
* **acronym**
* **sponsors**
	* **lead_sponsor**
		* **agency** - organization running the clinical trial
		* **agency_class** - the type of the organization
			* Values: NIH, US Fed, Industry, Other
	* **collaborator**
		* **agency** - organization supporting the clinical trial that is not the sponsor
		* **agency_class** - the type of the organization
			* Values: NIH, US Fed, Industry, Other
* **source** - same as lead_sponsor agency
* **oversight_info**
	* **has_dmc** - whether or not the study has a data monitoring committee
	* **is\_fda\_regulated_drug** - yes or no
	* **is\_fda\_regulated_device** - yes or no
	* **is\_unapproved\_device** - yes or no
	* **is_ppsd** - ???
	* **is\_us\_export** - yes or no
* **brief_summary**
	* **textblock** - short explanation of what the study is doing and looking to test
* **detailed_description**
	* **textblock** - more indepth explanation of the study, includes a lot more information than the breif summary
* **overall\_status** - potential values depend on the study_type
	* Study Type: Expanded Access - Values: Available, No Longer Available, Temporarily Not Available, Approved for Marketing
	* Study Type: N/A - Values: Withheld
	* Study Type: Anything Else - Values: Active not recruiting, Completed, Enrolling by initiative, Not yet recruiting, Recruiting, Suspended, Terminated, Withdrawn
* **last\_known\_status** - most recent status of a study that has not been verified in at least 2 years
* **why_stopped** - reason for discontinuing the study
* **start_date**
* **completion_date**
* **primary\_completion\_date**
* **phase** - current phase of the clinical trial (1-4)
* **study_type** - classification of the study
	* Values: Expanded Acess, N/A, Other
* **has\_expanded\_access** - does the clinical trial allow patients with immediately life threatening conditions to participate
* **expanded\_access\_info** 
	* **expanded\_access\_type\_individual**
	* **expanded\_access\_type\_intermediate**
	* **expanded\_access\_type\_treatment**
* **study\_design\_info**
	* **allocation** - how the tests are administered to the patients
		* Value: Randomized
	* **intervention_model** - general design of the strategy for assigning treatments to participants
	* **intervention\_model\_description**
	* **primary_purpose** - reason for the clinical trial
		* Values: Treatment
	* **observational_model**
	* **time_persepective**
	* **masking** - tells who knows which people were treated
	* **masking_description**
* **target_duration** - optional - desired length of the study
* **primary_outcome** - can be multiple (outcome=endpoint)
	* **measure** - important for evaluating the effect of the treatment, what it is supposed to do
	* **time_frame** - how long it takes to see the outcome's effects
	* **description**
* **secondary_outcome** - can be multiple
	* **measure** - important for evaluating the effect of the treatment, what it is supposed to do
	* **time_frame** - how long it takes to see the outcome's effects
	* **description**
* **other_outcome** - can be multiple
	* **measure** - important for evaluating the effect of the treatment, what it is supposed to do
	* **time_frame** - how long it takes to see the outcome's effects
	* **description**
* **number\_of\_arms** - number of groups/sub-groups in the clinical trial
* **enrollment** - number of participants in the clinical study tagged with a type
	* Types: Actual, Anticipated, Estimate
* **condition** - disease, disorder, etc being studied - can be multiple
* **arm_group**
	* **arm\_group\_label** - treatment group
	* **arm\_group\_type** - experimental or placebo comparator
	* **description**
* **intervention** - treatment (can be multiple)
	* **intervention_type** - type of treatment
		* Values: Behavioral, Biological, Combination Product, Device, Diagnostic Test, Dietary Supplement, Drug, Genetic, Procedure, Radiation, Other
	* **intervention_name** - name of treatment???
	* **description**
	* **arm\_group\_label** - arm group associated with this treatment
	* **other_name** - ???
* **biospec_retention**
	* Values: None Retained, Samples With DNA, Samples Without DNA
* **biospec_descr**
* **eligibility** - who can participate in the study
	* **study_pop** - population of the study
	* **sampling_method**
	* **criteria**
		* **textblock** - details about desired participants
	* **gender**
	* **gender_based**
	* **minimum_age**
	* **maximum_age**
	* **healthy_volunteers** - yes or no
* **overall_official** - person running the clinical study???
	* **first_name**
	* **middle_name**
	* **last_name**
	* **degree**
	* **role**
	* **affiliation**
* **overall_contact** - first person to call for more info about the study
	* **first_name**
	* **middle_name**
	* **last_name**
	* **degrees**
	* **phone**
	* **phone_ext**
	* **email**
* **overall\_contact\_backup** - second person to call for more info about the study
	* **first_name**
	* **middle_name**
	* **last_name**
	* **degrees**
	* **phone**
	* **phone_ext**
	* **email**
* **location** - where the study is being conducted, can be multiple
	* **facility**
		* **name** - name of the facility
		* **address**
			* **city**
			* **state**
			* **country**
	*  **status**
	*  **contact**
		* **first_name**
		* **middle_name**
		* **last_name**
		* **degrees**
		* **phone**
		* **phone_ext**
		* **email**
	*  **contact_backup**
		* **first_name**
		* **middle_name**
		* **last_name**
		* **degrees**
		* **phone**
		* **phone_ext**
		* **email**
	*  **investigator**
		* **first_name**
		* **middle_name**
		* **last_name**
		* **degree**
		* **role**
		* **affiliation**
* **location_countries** - countries the study is being conducted in
	* **country**
* **removed_countries** - countries no longer in the study
	* **country**
* **link**
	* **url**
	* **description**
* **reference** - sources of information for study???
	* **citation**
	* **PMID** - ???
* **results_reference**
	* **citation**
	* **PMID** - ???
* **verification_date** - most recent date that the study sponsor/investigator confirmed trial info is accurate
* **study\_first\_submitted** - date of first submission to ClinicalTrials.gov
* **study\_first\_submitted\_qc** - date when study was consistent with NLM quality control review criteria
* **study\_first\_posted** - date the study first appeared on ClinicalTrials.gov
* **results\_first\_submitted** - date the summary results were first submitted to ClinicalTrials.gov
* **results\_first\_submitted\_qc** - date when study results were consistent with NLM quality control review criteria
* **results\_first\_posted** - date the summary results first appeared on ClinicalTrials.gov
* **disposition\_first\_submitted** - date the disposition was first submitted to ClinicalTrials.gov
* **disposition\_first\_submitted\_qc** - date when disposition was consistent with NLM quality control review criteria
* **disposition\_first\_posted** - date the disposition first appeared on ClinicalTrials.gov
* **last\_update\_submitted** - last date the sponsor/investigator submitted updates to the trial on ClinicalTrials.gov
* **last\_update\_submitted\_qc** - date when study was consistent with NLM quality control review criteria
* **last\_update\_posted** - last date the sponsor/investigator updates were posted on ClinicalTrials.gov
* **responsible_party** - person responsible for submitting information about the study to ClinicalTrials.gov
	* **responsible\_party\_type**
		* Values: Sponsor, Principal Investigator, Sponsor-Investigator
* **keyword** 
* **condition_browse** - searchable conditions that this study would appear as a result of 
	* **mesh_term** - one condition (can be multiple)
* **intervention_browse** - searchable interventions that this study would appear as a result of 
	* **mesh_term** - one intervention (can be multiple)
* **patient_data** - information about the patients
	* **sharing_ipd** - whether or not they are sharing individual patient data
	* **ipd_description**
	* **ipd\_info\_type**
	* **ipd\_time\_frame**
	* **ipd\_access\_criteria**
	* **ipd_url**
* **study_docs**
	* **study_doc**
		* **doc_id**
		* **doc_type**
		* **doc_url**
		* **doc_comment**
* **pending_results** - appears only when the data provider has submitted study results for QC review, but those results have not yet been publicly posted
	* **submitted** - date
	* **returned** - date
	* **submission_canceled** - date
* **clinical_results** - results of the clinical trial
	* **participant_flow**
		* **group_list**
			* **group** - type specified as the phase
				* Values: P1, P2, P3, P4
			* **title**
			* **description**
		* **period_list**
			* **period** - can be multiple
				* **title**
				* **milestone_list**
					* **milestone**
						* **title**
						* **participants_list**
							* **participants** - has group_id (phase ) and count (number of people)
	* **baseline**
		* **group_list**
			* **group** - has group_id
				* Values: B1, B2, B3, B4, etc.
				* **title**
				* **description**
		* **analyzed_list**
			* **analyzed**
				* **units** - what is being analyzed (ex: Participants)
				* **scope**
				* **count_list**
					* **count** - has group_id similar to group above and value (number of units) 
		* **measure_list**
			* **measure** - ???
				* **title**
				* **units** - what is being measured (ex: Participants, mL)
				* **param** - the purpose or final result of the measurement
					* Values: Mean, Count, etc.
				* **dispersion** - how the spread is being calculated? (ex: Standard Deviation)
				* **class_list**
					* **class**
						* **category_list**
							* **category**
								* **measurement_list**
									* **measurement** - has a group_id and a value for the param
	* **outcome_list**
		* **outcome**
			* **type**
			* **title**
			* **description**
			* **time_frame**
			* **safety_issue**
			* **posting_date**
			* **population**
			* **group_list**
				* **group**
					* **title**
					* **description**
			* **measure**
				* **title**
				* **description**
				* **population**
				* **units** - what is being analyzed (ex: Participantsm mL)
				* **param** - the purpose or final result of the measurement
				* **analyzed_list**
					* **analyzed**
						* **units** - what is being analyzed (ex: Participantsm mL)
						* **scope**
						* **count_list**
							* **count** - has group_id similar to group 
				* **class_list**
					* **class**
						* **category_list**
							* **category**
								* **measurement_list**
									* **measurement** - has a group_id and a value for the param
	* **reported_events**
		* **time_frame**
		* **desc**
		* **group_list**
			* **group** - has group_id
				* Values: E1, E2, B1, B2, etc.
				* **title**
				* **description**
		* **serious_events**
			* **frequency_thresold**
			* **default_vocab**
			* **default_assessment**
			* **category_list**
				* **category**
					* **title**
					* **event_list**
						* **event**
							* **subtitle**
							* **assessment**
							* **description**
							* **counts**
		* **other_events**
			* **frequency_thresold**
			* **default_vocab**
			* **default_assessment**
			* **category_list**
				* **category**
					* **title**
					* **event_list**
						* **event**
							* **subtitle**
							* **assessment**
							* **description**
							* **counts**
	* **certain_agreements**
		* **pi_employmee** - whether or not all principal agents are employed by the sponsor of the study
		* **restrictive_agreement**
	* **point\_of\_contact**
		* **name\_or\_title**
		* **organization**
		* **phone**
		* **email**