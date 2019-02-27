# Clinical Trial Data from ClinicalTrials.gov
-
## Quick explanatory guide of the possible fields in one XML file 
### XML Conforms to this [Schema](https://clinicaltrials.gov/ct2/html/images/info/public.xsd) which is updated regularly
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
		* *can appear multiple times*
	* **nct_id** - ClinicalTrials.gov identifier for the study (unique)
	* **nct_alias**
		* *can appear multiple times*
* **brief_title** - title of the clinical trial
* **acronym**
* **sponsors**
	* **lead_sponsor**
		* **agency** - organization running the clinical trial
		* **agency_class** - the type of the organization
			* Values: NIH, US Fed, Industry, Other
	* **collaborator** - *can appear multiple times*
		* **agency** - organization supporting the clinical trial that is not the sponsor
		* **agency_class** - the type of the organization
			* Values: NIH, US Fed, Industry, Other
* **source** - same as lead_sponsor agency
* **oversight_info**
	* **has_dmc** - whether or not the study has a data monitoring committee
		* Values: Yes, No
	* **is\_fda\_regulated_drug**
		* Values: Yes, No
	* **is\_fda\_regulated_device**
		* Values: Yes, No
	* **is\_unapproved\_device**
		* Values: Yes, No
	* **is_ppsd** - ???
		* Values: Yes, No
	* **is\_us\_export**
		* Values: Yes, No
* **brief_summary**
	* **textblock** - short explanation of what the study is doing and looking to test
* **detailed_description**
	* **textblock** - more indepth explanation of the study, includes a lot more information than the breif summary
* **overall\_status** - potential values depend on the study_type
	* Study Type: Expanded Access - Values: Available, No Longer Available, Temporarily Not Available, Approved for Marketing
	* Study Type: N/A - Values: Withheld
	* Study Type: Anything Else - Values: "Active, not recruiting", Completed, Enrolling by invitation, Not yet recruiting, Recruiting, Suspended, Terminated, Withdrawn
* **last\_known\_status** - most recent status of a study that has not been verified in at least 2 years
* **why_stopped** - reason for discontinuing the study
* **start_date**
* **completion_date**
* **primary\_completion\_date**
* **phase** - current phase of the clinical trial (1-4)
	* Values: N/A, Early Phase 1, Phase 1, Phase 1/Phase2, Phase 2, Phase 2/Phase 3, Phase 3, Phase 4
* **study_type** - classification of the study
	* Values: Expanded Acess, Interventional, N/A, Observational, Observational [Patient Registry]
* **has\_expanded\_access** - does the clinical trial allow patients with immediately life threatening conditions to participate
	* Values: Yes, No
* **expanded\_access\_info** 
	* **expanded\_access\_type\_individual**
		* Values: Yes, No
	* **expanded\_access\_type\_intermediate**
		* Values: Yes, No
	* **expanded\_access\_type\_treatment**
		* Values: Yes, No
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
* **primary_outcome** - *can appear multiple times* (outcome=endpoint)
	* **measure** - important for evaluating the effect of the treatment, what it is supposed to do
	* **time_frame** - how long it takes to see the outcome's effects
	* **description**
* **secondary_outcome** - *can appear multiple times*
	* **measure** - important for evaluating the effect of the treatment, what it is supposed to do
	* **time_frame** - how long it takes to see the outcome's effects
	* **description**
* **other_outcome** - *can appear multiple times*
	* **measure** - important for evaluating the effect of the treatment, what it is supposed to do
	* **time_frame** - how long it takes to see the outcome's effects
	* **description**
* **number\_of\_arms** - number of groups/sub-groups in the clinical trial
* **number\_of\_groups**
* **enrollment** - number of participants in the clinical study tagged with a type
	* Types: Actual, Anticipated, Estimate
* **condition** - disease, disorder, etc being studied
	* *can appear multiple times*
* **arm_group** - *can appear multiple times*
	* **arm\_group\_label** - treatment group
	* **arm\_group\_type** - experimental or placebo comparator
	* **description**
* **intervention** - treatment
	* *can appear multiple times*
	* **intervention_type** - type of treatment
		* Values: Behavioral, Biological, Combination Product, Device, Diagnostic Test, Dietary Supplement, Drug, Genetic, Procedure, Radiation, Other
	* **intervention_name** - name of treatment???
	* **description**
	* **arm\_group\_label** - arm group associated with this treatment
		* *can appear multiple times*
	* **other_name** - ???
* **biospec_retention**
	* Values: None Retained, Samples With DNA, Samples Without DNA
* **biospec_descr**
* **eligibility** - who can participate in the study
	* **study_pop** - population of the study
	* **sampling_method**
		* Values: Probability Sample, Non-Probability Sample
	* **criteria**
		* **textblock** - details about desired participants
	* **gender**
		* Values: Female, Male, All
	* **gender_based**
		* Values: Yes, No
	* **gender_description**
	* **minimum_age**
	* **maximum_age**
	* **healthy_volunteers** - Yes or No
* **overall_official** - person running the clinical study???
	* *can appear multiple times*
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
* **location** - where the study is being conducted
	* *can appear multiple times*
	* **facility**
		* **name** - name of the facility
		* **address**
			* **city**
			* **state**
			* **country**
	* **status**
		* Values: "Active, not recruiting", Completed, Enrolling by invitation, Not yet recruiting, Recruiting, Suspended, Terminated, Withdrawn
	* **contact**
		* **first_name**
		* **middle_name**
		* **last_name**
		* **degrees**
		* **phone**
		* **phone_ext**
		* **email**
	* **contact_backup**
		* **first_name**
		* **middle_name**
		* **last_name**
		* **degrees**
		* **phone**
		* **phone_ext**
		* **email**
	* **investigator**
		* *can appear multiple times*
		* **first_name**
		* **middle_name**
		* **last_name**
		* **degree**
		* **role**
			* Values: Principal Investigator, Sub-Investigator, Study, Study Director
		* **affiliation**
* **location_countries** - countries the study is being conducted in
	* **country** - *can appear multiple times*
* **removed_countries** - countries no longer in the study
	* **country** - *can appear multiple times*
* **link** - *can appear multiple times*
	* **url**
	* **description**
* **reference** - sources of information for study???
	* *can appear multiple times*
	* **citation**
	* **PMID** - ???
* **results_reference**
	* *can appear multiple times*
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
	* **name_title** - *only used in old style*
	* **organization** - *only used in old style*
	* **responsible\_party\_type**
		* Values: Sponsor, Principal Investigator, Sponsor-Investigator
	* **investigator_affiliation**
	* **investigator\_full\_name**
	* **investigator_title**
* **keyword** - *can appear multiple times*
* **condition_browse** - searchable conditions that this study would appear as a result of 
	* **mesh_term** - one condition
		* *can appear multiple times*
* **intervention_browse** - searchable interventions that this study would appear as a result of 
	* **mesh_term** - one intervention
		* *can appear multiple times*
* **patient_data** - information about the patients
	* **sharing_ipd** - whether or not they are sharing individual patient data
	* **ipd_description**
	* **ipd\_info\_type**
		* *can appear multiple times*
	* **ipd\_time\_frame**
	* **ipd\_access\_criteria**
	* **ipd_url**
* **study_docs**
	* **study_doc** - *can appear multiple times*
		* **doc_id**
		* **doc_type**
		* **doc_url**
		* **doc_comment**
* **provided\_document\_section**
	* **provided_document** - *can appear multiple times*
		* **document_type**
		* **document\_has\_protocol**
		* **document_has_icf**
		* **document_has_sap**
		* **document_date**
		* **document_url**
* **pending_results** - appears only when the data provider has submitted study results for QC review, but those results have not yet been publicly posted
	* *can appear multiple times*
	* **submitted** - date
	* **returned** - date
	* **submission_canceled** - date
* **clinical_results** - results of the clinical trial (within clinical study wrapper)
	* **participant_flow**
		* **recruitment_details**
		* **pre\_assignment\_details**
		* **group_list**
			* **group** - has only a group_id as an attribute
				* *can appear multiple times*
				* Values: P1, P2, P3, P4
				* **title**
				* **description**
		* **period_list**
			* **period** - *can appear multiple times*
				* **title**
				* **milestone_list**
					* **milestone** - *can appear multiple times*
						* **title**
						* **participants_list**
							* **participants** - has group_id (phase) and count (number of people) as attributes
				* **drop\_withdraw\_reason\_list**
					* **drop\_withrow\_reason** - *can appear multiple times*
						* **title**
						* **participants_list**
							* **participants** - has group_id (phase) and count (number of people) as attributes
	* **baseline**
		* **population**
		* **group_list**
			* **group** - has only a group_id as attributes
				* *can appear multiple times*
				* Values: P1, P2, P3, P4
				* **title**
				* **description**
		* **analyzed_list**
			* **analyzed**
				* **units** - what is being analyzed (ex: Participants)
				* **scope**
				* **count_list**
					* **count** - has group_id similar to group above and count (number of units) as attributes
						* *can appear multiple times*
		* **measure_list**
			* **measure** - ???
				* *can appear multiple times*
				* **title**
				* **description**
				* **population**
				* **units** - what is being measured (ex: Participants, mL)
				* **param** - the purpose or final result of the measurement
					* Values: Geometric Mean, Geometric Least Squares Mean, Least Squares Mean, Log Mean, Mean, Median, Number, Count of Participants, Count of Units
				* **dispersion** - how the spread is being calculated
					* Values: 80% Confidence Interval, 90% Confidence Interval, 95% Confidence Interval, 97.5% Confidence Interval, 99% Confidence Interval, Full Range, Gemoetric Coefficient of Variation, Inter-Quartile Range, Standard Deviation, Standard Error
				* **units_analyzed**
				* **analyzed_list**
					* **analyzed** - *can appear multiple times*
						* **units** - what is being analyzed (ex: Participants)
						* **scope**
						* **count_list**
							* **count** - has group_id similar to group above and count (number of units) as attributes
								* *can appear multiple times*
				* **class_list**
					* **class** - *can appear multiple times*
						* **title**
						* * **analyzed_list**
							* **analyzed** - *can appear multiple times*
								* **units** - what is being analyzed (ex: Participants)
								* **scope**
								* **count_list**
									* **count** - has group_id similar to group above and count (number of units) 
						* **category_list**
							* **category** - *can appear multiple times*
								* **title**
								* **measurement_list**
									* **measurement** - has a group_id, value, spread, lower limit, upper limit as attributes
	* **outcome_list**
		* **outcome** - *can appear multiple times*
			* **type**
				* Values: Primary, Secondary, Other Pre-specified, Post-Hoc
			* **title**
			* **description**
			* **time_frame**
			* **safety_issue**
				* Values: Yes, No
			* **posting_date**
			* **population**
			* **group_list**
				* **group** - has only a group_id as attributes
					* *can appear multiple times*
					* Values: P1, P2, P3, P4
					* **title**
					* **description**
			* **measure** - ???
				* *can appear multiple times*
				* **title**
				* **description**
				* **population**
				* **units** - what is being measured (ex: Participants, mL)
				* **param** - the purpose or final result of the measurement
					* Values: Geometric Mean, Geometric Least Squares Mean, Least Squares Mean, Log Mean, Mean, Median, Number, Count of Participants, Count of Units
				* **dispersion** - how the spread is being calculated
					* Values: 80% Confidence Interval, 90% Confidence Interval, 95% Confidence Interval, 97.5% Confidence Interval, 99% Confidence Interval, Full Range, Gemoetric Coefficient of Variation, Inter-Quartile Range, Standard Deviation, Standard Error
				* **units_analyzed**
				* **analyzed_list**
					* **analyzed** - *can appear multiple times*
						* **units** - what is being analyzed (ex: Participants)
						* **scope**
						* **count_list**
							* **count** - has group_id similar to group above and count (number of units) as attributes
								* *can appear multiple times*
			* **analysis_list**
				* **analysis** - *can appear multiple times*
					* **group\_id\_list**
						* **group_id** - *can appear multiple times*
					* **groups_desc**
					* **non\_inferiority\_type**
						* Values: Superiority, Non-Inferiority, Equivalence, Other, Non-Inferiority or Equivalence, Superiority or Other
					* **non\_inferiority\_desc**
					* **p_value**
					* **p\_value\_desc**
					* **method**
					* **method_desc**
					* **param_type**
					* **param_value**
					* **dispersion_type**
						* Values: Standard Deviation, Standard Error of the Mean
					* **dispersion_value**
					* **ci_percent**
					* **ci\_n\_sides**
						* Values: 1-Sided, 2-Sided
					* **ci\_lower\_limit**
					* **ci\_upper\_limit**
					* **ci\_upper\_limit\_na\_comment**
					* **estimate_desc**
					* **other\_analysis\_desc**
	* **reported_events**
		* **time_frame**
		* **desc**
		* **group_list**
			* **group** - has only a group_id as attributes
				* *can appear multiple times*
				* Values: P1, P2, P3, P4
				* **title**
				* **description**
		* **serious_events**
			* **frequency_thresold**
			* **default_vocab**
			* **default_assessment**
			* **category_list**
				* **category** - *can appear multiple times*
					* **title**
					* **event_list**
						* **event** - *can appear multiple times*
							* **sub_title**
							* **assessment**
								* Values: Non-systematic Assessment, Systematic Assessment
							* **description**
							* **counts**
		* **other_events**
			* **frequency_thresold**
			* **default_vocab**
			* **default_assessment**
			* **category_list**
				* **category** - *can appear multiple times*
					* **title**
					* **event_list**
						* **event** - *can appear multiple times*
							* **sub_title**
							* **assessment**
								* Values: Non-systematic Assessment, Systematic Assessment
							* **description**
							* **counts**
	* **certain_agreements**
		* **pi_employmee** - whether or not all principal agents are employed by the sponsor of the study
			* Values: "All Principal Investigators ARE employed by the organization sponsoring the study.", "All Principal Investigators are NOT employed by the organization sponsoring the study."
		* **restrictive_agreement**
	* **limitations\_and\_caveats**
	* **point\_of\_contact**
		* **name\_or\_title**
		* **organization**
		* **phone**
		* **email**