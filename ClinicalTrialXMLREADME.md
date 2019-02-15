# Clinical Trial Data from ClinicalTrials.gov
-
## Quick explanatory guide of the possible fields in one XML file 
### XML Conforms to this [Schema](https://clinicaltrials.gov/ct2/html/images/info/public.xsd)
### Furhter explanation of important terms can be found [here](https://clinicaltrials.gov/ct2/about-studies/glossary)
-
* **clinical_study** - all data about the clinical trial stored under this field
* **required_header** - header that provides general info about the download
	* **download_date** - date the date was downloaded
	* **link_text** - the text that would display instead of the url if opened in a webpage
		* Says the same thing for each file
	* **url** - where to find the data for the file online
* **id_info** - different ways the classify the study id
	* **org\_study\_id** - full id of the study
	* **secondary_id** - shortened or different id to use to find the study
	* **nct_id** - ClinicalTrials.gov identifier for the study (unique)
* **brief_title** - title of the clinical trial
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
	* **textblock** - short explaination of what the study is doing and looking to test
* **detailed_description**
	* **textblock** - more indepth explanation of the study, includes a lot more information than the breif summary
* **overall\_status** - potential values depend on the study_type
	* Study Type: Expanded Access - Values: Available, No Longer Available, Temporarily Not Available, Approved for Marketing
	* Study Type: N/A - Values: Withheld
	* Study Type: Anythig Else - Values: Active not recruiting, Completed, Enrolling by initiative, Not yet recruiting, Recruiting, Suspended, Terminated, Withdrawn
* **last\_known\_status** - most recent status of a study that has not been verified in at least 2 years
* **why_stopped** - reason for discontinuing the study
* **start_date**
* **completion_date**
* **primary\_completion\_date**
* **phase** - current phase of the clinical trial (1-4)
* **study_type** - classification of the study
	* Values: Expanded Acess, N/A, Other
* **has\_expanded\_access** - does the clinical trial allow patients with immediately life threatening conditions to participate
* **study\_design\_info**
	* **allocation** - how the tests are administered to the patients
		* Value: Randomized
	* **intervention_model** - general design of the strategy for assigning treatments to participants
	* **primary_purpose** - reason for the clinical trial
		* Values: Treatment
	* **masking** - tells who knows which people were treated
* **primary_outcome**
	* **measure** - important for evaluating the effect of the treatment, what it is supposed to do
	* **time_frame** - ???
* **number\_of\_arms** - number of group/sub-groups in the clinical trial
* **enrollment** - number of participants in the clinical study tagged with a type
	* Types: Actual, Anticipated, Estimate
* **condition** - disease, disorder, etc being studied - can be multiple
* **arm_group** 
	* **arm\_group\_label**
	* **arm\_group\_type**
	* **description**
* **intervention** - treatment
	* **intervention_type** - type of treatment
		* Values: Behavioral, Biological, Combination Product, Device, Diagnostic Test, Dietary Supplement, Drug, Genetic, Procedure, Radiation, Other
	* **intervention_name** - name of treatment???
* **eligibility** - who can participate in the study
	* **criteria**
		* **textblock** - details about desired participants
	* **gender**
	* **minimum_age**
	* **maximum_age**
	* **healthy_volunteers** - yes or no
* **overall_official** - person running the clinical study???
	* **last_name**
	* **role**
	* **affiliation**
* **location** - where the study is being conducted, can be multiple
	* **facility**
		* **name** - name of the facility
		* **address**
			* **city**
			* **state**
			* **country**
* **location_countries** - countries the study is being conducted in
	* **country**
* **reference** - sources of information for study???
	* **citation**
* **verification_date** - most recent date that the study sponsor/investigator confirmed trial info is accurate
* **study\_first\_submitted** - date of first submission to ClinicalTrials.gov
* **study\_first\_submitted\_qc** - date when study was consistent with NLM quality control review criteria
* **study\_first\_posted** - date the study first appeared on ClinicalTrials.gov
* **results\_first\_submitted** - date the summary results were first submission to ClinicalTrials.gov
* **results\_first\_submitted\_qc** - date when study results were consistent with NLM quality control review criteria
* **results\_first\_posted** - date the summary results first appeared on ClinicalTrials.gov
* **last\_update\_submitted** - last date the sponsor/investigator submitted updates to the trial on ClinicalTrials.gov
* **last\_update\_submitted\_qc** - date when study was consistent with NLM quality control review criteria
* **last\_update\_posted** - last date the sponsor/investigator updates were posted on ClinicalTrials.gov
* **responsible_party** - person responsible for submitting information about the study to ClinicalTrials.gov
	* **responsible\_party\_type**
		* Values: Sponsor, Principal Investigator, Sponsor-Investigator 
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
* **pending_results** - appears only when the data provider has submitted study results for QC review, but those results have not yet been publicly posted
* **clinical_results** - results of the clinical trial