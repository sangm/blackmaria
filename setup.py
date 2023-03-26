from setuptools import setup, find_packages


NAME = "blackmaria"
DESCRIPTION = "Scraping webpages with natural language"
URL = "https://github.com/smyja/blackmaria"
EMAIL = "akpobimaro@gmail.com"
AUTHOR = "Maro Akpobi"
setup(
    name=NAME,
    version='0.1',
    packages=find_packages(),
    url= URL,
    license='MIT',
    author=AUTHOR,
    author_email=EMAIL,
    
    install_requires=[
        'bs4',
        'python-dotenv',
        "guardrails-ai",
        "gpt_index"
    ],
    
)
