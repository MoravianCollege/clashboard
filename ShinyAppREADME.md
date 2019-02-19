##Clinical Trials Dashboard
Using ShinyR and Shinyapps.io, allows users to navigate through large quantities of data using search terms for ease of use.

##Installation

Run the following command in the R console:
	
```bash
install.packages('rsconnect')
```
This command only needs to be ran once per computer. 

##Usage
To authorize the rsconnect package, paste the following command into your R console:

```bash
rsconnect::setAccountInfo(name='...', token='...', secret='...')
```
* (The secret token can be found in the 1Password manager).

After authorizing rsconnect, run the following lines in your R console:

```bash
library(rsconnect)
rsconnect::deployApp('path/to/your/app/folder')
```
You should now be able to launch the ShinyR app successfully. The link to your new app will be in the R console. 



