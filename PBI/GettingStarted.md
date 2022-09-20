# PowerBI Incremental Update Article

## Getting Started

1. unzip PBI/BlogArticle.zip
2. Open BlogArticle.pbix with Power BI
3. Dismiss the large yellow banner, click File, then click the button labeled "Browse Reports" in the "Open Report" Dialogue.  This launches File Explorer.  Navigate to where you "git cloned" this repo and then to the PBI directory.
4. Click on the Home Ribbon, then click on Transform Data, then choose "Transform Data" from the menu
5. That opens the Power Query Editor in a new Window.  Along the top ribbon, find the "Advanced Editor" button and click it.  This opens the Advanced Editor.  All we are going to do is change the Cosmos URL in a line that looks like this:

     Source = DocumentDB.Contents("https://test-power-bi.documents.azure.com:443/")
     
6. The Host URL is found in the Azure UI by going to the resource group your "Cosmos Provisioning" created, clicking on the "Azure Cosmos DB Account" and then selecting the "Keys" blade under Settings
7. All you care about is the URI Field. CLick the "Copy to Clipboard" icon and then paste that between the double quotes on the "Source = " line as shown in step 5 above
8. Click done to finish with the Advanced Editor
9. Next, click on "Blogger (2) and repeat the same steps
10. Finally, on the right of the Ribbon is the Close and Apply.
11. Finally to see all your work, click on the Data Icon on the right to see the data.

You are now ready to follow the Article to set-up an Incremental Refresh