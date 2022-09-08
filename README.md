# PowerBI Incremental Update Article
This repo contains the assets for the Power PBI Incremental refresh Blog Post

## Content
### ./data-generation - 
This directory contains the mgenerate.js template that is capable of generating simulated data.  This repo can be found at: https://github.com/rueckstiess/mgeneratejs

### ./data - 
This is a directory that contains 2 JSON arrays of pre-generated data, one with 1000 documents and the other with 1,000,000 documents

### ./PBI - 
This contains the Power BI Desktop file that is saved in a ZIP format.  Power BI desktop can only be run on Windows architectures.  The Desktop App is a free download.  You can also get a free Power BI System account - https://powerbi.microsoft.com/.  The PBIX file can be uploaded to Power BI system or opened in PowerBI desktop.  The more interesting part of the PBI desktop file can be found in the Power Query Editor (Started from the "Transform Data option on the Home Ribbon).  This shows the steps to flatten the embedded document for reporting.  All of the detailed steps are contained on the right pane in the editor.
[![](Power Query Editor)](./images/PQE.jpg)
![Power Query Editor](https://github.com/johndohoneyjr/PowerBI-Incremental-update-article/blob/main/images/PQE.jpg "Power Query - Flatten Steps")