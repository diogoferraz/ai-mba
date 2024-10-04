import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeResult

# Store connection information
endpoint = os.getenv("ENDPOINT")
key = os.getenv("API_KEY")

docUrl = "<url-of-document-to-analyze>" # e.g. "https://example.com/your-document.pdf"

document_analysis_client = DocumentIntelligenceClient(endpoint=endpoint, 
    credential=AzureKeyCredential(key))

poller = document_analysis_client.begin_analyze_document_from_url(
    "prebuilt-document", docUrl)
result: AnalyzeResult = poller.result()