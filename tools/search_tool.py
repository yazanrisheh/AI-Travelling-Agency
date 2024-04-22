import json
import os
import requests
from langchain.tools import tool
from crewai_tools import  SerperDevTool


search_tool = SerperDevTool()
